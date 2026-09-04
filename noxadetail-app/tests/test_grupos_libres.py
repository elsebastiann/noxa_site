"""Grupos de PPF armados dentro de la cotización.

Además del catálogo, se pueden marcar partes sueltas, ponerles nombre y
escribirles precio por marca. Es lo que se necesita cuando la marca, la
garantía o las partes no son las precargadas.
"""
import itertools
import json

import pytest

from conftest import app_module as A, make_user

_u = itertools.count(1)


@pytest.fixture
def sesion(client):
    with A.app.app_context():
        uid = make_user(f"gl{next(_u)}", role="admin").id
    with client.session_transaction() as sess:
        sess["user_id"] = uid
    return client


def _crear(client, **datos):
    base = {"customer_name": "Cliente Real"}
    base.update(datos)
    r = client.post("/quotes/new", data=base, follow_redirects=False)
    assert r.status_code == 302, "no creó la cotización"
    return r.headers["Location"].rstrip("/").split("/")[-1]


def _borrar(code):
    with A.app.app_context():
        c = A.Quote.query.filter_by(code=code).first()
        if c:
            A.db.session.delete(c)
            A.db.session.commit()


class TestElNombreDelClienteNoSePisa:
    """Un bucle reutilizaba la variable `nombre`, que arriba guarda el nombre
    del CLIENTE y abajo se usa para asignarlo. Cada cotización con un grupo
    armado quedaba con el nombre del grupo como cliente, en silencio: el
    formulario mandaba lo correcto y la base guardaba otra cosa."""

    def test_el_cliente_conserva_su_nombre(self, sesion):
        code = _crear(sesion, customer_name="Andrés Mejía",
                      libre_nombre=["Frente reforzado"],
                      libre_partes_0=["Capó"],
                      **{"libre_precio_0::Avery": "2800000"})
        try:
            with A.app.app_context():
                c = A.Quote.query.filter_by(code=code).first()
                assert c.customer_name == "Andrés Mejía"
                assert c.ppf_items[0].coverage == "Frente reforzado"
        finally:
            _borrar(code)

    def test_con_varios_grupos_tampoco(self, sesion):
        code = _crear(sesion, customer_name="Laura Ortiz",
                      libre_nombre=["Uno", "Dos"],
                      libre_partes_0=["Capó"], libre_partes_1=["Techo"],
                      **{"libre_precio_0::Avery": "100000",
                         "libre_precio_1::Avery": "200000"})
        try:
            with A.app.app_context():
                c = A.Quote.query.filter_by(code=code).first()
                assert c.customer_name == "Laura Ortiz"
                assert {i.coverage for i in c.ppf_items} == {"Uno", "Dos"}
        finally:
            _borrar(code)


class TestArmarUnGrupo:
    def test_guarda_partes_y_precios_escritos(self, sesion):
        code = _crear(sesion,
                      libre_nombre=["Frente reforzado"],
                      libre_partes_0=["Capó", "Bómper delantero"],
                      **{"libre_precio_0::Avery": "2800000",
                         "libre_precio_0::Xpel": "3900000"})
        try:
            with A.app.app_context():
                it = A.Quote.query.filter_by(code=code).first().ppf_items[0]
                assert it.es_personalizado
                assert it.partes == ["Capó", "Bómper delantero"]
                assert it.precios == {"Avery": 2_800_000, "Xpel": 3_900_000}
        finally:
            _borrar(code)

    def test_un_grupo_sin_ningun_precio_no_entra(self, sesion):
        """Sin precio no cotiza nada: sería una fila en blanco en el documento."""
        code = _crear(sesion, item_desc=["Lavado"], item_price=["90000"],
                      item_qty=["1"], item_service_id=[""], item_detail=[""],
                      libre_nombre=["Sin precio"], libre_partes_0=["Capó"])
        try:
            with A.app.app_context():
                assert A.Quote.query.filter_by(code=code).first().ppf_items == []
        finally:
            _borrar(code)

    def test_convive_con_los_del_catalogo(self, sesion):
        code = _crear(sesion, ppf_coverage=["Manijas"],
                      libre_nombre=["Frente reforzado"],
                      libre_partes_0=["Capó"],
                      **{"libre_precio_0::Xpel": "3900000"})
        try:
            with A.app.app_context():
                c = A.Quote.query.filter_by(code=code).first()
                assert {i.coverage for i in c.ppf_items} == {"Manijas", "Frente reforzado"}
                assert c.ppf_totales["Xpel"] == 350_000 + 3_900_000
        finally:
            _borrar(code)


class TestLasMarcasDeLaCotizacion:
    def test_se_cotiza_solo_con_las_elegidas(self, sesion):
        """Una cotización puede ir con dos marcas y no con las cinco."""
        code = _crear(sesion, ppf_coverage=["Manijas"],
                      ppf_marca=["Avery", "Xpel"],
                      **{"ppf_garantia::Avery": "7", "ppf_garantia::Xpel": "10"})
        try:
            with A.app.app_context():
                c = A.Quote.query.filter_by(code=code).first()
                assert [m for m, _g in c.ppf_marcas] == ["Avery", "Xpel"]
                assert "Spectra" not in c.ppf_totales
        finally:
            _borrar(code)

    def test_la_garantia_se_congela_como_se_cotizo(self, sesion):
        """Una negociación puede dar más años que la lista, y el papel tiene
        que decir lo que se prometió."""
        code = _crear(sesion, ppf_coverage=["Manijas"],
                      ppf_marca=["Xpel"], **{"ppf_garantia::Xpel": "12"})
        try:
            with A.app.app_context():
                assert dict(A.Quote.query.filter_by(code=code).first().ppf_marcas)["Xpel"] == 12
        finally:
            _borrar(code)


class TestFotocromatico:
    def test_se_suma_al_precio_del_grupo(self, sesion):
        code = _crear(sesion, ppf_coverage=["Farolas y Stops"],
                      **{"ppf_foto::Farolas y Stops": "1"})
        try:
            with A.app.app_context():
                c = A.Quote.query.filter_by(code=code).first()
                assert c.ppf_items[0].con_fotocromatico
                assert c.ppf_totales["Avery"] == 400_000 + 100_000
                assert c.ppf_totales["Xpel"] == 450_000 + 150_000
        finally:
            _borrar(code)

    def test_una_marca_que_no_lo_ofrece_no_lo_paga(self, sesion):
        """Spectra no hace fotocromático: su total no puede moverse."""
        code = _crear(sesion, ppf_coverage=["Farolas y Stops"],
                      **{"ppf_foto::Farolas y Stops": "1"})
        try:
            with A.app.app_context():
                assert A.Quote.query.filter_by(code=code).first().ppf_totales["Spectra"] == 350_000
        finally:
            _borrar(code)

    def test_no_se_puede_pedir_donde_no_aplica(self, sesion):
        """El servidor decide si el grupo lo admite, no el navegador."""
        code = _crear(sesion, ppf_coverage=["Manijas"],
                      **{"ppf_foto::Manijas": "1"})
        try:
            with A.app.app_context():
                c = A.Quote.query.filter_by(code=code).first()
                assert not c.ppf_items[0].con_fotocromatico
                assert c.ppf_totales["Xpel"] == 350_000
        finally:
            _borrar(code)

    def test_el_pdf_lo_muestra_como_linea(self, sesion):
        """Sumarlo callado dentro del precio dejaba un documento que no cuadra:
        las líneas daban una cosa y el total otra."""
        code = _crear(sesion, ppf_coverage=["Farolas y Stops"],
                      **{"ppf_foto::Farolas y Stops": "1"})
        try:
            with A.app.app_context():
                c = A.Quote.query.filter_by(code=code).first()
                assert A._construir_pdf_cotizacion(c).startswith(b"%PDF")
        finally:
            _borrar(code)
