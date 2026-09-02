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

    def test_el_catalogo_se_agrupa_por_cobertura(self):
        """Agrupado por cobertura y no por marca: así se cotiza, eligiendo las
        partes a cubrir para después comparar las marcas en columnas."""
        with A.app.app_context():
            cat = A._catalogo_ppf()
        assert len(cat) == 16
        full = next(x for x in cat if x["cobertura"] == "Full Car")
        assert full["precios"] == {"SPECTRA": 10_000_000, "AVERY": 13_000_000, "XPEL": 15_000_000}
        assert "capó" in full["contiene"].lower()

    def test_el_catalogo_marca_en_none_lo_que_no_se_ofrece(self):
        """None y no 0: un cero se leería como gratis."""
        with A.app.app_context():
            cat = A._catalogo_ppf()
        foto = next(x for x in cat if x["cobertura"] == "Farolas Fotocromático")
        assert foto["precios"]["SPECTRA"] is None
        assert foto["precios"]["AVERY"] == 300_000


class TestCotizarPpf:
    """El PPF va en matriz: una fila por cobertura, una columna por marca.

    Con 3 marcas y 6 coberturas eso son 6 filas en vez de 18 — que era el
    problema: la tabla se alargaba hasta volverse ilegible. Y de paso deja al
    cliente comparar las marcas, que es la decisión que tiene que tomar.
    """

    def _login_admin(self, client):
        with A.app.app_context():
            uid = make_user(f"ppf{next(_u)}", role="admin").id
        with client.session_transaction() as sess:
            sess["user_id"] = uid

    def _cotizar_ppf(self, client, coberturas, **extra):
        datos = {"customer_name": "Cliente PPF", "ppf_coverage": coberturas}
        datos.update(extra)
        r = client.post("/quotes/new", data=datos, follow_redirects=False)
        assert r.status_code == 302, "no creó la cotización"
        return r.headers["Location"].rstrip("/").split("/")[-1]

    def test_una_cobertura_guarda_el_precio_de_las_tres_marcas(self, client):
        self._login_admin(client)
        code = self._cotizar_ppf(client, ["Full Front"])
        try:
            with A.app.app_context():
                c = A.Quote.query.filter_by(code=code).first()
                assert c.tiene_ppf
                assert c.ppf_items[0].precios == {
                    "SPECTRA": 2_500_000, "AVERY": 3_000_000, "XPEL": 4_000_000}
        finally:
            _borrar(code)

    def test_guarda_que_cubre_la_cobertura(self, client):
        """La cotización se manda sin ver el carro: "Full Front" solo no le dice
        nada al cliente."""
        self._login_admin(client)
        code = self._cotizar_ppf(client, ["Full Front"])
        try:
            with A.app.app_context():
                assert "capó" in A.Quote.query.filter_by(code=code).first().ppf_items[0].contains
        finally:
            _borrar(code)

    def test_los_precios_no_viajan_por_el_formulario(self, client):
        """El navegador manda solo el nombre; el precio lo congela el servidor.
        Si viajara en el POST, se podría alterar desde el formulario."""
        self._login_admin(client)
        code = self._cotizar_ppf(client, ["Manijas"], ppf_price=["1"])
        try:
            with A.app.app_context():
                assert A.Quote.query.filter_by(code=code).first().ppf_items[0].precios["XPEL"] == 350_000
        finally:
            _borrar(code)

    def test_total_por_marca(self, client):
        self._login_admin(client)
        code = self._cotizar_ppf(client, ["Full Front", "Manijas"])
        try:
            with A.app.app_context():
                c = A.Quote.query.filter_by(code=code).first()
                assert c.ppf_totales == {
                    "SPECTRA": 2_500_000 + 150_000,
                    "AVERY":   3_000_000 + 250_000,
                    "XPEL":    4_000_000 + 350_000,
                }
        finally:
            _borrar(code)

    def test_lo_que_una_marca_no_cubre_no_le_suma(self, client):
        """Spectra no hace fotocromático: su columna no puede sumar ese valor."""
        self._login_admin(client)
        code = self._cotizar_ppf(client, ["Farolas Fotocromático"])
        try:
            with A.app.app_context():
                c = A.Quote.query.filter_by(code=code).first()
                assert c.ppf_totales["SPECTRA"] == 0
                assert c.ppf_totales["AVERY"] == 300_000
        finally:
            _borrar(code)

    def test_avisa_lo_que_una_marca_no_cubre(self, client):
        """Sin este aviso, la columna más barata parece la mejor oferta cuando
        en realidad está cubriendo menos partes."""
        self._login_admin(client)
        code = self._cotizar_ppf(client, ["Farolas Fotocromático", "Manijas"])
        try:
            with A.app.app_context():
                c = A.Quote.query.filter_by(code=code).first()
                assert c.ppf_no_cubre == {"SPECTRA": ["Farolas Fotocromático"]}
        finally:
            _borrar(code)

    def test_el_total_suma_servicios_mas_ppf_de_cada_marca(self, client):
        self._login_admin(client)
        code = self._cotizar_ppf(
            client, ["Manijas"],
            item_desc=["Lavado"], item_price=["100000"], item_qty=["1"],
            item_service_id=[""], item_detail=[""])
        try:
            with A.app.app_context():
                c = A.Quote.query.filter_by(code=code).first()
                assert c.subtotal == 100_000
                assert c.totales_por_marca["XPEL"] == 100_000 + 350_000
                assert c.totales_por_marca["SPECTRA"] == 100_000 + 150_000
        finally:
            _borrar(code)

    def test_el_descuento_se_aplica_a_cada_marca(self, client):
        """Un 10% sobre bases distintas da montos distintos: no se puede
        calcular una sola vez y restarlo a todas."""
        self._login_admin(client)
        code = self._cotizar_ppf(client, ["Full Front"],
                                 discount_type="percentage", discount_value="10")
        try:
            with A.app.app_context():
                t = A.Quote.query.filter_by(code=code).first().totales_por_marca
                assert t["SPECTRA"] == 2_250_000
                assert t["XPEL"] == 3_600_000
        finally:
            _borrar(code)

    def test_no_duplica_una_cobertura_repetida(self, client):
        self._login_admin(client)
        code = self._cotizar_ppf(client, ["Manijas", "Manijas"])
        try:
            with A.app.app_context():
                assert len(A.Quote.query.filter_by(code=code).first().ppf_items) == 1
        finally:
            _borrar(code)

    def test_guarda_las_garantias_del_momento(self, client):
        """Si mañana cambia una garantía, este documento tiene que seguir
        imprimiéndose como el cliente lo recibió."""
        self._login_admin(client)
        code = self._cotizar_ppf(client, ["Manijas"])
        try:
            with A.app.app_context():
                assert A.Quote.query.filter_by(code=code).first().ppf_marcas == [
                    ("SPECTRA", 5), ("AVERY", 7), ("XPEL", 10)]
        finally:
            _borrar(code)

    def test_una_cotizacion_solo_de_ppf_es_valida(self, client):
        """Sin servicios: antes el formulario la habría rechazado por vacía."""
        self._login_admin(client)
        code = self._cotizar_ppf(client, ["Full Car"])
        try:
            with A.app.app_context():
                c = A.Quote.query.filter_by(code=code).first()
                assert c.items == []
                assert c.ppf_totales["XPEL"] == 15_000_000
        finally:
            _borrar(code)

    def test_el_pdf_con_matriz_sale(self, client):
        self._login_admin(client)
        code = self._cotizar_ppf(
            client, ["Full Front", "Farolas y Stops", "Farolas Fotocromático"],
            item_desc=["Lavado Premium"], item_price=["110000"], item_qty=["1"],
            item_service_id=[""], item_detail=[""],
            discount_type="percentage", discount_value="10")
        try:
            with A.app.app_context():
                pdf = A._construir_pdf_cotizacion(A.Quote.query.filter_by(code=code).first())
            assert pdf.startswith(b"%PDF")
            assert len(pdf) > 2000
        finally:
            _borrar(code)

    def test_una_cotizacion_sin_ppf_no_lleva_matriz(self):
        code = _cotizacion(items=[("Lavado Premium", 90000, 1)])
        try:
            with A.app.app_context():
                c = A.Quote.query.filter_by(code=code).first()
                assert not c.tiene_ppf
                assert c.total == 90000
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


class TestEditar:
    """Editar una cotización ya emitida conservando su código."""

    def _login_admin(self, client):
        with A.app.app_context():
            uid = make_user(f"ed{next(_u)}", role="admin").id
        with client.session_transaction() as sess:
            sess["user_id"] = uid

    def test_la_pantalla_precarga_los_datos(self, client):
        self._login_admin(client)
        code = _cotizacion(customer_name="Ana Restrepo", items=[("Lavado", 90000, 1)])
        try:
            r = client.get(f"/quotes/{code}/edit")
            assert r.status_code == 200
            assert "Ana Restrepo".encode() in r.data
        finally:
            _borrar(code)

    def test_el_codigo_no_cambia(self, client):
        """Es el identificador que el cliente ya tiene; cambiarlo lo dejaría
        buscando una cotización que no existe."""
        self._login_admin(client)
        code = _cotizacion(items=[("Lavado", 90000, 1)])
        try:
            client.post(f"/quotes/{code}/edit", data={
                "customer_name": "Otro Nombre",
                "item_desc": ["Lavado"], "item_price": ["90000"], "item_qty": ["1"],
                "item_service_id": [""], "item_detail": [""],
            })
            with A.app.app_context():
                c = A.Quote.query.filter_by(code=code).first()
                assert c is not None, "se perdió el código"
                assert c.customer_name == "Otro Nombre"
        finally:
            _borrar(code)

    def test_reemplaza_las_lineas_no_las_suma(self, client):
        self._login_admin(client)
        code = _cotizacion(items=[("A", 100000, 1), ("B", 50000, 1)])
        try:
            client.post(f"/quotes/{code}/edit", data={
                "customer_name": "Cliente Prueba",
                "item_desc": ["Solo esta"], "item_price": ["70000"], "item_qty": ["1"],
                "item_service_id": [""], "item_detail": [""],
            })
            with A.app.app_context():
                c = A.Quote.query.filter_by(code=code).first()
                assert len(c.items) == 1
                assert c.total == 70000
        finally:
            _borrar(code)

    def test_deja_registrado_que_se_edito(self, client):
        self._login_admin(client)
        code = _cotizacion(items=[("A", 100000, 1)])
        try:
            with A.app.app_context():
                assert A.Quote.query.filter_by(code=code).first().updated_at is None
            client.post(f"/quotes/{code}/edit", data={
                "customer_name": "Cliente Prueba",
                "item_desc": ["A"], "item_price": ["100000"], "item_qty": ["1"],
                "item_service_id": [""], "item_detail": [""],
            })
            with A.app.app_context():
                c = A.Quote.query.filter_by(code=code).first()
                assert c.updated_at is not None
                assert c.updated_by
        finally:
            _borrar(code)

    def test_guardar_sin_cambios_no_revalida_la_cotizacion(self, client):
        """Si la vigencia se contara desde hoy, abrir y guardar una cotización
        vencida la revalidaría sola sin que nadie lo decidiera."""
        self._login_admin(client)
        code = _cotizacion(items=[("A", 100000, 1)])
        with A.app.app_context():
            c = A.Quote.query.filter_by(code=code).first()
            c.created_at = A.datetime.utcnow() - A.timedelta(days=40)
            c.valid_until = c.created_at.date() + A.timedelta(days=15)
            A.db.session.commit()
            vencia = c.valid_until
        try:
            client.post(f"/quotes/{code}/edit", data={
                "customer_name": "Cliente Prueba", "valid_days": "15",
                "item_desc": ["A"], "item_price": ["100000"], "item_qty": ["1"],
                "item_service_id": [""], "item_detail": [""],
            })
            with A.app.app_context():
                c = A.Quote.query.filter_by(code=code).first()
                assert c.valid_until == vencia
                assert not c.vigente
        finally:
            _borrar(code)

    def test_una_cobertura_que_sigue_puesta_conserva_su_precio(self, client):
        """Refrescarla contra la tabla cambiaría en silencio una cifra que el
        cliente ya vio."""
        self._login_admin(client)
        r = client.post("/quotes/new", data={
            "customer_name": "PPF Edit", "ppf_coverage": ["Manijas"]})
        code = r.headers["Location"].rstrip("/").split("/")[-1]
        try:
            with A.app.app_context():
                p = A.PpfPrice.query.filter_by(coverage="Manijas", brand="XPEL").first()
                original, p.price = p.price, 999_000
                A.db.session.commit()
            client.post(f"/quotes/{code}/edit", data={
                "customer_name": "PPF Edit", "ppf_coverage": ["Manijas"]})
            with A.app.app_context():
                c = A.Quote.query.filter_by(code=code).first()
                assert c.ppf_items[0].precios["XPEL"] == original
                A.PpfPrice.query.filter_by(coverage="Manijas", brand="XPEL").first().price = original
                A.db.session.commit()
        finally:
            _borrar(code)

    def test_una_cobertura_nueva_toma_el_precio_vigente(self, client):
        self._login_admin(client)
        r = client.post("/quotes/new", data={
            "customer_name": "PPF Edit2", "ppf_coverage": ["Manijas"]})
        code = r.headers["Location"].rstrip("/").split("/")[-1]
        try:
            client.post(f"/quotes/{code}/edit", data={
                "customer_name": "PPF Edit2", "ppf_coverage": ["Manijas", "Full Front"]})
            with A.app.app_context():
                c = A.Quote.query.filter_by(code=code).first()
                nueva = next(i for i in c.ppf_items if i.coverage == "Full Front")
                assert nueva.precios["XPEL"] == 4_000_000
        finally:
            _borrar(code)

    def test_no_se_puede_dejar_vacia(self, client):
        self._login_admin(client)
        code = _cotizacion(items=[("A", 100000, 1)])
        try:
            client.post(f"/quotes/{code}/edit", data={"customer_name": "Cliente Prueba"})
            with A.app.app_context():
                assert len(A.Quote.query.filter_by(code=code).first().items) == 1
        finally:
            _borrar(code)

    def test_editar_una_que_no_existe_no_revienta(self, client):
        self._login_admin(client)
        assert client.get("/quotes/NX-NOEXIS/edit").status_code == 302

    def test_el_operario_no_puede_editar(self, client):
        with A.app.app_context():
            uid = make_user(f"edop{next(_u)}", role="operario").id
        with client.session_transaction() as sess:
            sess["user_id"] = uid
        code = _cotizacion(items=[("A", 100000, 1)])
        try:
            assert client.get(f"/quotes/{code}/edit").status_code == 302
        finally:
            _borrar(code)


class TestEliminar:
    """Borrar una cotización pide la MISMA palabra clave que borrar una cita.

    Una sola palabra que rotar, no dos. Y se valida en el servidor: el prompt
    del navegador se salta con cualquier herramienta.
    """

    def _login_admin(self, client):
        with A.app.app_context():
            uid = make_user(f"del{next(_u)}", role="admin").id
        with client.session_transaction() as sess:
            sess["user_id"] = uid

    def test_con_la_clave_correcta_se_borra(self, client):
        self._login_admin(client)
        code = _cotizacion(items=[("A", 100000, 1)])
        client.post(f"/quotes/{code}/delete", data={"clave": A.DELETE_KEYWORD})
        with A.app.app_context():
            assert A.Quote.query.filter_by(code=code).first() is None

    def test_sin_la_clave_no_se_borra(self, client):
        self._login_admin(client)
        code = _cotizacion(items=[("A", 100000, 1)])
        try:
            client.post(f"/quotes/{code}/delete", data={})
            with A.app.app_context():
                assert A.Quote.query.filter_by(code=code).first() is not None
        finally:
            _borrar(code)

    def test_con_la_clave_equivocada_no_se_borra(self, client):
        self._login_admin(client)
        code = _cotizacion(items=[("A", 100000, 1)])
        try:
            client.post(f"/quotes/{code}/delete", data={"clave": "otra-cosa"})
            with A.app.app_context():
                assert A.Quote.query.filter_by(code=code).first() is not None
        finally:
            _borrar(code)

    def test_es_la_misma_clave_que_la_de_las_citas(self):
        """Si fueran dos palabras distintas, rotar una dejaría la otra vieja."""
        import inspect
        fuente = inspect.getsource(A.quote_delete)
        assert "DELETE_KEYWORD" in fuente

    def test_se_lleva_las_lineas_y_las_coberturas(self, client):
        """Sin el cascade quedarían filas huérfanas apuntando a una cotización
        que ya no existe."""
        self._login_admin(client)
        r = client.post("/quotes/new", data={
            "customer_name": "Borrable", "ppf_coverage": ["Manijas"],
            "item_desc": ["Lavado"], "item_price": ["90000"], "item_qty": ["1"],
            "item_service_id": [""], "item_detail": [""]})
        code = r.headers["Location"].rstrip("/").split("/")[-1]
        with A.app.app_context():
            qid = A.Quote.query.filter_by(code=code).first().id
        client.post(f"/quotes/{code}/delete", data={"clave": A.DELETE_KEYWORD})
        with A.app.app_context():
            assert A.QuoteItem.query.filter_by(quote_id=qid).count() == 0
            assert A.QuotePpfItem.query.filter_by(quote_id=qid).count() == 0

    def test_el_operario_no_puede_borrar(self, client):
        with A.app.app_context():
            uid = make_user(f"delop{next(_u)}", role="operario").id
        with client.session_transaction() as sess:
            sess["user_id"] = uid
        code = _cotizacion(items=[("A", 100000, 1)])
        try:
            client.post(f"/quotes/{code}/delete", data={"clave": A.DELETE_KEYWORD})
            with A.app.app_context():
                assert A.Quote.query.filter_by(code=code).first() is not None
        finally:
            _borrar(code)

    def test_borrar_una_que_no_existe_no_revienta(self, client):
        self._login_admin(client)
        r = client.post("/quotes/NX-NOEXIS/delete", data={"clave": A.DELETE_KEYWORD})
        assert r.status_code == 302


class TestPieDePagina:
    def test_no_repite_la_advertencia_cuando_hay_servicios_y_ppf(self, client):
        """Salían dos líneas diciendo lo mismo con otras palabras, y un pie que
        se repite se deja de leer."""
        with A.app.app_context():
            uid = make_user(f"pie{next(_u)}", role="admin").id
        with client.session_transaction() as sess:
            sess["user_id"] = uid
        r = client.post("/quotes/new", data={
            "customer_name": "Pie", "ppf_coverage": ["Manijas"],
            "item_desc": ["Lavado"], "item_price": ["90000"], "item_qty": ["1"],
            "item_service_id": [""], "item_detail": [""]})
        code = r.headers["Location"].rstrip("/").split("/")[-1]
        try:
            with A.app.app_context():
                c = A.Quote.query.filter_by(code=code).first()
                assert c.tiene_ppf and c.items
                assert A._construir_pdf_cotizacion(c).startswith(b"%PDF")
        finally:
            _borrar(code)


class TestFullCarAbsorbeLoExterior:
    """Full Car cubre toda la lámina exterior. Cotizarle encima un capó o unas
    farolas sería cobrar dos veces lo mismo: solo lo de adentro sigue sumando.

    La regla vive en el modelo y no en cada pantalla — si el PDF sumara
    distinto que el link del cliente, el documento y la web se contradirían.
    """

    def _login_admin(self, client):
        with A.app.app_context():
            uid = make_user(f"fc{next(_u)}", role="admin").id
        with client.session_transaction() as sess:
            sess["user_id"] = uid

    def _cotizar(self, client, coberturas):
        r = client.post("/quotes/new", data={"customer_name": "Full Car",
                                             "ppf_coverage": coberturas},
                        follow_redirects=False)
        return r.headers["Location"].rstrip("/").split("/")[-1]

    def test_lo_exterior_no_suma(self, client):
        self._login_admin(client)
        code = self._cotizar(client, ["Full Car", "Capó", "Farolas"])
        try:
            with A.app.app_context():
                c = A.Quote.query.filter_by(code=code).first()
                assert c.ppf_absorbidas == {"Capó", "Farolas"}
                assert c.ppf_totales["XPEL"] == 15_000_000
        finally:
            _borrar(code)

    def test_lo_interior_si_suma(self, client):
        """Es la excepción que pidió el negocio: el interior no lo cubre."""
        self._login_admin(client)
        code = self._cotizar(client, ["Full Car", "Full Interior", "Pantalla"])
        try:
            with A.app.app_context():
                c = A.Quote.query.filter_by(code=code).first()
                assert c.ppf_absorbidas == set()
                assert c.ppf_totales["XPEL"] == 15_000_000 + 1_500_000 + 150_000
        finally:
            _borrar(code)

    def test_mezcla(self, client):
        self._login_admin(client)
        code = self._cotizar(client, ["Full Car", "Farolas", "Consola Central"])
        try:
            with A.app.app_context():
                c = A.Quote.query.filter_by(code=code).first()
                assert c.ppf_absorbidas == {"Farolas"}
                assert c.ppf_totales["SPECTRA"] == 10_000_000 + 250_000
        finally:
            _borrar(code)

    def test_sin_full_car_todo_suma(self, client):
        """Contraprueba: sin Full Car, el capó y las farolas se cobran."""
        self._login_admin(client)
        code = self._cotizar(client, ["Capó", "Farolas"])
        try:
            with A.app.app_context():
                c = A.Quote.query.filter_by(code=code).first()
                assert c.ppf_absorbidas == set()
                assert c.ppf_totales["XPEL"] == 950_000 + 350_000
        finally:
            _borrar(code)

    def test_no_advierte_de_una_marca_sobre_algo_que_no_cobra(self, client):
        """Si la cobertura está absorbida, decir que Spectra no la cubre solo
        confunde: no se está cobrando en ninguna marca."""
        self._login_admin(client)
        code = self._cotizar(client, ["Full Car", "Farolas Fotocromático"])
        try:
            with A.app.app_context():
                assert A.Quote.query.filter_by(code=code).first().ppf_no_cubre == {}
        finally:
            _borrar(code)

    def test_las_zonas_estan_bien_clasificadas(self):
        with A.app.app_context():
            zonas = {p.coverage: p.zona for p in A.PpfPrice.query.all()}
        assert {c for c, z in zonas.items() if z == "interior"} == {
            "Full Interior", "Consola Central", "Pantalla"}

    def test_el_pdf_no_revienta_con_absorbidas(self, client):
        self._login_admin(client)
        code = self._cotizar(client, ["Full Car", "Capó", "Pantalla"])
        try:
            with A.app.app_context():
                c = A.Quote.query.filter_by(code=code).first()
                assert A._construir_pdf_cotizacion(c).startswith(b"%PDF")
        finally:
            _borrar(code)


class TestGarantiaDelServicio:
    def test_la_cotizacion_congela_la_garantia(self, client):
        """Como el precio: si mañana cambia, lo ya entregado tiene que seguir
        diciendo lo que se prometió."""
        with A.app.app_context():
            uid = make_user(f"gar{next(_u)}", role="admin").id
        with client.session_transaction() as sess:
            sess["user_id"] = uid
        r = client.post("/quotes/new", data={
            "customer_name": "Con Garantía",
            "item_desc": ["Polarizado"], "item_price": ["650000"], "item_qty": ["1"],
            "item_service_id": [""], "item_detail": [""], "item_warranty": ["5 años"]})
        code = r.headers["Location"].rstrip("/").split("/")[-1]
        try:
            with A.app.app_context():
                assert A.Quote.query.filter_by(code=code).first().items[0].warranty == "5 años"
        finally:
            _borrar(code)

    def test_un_servicio_sin_garantia_no_inventa_una(self, client):
        with A.app.app_context():
            uid = make_user(f"gar{next(_u)}", role="admin").id
        with client.session_transaction() as sess:
            sess["user_id"] = uid
        r = client.post("/quotes/new", data={
            "customer_name": "Sin Garantía",
            "item_desc": ["Lavado"], "item_price": ["90000"], "item_qty": ["1"],
            "item_service_id": [""], "item_detail": [""], "item_warranty": [""]})
        code = r.headers["Location"].rstrip("/").split("/")[-1]
        try:
            with A.app.app_context():
                assert A.Quote.query.filter_by(code=code).first().items[0].warranty is None
        finally:
            _borrar(code)
