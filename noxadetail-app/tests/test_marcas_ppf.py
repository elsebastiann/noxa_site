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
            assert set(m for m, _g in A.ppf_marcas_activas()) == {
                "Standard", "Avery", "Stark", "Spectra", "Xpel"}

    def test_van_ordenadas_de_menor_a_mayor_garantia(self):
        """Es como se le presentan al cliente: de la opción de entrada a la
        premium. Se prueba la regla y no una lista fija, que quedaría vieja al
        primer cambio de garantía."""
        with A.app.app_context():
            anios = [g for _m, g in A.ppf_marcas_activas() if g is not None]
        assert anios == sorted(anios)

    def test_las_que_no_tienen_garantia_van_al_final(self):
        with A.app.app_context():
            marcas = A.ppf_marcas_activas()
        sin = [i for i, (_m, g) in enumerate(marcas) if g is None]
        con = [i for i, (_m, g) in enumerate(marcas) if g is not None]
        assert not con or not sin or min(sin) > max(con)

    def test_el_singular_del_ano(self):
        """"1 años" se ve descuidado justo en el dato que sustenta el precio."""
        assert A.texto_garantia(1) == "1 año"
        assert A.texto_garantia(5) == "5 años"
        assert A.texto_garantia(None) == ""

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


class TestElFotocromaticoNuncaVaIncluido:
    """Es OTRA película, no una parte del carro. Ningún grupo lo trae: aunque
    Full Car cubra las farolas, la versión fotocromática se cobra aparte."""

    def _login_admin(self, client):
        with A.app.app_context():
            uid = make_user(f"foto{next(_u)}", role="admin").id
        with client.session_transaction() as sess:
            sess["user_id"] = uid

    def test_full_car_absorbe_el_grupo_pero_no_su_adicional(self, client):
        self._login_admin(client)
        r = client.post("/quotes/new", data={
            "customer_name": "Foto", "ppf_coverage": ["Full Car", "Farolas y Stops"],
            "ppf_foto::Farolas y Stops": "1"}, follow_redirects=False)
        code = r.headers["Location"].rstrip("/").split("/")[-1]
        try:
            with A.app.app_context():
                c = A.Quote.query.filter_by(code=code).first()
                assert "Farolas y Stops" in c.ppf_absorbidas, "Full Car debe cubrir el grupo"
                # 15.000.000 de Full Car + 150.000 del adicional, que no está
                # incluido en ningún grupo.
                assert c.ppf_totales["Xpel"] == 15_000_000 + 150_000
        finally:
            with A.app.app_context():
                q = A.Quote.query.filter_by(code=code).first()
                if q:
                    A.db.session.delete(q)
                    A.db.session.commit()


class TestPreciosPorParteSuelta:
    """Además del precio por grupo, cada pieza tiene el suyo.

    Son dos precios distintos y ninguno se deduce del otro: un capó dentro de
    un Full Front no cuesta lo que cuesta un capó suelto.
    """

    def test_la_pantalla_trae_las_dos_pestanas(self, client):
        _login_admin(client)
        cuerpo = client.get("/ppf-prices").data.decode()
        assert "Por grupo" in cuerpo and "Por parte suelta" in cuerpo

    def test_hay_casilla_para_cada_parte_y_marca(self, client):
        _login_admin(client)
        cuerpo = client.get("/ppf-prices").data.decode()
        assert 'name="parte::Capó||Avery"' in cuerpo
        assert 'name="parte::Uñeros||Xpel"' in cuerpo

    def test_el_comodin_no_se_tarifa(self, client):
        """"Otro" se nombra al usarla: no tiene precio de lista."""
        _login_admin(client)
        assert 'name="parte::Otro||Avery"' not in client.get("/ppf-prices").data.decode()

    def test_guardar_le_pone_precio_a_una_parte(self, client):
        _login_admin(client)
        client.post("/ppf-prices", data={"parte::Techo||Avery": "1200000"})
        try:
            with A.app.app_context():
                assert A.PpfPart.query.filter_by(name="Techo").first().precios["Avery"] == 1_200_000
        finally:
            with A.app.app_context():
                A.PpfPart.query.filter_by(name="Techo").first().prices_json = None
                A.db.session.commit()

    def test_vaciarla_quita_el_precio(self, client):
        _login_admin(client)
        client.post("/ppf-prices", data={"parte::Techo||Avery": "1200000"})
        client.post("/ppf-prices", data={"parte::Techo||Avery": ""})
        with A.app.app_context():
            assert "Avery" not in A.PpfPart.query.filter_by(name="Techo").first().precios

    def test_el_cotizador_recibe_los_precios_de_las_partes(self):
        """Es lo que le permite sugerir el precio de un grupo armado."""
        with A.app.app_context():
            pt = A.PpfPart.query.filter_by(name="Techo").first()
            pt.prices_json = A.json.dumps({"Avery": 1_200_000})
            A.db.session.commit()
        try:
            with A.app.app_context():
                partes = A._partes_ppf()
            techo = next(p for p in partes if p["nombre"] == "Techo")
            assert techo["precios"]["Avery"] == 1_200_000
        finally:
            with A.app.app_context():
                A.PpfPart.query.filter_by(name="Techo").first().prices_json = None
                A.db.session.commit()
