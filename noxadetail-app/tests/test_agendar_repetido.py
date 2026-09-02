"""Repetir [AGENDAR:] con los mismos datos no es un error: la cita ya está.

Caso real (Julio César Gómez, placa GBU708, cita del 05/09 a las 15:00):
Mariana agendó, se lo confirmó al cliente, el cliente le dio las gracias — y en
ese turno ella volvió a emitir el marcador. El guardia de duplicados lo trató
como fallo, le devolvió "no se pudo crear la cita", y ella terminó
preguntándole al cliente si quería CONSERVAR o MOVER una cita que ella misma
acababa de crear un mensaje atrás. El cliente tuvo que responderle "acabo de
agendarla".

Dos daños: Mariana queda como si no recordara lo que hizo, y le abre la puerta
al cliente a desagendar algo que estaba perfecto.

El prompt ya le prohíbe repetir el marcador (línea "Emítelo UNA sola vez por
cita") y aun así lo repite, así que el arreglo no puede ser otra regla de
prompt: la idempotencia tiene que estar en el código.
"""
import itertools

import pytest

from conftest import app_module as A
# Una sola definición de estos ayudantes, viven con los tests de festivos.
from test_festivos import proximo_habil, servicio_diagnostico  # noqa: F401

_tel = itertools.count(8300)
_placas = itertools.count(1)


@pytest.fixture
def conv():
    with A.app.app_context():
        c = A.Conversation(phone=f"+5730088{next(_tel):05d}", profile_name="Julio César")
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


@pytest.fixture
def placa():
    """Placa única por test: el guardia busca por placa, así que reusarla
    entre tests los haría interferir entre sí."""
    p = f"RPT{next(_placas):03d}"
    yield p
    with A.app.app_context():
        A.Appointment.query.filter_by(plate=p).delete()
        A.db.session.commit()


def _datos(placa, fecha, hora="10:00"):
    return {"nombre": "Julio César Gómez", "celular": "3001234567",
            "vehiculo": "Automovil", "placa": placa,
            "fecha": fecha.isoformat(), "hora": hora}


def _agendar(cid, datos):
    with A.app.app_context():
        conv = A.Conversation.query.get(cid)
        ok, detalle, appt = A.book_diagnostic_from_bot(conv, datos)
        # Se devuelve el id y no el objeto: fuera del app_context la instancia
        # queda desligada de la sesión y tocarla revienta.
        return ok, detalle, (appt.id if appt else None)


def _cuantas(placa):
    with A.app.app_context():
        return A.Appointment.query.filter_by(plate=placa).count()


class TestPedirLaMismaCitaDosVeces:
    def test_la_primera_vez_se_crea(self, servicio_diagnostico, conv, placa):
        """Contraprueba: sin esto los demás tests pasarían aunque nunca se
        hubiera creado nada."""
        ok, _detalle, appt_id = _agendar(conv, _datos(placa, proximo_habil()))
        assert ok is True
        assert appt_id is not None
        assert _cuantas(placa) == 1

    def test_repetirla_no_crea_una_segunda(self, servicio_diagnostico, conv, placa):
        datos = _datos(placa, proximo_habil())
        _agendar(conv, datos)
        _agendar(conv, datos)
        assert _cuantas(placa) == 1, "se duplicó la cita"

    def test_repetirla_no_es_un_fallo(self, servicio_diagnostico, conv, placa):
        """Lo que rompía la conversación: el segundo intento devolvía False y
        Mariana recibía un '[Sistema: no se pudo crear la cita]'."""
        datos = _datos(placa, proximo_habil())
        _agendar(conv, datos)
        ok, detalle, _ = _agendar(conv, datos)
        assert ok is True, detalle

    def test_no_reporta_haber_creado_una_cita(self, servicio_diagnostico, conv, placa):
        """El tercer valor es la cita que ESA llamada creó. En la repetición no
        creó ninguna, y por eso va None: es lo que evita que a Diana le llegue
        un segundo aviso de la misma cita."""
        datos = _datos(placa, proximo_habil())
        _agendar(conv, datos)
        _ok, _detalle, appt_id = _agendar(conv, datos)
        assert appt_id is None

    def test_apunta_a_la_cita_que_ya_existia(self, servicio_diagnostico, conv, placa):
        """El detalle que se registra tiene que identificar la cita real, para
        que el log sirva para algo cuando esto se revise."""
        datos = _datos(placa, proximo_habil())
        _ok, _d, primera = _agendar(conv, datos)
        _ok2, detalle, _ = _agendar(conv, datos)
        assert f"#{primera}" in detalle, detalle


class TestElChoqueDeVerdadSigueAvisando:
    """El arreglo no puede tragarse el caso legítimo: el vehículo ya tiene una
    cita a OTRA hora. Ahí sí hay que avisarle a Mariana para que le pregunte al
    cliente si la conserva o la mueve."""

    def test_otra_hora_el_mismo_dia_sigue_siendo_choque(self, servicio_diagnostico, conv, placa):
        dia = proximo_habil()
        _agendar(conv, _datos(placa, dia, "10:00"))
        ok, detalle, _ = _agendar(conv, _datos(placa, dia, "11:00"))
        assert ok is False
        assert "ya tiene una cita" in detalle, detalle

    def test_no_se_crea_la_segunda_cita_en_el_choque(self, servicio_diagnostico, conv, placa):
        dia = proximo_habil()
        _agendar(conv, _datos(placa, dia, "10:00"))
        _agendar(conv, _datos(placa, dia, "11:00"))
        assert _cuantas(placa) == 1

    def test_le_dice_a_mariana_que_use_reagendar(self, servicio_diagnostico, conv, placa):
        """Sin esta pista Mariana escalaba a un humano para mover una cita que
        ella misma puede mover."""
        dia = proximo_habil()
        _agendar(conv, _datos(placa, dia, "10:00"))
        _ok, detalle, _ = _agendar(conv, _datos(placa, dia, "11:00"))
        assert "REAGENDAR" in detalle, detalle
