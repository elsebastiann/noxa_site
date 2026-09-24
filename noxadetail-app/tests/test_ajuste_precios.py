"""El ajuste sobre precios de lista tiene que alcanzar a TODO lo que se cotiza.

Nació para los servicios del catálogo y para el PPF. Polarizado y wrap quedaron
por fuera sin que se notara: el servidor sí sabía subirlos, pero esa rama estaba
muerta porque el formulario siempre manda un precio en el campo —el de catálogo,
sin ajustar— y ese gana. Resultado: se ponía 15% y el polarizado salía al mismo
precio de siempre, sin ningún aviso.
"""
import itertools
import re

import pytest

from conftest import app_module as A
from conftest import make_user

_u = itertools.count(1)


@pytest.fixture(autouse=True)
def _catalogo_intacto():
    """Los tests tocan precios del catálogo compartido; hay que devolverlos."""
    with A.app.app_context():
        tint = [(t.id, t.precio) for t in A.TintOption.query.all()]
        wrap = [(w.id, w.price) for w in A.WrapPrice.query.all()]
    yield
    with A.app.app_context():
        for tid, precio in tint:
            o = A.TintOption.query.get(tid)
            if o:
                o.precio = precio
        for wid, precio in wrap:
            w = A.WrapPrice.query.get(wid)
            if w:
                w.price = precio
        A.db.session.commit()


@pytest.fixture
def sesion(client):
    with A.app.app_context():
        A.sembrar_catalogo_polarizado()
        A.sembrar_catalogo_wrap()
        uid = make_user(f"aju{next(_u)}", role="admin").id
    with client.session_transaction() as sess:
        sess["user_id"] = uid
    return client


def _cot(code):
    return A.Quote.query.filter_by(code=code).first()


def _borrar(code):
    with A.app.app_context():
        c = _cot(code)
        if c:
            A.db.session.delete(c)
            A.db.session.commit()


class TestElFormularioTraeElGancho:
    """Sin `data-lista` el navegador no tiene sobre qué re-tarifar y el ajuste
    se queda quieto sin decir nada — que es exactamente como estaba."""

    def test_el_polarizado_expone_su_precio_de_lista(self, sesion):
        html = sesion.get("/quotes/new").get_data(as_text=True)
        campos = re.findall(r'class="tint-precio"[^>]*data-lista="(\d+)"', html)
        assert campos, "los campos de polarizado no traen data-lista"
        assert all(int(v) > 0 for v in campos)

    def test_el_wrap_expone_su_precio_de_lista(self, sesion):
        with A.app.app_context():
            w = A.WrapPrice.query.filter_by(is_active=True).first()
            w.price = 1_500_000
            A.db.session.commit()
        html = sesion.get("/quotes/new").get_data(as_text=True)
        assert re.search(r'class="wrap-precio"[^>]*data-lista="\d+"', html)

    def test_el_data_lista_es_el_de_catalogo_no_el_ya_ajustado(self, sesion):
        """Si trajera el precio ajustado, mover el % lo compondría: 15% sobre
        un precio que ya venía con 15%."""
        with A.app.app_context():
            precios = {t.titulo: t.precio
                       for t in A.TintOption.query.filter_by(is_active=True).all()}
        html = sesion.get("/quotes/new").get_data(as_text=True)
        campos = {int(v) for v in
                  re.findall(r'class="tint-precio"[^>]*data-lista="(\d+)"', html)}
        assert campos == set(precios.values())


class TestElServidorSubeLoQueLlegaSinPrecio:
    """La red de seguridad: si el campo llega vacío, el precio sale del catálogo
    y el ajuste tiene que caerle encima igual."""

    def _crear(self, client, ajuste, extra):
        datos = {"customer_name": "Cliente Ajuste", "ajuste_pct": str(ajuste)}
        datos.update(extra)
        r = client.post("/quotes/new", data=datos, follow_redirects=False)
        assert r.status_code == 302, r.data[:300]
        return r.headers["Location"].rstrip("/").split("/")[-1]

    def test_el_polarizado_sube_con_el_ajuste(self, sesion):
        with A.app.app_context():
            op = A.TintOption.query.filter_by(is_active=True).order_by(
                A.TintOption.orden).first()
            titulo, lista = op.titulo, op.precio
        code = self._crear(sesion, 20, {"tint_opcion": [titulo]})
        try:
            with A.app.app_context():
                precio = _cot(code).tint_items[0].precio
            assert precio == int(round(lista * 1.20 / 1000)) * 1000
            assert precio > lista
        finally:
            _borrar(code)

    def test_el_wrap_sube_con_el_ajuste(self, sesion):
        with A.app.app_context():
            w = A.WrapPrice.query.filter_by(is_active=True).first()
            w.price = 2_000_000
            A.db.session.commit()
            cob = w.coverage
        code = self._crear(sesion, 10, {"wrap_coverage": [cob]})
        try:
            with A.app.app_context():
                assert _cot(code).wrap_items[0].price == 2_200_000
        finally:
            _borrar(code)

    def test_sin_ajuste_queda_el_precio_de_lista(self, sesion):
        with A.app.app_context():
            op = A.TintOption.query.filter_by(is_active=True).order_by(
                A.TintOption.orden).first()
            titulo, lista = op.titulo, op.precio
        code = self._crear(sesion, 0, {"tint_opcion": [titulo]})
        try:
            with A.app.app_context():
                assert _cot(code).tint_items[0].precio == lista
        finally:
            _borrar(code)

    def test_lo_escrito_a_mano_manda_sobre_el_ajuste(self, sesion):
        """Un precio puesto a mano ya es el que se decidió cobrar; el % no
        puede pisarlo."""
        with A.app.app_context():
            op = A.TintOption.query.filter_by(is_active=True).order_by(
                A.TintOption.orden).first()
            titulo = op.titulo
        code = self._crear(sesion, 50, {"tint_opcion": [titulo],
                                        f"tint_precio::{titulo}": "1234000"})
        try:
            with A.app.app_context():
                assert _cot(code).tint_items[0].precio == 1_234_000
        finally:
            _borrar(code)

    def test_el_ajuste_redondea_a_miles(self, sesion):
        """Una cotización con cifras como $2.587.431 se ve calculada con
        calculadora."""
        with A.app.app_context():
            op = A.TintOption.query.filter_by(is_active=True).order_by(
                A.TintOption.orden).first()
            op.precio = 699_137
            A.db.session.commit()
            titulo = op.titulo
        code = self._crear(sesion, 13, {"tint_opcion": [titulo]})
        try:
            with A.app.app_context():
                assert _cot(code).tint_items[0].precio % 1000 == 0
        finally:
            _borrar(code)
