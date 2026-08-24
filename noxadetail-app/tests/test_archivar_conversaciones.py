"""Archivar una conversación a mano: sale de la bandeja y deja de recibir
seguimientos automáticos.

Archivado va en columnas propias (`archived_at` / `archived_reason` /
`archived_by`) y NO en `status`: ese campo es la etapa del embudo, lo consumen
ESTADOS_CON_CITA y las analíticas, y Mariana lo reescribe con su [META:] en cada
turno — un estado "Archivado" ahí se desharía solo al turno siguiente.
"""
import itertools
from unittest.mock import patch

import pytest

from conftest import app_module as A
from conftest import login_as, make_user

_telefonos = itertools.count(7100)


@pytest.fixture
def admin(client):
    login_as(client, make_user("admin_archivar", role="admin"))
    return client


@pytest.fixture
def conv():
    with A.app.app_context():
        c = A.Conversation(
            phone=f"+5730077{next(_telefonos):05d}", profile_name="Cliente Archivo",
        )
        A.db.session.add(c)
        A.db.session.commit()
        cid = c.id
    yield cid
    with A.app.app_context():
        A.Message.query.filter_by(conversation_id=cid).delete()
        fila = A.Conversation.query.get(cid)
        if fila:
            A.db.session.delete(fila)
        A.db.session.commit()


def _archivar(client, cid, motivo="Ya compró en otro lado"):
    return client.post(f"/whatsapp/{cid}/archive", data={"motivo": motivo})


def _leer(cid):
    with A.app.app_context():
        return A.Conversation.query.get(cid)


class TestArchivar:
    def test_guarda_fecha_motivo_y_autor(self, admin, conv):
        r = _archivar(admin, conv, "No le interesó el precio")
        assert r.status_code == 302

        c = _leer(conv)
        assert c.archivada is True
        assert c.archived_at is not None
        assert c.archived_reason == "No le interesó el precio"
        assert c.archived_by, "no quedó registrado quién archivó"

    def test_sin_motivo_no_archiva(self, admin, conv):
        """La nota es el punto: sin ella, en un mes nadie sabe por qué se cerró.
        Se valida en el servidor porque el modal se salta apagando el JS."""
        r = admin.post(f"/whatsapp/{conv}/archive", data={"motivo": "   "})
        assert r.status_code == 302
        assert _leer(conv).archivada is False

    def test_la_hora_queda_en_utc(self, admin, conv):
        """La plantilla la muestra con el filtro `hora_bogota`, que convierte de
        UTC. Guardarla ya en hora local la restaba dos veces y el panel mostraba
        el archivado 5 horas antes de que ocurriera — visible solo en pantalla,
        que es como se detectó."""
        from datetime import datetime, timedelta

        _archivar(admin, conv)
        guardada = _leer(conv).archived_at
        assert abs(guardada - datetime.utcnow()) < timedelta(minutes=2), (
            f"archived_at={guardada} no parece UTC; "
            f"utcnow={datetime.utcnow()}, bogota={A.bogota_now()}"
        )

    def test_archivar_pausa_el_bot(self, admin, conv):
        _archivar(admin, conv)
        assert _leer(conv).bot_active is False

    def test_no_toca_el_estado_del_embudo(self, admin, conv):
        with A.app.app_context():
            c = A.Conversation.query.get(conv)
            c.status = "Cita agendada"
            A.db.session.commit()

        _archivar(admin, conv)
        assert _leer(conv).status == "Cita agendada"


class TestDesarchivar:
    def test_limpia_los_tres_campos(self, admin, conv):
        _archivar(admin, conv)
        r = admin.post(f"/whatsapp/{conv}/unarchive")
        assert r.status_code == 302

        c = _leer(conv)
        assert c.archivada is False
        assert c.archived_reason is None
        assert c.archived_by is None

    def test_no_reactiva_el_bot_solo(self, admin, conv):
        """Volver a la bandeja y volver a atender con el bot son decisiones
        distintas; para la segunda ya está su botón."""
        _archivar(admin, conv)
        admin.post(f"/whatsapp/{conv}/unarchive")
        assert _leer(conv).bot_active is False


class TestSeguimiento:
    """El filtro del job es lo que hace que archivar sirva de algo: sin él,
    Mariana le seguiría mandando reactivaciones a alguien ya cerrado."""

    def test_una_archivada_no_entra_al_seguimiento(self, admin, conv):
        _archivar(admin, conv)
        with A.app.app_context():
            # bot_active lo apagó el archivado; se reactiva para aislar la
            # variable y probar que lo que excluye es el archivado en sí.
            A.Conversation.query.get(conv).bot_active = True
            A.db.session.commit()
            ids = [c.id for c in A._candidatas_de_seguimiento()]
        assert conv not in ids

    def test_la_misma_sin_archivar_si_entra(self, admin, conv):
        """Contraprueba: sin esto el test de arriba pasaría por cualquier motivo
        que sacara la conversación del filtro."""
        with A.app.app_context():
            ids = [c.id for c in A._candidatas_de_seguimiento()]
        assert conv in ids


class TestClienteVuelveAEscribir:
    """Un mensaje entrante devuelve la conversación a la bandeja. El motivo del
    archivado no distingue "no le interesó" de "número equivocado", y dejar
    invisible a alguien que volvió a escribir es la falla que cuesta plata."""

    def _entrante(self, cid, texto="Hola, cambié de opinión"):
        with A.app.app_context():
            telefono = A.Conversation.query.get(cid).phone
        with patch.object(A, "_generate_and_send_reply", return_value=True):
            return A.app.test_client().post("/whatsapp/webhook", data={
                "From": f"whatsapp:{telefono}", "Body": texto,
                "ProfileName": "Cliente Archivo", "NumMedia": "0",
            })

    def test_desarchiva(self, admin, conv):
        _archivar(admin, conv, "No contestó nunca")
        self._entrante(conv)
        assert _leer(conv).archivada is False

    def test_reactiva_el_bot(self, admin, conv):
        """Archivar apaga el bot, así que sin esto la conversación volvía a la
        bandeja pero SIN nadie respondiendo: el cliente esperaba hasta que
        alguien viera la campanita. Archivar es "acá terminamos", y un mensaje
        nuevo abre un ciclo nuevo."""
        _archivar(admin, conv)
        assert _leer(conv).bot_active is False   # el archivado lo apagó

        self._entrante(conv)

        assert _leer(conv).bot_active is True

    def test_la_campanita_avisa_que_mariana_la_tomo(self, admin, conv):
        """No es una sorpresa si se avisa: quien la archivó se entera de que el
        bot volvió a responder y puede pausarlo otra vez en un clic."""
        _archivar(admin, conv, "No contestó nunca")
        with patch.object(A, "push_notification") as campanita:
            self._entrante(conv)

        cuerpos = [c.kwargs.get("body", "") for c in campanita.call_args_list]
        assert any("Mariana la está atendiendo" in b for b in cuerpos), cuerpos
        assert any("No contestó nunca" in b for b in cuerpos), cuerpos

    def test_avisa_por_campanita(self, admin, conv):
        _archivar(admin, conv, "Pidió no ser contactado")
        with patch.object(A, "push_notification") as campanita:
            self._entrante(conv)
        kinds = [c.kwargs.get("kind") for c in campanita.call_args_list]
        assert "conversacion_desarchivada" in kinds, (
            f"nadie se entera de que volvió; solo salió: {kinds}"
        )


class TestUnBotPausadoSinArchivarNoSeToca:
    """La distinción que hace segura la reactivación automática: un bot pausado
    en una conversación que NO está archivada es un humano que la tomó a
    propósito — un reclamo, una negociación, un escalamiento. Meter ahí a
    Mariana sería interrumpir a alguien trabajando."""

    def _entrante(self, cid, texto="Sigo esperando"):
        with A.app.app_context():
            telefono = A.Conversation.query.get(cid).phone
        with patch.object(A, "_generate_and_send_reply", return_value=True):
            return A.app.test_client().post("/whatsapp/webhook", data={
                "From": f"whatsapp:{telefono}", "Body": texto,
                "ProfileName": "Cliente Escalado", "NumMedia": "0",
            })

    def test_el_bot_sigue_pausado(self, admin, conv):
        with A.app.app_context():
            c = A.Conversation.query.get(conv)
            c.bot_active = False        # escalada a un humano, sin archivar
            A.db.session.commit()

        self._entrante(conv)

        assert _leer(conv).bot_active is False
        assert _leer(conv).archivada is False
