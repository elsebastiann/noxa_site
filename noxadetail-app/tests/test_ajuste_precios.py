"""El ajuste porcentual es interno: sube los precios, pero no se ve.

Quien cotiza puede subirle un % a los precios de lista mientras arma la
cotización. El cliente ve los valores YA con el aumento adentro — nunca el
aumento aparte, porque eso le diría cuánto se le movió el precio de lista.
"""
import itertools
import json

import pytest

from conftest import app_module as A, make_user
from precios_ppf import foto, precio

_u = itertools.count(1)


@pytest.fixture
def sesion(client):
    with A.app.app_context():
        uid = make_user(f"aj{next(_u)}", role="admin").id
    with client.session_transaction() as sess:
        sess["user_id"] = uid
    return client


def _crear(client, **datos):
    base = {"customer_name": "Laura Ortiz"}
    base.update(datos)
    r = client.post("/quotes/new", data=base, follow_redirects=False)
    assert r.status_code == 302
    return r.headers["Location"].rstrip("/").split("/")[-1]


def _borrar(code):
    with A.app.app_context():
        c = A.Quote.query.filter_by(code=code).first()
        if c:
            A.db.session.delete(c)
            A.db.session.commit()


class TestElAjusteSubeLosPrecios:
    def test_el_precio_congelado_ya_lo_trae(self, sesion):
        base = precio("Manijas", "Xpel")
        code = _crear(sesion, ppf_coverage=["Manijas"], ajuste_pct="20")
        try:
            with A.app.app_context():
                guardado = A.Quote.query.filter_by(code=code).first().ppf_items[0].precios["Xpel"]
            assert guardado == round(base * 1.2 / 1000) * 1000
        finally:
            _borrar(code)

    def test_sin_ajuste_queda_el_de_lista(self, sesion):
        """Contraprueba: si no, el test de arriba pasaría por cualquier motivo."""
        code = _crear(sesion, ppf_coverage=["Manijas"])
        try:
            with A.app.app_context():
                c = A.Quote.query.filter_by(code=code).first()
                assert c.ppf_items[0].precios["Xpel"] == precio("Manijas", "Xpel")
                assert c.ajuste_pct is None
        finally:
            _borrar(code)

    def test_tambien_sube_el_adicional_de_fotocromatico(self, sesion):
        extra = foto("Farolas y Stops", "Xpel")
        code = _crear(sesion, ppf_coverage=["Farolas y Stops"],
                      **{"ppf_foto::Farolas y Stops": "1", "ajuste_pct": "20"})
        try:
            with A.app.app_context():
                it = A.Quote.query.filter_by(code=code).first().ppf_items[0]
                assert it.precios_foto["Xpel"] == round(extra * 1.2 / 1000) * 1000
        finally:
            _borrar(code)

    def test_lo_calcula_el_servidor_no_el_navegador(self, sesion):
        """Los precios de catálogo se congelan en el servidor justamente para
        que no se puedan alterar desde el formulario. Si el aumento llegara ya
        calculado, se abriría esa puerta."""
        import inspect
        fuente = inspect.getsource(A._leer_formulario_de_cotizacion)
        assert 'request.form.get("ajuste_pct")' in fuente
        assert "def con_ajuste" in fuente

    def test_un_porcentaje_absurdo_se_topa(self, sesion):
        code = _crear(sesion, ppf_coverage=["Manijas"], ajuste_pct="9999")
        try:
            with A.app.app_context():
                assert A.Quote.query.filter_by(code=code).first().ajuste_pct == 200
        finally:
            _borrar(code)

    def test_redondea_a_mil(self, sesion):
        """Una cotización con cifras como $2.587.431 se ve calculada con
        calculadora."""
        code = _crear(sesion, ppf_coverage=["Full Front"], ajuste_pct="13")
        try:
            with A.app.app_context():
                for v in A.Quote.query.filter_by(code=code).first().ppf_items[0].precios.values():
                    assert v % 1000 == 0, v
        finally:
            _borrar(code)


class TestElClienteNoVeElAjuste:
    def test_el_link_no_lo_menciona(self, sesion):
        code = _crear(sesion, ppf_coverage=["Manijas"], ajuste_pct="20")
        try:
            with A.app.app_context():
                token = A.Quote.query.filter_by(code=code).first().public_token
            cuerpo = sesion.get(f"/c/{token}").data.decode().lower()
            for rastro in ("ajuste", "20%", "precio de lista", "incremento"):
                assert rastro not in cuerpo, f"se le coló «{rastro}» al cliente"
        finally:
            _borrar(code)

    def test_el_pdf_no_lo_menciona(self, sesion):
        import inspect
        fuente = inspect.getsource(A._construir_pdf_cotizacion)
        assert "ajuste_pct" not in fuente, "el PDF no puede nombrar el ajuste"

    def test_pero_las_cifras_del_cliente_ya_lo_traen(self, sesion):
        """Es la razón de meterlo en el precio y no en una línea aparte: si el
        cliente viera el precio de lista y un total distinto, no cuadraría."""
        base = precio("Manijas", "Xpel")
        code = _crear(sesion, ppf_coverage=["Manijas"], ajuste_pct="20")
        try:
            with A.app.app_context():
                c = A.Quote.query.filter_by(code=code).first()
                esperado = round(base * 1.2 / 1000) * 1000
                assert c.ppf_totales["Xpel"] == esperado
                token = c.public_token
            # El link arma los montos en JavaScript a partir del JSON que le
            # embebemos, así que en el HTML servido la cifra viaja cruda.
            assert str(esperado) in sesion.get(f"/c/{token}").data.decode()
        finally:
            _borrar(code)

    def test_la_vista_interna_si_lo_dice(self, sesion):
        code = _crear(sesion, ppf_coverage=["Manijas"], ajuste_pct="20")
        try:
            cuerpo = sesion.get(f"/quotes/{code}").data.decode()
            assert "+20%" in cuerpo and "solo visible aquí" in cuerpo
        finally:
            _borrar(code)


class TestConvieneConElDescuento:
    def test_el_descuento_se_aplica_sobre_el_precio_ya_subido(self, sesion):
        """El orden importa: primero sube el precio de lista, después se
        descuenta. Al revés daría otra cifra."""
        base = precio("Manijas", "Xpel")
        code = _crear(sesion, ppf_coverage=["Manijas"], ajuste_pct="20",
                      discount_type="percentage", discount_value="10")
        try:
            with A.app.app_context():
                c = A.Quote.query.filter_by(code=code).first()
                subido = round(base * 1.2 / 1000) * 1000
                assert c.totales_por_marca["Xpel"] == subido - round(subido * 0.1)
        finally:
            _borrar(code)
