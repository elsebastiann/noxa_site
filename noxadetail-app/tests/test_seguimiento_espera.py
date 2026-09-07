"""El job de seguimiento no debe insistir a diario cuando el cliente ya dijo
que después.

Antes de esto, "tal vez después" se trataba exactamente igual que un silencio:
resetea followup_count como cualquier mensaje entrante y el job sigue la
cadencia corta (24h, +2d, +5d...) con el mismo "¿seguimos?" — visto en
producción el 2026-08-26 (caso Armandito: dijo "tal vez después" el 18/08 y le
llegó seguimiento el 19, el 21 y el 26)."""
import datetime as dt
from unittest.mock import MagicMock, patch

import pytest

from conftest import app_module as A


@pytest.fixture(autouse=True)
def _limpio():
    def borrar():
        with A.app.app_context():
            for c in A.Conversation.query.filter(A.Conversation.phone.like("+5730022%")).all():
                A.Message.query.filter_by(conversation_id=c.id).delete()
                A.db.session.delete(c)
            A.db.session.commit()
    borrar()
    yield
    borrar()


def _conv(tel):
    c = A.Conversation(phone=tel, profile_name="Cliente Espera", status="En proceso",
                       priority="Alta", bot_active=True, calificacion=4)
    A.db.session.add(c)
    A.db.session.commit()
    return c


def _msg(conv, direction, texto, hace_dias=0):
    m = A.Message(conversation_id=conv.id, direction=direction, body=texto,
                  created_at=A.bogota_now() - dt.timedelta(days=hace_dias))
    A.db.session.add(m)
    A.db.session.commit()
    return m


class TestClientePidioEsperar:
    @pytest.mark.parametrize("texto", [
        "Hola Mariana, tal vez después",
        "más adelante te escribo",
        "ahorita no puedo, otro día vemos",
        "dejame pensarlo",
        "yo te aviso",
        "en unos días te cuento",
    ])
    def test_detecta_frases_de_espera(self, texto):
        with A.app.app_context():
            c = _conv("+573002200001")
            _msg(c, "in", texto)
            assert A._cliente_pidio_esperar(c) is True

    @pytest.mark.parametrize("texto", [
        "Hola, cuánto cuesta el cerámico",
        "sí, agendemos para mañana",
        "el carro es un Mazda CX-9 2023",
    ])
    def test_no_dispara_con_un_mensaje_normal(self, texto):
        with A.app.app_context():
            c = _conv("+573002200002")
            _msg(c, "in", texto)
            assert A._cliente_pidio_esperar(c) is False

    def test_sin_mensajes_entrantes_no_dispara(self):
        with A.app.app_context():
            c = _conv("+573002200003")
            assert A._cliente_pidio_esperar(c) is False

    def test_solo_mira_el_ultimo_entrante(self):
        """Si el cliente ya retomó por su cuenta después del "después", ya no aplica."""
        with A.app.app_context():
            c = _conv("+573002200004")
            _msg(c, "in", "tal vez después", hace_dias=3)
            _msg(c, "in", "listo, hagámoslo ya", hace_dias=0)
            assert A._cliente_pidio_esperar(c) is False


class TestGenerateFollowupMessageRespetaEspera:
    def test_pregunta_que_lo_detiene_en_vez_de_repetir(self):
        with A.app.app_context():
            c = _conv("+573002200005")
            _msg(c, "in", "tal vez después")
            with patch.object(A, "_call_claude", return_value=["ok"]) as mock_call:
                A.generate_followup_message(c, "ancla_de_valor")
        instruccion = mock_call.call_args[0][0][-1]["content"]
        assert "qué es específicamente lo que lo está deteniendo" in instruccion
        assert "genera un mensaje de seguimiento — etapa" not in instruccion

    def test_mensaje_normal_de_silencio_cuando_no_hubo_espera(self):
        with A.app.app_context():
            c = _conv("+573002200006")
            _msg(c, "in", "hola, cuánto cuesta el cerámico")
            with patch.object(A, "_call_claude", return_value=["ok"]) as mock_call:
                A.generate_followup_message(c, "ancla_de_valor")
        instruccion = mock_call.call_args[0][0][-1]["content"]
        assert "quedó en silencio" in instruccion
        assert "qué es específicamente lo que lo está deteniendo" not in instruccion


class TestUmbralSeEstiraConEspera:
    """La lógica exacta que usa _job_whatsapp_followup para decidir el umbral —
    ejercida aparte porque correr el job completo exige simular hora de Bogotá,
    horario de atención y el envío real por Twilio (mismo criterio ya usado
    para _candidatas_de_seguimiento, ver test_seguimiento.py)."""

    def test_el_primer_toque_se_va_a_una_semana_si_pidio_esperar(self):
        """El primer toque normal sale al día siguiente. A quien pidió tiempo se
        le da la semana completa: escribirle mañana contradice a la cara lo que
        acaba de pedir."""
        escrito = dt.datetime(2026, 9, 1, 15, 0)
        normal = A.momento_de_seguimiento(escrito, 0)
        con_espera = A._dentro_de_la_franja(escrito + dt.timedelta(days=7))

        assert normal.date() == dt.date(2026, 9, 2)
        assert max(normal, con_espera) == con_espera
        assert con_espera.date() == dt.date(2026, 9, 8)

    def _corre_el_job(self, tel, texto_del_cliente):
        """El job real, con el reloj fijo. Nada relativo a "ahora": si dependiera
        de la hora a la que corren los tests, fuera de la franja 9-17:30 el job
        se sale al primer if y el test pasaría sin probar nada."""
        # El cliente escribió el martes 1 de septiembre a las 10 AM de Bogotá
        # (15:00 UTC, que es como se guarda), y le contestamos enseguida.
        with A.app.app_context():
            c = _conv(tel)
            # La respuesta va un minuto después y no en el mismo instante: el
            # job mira cuál fue el ÚLTIMO mensaje para saber si el cliente ya
            # contestó, y con dos timestamps idénticos ese orden queda al azar.
            for minuto, (direccion, cuerpo) in enumerate(
                    (("in", texto_del_cliente), ("out", "listo"))):
                A.db.session.add(A.Message(conversation_id=c.id, direction=direccion,
                                           body=cuerpo,
                                           created_at=dt.datetime(2026, 9, 1, 15, minuto)))
            A.db.session.commit()

            enviados = []
            with patch.object(A, "send_whatsapp",
                              side_effect=lambda *a, **k: enviados.append(a) or (True, "SM1")), \
                 patch.object(A, "generate_followup_message", return_value="hola"), \
                 patch.object(A, "es_dia_habil", return_value=True), \
                 patch.object(A, "bogota_now",
                              return_value=dt.datetime(2026, 9, 2, 12, 30)):
                A._job_whatsapp_followup()
            return enviados

    def test_el_job_aplaza_de_verdad_al_que_pidio_esperar(self):
        """Contra el job real y no contra una copia de su lógica: la versión
        anterior de este test rehacía la cuenta a mano, así que habría seguido
        en verde aunque el job dejara de aplazar."""
        assert not self._corre_el_job("+573002200007", "tal vez después"), \
            "le escribió al día siguiente a alguien que pidió esperar"

    def test_al_que_solo_se_quedo_callado_si_le_escribe(self):
        """Contraprueba: mismo montaje, misma hora, solo cambia lo que dijo el
        cliente. Sin esto, el test de arriba pasaría aunque el job no mandara
        nada nunca."""
        assert self._corre_el_job("+573002200008", "hola, cuánto cuesta el cerámico"), \
            "no le escribió al día siguiente a un lead que se quedó callado"
