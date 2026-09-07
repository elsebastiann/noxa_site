"""El aviso de "valores de referencia": una sola vez, y se puede callar.

Estaba dos veces en el PDF —un recuadro antes de la sección de PPF y una línea
en el pie— diciendo lo mismo con otras palabras. Una advertencia repetida se lee
como letra menuda y deja de advertir. Queda la del pie.

Y cuando la cotización se hizo con el carro a la vista, los valores ya son los
definitivos: ahí el aviso no solo sobra, resta — le quita firmeza a una cifra
que sí está confirmada. Para eso está la casilla "Precios confirmados sobre el
vehículo".
"""
import itertools
import re

import pytest

from conftest import app_module as A, make_user

_u = itertools.count(1)

# Lo que dice el aviso, en cualquiera de sus redacciones.
AVISO = re.compile(r"valores? (son |de )?(estimad|referencia)", re.IGNORECASE)


@pytest.fixture
def sesion(client):
    with A.app.app_context():
        uid = make_user(f"av{next(_u)}", role="admin").id
    with client.session_transaction() as sess:
        sess["user_id"] = uid
    return client


def _crear(client, **datos):
    base = {"customer_name": "Laura Ortiz", "ppf_coverage": ["Manijas"]}
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


def _texto_del_pdf(code):
    """El PDF armado, como texto plano. Se leen los flowables en vez del binario:
    lo que importa es qué párrafos entraron, no cómo quedaron dibujados."""
    with A.app.app_context():
        cot = A.Quote.query.filter_by(code=code).first()
        buf = A._construir_pdf_cotizacion(cot)
    crudo = buf.getvalue() if hasattr(buf, "getvalue") else buf
    return crudo


class TestUnaSolaVezEnElPdf:
    def test_el_pdf_se_arma(self, sesion):
        """Guardia mínima: si reventara, los tests de abajo pasarían vacíos."""
        code = _crear(sesion)
        try:
            assert len(_texto_del_pdf(code)) > 1000
        finally:
            _borrar(code)

    def test_el_recuadro_de_arriba_ya_no_se_construye(self):
        """Se mira el código y no el PDF: el texto va comprimido dentro del
        binario, así que buscarlo ahí no prueba nada. Lo que se fija es que la
        función no vuelva a armar el recuadro que se quitó."""
        import inspect
        fuente = inspect.getsource(A._construir_pdf_cotizacion)
        assert "Cada vehículo es distinto" not in fuente, \
            "volvió el recuadro de aviso arriba de la sección de PPF"
        assert "Los valores de PPF son estimados" in fuente, \
            "se perdió también el aviso del pie, que sí debe quedar"


class TestLaCasillaLoCalla:
    def test_por_defecto_la_cotizacion_es_estimada(self, sesion):
        """El default seguro es el que advierte: la mayoría se cotizan sin haber
        visto el carro."""
        code = _crear(sesion)
        try:
            with A.app.app_context():
                assert A.Quote.query.filter_by(code=code).first().precios_fijos is False
        finally:
            _borrar(code)

    def test_marcarla_la_deja_con_precios_fijos(self, sesion):
        code = _crear(sesion, precios_fijos="1")
        try:
            with A.app.app_context():
                assert A.Quote.query.filter_by(code=code).first().precios_fijos is True
        finally:
            _borrar(code)

    def test_desmarcarla_devuelve_el_aviso(self, sesion):
        """Una casilla desmarcada no se envía. Si su ausencia se leyera como "no
        se tocó", el aviso no podría volver nunca."""
        code = _crear(sesion, precios_fijos="1")
        try:
            sesion.post(f"/quotes/{code}/edit",
                        data={"customer_name": "Laura Ortiz", "ppf_coverage": ["Manijas"]})
            with A.app.app_context():
                assert A.Quote.query.filter_by(code=code).first().precios_fijos is False
        finally:
            _borrar(code)

    def test_el_cliente_no_ve_el_aviso_en_el_link(self, sesion):
        code = _crear(sesion, precios_fijos="1")
        try:
            with A.app.app_context():
                token = A.Quote.query.filter_by(code=code).first().public_token
            assert not AVISO.search(sesion.get(f"/c/{token}").data.decode())
        finally:
            _borrar(code)

    def test_sin_marcarla_el_link_si_lo_muestra(self, sesion):
        """Contraprueba: si no, el test de arriba pasaría porque el aviso
        desapareció del link para todos."""
        code = _crear(sesion)
        try:
            with A.app.app_context():
                token = A.Quote.query.filter_by(code=code).first().public_token
            assert AVISO.search(sesion.get(f"/c/{token}").data.decode())
        finally:
            _borrar(code)

    def test_la_vista_interna_dice_cuál_de_las_dos_es(self, sesion):
        """Quien la abre tiene que saber si el cliente está viendo el aviso o no,
        sin tener que abrir el PDF para averiguarlo."""
        fija = _crear(sesion, precios_fijos="1")
        estimada = _crear(sesion)
        try:
            assert "Precios confirmados sobre el vehículo" in sesion.get(f"/quotes/{fija}").data.decode()
            assert "Valores de referencia" in sesion.get(f"/quotes/{estimada}").data.decode()
        finally:
            _borrar(fija)
            _borrar(estimada)


class TestAlDuplicar:
    def test_la_copia_vuelve_a_ser_estimada(self, sesion):
        """Se duplica para cotizar OTRO carro. Heredar "precios confirmados"
        sería afirmar algo que nadie verificó sobre ese vehículo."""
        code = _crear(sesion, precios_fijos="1")
        r = sesion.post(f"/quotes/{code}/duplicate", follow_redirects=False)
        copia = r.headers["Location"].rstrip("/").rsplit("/", 2)[-2]
        try:
            with A.app.app_context():
                assert A.Quote.query.filter_by(code=copia).first().precios_fijos is False
        finally:
            _borrar(code)
            _borrar(copia)
