"""Filtro de fechas de la bandeja de WhatsApp.

Filtra por el día del PRIMER mensaje de la conversación: importa cuándo entró el
lead, no cuándo se le contestó de último. Una conversación que arrancó el 31 de
agosto y siguió viva hasta el 3 de septiembre pertenece a agosto.

El filtrado en sí lo hace el navegador sobre `data-primer`, así que lo que se
prueba acá es que ese dato llegue bien: con el día correcto y en la zona
correcta. Si el atributo trae el día equivocado, el filtro miente aunque su
comparación sea perfecta.
"""
import itertools
import re
from datetime import datetime, timedelta

import pytest

from conftest import app_module as A
from conftest import login_as, make_user

_telefonos = itertools.count(8300)


@pytest.fixture
def admin(client):
    login_as(client, make_user("admin_fechas", role="admin"))
    return client


@pytest.fixture
def conv():
    """Una conversación vacía; cada test le pone los mensajes que necesita."""
    with A.app.app_context():
        c = A.Conversation(phone=f"+5730088{next(_telefonos):05d}",
                           profile_name="Cliente Fechas")
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


def _mensajes(cid, *fechas_utc):
    with A.app.app_context():
        for i, cuando in enumerate(fechas_utc):
            A.db.session.add(A.Message(
                conversation_id=cid, direction="in" if i % 2 == 0 else "out",
                body=f"mensaje {i}", created_at=cuando))
        A.db.session.commit()


def _primer_dia(client, cid):
    """El `data-primer` que la bandeja le pinta a esa conversación."""
    cuerpo = client.get("/whatsapp").data.decode()
    fila = re.search(rf'href="/whatsapp/{cid}"', cuerpo)
    assert fila, "la conversación no aparece en la bandeja"
    # El atributo va antes del href, dentro de la misma etiqueta <a>.
    inicio = cuerpo.rfind("<a ", 0, fila.start())
    etiqueta = cuerpo[inicio:fila.end()]
    m = re.search(r'data-primer="([^"]*)"', etiqueta)
    assert m, f"la fila no lleva data-primer: {etiqueta[:300]}"
    return m.group(1)


class TestElDiaQueSeFiltra:
    def test_es_el_del_primer_mensaje_no_el_del_ultimo(self, admin, conv):
        """El caso de la hoja: arranca el 31 de agosto, sigue hasta el 3 de
        septiembre. Cuenta como agosto."""
        _mensajes(conv,
                  datetime(2026, 8, 31, 15, 0),
                  datetime(2026, 9, 1, 10, 0),
                  datetime(2026, 9, 3, 18, 0))
        assert _primer_dia(admin, conv) == "2026-08-31"

    def test_una_conversacion_sin_mensajes_usa_cuando_se_creo(self, admin, conv):
        """Existen: se crean al recibir el webhook y el mensaje puede fallar
        después. Sin esto la fila quedaría sin fecha y se escaparía de todo
        rango."""
        with A.app.app_context():
            A.Conversation.query.get(conv).created_at = datetime(2026, 8, 27, 14, 0)
            A.db.session.commit()
        assert _primer_dia(admin, conv) == "2026-08-27"

    def test_va_en_iso_para_poder_compararlo_con_el_input(self, admin, conv):
        """El navegador lo compara como texto contra un <input type="date">, que
        entrega aaaa-mm-dd. Cualquier otro formato rompe la comparación en
        silencio: no da error, solo filtra mal."""
        _mensajes(conv, datetime(2026, 9, 1, 12, 0))
        assert re.fullmatch(r"\d{4}-\d{2}-\d{2}", _primer_dia(admin, conv))


class TestLaZonaHoraria:
    """Los timestamps se guardan en UTC y Bogotá va cinco horas atrás. De noche
    las dos fechas no coinciden, y ahí es donde un filtro por día se equivoca."""

    def test_la_noche_del_31_sigue_siendo_agosto(self, admin, conv):
        """02:00 UTC del 1 de septiembre son las 9 de la noche del 31 en Bogotá.
        Tomando el día en UTC, esta conversación se saldría de un rango que
        termina el 31 de agosto."""
        _mensajes(conv, datetime(2026, 9, 1, 2, 0))
        assert _primer_dia(admin, conv) == "2026-08-31"

    def test_de_dia_las_dos_fechas_coinciden(self, admin, conv):
        """Contraprueba: si no, el test de arriba pasaría con cualquier resta."""
        _mensajes(conv, datetime(2026, 9, 1, 15, 0))
        assert _primer_dia(admin, conv) == "2026-09-01"


class TestLaLogicaDelRango:
    """La comparación vive en JavaScript, pero la regla se puede fijar acá: es
    exactamente la de la hoja que definió el filtro, con los extremos adentro."""

    @staticmethod
    def _entra(primer, desde, hasta):
        return (not desde or primer >= desde) and (not hasta or primer <= hasta)

    @pytest.mark.parametrize("primer, esperado", [
        ("2026-08-31", True),    # arranca dentro, termina después: entra
        ("2026-09-02", False),   # arranca después del hasta
        ("2026-08-20", False),   # arranca antes del desde
        ("2026-08-27", True),
        ("2026-08-26", True),    # el extremo de abajo entra
        ("2026-09-01", True),    # el extremo de arriba entra
    ])
    def test_los_casos_que_definieron_el_filtro(self, primer, esperado):
        assert self._entra(primer, "2026-08-26", "2026-09-01") is esperado

    def test_solo_desde_deja_todo_lo_posterior(self):
        assert self._entra("2026-12-31", "2026-08-26", "")
        assert not self._entra("2026-08-25", "2026-08-26", "")

    def test_solo_hasta_deja_todo_lo_anterior(self):
        assert self._entra("2020-01-01", "", "2026-09-01")
        assert not self._entra("2026-09-02", "", "2026-09-01")
