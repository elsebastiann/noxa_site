"""Precio exacto para un grupo del catálogo.

Los precios de lista son una referencia: cada carro es distinto y un grupo puede
no valer lo mismo en este que en el promedio. Hasta ahora la única salida era
armar a mano un grupo que ya existía, con el trabajo de volver a elegirle las
partes y el riesgo de que quedara con otro nombre en el documento.

Lo que se escribe a mano manda sobre el catálogo Y sobre el ajuste porcentual:
ya es la cifra que se decidió cobrar, no un precio de lista al que haya que
subirle nada.
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
        uid = make_user(f"px{next(_u)}", role="admin").id
    with client.session_transaction() as sess:
        sess["user_id"] = uid
    return client


def _crear(client, **datos):
    base = {"customer_name": "Laura Ortiz"}
    base.update(datos)
    r = client.post("/quotes/new", data=base, follow_redirects=False)
    assert r.status_code == 302
    return r.headers["Location"].rstrip("/").split("/")[-1]


def _editar(client, code, **datos):
    base = {"customer_name": "Laura Ortiz"}
    base.update(datos)
    r = client.post(f"/quotes/{code}/edit", data=base, follow_redirects=False)
    assert r.status_code == 302
    return code


def _precios(code, cobertura=GRUPO):
    with A.app.app_context():
        c = A.Quote.query.filter_by(code=code).first()
        it = next(x for x in c.ppf_items if x.coverage == cobertura)
        return it.precios


def _borrar(code):
    with A.app.app_context():
        c = A.Quote.query.filter_by(code=code).first()
        if c:
            A.db.session.delete(c)
            A.db.session.commit()


class TestElValorEscritoManda:
    def test_reemplaza_al_de_lista(self, sesion):
        code = _crear(sesion, ppf_coverage=[GRUPO],
                      **{f"ppf_precio::{GRUPO}||Xpel": "777000"})
        try:
            assert _precios(code)["Xpel"] == 777000
        finally:
            _borrar(code)

    def test_el_ajuste_no_se_le_suma_encima(self, sesion):
        """Es la razón de que se llame exacto: quien lo escribe ya hizo la
        cuenta. Subirle el % encima le cambiaría la cifra por debajo."""
        code = _crear(sesion, ppf_coverage=[GRUPO], ajuste_pct="30",
                      **{f"ppf_precio::{GRUPO}||Xpel": "777000"})
        try:
            assert _precios(code)["Xpel"] == 777000
        finally:
            _borrar(code)

    def test_las_demas_marcas_siguen_de_lista(self, sesion):
        """Se tarifa una columna, no la fila entera."""
        code = _crear(sesion, ppf_coverage=[GRUPO], ajuste_pct="20",
                      **{f"ppf_precio::{GRUPO}||Xpel": "777000"})
        try:
            guardados = _precios(code)
            assert guardados["Xpel"] == 777000
            esperado = round(precio(GRUPO, "Avery") * 1.2 / 1000) * 1000
            assert guardados["Avery"] == esperado
        finally:
            _borrar(code)

    def test_vacio_significa_el_de_lista_y_no_gratis(self, sesion):
        """El navegador no manda el campo cuando nadie lo tocó. Si un campo
        vacío se leyera como cero, un grupo sin tocar saldría regalado."""
        code = _crear(sesion, ppf_coverage=[GRUPO],
                      **{f"ppf_precio::{GRUPO}||Xpel": "   "})
        try:
            assert _precios(code)["Xpel"] == precio(GRUPO, "Xpel")
        finally:
            _borrar(code)

    def test_le_pone_precio_a_una_marca_que_el_catalogo_no_ofrece(self, sesion):
        """El catálogo dice qué se vende normalmente, no qué se puede vender.
        Si el instalador sí lo hace en esa marca, la cotización debe poder
        decirlo sin tener que cargarlo en la lista para todos."""
        # Hoy el catálogo tiene las cinco marcas en todos los grupos, así que la
        # situación se arma acá en vez de saltarse el test: la regla existe para
        # cuando alguien cargue un grupo a medias, y hay que probarla igual.
        marca = A.ppf_marcas_activas()[0][0]
        with A.app.app_context():
            g = A.PpfPackage(name="Grupo de prueba a medias", orden=999,
                             prices_json="{}")
            A.db.session.add(g)
            A.db.session.commit()
        code = None
        try:
            code = _crear(sesion, ppf_coverage=["Grupo de prueba a medias"],
                          **{f"ppf_precio::Grupo de prueba a medias||{marca}": "480000"})
            assert _precios(code, "Grupo de prueba a medias")[marca] == 480000
        finally:
            if code:
                _borrar(code)
            with A.app.app_context():
                sobra = A.PpfPackage.query.filter_by(name="Grupo de prueba a medias").first()
                if sobra:
                    A.db.session.delete(sobra)
                    A.db.session.commit()

    def test_elegir_marcas_no_le_cambia_el_nombre_al_cliente(self, sesion):
        """El bucle que lee las marcas usaba la misma variable que el nombre del
        cliente y se lo pisaba: toda cotización con marcas elegidas quedaba a
        nombre de la última marca. Se vio al guardar una y encontrar «Xpel» de
        cliente."""
        code = _crear(sesion, ppf_coverage=[GRUPO], ppf_marca=["Avery", "Xpel"],
                      **{"ppf_garantia::Avery": "7", "ppf_garantia::Xpel": "10"})
        try:
            with A.app.app_context():
                assert A.Quote.query.filter_by(code=code).first().customer_name == "Laura Ortiz"
        finally:
            _borrar(code)

    def test_una_marca_que_no_se_esta_cotizando_no_entra(self, sesion):
        """El precio viaja con el nombre de la marca adentro. Sin filtrar por
        las marcas elegidas, un campo viejo en el formulario metería una
        columna que esta cotización no compara."""
        code = _crear(sesion, ppf_coverage=[GRUPO], ppf_marca=["Xpel"],
                      **{"ppf_garantia::Xpel": "10",
                         f"ppf_precio::{GRUPO}||Avery": "480000"})
        try:
            assert "Avery" not in _precios(code)
        finally:
            _borrar(code)


class TestElClienteLoVeComoUnPrecioMas:
    def test_el_link_muestra_la_cifra_escrita(self, sesion):
        code = _crear(sesion, ppf_coverage=[GRUPO],
                      **{f"ppf_precio::{GRUPO}||Xpel": "777000"})
        try:
            with A.app.app_context():
                token = A.Quote.query.filter_by(code=code).first().public_token
            cuerpo = sesion.get(f"/c/{token}").data.decode()
            assert "777000" in cuerpo
            assert "exacto" not in cuerpo.lower()
        finally:
            _borrar(code)

    def test_el_total_por_marca_suma_la_escrita(self, sesion):
        code = _crear(sesion, ppf_coverage=[GRUPO],
                      **{f"ppf_precio::{GRUPO}||Xpel": "777000"})
        try:
            with A.app.app_context():
                c = A.Quote.query.filter_by(code=code).first()
                assert c.ppf_totales["Xpel"] == 777000
        finally:
            _borrar(code)


class TestAlEditar:
    def test_conserva_lo_que_ya_se_habia_emitido(self, sesion):
        """Sin tocar precios, una cobertura que ya estaba no se retarifa: el
        cliente ya vio esa cifra."""
        code = _crear(sesion, ppf_coverage=[GRUPO],
                      **{f"ppf_precio::{GRUPO}||Xpel": "777000"})
        try:
            _editar(sesion, code, ppf_coverage=[GRUPO])
            assert _precios(code)["Xpel"] == 777000
        finally:
            _borrar(code)

    def test_lo_escrito_despues_pisa_lo_anterior(self, sesion):
        code = _crear(sesion, ppf_coverage=[GRUPO],
                      **{f"ppf_precio::{GRUPO}||Xpel": "777000"})
        try:
            _editar(sesion, code, ppf_coverage=[GRUPO],
                    **{f"ppf_precio::{GRUPO}||Xpel": "820000"})
            assert _precios(code)["Xpel"] == 820000
        finally:
            _borrar(code)

    def test_cambiar_el_ajuste_si_retarifa(self, sesion):
        """La pantalla muestra los precios subiendo mientras se mueve el %. Si
        el servidor conservara los viejos por ser una edición, la pantalla
        estaría diciendo una cifra y el PDF saldría con otra."""
        code = _crear(sesion, ppf_coverage=[GRUPO])
        try:
            _editar(sesion, code, ppf_coverage=[GRUPO], ajuste_pct="20")
            esperado = round(precio(GRUPO, "Xpel") * 1.2 / 1000) * 1000
            assert _precios(code)["Xpel"] == esperado
        finally:
            _borrar(code)

    def test_una_marca_agregada_despues_recibe_precio(self, sesion):
        """Antes se conservaba el JSON anterior entero, así que la marca nueva
        quedaba sin cifra debajo de su propia columna."""
        code = _crear(sesion, ppf_coverage=[GRUPO], ppf_marca=["Xpel"],
                      **{"ppf_garantia::Xpel": "10"})
        try:
            _editar(sesion, code, ppf_coverage=[GRUPO], ppf_marca=["Xpel", "Avery"],
                    **{"ppf_garantia::Xpel": "10", "ppf_garantia::Avery": "5"})
            assert _precios(code)["Avery"] == precio(GRUPO, "Avery")
        finally:
            _borrar(code)
