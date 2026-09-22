"""Polarizado en la cotización: cajones que se comparan, como las marcas de PPF.

Las tres líneas hacen lo mismo; lo que el cliente decide es cuál, y eso se
decide comparando garantía contra rechazo de infrarrojo. Por eso van en cajones
y no como servicios sueltos en una lista.

Solo la elegida suma al total. Las otras quedan en el documento como la
alternativa que descartó.
"""
import itertools

import pytest

from conftest import app_module as A, make_user

_u = itertools.count(1)

HD = "Nanocerámica HD · Tecnofilm"
SPECTRA = "Nanocerámica · Spectra"
ULTRA = "Nanocerámica Ultraoptic · Spectra o Govision"


@pytest.fixture(autouse=True)
def _catalogo_intacto():
    """Varios tests cambian el precio o la garantía del catálogo para probar que
    lo congelado no se mueve. Esas filas viven en la base de los tests y NO se
    limpian entre tests: sin esto, un test le dejaba a otro un precio de dos
    millones y una garantía de 1 año, y fallaban tres que no tenían la culpa."""
    with A.app.app_context():
        A.sembrar_catalogo_polarizado()
        antes = [(o.id, o.precio, o.garantia, o.rechazo_ir, o.nota, o.is_active)
                 for o in A.TintOption.query.all()]
    yield
    with A.app.app_context():
        for oid, precio, gar, ir, nota, activo in antes:
            o = A.TintOption.query.get(oid)
            if o:
                o.precio, o.garantia, o.rechazo_ir = precio, gar, ir
                o.nota, o.is_active = nota, activo
        A.db.session.commit()


@pytest.fixture
def sesion(client):
    with A.app.app_context():
        A.sembrar_catalogo_polarizado()
        uid = make_user(f"pol{next(_u)}", role="admin").id
    with client.session_transaction() as sess:
        sess["user_id"] = uid
    return client


def _crear(client, **datos):
    base = {"customer_name": "Karla Hernandez"}
    base.update(datos)
    r = client.post("/quotes/new", data=base, follow_redirects=False)
    assert r.status_code == 302, r.data[:300]
    return r.headers["Location"].rstrip("/").split("/")[-1]


def _cot(code):
    return A.Quote.query.filter_by(code=code).first()


def _borrar(code):
    with A.app.app_context():
        c = _cot(code)
        if c:
            A.db.session.delete(c)
            A.db.session.commit()


class TestElCatalogo:
    def test_trae_las_tres_lineas_con_garantia_y_rechazo(self, sesion):
        with A.app.app_context():
            ops = {o.titulo: o for o in A.TintOption.query.all()}
            assert set(ops) >= {HD, SPECTRA, ULTRA}
            assert ops[HD].precio == 699_000
            assert ops[HD].garantia == "8 años"
            assert ops[HD].rechazo_ir == "80%–87%"
            assert "visibilidad" in (ops[ULTRA].nota or "")

    def test_sembrar_dos_veces_no_duplica(self, sesion):
        with A.app.app_context():
            antes = A.TintOption.query.count()
            assert A.sembrar_catalogo_polarizado() == 0
            assert A.TintOption.query.count() == antes


class TestEnLaCotizacion:
    def test_se_ofrecen_varias_y_congelan_su_info(self, sesion):
        """Garantía y rechazo se copian: son la mitad de la decisión y no pueden
        cambiar solas si mañana se ajusta el catálogo."""
        code = _crear(sesion, tint_opcion=[HD, SPECTRA])
        try:
            with A.app.app_context():
                c = _cot(code)
                assert [t.titulo for t in c.tint_items] == [HD, SPECTRA]
                assert c.tint_items[0].garantia == "8 años"
                assert c.tint_items[0].rechazo_ir == "80%–87%"
                with A.app.app_context():
                    o = A.TintOption.query.filter_by(linea="Nanocerámica HD").first()
                    o.garantia = "1 año"
                    A.db.session.commit()
                assert _cot(code).tint_items[0].garantia == "8 años"
        finally:
            _borrar(code)

    def test_solo_la_elegida_suma(self, sesion):
        code = _crear(sesion, tint_opcion=[HD, SPECTRA, ULTRA], tint_elegido=SPECTRA)
        try:
            with A.app.app_context():
                c = _cot(code)
                assert c.subtotal_polarizado == 859_000
                assert c.total == 859_000
        finally:
            _borrar(code)

    def test_sin_elegir_manda_la_primera(self, sesion):
        """Un total no puede depender de que alguien se acuerde de elegir."""
        code = _crear(sesion, tint_opcion=[HD, SPECTRA])
        try:
            with A.app.app_context():
                assert _cot(code).subtotal_polarizado == 699_000
        finally:
            _borrar(code)

    def test_una_elegida_que_no_se_ofrece_no_suma(self, sesion):
        """Si se quita al editar, manda la primera en vez de sumar un precio que
        ya no está en el documento."""
        code = _crear(sesion, tint_opcion=[HD], tint_elegido=ULTRA)
        try:
            with A.app.app_context():
                c = _cot(code)
                assert c.tint_elegido is None
                assert c.subtotal_polarizado == 699_000
        finally:
            _borrar(code)

    def test_el_precio_exacto_le_gana_al_de_lista(self, sesion):
        code = _crear(sesion, tint_opcion=[HD], **{"tint_precio::" + HD: "750000"})
        try:
            with A.app.app_context():
                assert _cot(code).tint_items[0].precio == 750_000
        finally:
            _borrar(code)

    def test_una_linea_inventada_no_entra(self, sesion):
        code = _crear(sesion, tint_opcion=[HD, "Papel celofán"])
        try:
            with A.app.app_context():
                assert [t.titulo for t in _cot(code).tint_items] == [HD]
        finally:
            _borrar(code)

    def test_una_cotizacion_de_solo_polarizado_es_valida(self, sesion):
        code = _crear(sesion, tint_opcion=[HD])
        try:
            with A.app.app_context():
                c = _cot(code)
                assert c.items == [] and c.ppf_items == []
                assert c.tiene_polarizado and c.total == 699_000
        finally:
            _borrar(code)

    def test_el_descuento_le_cae_encima(self, sesion):
        code = _crear(sesion, tint_opcion=[HD], discount_type="percentage",
                      discount_value="10")
        try:
            with A.app.app_context():
                assert _cot(code).total == 629_100
        finally:
            _borrar(code)

    def test_al_editar_conserva_el_precio_emitido(self, sesion):
        code = _crear(sesion, tint_opcion=[HD])
        try:
            with A.app.app_context():
                o = A.TintOption.query.filter_by(linea="Nanocerámica HD").first()
                o.precio = 2_000_000
                A.db.session.commit()
            sesion.post(f"/quotes/{code}/edit", data={
                "customer_name": "Karla Hernandez", "tint_opcion": [HD]})
            with A.app.app_context():
                assert _cot(code).tint_items[0].precio == 699_000
        finally:
            _borrar(code)


class TestEnLasPantallas:
    def _token(self, code):
        with A.app.app_context():
            return _cot(code).public_token

    def test_el_detalle_muestra_los_cajones_con_su_info(self, sesion):
        code = _crear(sesion, tint_opcion=[HD, SPECTRA], tint_elegido=SPECTRA)
        try:
            cuerpo = sesion.get(f"/quotes/{code}").data.decode()
            assert "Polarizado" in cuerpo
            assert "Garantía de 8 años" in cuerpo
            assert "Rechazo IR del 89%–94%" in cuerpo
            assert "Va en el total" in cuerpo
        finally:
            _borrar(code)

    def test_el_link_del_cliente_los_muestra_como_cajones(self, sesion, client):
        code = _crear(sesion, tint_opcion=[HD, SPECTRA, ULTRA])
        try:
            with client.session_transaction() as s:
                s.clear()
            cuerpo = client.get(f"/c/{self._token(code)}").data.decode()
            for titulo in (HD, SPECTRA, ULTRA):
                assert f'data-tint="{titulo}"' in cuerpo
            assert "Rechazo IR del 95%–99%" in cuerpo
            assert "mejor visibilidad" in cuerpo.lower()
        finally:
            _borrar(code)

    def test_el_pdf_las_imprime_todas_y_marca_la_incluida(self, sesion):
        """El papel es para decidir: comparar garantía contra rechazo ES la
        decisión."""
        import io
        from pypdf import PdfReader
        code = _crear(sesion, tint_opcion=[HD, SPECTRA], tint_elegido=SPECTRA)
        try:
            with A.app.app_context():
                pdf = A._construir_pdf_cotizacion(_cot(code))
            texto = "\n".join(p.extract_text() or ""
                              for p in PdfReader(io.BytesIO(pdf)).pages)
            assert "POLARIZADO" in texto.upper()
            assert "Garantía de 8 años" in texto and "Rechazo IR del 89%–94%" in texto
            assert "incluida en el total" in texto
            assert "$859.000" in texto
        finally:
            _borrar(code)

    def test_sin_polarizado_no_aparece_la_seccion(self, sesion):
        import io
        from pypdf import PdfReader
        code = _crear(sesion, item_desc=["Lavada"], item_price=["50000"],
                      item_qty=["1"], item_service_id=[""], item_detail=[""],
                      item_warranty=[""])
        try:
            assert "data-tint" not in sesion.get(f"/quotes/{code}").data.decode()
            with A.app.app_context():
                pdf = A._construir_pdf_cotizacion(_cot(code))
            texto = "\n".join(p.extract_text() or ""
                              for p in PdfReader(io.BytesIO(pdf)).pages)
            assert "POLARIZADO" not in texto.upper()
        finally:
            _borrar(code)


class TestElClienteElige:
    def _token(self, code):
        with A.app.app_context():
            return _cot(code).public_token

    def test_cambiar_de_pelicula_cambia_el_total(self, sesion, client):
        code = _crear(sesion, tint_opcion=[HD, SPECTRA, ULTRA])
        try:
            with client.session_transaction() as s:
                s.clear()
            r = client.post(f"/c/{self._token(code)}/seleccion",
                            json={"items": [], "ppf": [], "marca": None, "tint": ULTRA})
            assert r.get_json()["total"] == 969_000
        finally:
            _borrar(code)

    def test_queda_registrado_en_la_version(self, sesion, client):
        code = _crear(sesion, tint_opcion=[HD, ULTRA])
        try:
            with client.session_transaction() as s:
                s.clear()
            client.post(f"/c/{self._token(code)}/seleccion",
                        json={"items": [], "ppf": [], "marca": None, "tint": ULTRA})
            with A.app.app_context():
                assert _cot(code).versiones[-1].tint_option == ULTRA
        finally:
            _borrar(code)

    def test_una_pelicula_que_no_se_le_ofreció_no_se_cuela(self, sesion, client):
        code = _crear(sesion, tint_opcion=[HD])
        try:
            with client.session_transaction() as s:
                s.clear()
            r = client.post(f"/c/{self._token(code)}/seleccion",
                            json={"items": [], "ppf": [], "marca": None, "tint": ULTRA})
            assert r.get_json()["total"] == 699_000
        finally:
            _borrar(code)

    def test_el_pdf_que_baja_sale_con_la_que_eligió(self, sesion, client):
        code = _crear(sesion, tint_opcion=[HD, ULTRA])
        try:
            with client.session_transaction() as s:
                s.clear()
            r = client.post(f"/c/{self._token(code)}/pdf", data={"tint": ULTRA})
            assert r.status_code == 200 and r.data[:5] == b"%PDF-"
            with A.app.app_context():
                assert _cot(code).versiones[-1].total == 969_000
        finally:
            _borrar(code)

    def test_una_version_vieja_usa_la_primera(self, sesion):
        """Las versiones de antes del módulo tienen la columna en NULL."""
        import io, json
        from pypdf import PdfReader
        code = _crear(sesion, tint_opcion=[HD, ULTRA])
        try:
            with A.app.app_context():
                c = _cot(code)
                v = A.QuoteVersion(quote_id=c.id, numero=2, item_ids=json.dumps([]),
                                   ppf_coverages=json.dumps([]), total=0)
                v.tint_option = None
                A.db.session.add(v)
                A.db.session.commit()
                pdf = A._construir_pdf_cotizacion(c, version=v)
            texto = "\n".join(p.extract_text() or ""
                              for p in PdfReader(io.BytesIO(pdf)).pages)
            assert "$699.000" in texto
        finally:
            _borrar(code)


class TestNoSeOfreceDosVeces:
    """Visto en producción el 22/09 (cotización NX-YWN3PE): las tres películas
    salieron como servicios sueltos de la Parte 1, las tres marcadas, y las tres
    sumando al total — $5.825.000 por ponerle tres polarizados al mismo carro.

    El módulo de cajones existe justo para elegir UNA. Mientras el polarizado se
    pueda marcar también como servicio suelto, los cajones no sirven de nada.
    """

    @pytest.fixture
    def servicio_suelto(self):
        """Un polarizado en el catálogo de servicios, con precio: así es como
        está hoy en producción."""
        with A.app.app_context():
            vt = A.VehicleType.query.filter_by(is_active=True).first()
            svc = A.Service(name="Polarizado Nanocerámica Spectra",
                            duration_minutes=180, is_active=True,
                            is_outsourced=True, default_installer_share=65)
            A.db.session.add(svc)
            A.db.session.commit()
            A.db.session.add(A.ServicePrice(service_id=svc.id, vehicle_type_id=vt.id,
                                            price=859_000, duration_minutes=180,
                                            is_active=True))
            A.db.session.commit()
            ids = (svc.id, vt.id)
        yield ids
        with A.app.app_context():
            A.ServicePrice.query.filter_by(service_id=ids[0]).delete()
            A.Service.query.filter_by(id=ids[0]).delete()
            A.db.session.commit()

    def test_el_polarizado_no_aparece_entre_los_servicios_a_cotizar(self, servicio_suelto):
        svc_id, vt_id = servicio_suelto
        with A.app.app_context():
            ofrecidos = A._catalogo_para_cotizar().get(vt_id, [])
        assert svc_id not in [s["id"] for s in ofrecidos]
        assert not any("polarizado" in s["nombre"].lower() for s in ofrecidos)

    def test_los_demas_servicios_siguen_apareciendo(self, servicio_suelto):
        """El filtro es por polarizado, no una escoba que se lleve el catálogo."""
        _, vt_id = servicio_suelto
        with A.app.app_context():
            ofrecidos = A._catalogo_para_cotizar().get(vt_id, [])
        assert len(ofrecidos) > 0

    def test_sigue_siendo_agendable_y_tercerizable(self, servicio_suelto):
        """No se desactiva del catálogo de servicios: un polarizado sí se agenda
        y sí entra al corte del instalador. Quitarlo de ahí dejaría el trabajo
        sin cómo entrar a la agenda."""
        svc_id, _ = servicio_suelto
        with A.app.app_context():
            svc = A.Service.query.get(svc_id)
            assert svc.is_active is True
            assert svc_id in [s.id for s in
                              A.Service.query.filter_by(is_active=True).all()]

    def test_reconoce_el_nombre_aunque_venga_sin_tilde_o_en_mayusculas(self):
        assert A.se_cotiza_aparte("POLARIZADO Nanocerámica")
        assert A.se_cotiza_aparte("Polarizado")
        assert not A.se_cotiza_aparte("Coating Ceramico 9H")
        assert not A.se_cotiza_aparte("Lavado Premium")
