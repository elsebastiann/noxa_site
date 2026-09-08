"""El descuento tiene que salir en el PDF, no solo en el link.

Una cotización de solo PPF con 7% de convenio: el link mostraba subtotal,
descuento y total, y el PDF salía con los precios de lista y sin una línea de
descuento. Dos documentos de la misma cotización, con el mismo código, diciendo
totales distintos — y el que se manda por correo es el PDF.

La causa: el bloque de totales solo se imprimía si había servicios o si había
descuento SOBRE EL SUBTOTAL DE SERVICIOS. En una cotización de solo PPF ese
subtotal es cero, así que el descuento existía, se aplicaba a los totales por
marca, y el bloque que los imprime no se dibujaba nunca.
"""
import itertools

import pytest

from conftest import app_module as A, make_user
from precios_ppf import precio

_u = itertools.count(1)

GRUPO = "Manijas"


@pytest.fixture
def sesion(client):
    with A.app.app_context():
        uid = make_user(f"dpdf{next(_u)}", role="admin").id
    with client.session_transaction() as sess:
        sess["user_id"] = uid
    return client


def _crear(client, **datos):
    base = {"customer_name": "Andres Rincon", "ppf_coverage": [GRUPO]}
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


def _pdf_arma(code):
    """Arma el PDF y devuelve su tamaño; sirve de guardia de que no revienta."""
    with A.app.app_context():
        cot = A.Quote.query.filter_by(code=code).first()
        buf = A._construir_pdf_cotizacion(cot)
    return len(buf.getvalue() if hasattr(buf, "getvalue") else buf)


class TestUnaCotizacionDeSoloPpfConDescuento:
    def test_los_totales_del_modelo_ya_traen_el_descuento(self, sesion):
        """El cálculo nunca estuvo mal: lo que faltaba era imprimirlo."""
        code = _crear(sesion, discount_type="percentage", discount_value="7",
                      discount_label="CMB Classic")
        try:
            with A.app.app_context():
                c = A.Quote.query.filter_by(code=code).first()
                lista = precio(GRUPO, "Xpel")
                assert c.totales_por_marca["Xpel"] == lista - round(lista * 0.07)
        finally:
            _borrar(code)

    def test_el_pdf_se_arma(self, sesion):
        code = _crear(sesion, discount_type="percentage", discount_value="7",
                      discount_label="CMB Classic")
        try:
            assert _pdf_arma(code) > 1000
        finally:
            _borrar(code)

    def test_el_bloque_de_totales_ya_no_depende_del_subtotal_de_servicios(self):
        """Se mira el código porque el texto del PDF viaja comprimido y buscarlo
        en el binario no probaría nada. Lo que se fija es la condición: mirar
        `_descuento_sobre(subtotal)` es lo que dejaba fuera a las cotizaciones
        de solo PPF."""
        import inspect
        fuente = inspect.getsource(A._construir_pdf_cotizacion)
        assert "if items or cot._descuento_sobre(subtotal):" not in fuente
        assert "if items or (cot.discount_type and cot.discount_value):" in fuente


class TestNoSeRompioLoQueYaFuncionaba:
    def test_sin_descuento_y_sin_servicios_no_se_imprime_el_bloque(self, sesion):
        """La fila "TOTAL PPF" ya dice lo mismo: repetirlo llenaría el documento
        de cifras iguales."""
        import inspect
        code = _crear(sesion)
        try:
            with A.app.app_context():
                c = A.Quote.query.filter_by(code=code).first()
                assert not (c.discount_type and c.discount_value)
                assert not c.items
            assert _pdf_arma(code) > 1000
        finally:
            _borrar(code)

    def test_con_servicios_y_sin_descuento_sigue_saliendo(self, sesion):
        code = _crear(sesion, item_desc=["Chrome Delete"], item_price=["650000"],
                      item_qty=["1"], item_service_id=[""], item_detail=[""],
                      item_warranty=[""])
        try:
            with A.app.app_context():
                assert A.Quote.query.filter_by(code=code).first().items
            assert _pdf_arma(code) > 1000
        finally:
            _borrar(code)

    def test_un_descuento_de_valor_cero_no_cuenta(self, sesion):
        """El formulario limpia el tipo cuando el valor es 0. Si no lo hiciera,
        el PDF imprimiría una línea de "descuento" de cero pesos."""
        code = _crear(sesion, discount_type="percentage", discount_value="0")
        try:
            with A.app.app_context():
                c = A.Quote.query.filter_by(code=code).first()
                assert not (c.discount_type and c.discount_value)
        finally:
            _borrar(code)
