"""Prioridad de un lead: "todavía no sé" no es "no vale la pena".

Un Renault Arkana 2026 aparecía como prioridad Baja solo porque nadie lo había
calificado — indistinguible de los leads de descarte, y por eso invisible tanto
en la bandeja como en el tablero de seguimiento.
"""
import datetime as dt

import pytest

from conftest import app_module as A


class TestSinCalificar:
    def test_sin_calificacion_no_es_baja(self):
        assert A._compute_priority("En proceso", None) == "Sin calificar"

    def test_una_calificacion_baja_de_verdad_si_es_baja(self):
        """Acá sí hubo juicio: se evaluó y dio bajo. Es distinto de no saber."""
        assert A._compute_priority("En proceso", 0) == "Baja"
        assert A._compute_priority("En proceso", 1) == "Baja"

    def test_no_cambia_lo_que_ya_funcionaba(self):
        assert A._compute_priority("En proceso", 5) == "Alta"
        assert A._compute_priority("En proceso", 4) == "Alta"
        assert A._compute_priority("En proceso", 3) == "Media"
        assert A._compute_priority("En proceso", 2) == "Media"

    def test_un_no_interesado_sin_calificar_sigue_siendo_baja(self):
        """Ahí sí hubo una señal clara del cliente: dijo que no. No es un lead
        pendiente de revisar."""
        assert A._compute_priority("No interesado", None) == "Baja"

    def test_remarketing_intacto(self):
        assert A._compute_priority("No interesado", 5) == "Remarketing"

    def test_esta_en_la_lista_de_filtros(self):
        """Si no está en PRIORITY_LEVELS no se puede filtrar por ella, que es
        justo lo que hace falta para ir a revisarlas."""
        assert "Sin calificar" in A.PRIORITY_LEVELS


class TestNoSePierdenEnElTablero:
    @pytest.fixture(autouse=True)
    def _limpio(self):
        def borrar():
            with A.app.app_context():
                A.SeguimientoGestion.query.delete()
                for c in A.Conversation.query.filter(A.Conversation.phone.like("+5730012%")).all():
                    A.Message.query.filter_by(conversation_id=c.id).delete()
                    A.db.session.delete(c)
                A.db.session.commit()
        borrar()
        yield
        borrar()

    def _conv(self, tel, **kw):
        datos = dict(phone=tel, profile_name="Robinson", status="En proceso",
                     bot_active=True, calificacion=None, carro="", marca="")
        datos.update(kw)
        datos["priority"] = A._compute_priority(datos["status"], datos["calificacion"])
        c = A.Conversation(**datos)
        A.db.session.add(c)
        A.db.session.commit()
        return c

    def test_un_lead_sin_calificar_con_carro_si_aparece(self):
        """El caso real: Renault Arkana 2026, conversación avanzada, sin
        calificar. Antes no salía en ninguna parte."""
        self._conv("+573001200001", carro="Renault Arkana 2026", marca="Renault")

        tablero = A._tablero_seguimiento()
        col = next(c for c in tablero["columnas"] if c["clave"] == "caliente")
        assert "+573001200001" in [t["telefono"] for t in col["tarjetas"]]

    def test_sin_carro_todavia_no_entra(self):
        """Sin saber ni qué carro tiene no hubo conversación real: meterlo
        llenaría la columna de gente que solo dijo "hola"."""
        self._conv("+573001200002", carro="")

        tablero = A._tablero_seguimiento()
        col = next(c for c in tablero["columnas"] if c["clave"] == "caliente")
        assert "+573001200002" not in [t["telefono"] for t in col["tarjetas"]]

    def test_un_lead_evaluado_como_bajo_sigue_fuera(self):
        self._conv("+573001200003", calificacion=1, carro="Renault Logan 2010")

        tablero = A._tablero_seguimiento()
        col = next(c for c in tablero["columnas"] if c["clave"] == "caliente")
        assert "+573001200003" not in [t["telefono"] for t in col["tarjetas"]]
