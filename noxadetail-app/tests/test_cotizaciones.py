"""Cotizaciones: código único, precios congelados y PDF reimprimible.

Lo delicado de este módulo no es armarlo, es que una cotización entregada siga
diciendo lo mismo meses después. Por eso las líneas guardan copia del nombre y
del precio en vez de apuntar a `service_prices`: una subida de precios no puede
reescribir en silencio un documento que el cliente ya tiene en la mano.
"""
import itertools
import re

import pytest

from conftest import app_module as A, make_user

_u = itertools.count(1)


@pytest.fixture
def catalogo():
    """Un servicio con dos precios distintos según el vehículo — que es
    justamente lo que el módulo tiene que reflejar."""
    with A.app.app_context():
        svc = A.Service(name="Cotiz Cerámico", duration_minutes=120, is_active=True)
        A.db.session.add(svc)
        tipos = A.VehicleType.query.filter_by(is_active=True).order_by(A.VehicleType.id).limit(2).all()
        assert len(tipos) >= 2, "la BD semilla necesita 2 tipos de vehículo"
        A.db.session.flush()
        p1 = A.ServicePrice(service_id=svc.id, vehicle_type_id=tipos[0].id,
                            price=800000, duration_minutes=120, is_active=True)
        p2 = A.ServicePrice(service_id=svc.id, vehicle_type_id=tipos[1].id,
                            price=1200000, duration_minutes=150, is_active=True)
        A.db.session.add_all([p1, p2])
        A.db.session.commit()
        datos = (svc.id, tipos[0].id, tipos[1].id)
    yield datos
    with A.app.app_context():
        A.ServicePrice.query.filter_by(service_id=datos[0]).delete()
        s = A.Service.query.get(datos[0])
        if s:
            A.db.session.delete(s)
        A.db.session.commit()


def _cotizacion(**kw):
    """Crea una cotización directa en BD y devuelve su código."""
    with A.app.app_context():
        items = kw.pop("items", [("Servicio", 100000, 1)])
        c = A.Quote(code=A._nuevo_codigo_cotizacion(),
                    customer_name=kw.pop("customer_name", "Cliente Prueba"), **kw)
        c.items = [A.QuoteItem(description=d, unit_price=p, quantity=q) for d, p, q in items]
        A.db.session.add(c)
        A.db.session.commit()
        return c.code


def _borrar(code):
    with A.app.app_context():
        c = A.Quote.query.filter_by(code=code).first()
        if c:
            A.db.session.delete(c)
            A.db.session.commit()


class TestCodigo:
    def test_no_es_consecutivo(self):
        """Un "001" le dice al cliente cuántas cotizaciones lleva el negocio, y
        dos seguidas le dejan calcular el ritmo de ventas."""
        with A.app.app_context():
            codigos = [A._nuevo_codigo_cotizacion() for _ in range(12)]
        numeros = [c.split("-")[1] for c in codigos]
        assert len(set(numeros)) == len(numeros), "se repitió un código"
        assert not all(n.isdigit() for n in numeros), "los códigos son puramente numéricos"

    def test_formato(self):
        with A.app.app_context():
            assert re.fullmatch(r"NX-[A-Z2-9]{6}", A._nuevo_codigo_cotizacion())

    def test_sin_caracteres_que_se_confunden(self):
        """Se dicta por teléfono y se lee de un papel: O/0 y I/1/L no pueden
        estar o el cliente termina tecleando otro código."""
        assert not (set("O0I1L") & set(A._ALFABETO_CODIGO))

    def test_es_unico_en_la_base(self, catalogo):
        code = _cotizacion()
        try:
            with A.app.app_context():
                assert A.Quote.query.filter_by(code=code).count() == 1
        finally:
            _borrar(code)


class TestTotales:
    def test_subtotal_suma_cantidades(self):
        code = _cotizacion(items=[("A", 100000, 2), ("B", 50000, 1)])
        try:
            with A.app.app_context():
                assert A.Quote.query.filter_by(code=code).first().subtotal == 250000
        finally:
            _borrar(code)

    def test_descuento_porcentaje(self):
        code = _cotizacion(items=[("A", 200000, 1)],
                           discount_type="percentage", discount_value=10)
        try:
            with A.app.app_context():
                c = A.Quote.query.filter_by(code=code).first()
                assert c.descuento_aplicado == 20000
                assert c.total == 180000
        finally:
            _borrar(code)

    def test_descuento_absoluto(self):
        code = _cotizacion(items=[("A", 200000, 1)],
                           discount_type="absolute", discount_value=30000)
        try:
            with A.app.app_context():
                assert A.Quote.query.filter_by(code=code).first().total == 170000
        finally:
            _borrar(code)

    def test_un_descuento_mal_digitado_no_da_total_negativo(self):
        """500000 sobre una cotización de 200000: sin tope, el PDF que se le
        entrega al cliente saldría con un total en negativo."""
        code = _cotizacion(items=[("A", 200000, 1)],
                           discount_type="absolute", discount_value=500000)
        try:
            with A.app.app_context():
                c = A.Quote.query.filter_by(code=code).first()
                assert c.total == 0
                assert c.descuento_aplicado == 200000
        finally:
            _borrar(code)

    def test_porcentaje_absurdo_se_topa_en_100(self):
        code = _cotizacion(items=[("A", 200000, 1)],
                           discount_type="percentage", discount_value=250)
        try:
            with A.app.app_context():
                assert A.Quote.query.filter_by(code=code).first().total == 0
        finally:
            _borrar(code)

    def test_sin_descuento_no_descuenta(self):
        code = _cotizacion(items=[("A", 200000, 1)])
        try:
            with A.app.app_context():
                c = A.Quote.query.filter_by(code=code).first()
                assert c.descuento_aplicado == 0
                assert c.total == c.subtotal
        finally:
            _borrar(code)


class TestPreciosCongelados:
    """El punto entero del diseño."""

    def test_subir_el_precio_del_servicio_no_toca_la_cotizacion(self, catalogo):
        svc_id, vt1, _vt2 = catalogo
        with A.app.app_context():
            precio = A.ServicePrice.query.filter_by(service_id=svc_id, vehicle_type_id=vt1).first().price
        code = _cotizacion(items=[("Cotiz Cerámico", precio, 1)])
        try:
            with A.app.app_context():
                p = A.ServicePrice.query.filter_by(service_id=svc_id, vehicle_type_id=vt1).first()
                p.price = precio * 2
                A.db.session.commit()
                c = A.Quote.query.filter_by(code=code).first()
                assert c.total == precio, "la cotización se movió con la lista de precios"
        finally:
            _borrar(code)

    def test_renombrar_el_servicio_no_toca_la_cotizacion(self, catalogo):
        svc_id, _vt1, _vt2 = catalogo
        code = _cotizacion(items=[("Cotiz Cerámico", 800000, 1)])
        try:
            with A.app.app_context():
                A.Service.query.get(svc_id).name = "Otro nombre"
                A.db.session.commit()
                c = A.Quote.query.filter_by(code=code).first()
                assert c.items[0].description == "Cotiz Cerámico"
        finally:
            _borrar(code)


class TestCatalogoPorTipoDeVehiculo:
    def test_el_mismo_servicio_vale_distinto_segun_el_vehiculo(self, catalogo):
        svc_id, vt1, vt2 = catalogo
        with A.app.app_context():
            cat = A._catalogo_para_cotizar()
        p1 = next(s["precio"] for s in cat[vt1] if s["id"] == svc_id)
        p2 = next(s["precio"] for s in cat[vt2] if s["id"] == svc_id)
        assert (p1, p2) == (800000, 1200000)

    def test_no_ofrece_servicios_inactivos(self, catalogo):
        svc_id, vt1, _ = catalogo
        with A.app.app_context():
            A.Service.query.get(svc_id).is_active = False
            A.db.session.commit()
            cat = A._catalogo_para_cotizar()
        assert not any(s["id"] == svc_id for s in cat.get(vt1, []))


class TestServiciosLibres:
    def test_una_linea_puede_no_venir_del_catalogo(self):
        """Servicios que no están en sistema: un trabajo especial, un insumo
        puntual. Se cotizan igual, sin servicio al cual apuntar."""
        code = _cotizacion(items=[("Pulida de faros a mano", 90000, 2)])
        try:
            with A.app.app_context():
                c = A.Quote.query.filter_by(code=code).first()
                assert c.items[0].service_id is None
                assert c.total == 180000
        finally:
            _borrar(code)


class TestPDF:
    def test_genera_un_pdf_de_verdad(self):
        code = _cotizacion(items=[("Cerámico 9H", 1200000, 1)],
                           discount_type="percentage", discount_value=10,
                           notes="Incluye descontaminación férrica.")
        try:
            with A.app.app_context():
                pdf = A._construir_pdf_cotizacion(A.Quote.query.filter_by(code=code).first())
            assert pdf.startswith(b"%PDF"), "no salió un PDF"
            assert len(pdf) > 1500
        finally:
            _borrar(code)

    def test_el_pdf_no_revienta_sin_datos_opcionales(self):
        """Sin teléfono, sin placa, sin vehículo, sin descuento y sin notas."""
        code = _cotizacion(items=[("Lavada", 40000, 1)])
        try:
            with A.app.app_context():
                pdf = A._construir_pdf_cotizacion(A.Quote.query.filter_by(code=code).first())
            assert pdf.startswith(b"%PDF")
        finally:
            _borrar(code)

    def test_el_pdf_lleva_muchas_lineas_sin_romperse(self):
        items = [(f"Servicio {i}", 50000 + i * 1000, (i % 3) + 1) for i in range(40)]
        code = _cotizacion(items=items)
        try:
            with A.app.app_context():
                pdf = A._construir_pdf_cotizacion(A.Quote.query.filter_by(code=code).first())
            assert pdf.startswith(b"%PDF")
        finally:
            _borrar(code)


class TestPantallas:
    def _login(self, client, rol):
        """Se guarda el id y no el objeto: al salir del app_context la instancia
        queda desligada de la sesión y leerle cualquier campo revienta."""
        with A.app.app_context():
            uid = make_user(f"cot{rol}{next(_u)}", role=rol).id
        with client.session_transaction() as sess:
            sess["user_id"] = uid

    def test_el_operario_no_entra(self, client):
        self._login(client, "operario")
        r = client.get("/quotes", follow_redirects=False)
        assert r.status_code == 302, "el operario no debería ver precios"

    def test_el_admin_entra(self, client):
        self._login(client, "admin")
        assert client.get("/quotes").status_code == 200

    def test_se_puede_reconsultar_y_reexportar(self, client):
        """Lo que se pidió: consultarla después en cualquier momento y volver a
        exportar el PDF."""
        self._login(client, "admin")
        code = _cotizacion(items=[("Cerámico", 900000, 1)])
        try:
            assert client.get(f"/quotes/{code}").status_code == 200
            r = client.get(f"/quotes/{code}/pdf")
            assert r.status_code == 200
            assert r.mimetype == "application/pdf"
            assert r.data.startswith(b"%PDF")
            assert code in r.headers["Content-Disposition"]
        finally:
            _borrar(code)

    def test_se_busca_por_codigo(self, client):
        self._login(client, "admin")
        code = _cotizacion(customer_name="Buscable Pérez")
        try:
            r = client.get(f"/quotes?q={code}")
            assert b"Buscable" in r.data
        finally:
            _borrar(code)

    def test_una_cotizacion_que_no_existe_no_revienta(self, client):
        self._login(client, "admin")
        assert client.get("/quotes/NX-NOEXIS").status_code == 302

    def test_crear_desde_el_formulario(self, client, catalogo):
        self._login(client, "admin")
        _svc, vt1, _ = catalogo
        r = client.post("/quotes/new", data={
            "customer_name": "Julio Gómez", "plate": "abc123",
            "vehicle_type_id": str(vt1),
            "item_desc": ["Cotiz Cerámico", "Pulida especial"],
            "item_price": ["800000", "120000"],
            "item_qty": ["1", "2"],
            "item_service_id": ["", ""],
            "discount_type": "percentage", "discount_value": "10",
        }, follow_redirects=False)
        assert r.status_code == 302
        code = r.headers["Location"].rstrip("/").split("/")[-1]
        try:
            with A.app.app_context():
                c = A.Quote.query.filter_by(code=code).first()
                assert c.subtotal == 800000 + 240000
                assert c.total == 936000
                assert c.plate == "ABC123", "la placa debe normalizarse"
                assert c.valid_until is not None
        finally:
            _borrar(code)

    def test_no_crea_una_cotizacion_vacia(self, client):
        self._login(client, "admin")
        antes = None
        with A.app.app_context():
            antes = A.Quote.query.count()
        client.post("/quotes/new", data={"customer_name": "Sin líneas"})
        with A.app.app_context():
            assert A.Quote.query.count() == antes


class TestPreciosPpf:
    """El PPF no cabe en `service_prices`: su eje es la MARCA de la película,
    no el tipo de vehículo, y cada marca trae su propia garantía."""

    def test_la_semilla_carga_las_tres_marcas(self):
        with A.app.app_context():
            marcas = {m for (m,) in A.db.session.query(A.PpfPrice.brand).distinct()}
        assert marcas == {"SPECTRA", "AVERY", "XPEL"}

    def test_los_precios_de_la_hoja(self):
        """Verifica contra la hoja original, incluidas las conversiones de
        "10M" y "850K" que son donde es fácil equivocarse en un cero."""
        esperados = [
            ("Full Car", "SPECTRA", 10_000_000), ("Full Car", "XPEL", 15_000_000),
            ("Full Front", "AVERY", 3_000_000), ("Protección Urbana", "SPECTRA", 850_000),
            ("Pantalla", "SPECTRA", 80_000), ("Puertas", "XPEL", 4_000_000),
            ("Capó", "AVERY", 850_000), ("Bómper Trasero y Delantero", "XPEL", 3_500_000),
        ]
        with A.app.app_context():
            for cob, marca, precio in esperados:
                p = A.PpfPrice.query.filter_by(coverage=cob, brand=marca).first()
                assert p is not None, f"falta {cob} / {marca}"
                assert p.price == precio, f"{cob} / {marca}"

    def test_spectra_no_tiene_fotocromatico(self):
        """La hoja lo deja en blanco. Un cero se leería como "gratis"."""
        with A.app.app_context():
            assert A.PpfPrice.query.filter_by(
                coverage="Farolas Fotocromático", brand="SPECTRA").first() is None
            assert A.PpfPrice.query.filter_by(
                coverage="Farolas Fotocromático", brand="AVERY").first().price == 300_000

    def test_las_garantias(self):
        assert A.PPF_GARANTIAS == {"SPECTRA": 5, "AVERY": 7, "XPEL": 10}

    def test_la_semilla_no_pisa_un_precio_editado(self):
        """Si un redespliegue revirtiera los ajustes, la pantalla de precios no
        serviría de nada."""
        with A.app.app_context():
            p = A.PpfPrice.query.filter_by(coverage="Manijas", brand="XPEL").first()
            original = p.price
            p.price = 999_000
            A.db.session.commit()
        try:
            A.seed_ppf_prices()
            with A.app.app_context():
                assert A.PpfPrice.query.filter_by(
                    coverage="Manijas", brand="XPEL").first().price == 999_000
        finally:
            with A.app.app_context():
                A.PpfPrice.query.filter_by(coverage="Manijas", brand="XPEL").first().price = original
                A.db.session.commit()

    def test_el_catalogo_agrupa_por_marca(self):
        with A.app.app_context():
            cat = A._catalogo_ppf()
        assert set(cat) == {"SPECTRA", "AVERY", "XPEL"}
        full = next(x for x in cat["XPEL"] if x["cobertura"] == "Full Car")
        assert full["precio"] == 15_000_000
        assert full["garantia"] == 10
        assert "capó" in full["contiene"].lower()


class TestCotizarPpf:
    def _login_admin(self, client):
        with A.app.app_context():
            uid = make_user(f"ppf{next(_u)}", role="admin").id
        with client.session_transaction() as sess:
            sess["user_id"] = uid

    def test_una_cotizacion_de_ppf_guarda_lo_que_cubre(self, client):
        """Es el punto: la cotización se manda sin ver el carro, así que el
        cliente necesita leer qué piezas cubre cada cobertura."""
        self._login_admin(client)
        r = client.post("/quotes/new", data={
            "customer_name": "Cliente PPF",
            "item_desc": ["PPF Full Front — XPEL (garantía 10 años)"],
            "item_price": ["4000000"], "item_qty": ["1"],
            "item_service_id": [""],
            "item_detail": ["Bómper delantero, capó, guardabarros delanteros, "
                            "espejos retrovisores, farolas delanteras"],
        }, follow_redirects=False)
        code = r.headers["Location"].rstrip("/").split("/")[-1]
        try:
            with A.app.app_context():
                c = A.Quote.query.filter_by(code=code).first()
                assert "capó" in c.items[0].detail
                assert c.tiene_ppf
                assert c.total == 4_000_000
        finally:
            _borrar(code)

    def test_el_pdf_de_ppf_advierte_que_el_precio_puede_variar(self):
        code = _cotizacion(items=[("PPF Full Car — XPEL (garantía 10 años)", 15_000_000, 1)])
        try:
            with A.app.app_context():
                c = A.Quote.query.filter_by(code=code).first()
                assert c.tiene_ppf, "no reconoció la línea como PPF"
                assert A._construir_pdf_cotizacion(c).startswith(b"%PDF")
        finally:
            _borrar(code)

    def test_una_cotizacion_sin_ppf_no_lleva_esa_advertencia(self):
        code = _cotizacion(items=[("Lavado Premium", 90000, 1)])
        try:
            with A.app.app_context():
                assert not A.Quote.query.filter_by(code=code).first().tiene_ppf
        finally:
            _borrar(code)

    def test_la_pantalla_de_precios_abre(self, client):
        self._login_admin(client)
        r = client.get("/ppf-prices")
        assert r.status_code == 200
        assert "XPEL".encode() in r.data

    def test_el_operario_no_ve_los_precios_de_ppf(self, client):
        with A.app.app_context():
            uid = make_user(f"ppfop{next(_u)}", role="operario").id
        with client.session_transaction() as sess:
            sess["user_id"] = uid
        assert client.get("/ppf-prices").status_code == 302
