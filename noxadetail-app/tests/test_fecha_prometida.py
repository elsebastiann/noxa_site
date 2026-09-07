"""Cuando queda una fecha en la mesa, esa fecha manda sobre la cadencia.

Tres formas de que quede una: el cliente pide que le escriban después, el
cliente dice cuándo va a estar listo ("me entregan el carro en 3 semanas"), o
Mariana misma se compromete ("la próxima semana te escribo"). En los tres casos
ella emite [ESPERAR: fecha] y hasta ese día no sale ningún seguimiento
automático.

El caso que motivó esto salió en producción: Mariana escribió "la próxima semana
te escribo para cuadrar el diagnóstico" y con la cadencia normal le habría
escrito al día siguiente, contradiciéndose sola delante del cliente.
"""
import itertools
from datetime import date, datetime, timedelta
from unittest.mock import patch

import pytest

from conftest import app_module as A, login_as, make_user

_u = itertools.count(1)
_tel = itertools.count(4400)


@pytest.fixture(autouse=True)
def _limpio():
    def borrar():
        with A.app.app_context():
            for c in A.Conversation.query.filter(A.Conversation.phone.like("+5730044%")).all():
                A.Message.query.filter_by(conversation_id=c.id).delete()
                A.db.session.delete(c)
            A.db.session.commit()
    borrar()
    yield
    borrar()


def _conv(pausa=None, count=0, escribio=None, contestamos=None):
    """Un lead callado, con los mensajes en las fechas que se le pidan (UTC)."""
    c = A.Conversation(phone=f"+5730044{next(_tel):05d}", profile_name="Claudia",
                       status="En proceso", priority="Alta", bot_active=True,
                       followup_count=count, seguimiento_pausado_hasta=pausa)
    A.db.session.add(c)
    A.db.session.commit()
    A.db.session.add(A.Message(conversation_id=c.id, direction="in",
                               body="me entregan el carro en 3 semanas",
                               created_at=escribio))
    if contestamos:
        A.db.session.add(A.Message(conversation_id=c.id, direction="out",
                                   body="listo, te escribo entonces",
                                   created_at=contestamos))
    A.db.session.commit()
    return c


def _sellar_ultimo_nuestro(conv, cuando):
    """Le pone la hora simulada al último mensaje que mandamos nosotros."""
    m = (A.Message.query.filter_by(conversation_id=conv.id, direction="out")
         .order_by(A.Message.id.desc()).first())
    m.created_at = cuando
    A.db.session.commit()


def _corre(cuando):
    """El job con el reloj fijo. Devuelve las etapas que despachó."""
    enviados = []
    with patch.object(A, "send_whatsapp",
                      side_effect=lambda *a, **k: enviados.append(k.get("kind")) or (True, "SM")), \
         patch.object(A, "generate_followup_message", return_value="hola"), \
         patch.object(A, "es_dia_habil", return_value=True), \
         patch.object(A, "bogota_now", return_value=cuando):
        A._job_whatsapp_followup()
    return enviados


class TestLaFechaPrometidaApagaLaCadencia:
    def test_no_le_escribe_antes_de_la_fecha(self):
        """Lo que se vio en producción: prometerle la otra semana y escribirle
        mañana."""
        with A.app.app_context():
            _conv(pausa=date(2026, 9, 14),
                  escribio=datetime(2026, 9, 7, 14, 22),
                  contestamos=datetime(2026, 9, 7, 14, 23))
            assert _corre(datetime(2026, 9, 8, 12, 30)) == []

    def test_el_dia_prometido_si_le_escribe(self):
        """Contraprueba: la pausa aplaza, no cancela. Sin esto el lead se
        quedaría esperando para siempre una llamada que prometimos."""
        with A.app.app_context():
            _conv(pausa=date(2026, 9, 14),
                  escribio=datetime(2026, 9, 7, 14, 22),
                  contestamos=datetime(2026, 9, 7, 14, 23))
            assert _corre(datetime(2026, 9, 14, 10, 0)) == ["lead_seguimiento_primer_toque"]

    def test_una_fecha_lejana_tambien_se_respeta(self):
        """"Me entregan el carro en 3 semanas" no es un silencio: es una cita."""
        with A.app.app_context():
            _conv(pausa=date(2026, 9, 28),
                  escribio=datetime(2026, 9, 7, 14, 22),
                  contestamos=datetime(2026, 9, 7, 14, 23))
            assert _corre(datetime(2026, 9, 20, 10, 0)) == []


class TestNoSeLeMandanDosSeguidos:
    """El bug que trajo la cadencia de dos toques.

    Los dos momentos se calculan desde el mensaje del cliente. Cuando el
    seguimiento arranca tarde —una fecha prometida lejana, un lead que llevaba
    semanas callado— los dos ya quedaron en el pasado, así que el job mandaba el
    primero en un tick y el segundo media hora después. Dos mensajes seguidos es
    exactamente lo que la regla de dos toques vino a evitar.
    """

    def test_entre_nuestros_dos_mensajes_hay_una_semana(self):
        with A.app.app_context():
            c = _conv(pausa=date(2026, 9, 28),
                      escribio=datetime(2026, 9, 7, 14, 22),
                      contestamos=datetime(2026, 9, 7, 14, 23))
            primero = _corre(datetime(2026, 9, 28, 10, 0))
            # El mensaje que acaba de guardar el job quedó sellado con el reloj
            # REAL: `Message.created_at` tiene su default en la columna y no pasa
            # por `bogota_now`, así que no lo alcanza el parche. Se le pone la
            # hora simulada para que el segundo tick vea lo que vería producción.
            _sellar_ultimo_nuestro(c, datetime(2026, 9, 28, 15, 0))
            segundo = _corre(datetime(2026, 9, 28, 10, 30))

            assert primero == ["lead_seguimiento_primer_toque"]
            assert segundo == [], "le mandó el segundo toque media hora después"
            assert A.Conversation.query.get(c.id).followup_count == 1

    def test_el_segundo_llega_a_la_semana_del_primero(self):
        with A.app.app_context():
            _conv(count=1, pausa=None,
                  escribio=datetime(2026, 9, 1, 15, 0),
                  contestamos=datetime(2026, 9, 20, 15, 0))   # el primer toque
            # A la semana del mensaje del cliente ya pasó, pero del nuestro no.
            assert _corre(datetime(2026, 9, 24, 10, 0)) == []
            assert _corre(datetime(2026, 9, 28, 10, 0)) == ["lead_seguimiento_cierre_semana"]


class TestElPanelLoMuestra:
    """Si la pausa no se ve, quien mira el panel cree que el lead se quedó sin
    seguimiento y le escribe encima — rompiendo el mismo acuerdo."""

    @pytest.fixture
    def admin(self, client):
        login_as(client, make_user(f"adm_fp{next(_u)}", role="admin"))
        return client

    def test_la_fila_avisa_cuando_hay_que_retomar(self, admin):
        with A.app.app_context():
            _conv(pausa=A.bogota_today() + timedelta(days=5),
                  escribio=datetime(2026, 9, 7, 14, 22))
        cuerpo = admin.get("/whatsapp").data.decode()
        assert "Retomar" in cuerpo

    def test_sin_fecha_no_aparece_el_aviso(self, admin):
        with A.app.app_context():
            _conv(pausa=None, escribio=datetime(2026, 9, 7, 14, 22))
        # Se busca la etiqueta y no la clase: el CSS de la clase está siempre
        # en la página, tenga o no alguna fila con fecha.
        assert "Retomar" not in admin.get("/whatsapp").data.decode()

    def test_una_fecha_ya_pasada_deja_de_avisar(self, admin):
        """Ya se retomó: seguir mostrándolo sería un recordatorio que miente."""
        with A.app.app_context():
            _conv(pausa=A.bogota_today() - timedelta(days=1),
                  escribio=datetime(2026, 9, 7, 14, 22))
        assert "Retomar" not in admin.get("/whatsapp").data.decode()


class TestElPromptSabeCuandoMarcarla:
    PROMPT = A.NOXA_SYSTEM_PROMPT

    def test_cubre_que_mariana_misma_se_comprometa(self):
        """El caso de producción: lo dijo ella, el cliente no pidió nada."""
        i = self.PROMPT.index("CUANDO QUEDA UNA FECHA FUTURA EN LA MESA")
        bloque = self.PROMPT[i:i + 2000]
        assert "TÚ te comprometes a escribirle en una fecha" in bloque
        assert "no importa si él contestó o no" in bloque

    def test_cubre_que_el_cliente_diga_cuando_estara_listo(self):
        i = self.PROMPT.index("CUANDO QUEDA UNA FECHA FUTURA EN LA MESA")
        assert "me entregan el carro en 3 semanas" in self.PROMPT[i:i + 2000]

    def test_sigue_explicando_el_formato_exacto(self):
        """El marcador se parsea con una expresión regular exacta: si el prompt
        deja de mostrar el formato, Mariana escribe algo parecido y no se
        detecta nada."""
        assert "[ESPERAR: <AAAA-MM-DD>]" in self.PROMPT
        assert A._ESPERAR_RE.match("[ESPERAR: 2026-09-14]")
