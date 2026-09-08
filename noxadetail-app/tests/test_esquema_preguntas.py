"""El esquema que se le manda al modelo tiene que decir QUÉ guarda cada columna,
no solo cómo se llama.

Preguntando "cuántos mensajes han entrado por día" el modelo escribió
`direction = 'inbound'` contra una columna que guarda 'in'. La consulta corrió
sin error y devolvió cero filas — el peor resultado posible, porque un cero se
lee como "no pasó nada" y no como "pregunté mal".

Los valores se leen de la base, no de una lista escrita a mano: a mano se
desactualiza en silencio con la próxima migración, que es exactamente el
problema que el esquema autogenerado ya venía resolviendo para las columnas.
"""
import itertools
from datetime import datetime

import pytest

from conftest import app_module as A

_tel = itertools.count(6600)


@pytest.fixture
def conversacion():
    with A.app.app_context():
        c = A.Conversation(phone=f"+5730066{next(_tel):05d}",
                           profile_name="Cliente Esquema", status="En proceso")
        A.db.session.add(c)
        A.db.session.commit()
        for d in ("in", "out", "in"):
            A.db.session.add(A.Message(conversation_id=c.id, direction=d, body="hola",
                                       created_at=datetime(2026, 9, 3, 12, 0)))
        A.db.session.commit()
        cid = c.id
    yield cid
    with A.app.app_context():
        A.Message.query.filter_by(conversation_id=cid).delete()
        fila = A.Conversation.query.get(cid)
        if fila:
            A.db.session.delete(fila)
        A.db.session.commit()


def _esquema():
    with A.app.app_context():
        return A._esquema_para_preguntas()


class TestElEsquemaDiceLosValores:
    def test_direction_dice_in_y_out(self, conversacion):
        """El caso exacto que falló."""
        linea = next(l for l in _esquema().splitlines() if l.startswith("whatsapp_messages("))
        assert "valores: in|out" in linea

    def test_no_aparece_el_valor_que_el_modelo_habia_inventado(self, conversacion):
        assert "inbound" not in _esquema()

    def test_los_estados_de_una_cita_tambien(self, conversacion):
        """Son una lista cerrada y el modelo los usa en casi toda pregunta de
        citas."""
        with A.app.app_context():
            hay = A.Appointment.query.first() is not None
        if not hay:
            pytest.skip("sin citas en la base de prueba")
        linea = next(l for l in _esquema().splitlines() if l.startswith("appointments("))
        assert "status" in linea and "valores:" in linea


class TestNoSeLeMandanDatosPersonales:
    """El esquema viaja entero en cada pregunta. Listar los valores de una
    columna de nombres o teléfonos sería mandarle la base de clientes al modelo
    cada vez — y en un negocio pequeño el filtro por cantidad no lo frenaría."""

    def test_ni_nombres_ni_telefonos(self, conversacion):
        esquema = _esquema()
        with A.app.app_context():
            conv = A.Conversation.query.get(conversacion)
            assert conv.phone not in esquema
            assert conv.profile_name not in esquema

    @pytest.mark.parametrize("columna", [
        "customer_name", "phone", "plate", "body", "description", "notes",
    ])
    def test_esas_columnas_van_sin_muestra(self, columna, conversacion):
        """Se comprueba la regla y no solo un dato: mañana entra otro cliente y
        el test tiene que seguir cuidando lo mismo."""
        assert A._COLUMNAS_SIN_MUESTRA.search(columna), \
            f"«{columna}» debería estar excluida de las muestras"

    def test_una_columna_de_texto_libre_no_se_lista(self, conversacion):
        """Aunque no esté en la lista negra: si tiene muchos valores distintos
        no es una lista de opciones, es un dato."""
        with A.app.app_context():
            assert A._valores_posibles(None, "whatsapp_messages",
                                       {"name": "body", "type": "TEXT"}) == ""


class TestSigueSiendoUnEsquemaUtil:
    def test_las_tablas_vetadas_no_entran(self, conversacion):
        esquema = _esquema()
        for tabla in A.TABLAS_VETADAS:
            assert f"{tabla}(" not in esquema

    def test_la_tabla_de_ingresos_sigue_declarada(self, conversacion):
        """No es una tabla real; se materializa por consulta. Si se cae del
        esquema, el modelo vuelve a calcular la plata a mano desde appointments,
        que es justo lo que el prompt prohíbe."""
        assert "ingresos(fecha TEXT" in _esquema()

    def test_es_estable_entre_llamadas(self, conversacion):
        """Va dentro del prompt cacheado: si el orden cambiara entre preguntas,
        cada una pagaría el esquema completo de nuevo."""
        assert _esquema() == _esquema()
