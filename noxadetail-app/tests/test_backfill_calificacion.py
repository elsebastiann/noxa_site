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
