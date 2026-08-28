"""Si se acordó hablar más adelante, no se le escribe antes.

Caso real (2026-08-25): el cliente dijo "esta semana no puedo", Mariana le
propuso escribirle la próxima semana, él aceptó — y el job le mandó un
seguimiento AL DÍA SIGUIENTE. Prometerle esperar y contradecirlo al otro día
es la peor forma de perder un lead que estaba dispuesto.

El job decide por tiempo transcurrido y no tenía forma de enterarse del
acuerdo. Ahora Mariana lo marca con [ESPERAR: fecha] y el job lo respeta.
"""
import datetime as dt
import itertools
from unittest.mock import patch

import pytest

from conftest import app_module as A

_tel = itertools.count(7100)


@pytest.fixture
def conv():
    with A.app.app_context():
        c = A.Conversation(phone=f"+5730077{next(_tel):05d}", profile_name="Jefferson",
                           status="En proceso", bot_active=True, followup_count=0)
        A.db.session.add(c)
        A.db.session.commit()
        cid = c.id
    yield cid
    with A.app.app_context():
        A.Message.query.filter_by(conversation_id=cid).delete()
        c = A.Conversation.query.get(cid)
        if c:
            A.db.session.delete(c)
        A.db.session.commit()


def _es_candidata(cid):
    with A.app.app_context():
        return any(c.id == cid for c in A._candidatas_de_seguimiento())


def _pausar(cid, dias):
    with A.app.app_context():
        c = A.Conversation.query.get(cid)
        c.seguimiento_pausado_hasta = A.bogota_now().date() + dt.timedelta(days=dias)
        A.db.session.commit()


class TestElJobRespetaElAcuerdo:
    def test_con_pausa_vigente_no_se_le_escribe(self, conv):
        """El caso exacto que se vio en producción."""
        _pausar(conv, 7)
        assert not _es_candidata(conv)

    def test_sin_pausa_si_se_le_escribe(self, conv):
        """Contraprueba: si tampoco entrara sin pausa, el test de arriba pasaría
        por cualquier otro motivo."""
        assert _es_candidata(conv)

    def test_cumplida_la_fecha_se_reanuda(self, conv):
        _pausar(conv, -1)   # la fecha ya pasó
        assert _es_candidata(conv)

    def test_el_mismo_dia_ya_se_puede_escribir(self, conv):
        _pausar(conv, 0)
        assert _es_candidata(conv)


class TestPropiedad:
    def test_en_pausa_mientras_no_llegue_la_fecha(self, conv):
        _pausar(conv, 3)
        with A.app.app_context():
            assert A.Conversation.query.get(conv).seguimiento_en_pausa

    def test_sin_fecha_no_esta_en_pausa(self, conv):
        with A.app.app_context():
            assert not A.Conversation.query.get(conv).seguimiento_en_pausa

    def test_fecha_pasada_no_esta_en_pausa(self, conv):
        _pausar(conv, -5)
        with A.app.app_context():
            assert not A.Conversation.query.get(conv).seguimiento_en_pausa


class TestMarcador:
    def _turno(self, cid, partes):
        with A.app.app_context():
            c = A.Conversation.query.get(cid)
            with patch.object(A, "send_whatsapp", return_value=(True, "")), \
                 patch.object(A, "get_claude_reply", return_value=list(partes)), \
                 patch.object(A, "push_notification"):
                A._generate_and_send_reply(c, c.phone)

    def test_esperar_guarda_la_fecha(self, conv):
        objetivo = A.bogota_now().date() + dt.timedelta(days=7)
        self._turno(conv, ["Listo, te escribo la próxima semana.",
                           f"[ESPERAR: {objetivo.isoformat()}]"])
        with A.app.app_context():
            assert A.Conversation.query.get(conv).seguimiento_pausado_hasta == objetivo

    def test_tras_el_acuerdo_el_job_ya_no_lo_persigue(self, conv):
        """La cadena completa: Mariana acuerda, se guarda, el job lo excluye."""
        objetivo = A.bogota_now().date() + dt.timedelta(days=7)
        assert _es_candidata(conv)
        self._turno(conv, ["Listo, quedamos así.", f"[ESPERAR: {objetivo.isoformat()}]"])
        assert not _es_candidata(conv)

    def test_el_marcador_no_se_le_manda_al_cliente(self, conv):
        enviados = []

        def fake(to, body, **kw):
            enviados.append(body)
            return True, ""

        with A.app.app_context():
            c = A.Conversation.query.get(conv)
            objetivo = A.bogota_now().date() + dt.timedelta(days=7)
            with patch.object(A, "send_whatsapp", side_effect=fake), \
                 patch.object(A, "get_claude_reply",
                              return_value=["Listo, te escribo luego.",
                                            f"[ESPERAR: {objetivo.isoformat()}]"]), \
                 patch.object(A, "push_notification"):
                A._generate_and_send_reply(c, c.phone)
        assert not any("ESPERAR" in m for m in enviados), "el marcador se le coló al cliente"

    def test_una_fecha_invalida_no_tumba_el_turno(self, conv):
        self._turno(conv, ["Listo.", "[ESPERAR: la otra semana]"])
        with A.app.app_context():
            # No se guarda nada, pero el turno no revienta y el cliente recibe su mensaje.
            assert A.Conversation.query.get(conv).seguimiento_pausado_hasta is None


class TestNoSeRompioElResto:
    def test_los_otros_filtros_siguen(self, conv):
        with A.app.app_context():
            c = A.Conversation.query.get(conv)
            c.status = "Cita agendada"
            A.db.session.commit()
        assert not _es_candidata(conv)

    def test_archivada_sigue_excluida(self, conv):
        with A.app.app_context():
            c = A.Conversation.query.get(conv)
            c.archived_at = A.datetime.utcnow()
            A.db.session.commit()
        assert not _es_candidata(conv)
