"""Las marcas de PPF son datos, no una constante.

Eran tres escritas en el código. Entraron dos más (Standard y Stark) y la fase
siguiente necesita poder elegirlas y ajustarles la garantía por cotización, así
que viven en tabla y la pantalla de precios las edita.
"""
import itertools

import pytest

from conftest import app_module as A, make_user

_u = itertools.count(1)


def _login_admin(client, usuario="diana"):
    """La pantalla de precios solo la edita sa/diana."""
    with A.app.app_context():
        existente = A.User.query.filter_by(username=usuario).first()
        uid = existente.id if existente else make_user(usuario, role="admin").id
    with client.session_transaction() as sess:
        sess["user_id"] = uid


class TestLasCincoMarcas:
    def test_estan_las_cinco(self):
        with A.app.app_context():
            assert [m for m, _g in A.ppf_marcas_activas()] == [
                "Standard", "Avery", "Stark", "Spectra", "Xpel"]

    def test_las_garantias_conocidas(self):
        with A.app.app_context():
            g = dict(A.ppf_marcas_activas())
        assert (g["Avery"], g["Spectra"], g["Xpel"]) == (7, 5, 10)

    def test_las_nuevas_entran_sin_garantia(self):
        """En blanco y no en cero: nadie la ha definido, y un cero se leería
        como "sin garantía" cuando en realidad es "no sabemos"."""
        with A.app.app_context():
            g = dict(A.ppf_marcas_activas())
        assert g["Standard"] is None and g["Stark"] is None

    def test_sembrar_dos_veces_no_duplica(self):
        with A.app.app_context():
            antes = A.PpfFilmBrand.query.count()
        A.seed_ppf_brands()
        with A.app.app_context():
            assert A.PpfFilmBrand.query.count() == antes


class TestLaMigracionDeNombres:
    """Los precios se sembraron con SPECTRA/AVERY/XPEL en mayúsculas y las
    marcas son Spectra/Avery/Xpel. Se comparan por nombre exacto en varios
    sitios: sin normalizar, cada precio quedaría huérfano y la matriz entera
    saldría en "no aplica" sin ningún error visible."""

    def test_no_quedan_marcas_en_mayusculas(self):
        with A.app.app_context():
            nombres = {p.brand for p in A.PpfPrice.query.all()}
        assert not (nombres & {"SPECTRA", "AVERY", "XPEL"})

    def test_los_precios_siguen_apuntando_a_su_marca(self):
        with A.app.app_context():
            cat = A._catalogo_ppf()
        ff = next(x for x in cat if x["cobertura"] == "Full Front")
        assert ff["precios"]["Spectra"] == 2_500_000
        assert ff["precios"]["Xpel"] == 4_000_000

    def test_correrla_dos_veces_no_duplica(self):
        """Es lo que rompió durante el desarrollo: el sembrado corrió antes que
        la normalización, no reconoció las filas viejas y creó 46 copias."""
        with A.app.app_context():
            antes = A.PpfPrice.query.count()
        A.normalizar_marcas_en_precios()
        A.seed_ppf_prices()
        with A.app.app_context():
            assert A.PpfPrice.query.count() == antes


def _quitar_precio(grupo, marca):
    with A.app.app_context():
        g = A.PpfPackage.query.filter_by(name=grupo).first()
        precios = g.precios
        precios.pop(marca, None)
        g.prices_json = A.json.dumps(precios)
        A.db.session.commit()


class TestLaPantallaDePrecios:
    def test_abre_con_las_cinco_columnas(self, client):
        _login_admin(client)
        cuerpo = client.get("/ppf-prices").data.decode()
        for marca in ("Standard", "Avery", "Stark", "Spectra", "Xpel"):
            assert marca in cuerpo

    def test_muestra_las_partes_de_cada_grupo(self, client):
        """Es el punto de la migración: el texto de "qué contiene" era
        decorativo y ahora son partes de verdad."""
        _login_admin(client)
        cuerpo = client.get("/ppf-prices").data.decode()
        assert "Guardabarros delanteros" in cuerpo
        assert "cubre todo lo exterior" in cuerpo   # Full Car

    def test_el_adicional_solo_sale_donde_aplica(self, client):
        _login_admin(client)
        cuerpo = client.get("/ppf-prices").data.decode()
        assert 'name="foto::Farolas||Avery"' in cuerpo
        assert 'name="foto::Manijas||Avery"' not in cuerpo

    def test_hay_casilla_incluso_donde_no_hay_precio(self, client):
        """Sin esto, una marca nueva quedaría para siempre en "no aplica" sin
        manera de cargarle nada."""
        _login_admin(client)
        cuerpo = client.get("/ppf-prices").data.decode()
        assert 'name="precio::Full Front||Standard"' in cuerpo

    def test_guardar_le_pone_precio_a_una_marca_que_no_lo_tenia(self, client):
        _login_admin(client)
        client.post("/ppf-prices", data={"precio::Manijas||Standard": "120000"})
        try:
            with A.app.app_context():
                g = A.PpfPackage.query.filter_by(name="Manijas").first()
                assert g.precios["Standard"] == 120_000
        finally:
            _quitar_precio("Manijas", "Standard")

    def test_guarda_el_adicional_de_fotocromatico(self, client):
        _login_admin(client)
        client.post("/ppf-prices", data={"foto::Farolas||Standard": "40000"})
        try:
            with A.app.app_context():
                g = A.PpfPackage.query.filter_by(name="Farolas").first()
                assert g.precios_fotocromatico["Standard"] == 40_000
        finally:
            with A.app.app_context():
                g = A.PpfPackage.query.filter_by(name="Farolas").first()
                foto = g.precios_fotocromatico
                foto.pop("Standard", None)
                g.foto_prices_json = A.json.dumps(foto)
                A.db.session.commit()

    def test_vaciar_la_casilla_quita_el_precio(self, client):
        """Vacío significa "esta marca no ofrece este grupo", que no es lo
        mismo que cero."""
        _login_admin(client)
        client.post("/ppf-prices", data={"precio::Manijas||Standard": "120000"})
        client.post("/ppf-prices", data={"precio::Manijas||Standard": ""})
        with A.app.app_context():
            assert "Standard" not in A.PpfPackage.query.filter_by(name="Manijas").first().precios

    def test_guarda_la_garantia(self, client):
        _login_admin(client)
        with A.app.app_context():
            bid = A.PpfFilmBrand.query.filter_by(name="Stark").first().id
        try:
            client.post("/ppf-prices", data={f"garantia_{bid}": "8"})
            with A.app.app_context():
                assert A.PpfFilmBrand.query.get(bid).warranty_years == 8
        finally:
            with A.app.app_context():
                A.PpfFilmBrand.query.get(bid).warranty_years = None
                A.db.session.commit()

    def test_un_admin_cualquiera_no_puede_guardar(self, client):
        """Los precios los mueven solo sa y diana, igual que borrar servicios."""
        with A.app.app_context():
            uid = make_user(f"otro{next(_u)}", role="admin").id
        with client.session_transaction() as sess:
            sess["user_id"] = uid
        client.post("/ppf-prices", data={"precio::Manijas||Standard": "999000"})
        with A.app.app_context():
            assert "Standard" not in A.PpfPackage.query.filter_by(name="Manijas").first().precios
