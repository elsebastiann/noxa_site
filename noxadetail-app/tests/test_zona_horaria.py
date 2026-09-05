"""Todo lo que sea "hoy" o "qué día fue esto" se calcula en hora de Bogotá.

El servidor de Railway corre en UTC y Colombia va cinco horas atrás, así que
entre las 7 de la noche y la medianoche el día en UTC ya es el siguiente. Todo
cálculo que use el día del servidor se corre uno en esa franja: el formulario de
gastos precarga mañana, la ventana de agendamiento cierra el día de hoy, una
tarjeta de seguimiento dice "escrita hace -1 días".

No es hipotético — ya había pasado con el recordatorio de citas, que corre
justo a las 7 PM, y se arregló solo ahí. Estos tests fijan la regla completa y
la de abajo impide que vuelva a entrar por otro lado.
"""
import itertools
import pathlib
import re
from datetime import date, datetime, timedelta

import pytest

from conftest import app_module as A, make_user

_u = itertools.count(1)

RAIZ = pathlib.Path(__file__).resolve().parent.parent


class TestLosAyudantes:
    def test_la_noche_en_bogota_todavia_es_el_dia_anterior(self):
        """02:00 UTC del 1 de septiembre son las 9 de la noche del 31 acá."""
        assert A.dia_bogota(datetime(2026, 9, 1, 2, 0)) == date(2026, 8, 31)

    def test_de_dia_los_dos_calendarios_coinciden(self):
        """Contraprueba: si no, el de arriba pasaría restando un día siempre."""
        assert A.dia_bogota(datetime(2026, 9, 1, 15, 0)) == date(2026, 9, 1)

    def test_sin_fecha_no_inventa_una(self):
        assert A.dia_bogota(None) is None
        assert A.hora_bogota_naive(None) is None

    def test_la_hora_se_expresa_en_bogota(self):
        """Colombia no tiene horario de verano: son cinco horas fijas."""
        assert A.hora_bogota_naive(datetime(2026, 9, 1, 15, 0)) == datetime(2026, 9, 1, 10, 0)

    def test_hoy_es_el_hoy_de_bogota_no_el_del_servidor(self):
        """Amarra las dos funciones: si `bogota_today` volviera a ser
        `date.today()`, en la franja de la noche dejarían de coincidir."""
        assert A.bogota_today() == A.dia_bogota(datetime.utcnow())


class TestNoQuedaNadaCalculandoEnUtc:
    """Guardas de regresión. El error es invisible 19 horas al día, así que no
    se puede confiar en que alguien lo note al revisar un cambio."""

    def test_el_codigo_no_usa_date_today(self):
        codigo = (RAIZ / "app.py").read_text(encoding="utf-8")
        # Se busca la llamada, no la palabra: los comentarios que explican por
        # qué NO se usa deben poder nombrarla.
        sobras = [n for n, linea in enumerate(codigo.splitlines(), 1)
                  if "date.today()" in linea and not linea.strip().startswith("#")
                  and '"""' not in linea and "`date.today()`" not in linea]
        assert not sobras, f"date.today() sigue vivo en app.py, líneas {sobras}"

    def test_ninguna_plantilla_imprime_un_timestamp_crudo(self):
        """`created_at.strftime(...)` en una plantilla pinta la hora UTC tal
        cual: cinco horas adelante, sin nada que lo delate. El filtro
        `hora_bogota` existe justo para eso."""
        malas = []
        for html in (RAIZ / "templates").glob("*.html"):
            for n, linea in enumerate(html.read_text(encoding="utf-8").splitlines(), 1):
                if re.search(r"_at\.strftime\(", linea):
                    malas.append(f"{html.name}:{n}")
        assert not malas, "usa | hora_bogota(...) en: " + ", ".join(malas)


class TestLaFechaDeUnaCotizacion:
    """La que ve el cliente en el PDF y la que decide hasta cuándo vale."""

    @pytest.fixture
    def sesion(self, client):
        with A.app.app_context():
            uid = make_user(f"tz{next(_u)}", role="admin").id
        with client.session_transaction() as sess:
            sess["user_id"] = uid
        return client

    def test_una_cotizacion_de_la_noche_no_sale_fechada_mañana(self, sesion):
        """Hecha a las 9 de la noche del 31, el documento decía 1 de
        septiembre: la fecha que el cliente lee no era la del día en que se la
        mandaron."""
        r = sesion.post("/quotes/new", data={"customer_name": "Laura Ortiz",
                                             "ppf_coverage": ["Manijas"]})
        code = r.headers["Location"].rstrip("/").split("/")[-1]
        try:
            with A.app.app_context():
                c = A.Quote.query.filter_by(code=code).first()
                c.created_at = datetime(2026, 9, 1, 2, 0)   # 31 ago, 9 PM en Bogotá
                A.db.session.commit()
            cuerpo = sesion.get(f"/quotes/{code}").data.decode()
            assert "31/08/2026" in cuerpo
            assert "01/09/2026" not in cuerpo
        finally:
            with A.app.app_context():
                c = A.Quote.query.filter_by(code=code).first()
                if c:
                    A.db.session.delete(c)
                    A.db.session.commit()

    def test_la_vigencia_se_cuenta_desde_ese_mismo_dia(self, sesion):
        """Si la fecha impresa y la del vencimiento salieran de calendarios
        distintos, el documento se contradiría solo: emitida el 31 y vigente
        "30 días" hasta el 1 + 30."""
        r = sesion.post("/quotes/new", data={"customer_name": "Laura Ortiz",
                                             "ppf_coverage": ["Manijas"],
                                             "valid_days": "15"})
        code = r.headers["Location"].rstrip("/").split("/")[-1]
        try:
            with A.app.app_context():
                c = A.Quote.query.filter_by(code=code).first()
                assert c.valid_until == A.dia_bogota(c.created_at) + timedelta(days=15)
        finally:
            with A.app.app_context():
                c = A.Quote.query.filter_by(code=code).first()
                if c:
                    A.db.session.delete(c)
                    A.db.session.commit()
