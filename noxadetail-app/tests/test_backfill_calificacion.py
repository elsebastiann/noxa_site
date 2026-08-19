"""Backfill de calificación para conversaciones que existían antes de que ese
campo existiera — se quedaron con calificacion=None y nunca se les vuelve a
generar un [META:] real a menos que el cliente escriba de nuevo. La ruta lee
el historial con Claude y las clasifica sin mandarle nada al cliente."""
import itertools
from unittest.mock import MagicMock, patch

import pytest

from conftest import app_module as A, make_user, login_as

_telefonos = itertools.count(9500)


@pytest.fixture
def conversacion_vieja():
    """Una conversación con mensajes pero sin ninguna de las columnas nuevas —
    el estado exacto en el que quedaron las conversaciones reales de antes de
    esta función."""
    with A.app.app_context():
        conv = A.Conversation(
            phone=f"+5730077{next(_telefonos):05d}", profile_name="Cliente Viejo",
            status="En proceso", service_tag="", carro="", marca="", calificacion=None,
            priority="Baja",
        )
        A.db.session.add(conv)
        A.db.session.commit()
        A.db.session.add(A.Message(conversation_id=conv.id, direction="in",
                                    body="Hola, tengo un Audi Q5 2022 y quiero el cerámico 9H"))
        A.db.session.add(A.Message(conversation_id=conv.id, direction="out",
                                    body="Con gusto, el 9H tiene 5 años de garantía y cuesta $2.199.000"))
        A.db.session.add(A.Message(conversation_id=conv.id, direction="in",
                                    body="Perfecto, ¿cuándo puedo llevarlo?"))
        A.db.session.commit()
        conv_id = conv.id
    yield conv_id
    with A.app.app_context():
        A.Message.query.filter_by(conversation_id=conv_id).delete()
        conv = A.Conversation.query.get(conv_id)
        if conv:
            A.db.session.delete(conv)
        A.db.session.commit()


def _fake_claude_response(texto):
    bloque = MagicMock()
    bloque.type = "text"
    bloque.text = texto
    respuesta = MagicMock()
    respuesta.content = [bloque]
    return respuesta


class TestClasificarConversacionHistorica:
    def test_parsea_la_clasificacion_de_claude(self, conversacion_vieja):
        marcador = (
            "[META: estado=En proceso; servicios=Cerámico; "
            "carro=Audi Q5 2022; marca=Audi; calificacion=5]"
        )
        with A.app.app_context():
            conv = A.Conversation.query.get(conversacion_vieja)
            with patch.object(A, "_get_claude_client") as fake_client:
                fake_client.return_value.messages.create.return_value = _fake_claude_response(marcador)
                resultado = A._clasificar_conversacion_historica(conv)

        assert resultado["estado"] == "En proceso"
        assert resultado["servicios"] == ["Cerámico"]
        assert resultado["carro"] == "Audi Q5 2022"
        assert resultado["marca"] == "Audi"
        assert resultado["calificacion"] == 5

    def test_sin_historial_no_llama_a_claude(self):
        with A.app.app_context():
            conv = A.Conversation(phone="+573007799999", profile_name="Sin mensajes")
            A.db.session.add(conv)
            A.db.session.commit()
            with patch.object(A, "_get_claude_client") as fake_client:
                resultado = A._clasificar_conversacion_historica(conv)
            assert not fake_client.called
            assert resultado is None
            A.db.session.delete(conv)
            A.db.session.commit()

    def test_respuesta_sin_meta_reconocible_devuelve_none(self, conversacion_vieja):
        with A.app.app_context():
            conv = A.Conversation.query.get(conversacion_vieja)
            with patch.object(A, "_get_claude_client") as fake_client:
                fake_client.return_value.messages.create.return_value = _fake_claude_response(
                    "Perdón, no puedo ayudarte con eso."
                )
                resultado = A._clasificar_conversacion_historica(conv)
        assert resultado is None

    def test_marca_no_reconocida_cae_a_vacio_pero_conserva_lo_demas(self, conversacion_vieja):
        marcador = (
            "[META: estado=En proceso; servicios=Cerámico; "
            "carro=Lada Niva 1990; marca=Lada; calificacion=1]"
        )
        with A.app.app_context():
            conv = A.Conversation.query.get(conversacion_vieja)
            with patch.object(A, "_get_claude_client") as fake_client:
                fake_client.return_value.messages.create.return_value = _fake_claude_response(marcador)
                resultado = A._clasificar_conversacion_historica(conv)
        assert resultado["marca"] == ""
        assert resultado["carro"] == "Lada Niva 1990"
        assert resultado["calificacion"] == 1


class TestRutaBackfill:
    def test_requiere_admin(self, client, conversacion_vieja):
        # "lider" y no "operario": operario ya está bloqueado antes de llegar acá
        # por la lista blanca de OPERARIO_ENDPOINTS (otro mecanismo, ver
        # before_request) — este test cubre el chequeo propio de la ruta.
        lider = make_user("lider_backfill", role="lider")
        login_as(client, lider)
        resp = client.post("/whatsapp/backfill-calificacion", follow_redirects=True)
        assert "Acceso restringido".encode() in resp.data

    def test_clasifica_solo_las_que_no_tienen_calificacion(self, client, conversacion_vieja):
        """Idempotencia: una conversación que YA tiene calificación no se toca,
        así que repetir el backfill no vuelve a gastar en ella."""
        admin = make_user("admin_backfill", role="admin")
        ya_clasificada = A.Conversation(
            phone="+573007788888", profile_name="Ya clasificada",
            status="En proceso", calificacion=3, priority="Media",
        )
        A.db.session.add(ya_clasificada)
        A.db.session.commit()
        ya_id = ya_clasificada.id

        login_as(client, admin)
        marcador = (
            "[META: estado=Cita agendada; servicios=Cerámico; "
            "carro=Audi Q5 2022; marca=Audi; calificacion=5]"
        )
        with patch.object(A, "_get_claude_client") as fake_client:
            fake_client.return_value.messages.create.return_value = _fake_claude_response(marcador)
            client.post("/whatsapp/backfill-calificacion", follow_redirects=True)
            llamadas_antes = fake_client.return_value.messages.create.call_count
            # Segunda pasada: la que se acaba de clasificar ya no debería tocarse.
            client.post("/whatsapp/backfill-calificacion", follow_redirects=True)
            llamadas_despues = fake_client.return_value.messages.create.call_count

        with A.app.app_context():
            conv = A.Conversation.query.get(conversacion_vieja)
            assert conv.calificacion == 5
            assert conv.carro == "Audi Q5 2022"
            assert conv.marca == "Audi"
            assert conv.priority == "Alta"
            assert "Cerámico" in conv.service_tag

            intacta = A.Conversation.query.get(ya_id)
            assert intacta.calificacion == 3  # nunca se tocó

            A.db.session.delete(intacta)
            A.db.session.commit()

        assert llamadas_antes == 1  # solo la vieja sin calificación
        assert llamadas_despues == 1  # la segunda pasada no sumó llamadas nuevas


class TestRegresionProduccion:
    """Dos fallas vistas en vivo el 2026-08-18 al correr el backfill contra
    conversaciones reales: un service_tag heredado del catálogo viejo tumbaba
    la ruta entera con 500 (ValueError en SERVICE_TAGS.index), y un mensaje con
    body vacío de antes de que el webhook garantizara texto de reemplazo
    tumbaba la llamada a Claude (400 'messages must have non-empty content')."""

    def test_build_message_history_salta_mensajes_con_body_vacio(self):
        conv = A.Conversation(phone="+573007766666", profile_name="Legado")
        A.db.session.add(conv)
        A.db.session.commit()
        A.db.session.add(A.Message(conversation_id=conv.id, direction="in", body="Hola"))
        A.db.session.add(A.Message(conversation_id=conv.id, direction="out", body=""))
        A.db.session.add(A.Message(conversation_id=conv.id, direction="in", body="  "))
        A.db.session.add(A.Message(conversation_id=conv.id, direction="in", body="¿Cuánto vale el cerámico?"))
        A.db.session.commit()

        history = A._build_message_history(conv)

        assert all(m["content"].strip() for m in history), history
        # "Hola" y la pregunta son ambos "in" seguidos (el "out" vacío se saltó
        # de por medio), así que se fusionan en un solo mensaje user.
        assert history == [{"role": "user", "content": "Hola\n¿Cuánto vale el cerámico?"}]

        A.Message.query.filter_by(conversation_id=conv.id).delete()
        A.db.session.delete(conv)
        A.db.session.commit()

    def test_service_tag_heredado_del_catalogo_viejo_no_tumba_la_ruta(self, client, conversacion_vieja):
        """'Otro servicio' y 'PPF o wrap' existían en el SERVICE_TAGS de antes de
        ampliar el catálogo a 10 categorías — conversaciones reales todavía los
        tienen guardados tal cual. SERVICE_TAGS.index() no los reconoce."""
        conv = A.Conversation.query.get(conversacion_vieja)
        conv.service_tag = "Otro servicio"
        A.db.session.commit()

        admin = make_user("admin_legado", role="admin")
        login_as(client, admin)
        marcador = (
            "[META: estado=En proceso; servicios=Cerámico; "
            "carro=Audi Q5 2022; marca=Audi; calificacion=5]"
        )
        with patch.object(A, "_get_claude_client") as fake_client:
            fake_client.return_value.messages.create.return_value = _fake_claude_response(marcador)
            resp = client.post("/whatsapp/backfill-calificacion", follow_redirects=True)

        assert resp.status_code == 200  # antes del fix, esto era un 500
        assert "0 con error".encode() in resp.data

        conv = A.Conversation.query.get(conversacion_vieja)
        # La etiqueta vieja se descarta (ya no existe en el catálogo actual); la
        # nueva calificación sí se aplica con normalidad.
        assert "Otro servicio" not in conv.service_tag
        assert "Cerámico" in conv.service_tag
        assert conv.calificacion == 5

    def test_una_conversacion_con_error_no_tumba_el_resto_del_lote(self, client, conversacion_vieja):
        """Antes del fix, el try/except solo cubría la llamada a Claude — un
        ValueError más abajo (ej. el del service_tag heredado) se propagaba sin
        capturar y devolvía un 500 que interrumpía el for entero."""
        otra = A.Conversation(phone="+573007755555", profile_name="La que sí sirve",
                               status="En proceso")
        A.db.session.add(otra)
        A.db.session.commit()
        A.db.session.add(A.Message(conversation_id=otra.id, direction="in", body="Hola, cuánto vale un cerámico"))
        A.db.session.commit()
        otra_id = otra.id

        conv = A.Conversation.query.get(conversacion_vieja)
        conv.service_tag = "Otro servicio"  # esta forzaba el 500 antes del fix
        A.db.session.commit()

        admin = make_user("admin_lote", role="admin")
        login_as(client, admin)
        marcador = (
            "[META: estado=En proceso; servicios=Cerámico; "
            "carro=Sin dato; marca=Sin dato; calificacion=3]"
        )
        with patch.object(A, "_get_claude_client") as fake_client:
            fake_client.return_value.messages.create.return_value = _fake_claude_response(marcador)
            resp = client.post("/whatsapp/backfill-calificacion", follow_redirects=True)

        assert resp.status_code == 200
        # La otra conversación del lote sí se procesó, aunque la primera hubiera
        # tenido un service_tag heredado problemático.
        assert A.Conversation.query.get(otra_id).calificacion == 3
        A.Message.query.filter_by(conversation_id=otra_id).delete()
        A.db.session.delete(A.Conversation.query.get(otra_id))
        A.db.session.commit()
