"""Wrap en la cotización.

Es el módulo de PPF con un eje menos: una cobertura, un precio. En película de
protección la marca ES la decisión del cliente —cambia el precio y la garantía—;
en vinilo lo que manda es qué se forra.

Chrome Delete vive acá adentro y ya no como servicio del catálogo: cotizarlo por
dos caminos con precios que se desincronizan era el problema.
"""
import itertools

import pytest

from conftest import app_module as A, make_user

_u = itertools.count(1)


@pytest.fixture
def sesion(client):
    """Se llama "sa" a propósito: tocar precios se autoriza por NOMBRE de
    usuario (USUARIOS_PUEDEN_BORRAR_SERVICIOS), no por rol."""
    with A.app.app_context():
        uid = make_user("sa", role="admin").id
    with client.session_transaction() as sess:
        sess["user_id"] = uid
    return client


@pytest.fixture
def catalogo():
    """Deja Techo y Chrome Delete con precio, como estarían en producción."""
    with A.app.app_context():
        A.sembrar_catalogo_wrap()
        for nombre, precio in (("Techo", 900_000), ("Chrome Delete", 1_200_000)):
            w = A.WrapPrice.query.filter_by(coverage=nombre).first()
            w.price, w.is_active = precio, True
            A.db.session.commit()
    yield
    with A.app.app_context():
        for nombre in ("Techo", "Chrome Delete"):
            w = A.WrapPrice.query.filter_by(coverage=nombre).first()
            if w:
                w.price = 0
        A.db.session.commit()


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
    def test_nace_con_las_coberturas_y_sin_precio(self):
        """Sembrar con cifras inventadas es peor que no tener ninguna: alguien
        cotizaría con ellas creyendo que son las del negocio."""
        with A.app.app_context():
            A.sembrar_catalogo_wrap()
            nombres = [w.coverage for w in A.WrapPrice.query.all()]
            assert "Full Car" in nombres and "Chrome Delete" in nombres

    def test_sembrar_dos_veces_no_duplica_ni_pisa_precios(self, catalogo):
        with A.app.app_context():
            antes = A.WrapPrice.query.count()
            assert A.sembrar_catalogo_wrap() == 0
            assert A.WrapPrice.query.count() == antes
            assert A.WrapPrice.query.filter_by(coverage="Techo").first().price == 900_000

    def test_la_pantalla_avisa_cuáles_están_sin_precio(self, sesion, catalogo):
        cuerpo = sesion.get("/wrap-prices").data.decode()
        assert "sin precio" in cuerpo
        assert "Chrome Delete" in cuerpo

    def test_un_admin_puede_cambiar_el_precio(self, sesion, catalogo):
        with A.app.app_context():
            wid = A.WrapPrice.query.filter_by(coverage="Techo").first().id
        sesion.post("/wrap-prices", data={f"precio_{wid}": "1100000", f"activa_{wid}": "1"})
        with A.app.app_context():
            assert A.WrapPrice.query.get(wid).price == 1_100_000

    def test_quien_no_es_admin_no_los_cambia(self, client, catalogo):
        """Misma regla que los precios de PPF."""
        with A.app.app_context():
            uid = make_user(f"wr_no{next(_u)}", role="lider").id
            wid = A.WrapPrice.query.filter_by(coverage="Techo").first().id
        with client.session_transaction() as s:
            s["user_id"] = uid
        client.post("/wrap-prices", data={f"precio_{wid}": "1", f"activa_{wid}": "1"})
        with A.app.app_context():
            assert A.WrapPrice.query.get(wid).price == 900_000


class TestEnLaCotizacion:
    def test_se_cotiza_una_cobertura(self, sesion, catalogo):
        code = _crear(sesion, wrap_coverage=["Techo"])
        try:
            with A.app.app_context():
                c = _cot(code)
                assert [w.coverage for w in c.wrap_items] == ["Techo"]
                assert c.wrap_items[0].price == 900_000
                assert c.total == 900_000
        finally:
            _borrar(code)

    def test_el_precio_exacto_le_gana_al_de_lista(self, sesion, catalogo):
        """El de catálogo es una referencia; con el carro a la vista se escribe
        el que vale de verdad."""
        code = _crear(sesion, wrap_coverage=["Techo"],
                      **{"wrap_precio::Techo": "1350000"})
        try:
            with A.app.app_context():
                assert _cot(code).wrap_items[0].price == 1_350_000
        finally:
            _borrar(code)

    def test_congela_lo_que_contiene(self, sesion, catalogo):
        """Como el PPF: si mañana se edita el catálogo, el documento entregado
        tiene que seguir diciendo lo mismo."""
        code = _crear(sesion, wrap_coverage=["Chrome Delete"])
        try:
            with A.app.app_context():
                assert "cromados" in (_cot(code).wrap_items[0].contains or "")
                w = A.WrapPrice.query.filter_by(coverage="Chrome Delete").first()
                w.contains = "otra cosa"
                A.db.session.commit()
                assert "cromados" in (_cot(code).wrap_items[0].contains or "")
        finally:
            _borrar(code)

    def test_varias_coberturas_suman(self, sesion, catalogo):
        code = _crear(sesion, wrap_coverage=["Techo", "Chrome Delete"])
        try:
            with A.app.app_context():
                c = _cot(code)
                assert c.subtotal_wrap == 2_100_000
                assert c.total == 2_100_000
        finally:
            _borrar(code)

    def test_una_cotizacion_de_solo_wrap_es_valida(self, sesion, catalogo):
        code = _crear(sesion, wrap_coverage=["Techo"])
        try:
            with A.app.app_context():
                c = _cot(code)
                assert c.items == [] and c.ppf_items == []
                assert c.tiene_wrap
        finally:
            _borrar(code)

    def test_el_descuento_le_cae_encima(self, sesion, catalogo):
        code = _crear(sesion, wrap_coverage=["Techo"],
                      discount_type="percentage", discount_value="10")
        try:
            with A.app.app_context():
                assert _cot(code).total == 810_000
        finally:
            _borrar(code)

    def test_una_cobertura_inventada_no_entra(self, sesion, catalogo):
        """El navegador manda nombres; el catálogo decide cuáles existen."""
        code = _crear(sesion, wrap_coverage=["Techo", "Forrar el perro"])
        try:
            with A.app.app_context():
                assert [w.coverage for w in _cot(code).wrap_items] == ["Techo"]
        finally:
            _borrar(code)

    def test_al_editar_conserva_el_precio_emitido(self, sesion, catalogo):
        """Si el catálogo sube, la cotización ya entregada no puede cambiar de
        precio sola al volver a guardarla."""
        code = _crear(sesion, wrap_coverage=["Techo"])
        try:
            with A.app.app_context():
                w = A.WrapPrice.query.filter_by(coverage="Techo").first()
                w.price = 2_000_000
                A.db.session.commit()
            sesion.post(f"/quotes/{code}/edit", data={
                "customer_name": "Karla Hernandez", "wrap_coverage": ["Techo"]})
            with A.app.app_context():
                assert _cot(code).wrap_items[0].price == 900_000
        finally:
            _borrar(code)

    def test_se_puede_quitar_al_editar(self, sesion, catalogo):
        code = _crear(sesion, wrap_coverage=["Techo", "Chrome Delete"])
        try:
            sesion.post(f"/quotes/{code}/edit", data={
                "customer_name": "Karla Hernandez", "wrap_coverage": ["Techo"]})
            with A.app.app_context():
                assert [w.coverage for w in _cot(code).wrap_items] == ["Techo"]
        finally:
            _borrar(code)


class TestEnLasPantallas:
    def _token(self, code):
        with A.app.app_context():
            return _cot(code).public_token

    def test_el_detalle_interno(self, sesion, catalogo):
        code = _crear(sesion, wrap_coverage=["Chrome Delete"])
        try:
            cuerpo = sesion.get(f"/quotes/{code}").data.decode()
            assert "Wrap" in cuerpo and "Chrome Delete" in cuerpo
            assert "$1.200.000" in cuerpo
        finally:
            _borrar(code)

    def test_el_link_del_cliente(self, sesion, catalogo, client):
        code = _crear(sesion, wrap_coverage=["Chrome Delete"])
        try:
            with client.session_transaction() as s:
                s.clear()
            cuerpo = client.get(f"/c/{self._token(code)}").data.decode()
            assert 'data-wrap="Chrome Delete"' in cuerpo
            assert "$1.200.000" in cuerpo
        finally:
            _borrar(code)

    def test_el_pdf(self, sesion, catalogo):
        code = _crear(sesion, wrap_coverage=["Chrome Delete"])
        try:
            with A.app.app_context():
                pdf = A._construir_pdf_cotizacion(_cot(code))
            assert pdf[:5] == b"%PDF-"
            import io
            from pypdf import PdfReader
            texto = "\n".join(p.extract_text() or ""
                              for p in PdfReader(io.BytesIO(pdf)).pages)
            assert "WRAP" in texto.upper()
            assert "Chrome Delete" in texto
            assert "$1.200.000" in texto
        finally:
            _borrar(code)

    def test_sin_wrap_no_aparece_la_seccion(self, sesion):
        """Contraprueba: si no, los de arriba pasarían con la sección pintada
        siempre."""
        code = _crear(sesion, item_desc=["Lavada"], item_price=["50000"],
                      item_qty=["1"], item_service_id=[""], item_detail=[""],
                      item_warranty=[""])
        try:
            cuerpo = sesion.get(f"/quotes/{code}").data.decode()
            assert "data-wrap" not in cuerpo
            with A.app.app_context():
                pdf = A._construir_pdf_cotizacion(_cot(code))
            import io
            from pypdf import PdfReader
            texto = "\n".join(p.extract_text() or ""
                              for p in PdfReader(io.BytesIO(pdf)).pages)
            assert "WRAP" not in texto.upper()
        finally:
            _borrar(code)


class TestElClienteLoPuedeQuitar:
    def _token(self, code):
        with A.app.app_context():
            return _cot(code).public_token

    def test_quitar_una_cobertura_baja_el_total(self, sesion, catalogo, client):
        code = _crear(sesion, wrap_coverage=["Techo", "Chrome Delete"])
        try:
            with client.session_transaction() as s:
                s.clear()
            r = client.post(f"/c/{self._token(code)}/seleccion",
                            json={"items": [], "ppf": [], "marca": None,
                                  "wrap": ["Techo"]})
            assert r.get_json()["total"] == 900_000
        finally:
            _borrar(code)

    def test_queda_registrado_en_la_version(self, sesion, catalogo, client):
        code = _crear(sesion, wrap_coverage=["Techo", "Chrome Delete"])
        try:
            with client.session_transaction() as s:
                s.clear()
            client.post(f"/c/{self._token(code)}/seleccion",
                        json={"items": [], "ppf": [], "marca": None, "wrap": ["Techo"]})
            with A.app.app_context():
                assert _cot(code).versiones[-1].wraps_marcados == ["Techo"]
        finally:
            _borrar(code)

    def test_una_cobertura_ajena_no_se_cuela(self, sesion, catalogo, client):
        code = _crear(sesion, wrap_coverage=["Techo"])
        try:
            with client.session_transaction() as s:
                s.clear()
            r = client.post(f"/c/{self._token(code)}/seleccion",
                            json={"items": [], "ppf": [], "marca": None,
                                  "wrap": ["Techo", "Full Car"]})
            assert r.get_json()["total"] == 900_000
        finally:
            _borrar(code)

    def test_el_pdf_del_cliente_respeta_lo_marcado(self, sesion, catalogo, client):
        code = _crear(sesion, wrap_coverage=["Techo", "Chrome Delete"])
        try:
            with client.session_transaction() as s:
                s.clear()
            r = client.post(f"/c/{self._token(code)}/pdf", data={"wrap": ["Techo"]})
            assert r.status_code == 200 and r.data[:5] == b"%PDF-"
            with A.app.app_context():
                assert _cot(code).versiones[-1].total == 900_000
        finally:
            _borrar(code)

    def test_una_version_vieja_imprime_todo_el_wrap(self, sesion, catalogo):
        """Las versiones de antes del wrap tienen la columna en NULL. Eso no es
        "las quitó todas"."""
        import io, json
        from pypdf import PdfReader
        code = _crear(sesion, wrap_coverage=["Techo"])
        try:
            with A.app.app_context():
                c = _cot(code)
                v = A.QuoteVersion(quote_id=c.id, numero=2, item_ids=json.dumps([]),
                                   ppf_coverages=json.dumps([]), total=0)
                v.wrap_coverages = None
                A.db.session.add(v)
                A.db.session.commit()
                pdf = A._construir_pdf_cotizacion(c, version=v)
            texto = "\n".join(p.extract_text() or ""
                              for p in PdfReader(io.BytesIO(pdf)).pages)
            assert "$900.000" in texto
        finally:
            _borrar(code)


class TestChromeDelete:
    def test_es_una_cobertura_de_wrap(self):
        with A.app.app_context():
            A.sembrar_catalogo_wrap()
            assert A.WrapPrice.query.filter_by(coverage="Chrome Delete").first()

    def test_ya_no_es_un_servicio_activo_del_catalogo(self):
        """Cotizarlo por dos caminos deja dos precios que se desincronizan."""
        with A.app.app_context():
            activos = [s.name for s in A.Service.query.filter_by(is_active=True).all()
                       if "chrome delete" in (s.name or "").lower()]
            assert activos == [], f"siguen activos: {activos}"

    def test_el_retiro_corre_una_sola_vez(self):
        """Si volviera a correr, desactivaría un servicio que alguien reactivó
        a propósito."""
        with A.app.app_context():
            assert A.migracion_ya_aplicada("chrome_delete_a_wrap_2026_09")
