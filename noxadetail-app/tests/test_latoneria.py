"""Latonería y pintura en la cotización.

No va por catálogo como el PPF: cada trabajo es distinto —qué piezas, qué tan
hundido, si hay que reemplazar— y una matriz de precios obligaría a inventar
categorías que ningún presupuesto real respeta. Es un valor y una descripción
sin límite de largo.

Lo que hay que sostener: que suma al total, que el descuento le cae encima, que
el cliente la puede quitar desde su link, y que una cotización de SOLO latonería
es válida.
"""
import itertools
import json

import pytest

from conftest import app_module as A, make_user

_u = itertools.count(1)

DETALLE = ("Capó y guardafango delantero derecho: desabollado, masillado y pintura "
           "completa con difuminado en la puerta. Incluye desmonte y montaje de "
           "farola derecha y pulida final de la zona intervenida.")


@pytest.fixture
def sesion(client):
    with A.app.app_context():
        uid = make_user(f"lat{next(_u)}", role="admin").id
    with client.session_transaction() as sess:
        sess["user_id"] = uid
    return client


def _crear(client, **datos):
    base = {"customer_name": "Karla Hernandez"}
    base.update(datos)
    r = client.post("/quotes/new", data=base, follow_redirects=False)
    assert r.status_code == 302, r.data[:200]
    return r.headers["Location"].rstrip("/").split("/")[-1]


def _cot(code):
    return A.Quote.query.filter_by(code=code).first()


def _borrar(code):
    with A.app.app_context():
        c = _cot(code)
        if c:
            A.db.session.delete(c)
            A.db.session.commit()


class TestSeGuarda:
    def test_valor_y_descripcion(self, sesion):
        code = _crear(sesion, body_amount="3500000", body_detail=DETALLE)
        try:
            with A.app.app_context():
                c = _cot(code)
                assert c.body_amount == 3_500_000
                assert c.body_detail == DETALLE
        finally:
            _borrar(code)

    def test_la_descripcion_no_se_recorta(self, sesion):
        """Se pidió explícitamente sin límite de caracteres: ahí va qué piezas
        se tocan y qué se les hace, y eso no cabe en un campo corto."""
        largo = DETALLE * 20
        code = _crear(sesion, body_amount="3500000", body_detail=largo)
        try:
            with A.app.app_context():
                assert _cot(code).body_detail == largo
                assert len(_cot(code).body_detail) > 2000
        finally:
            _borrar(code)

    def test_sin_valor_no_queda_linea(self, sesion):
        """Una descripción sin valor no es una línea de cotización."""
        code = _crear(sesion, item_desc=["Lavada"], item_price=["50000"],
                      item_qty=["1"], item_service_id=[""], item_detail=[""],
                      item_warranty=[""], body_amount="", body_detail=DETALLE)
        try:
            with A.app.app_context():
                assert _cot(code).body_amount is None
        finally:
            _borrar(code)

    def test_una_cotizacion_de_solo_latoneria_es_valida(self, sesion):
        """Sin servicios ni PPF. Es un presupuesto perfectamente normal y antes
        el formulario lo habría rechazado."""
        code = _crear(sesion, body_amount="3500000", body_detail=DETALLE)
        try:
            with A.app.app_context():
                c = _cot(code)
                assert c.items == [] and c.ppf_items == []
                assert c.total == 3_500_000
        finally:
            _borrar(code)

    def test_se_puede_quitar_al_editar(self, sesion):
        code = _crear(sesion, body_amount="3500000", body_detail=DETALLE)
        try:
            sesion.post(f"/quotes/{code}/edit", data={
                "customer_name": "Karla Hernandez", "body_amount": "",
                "item_desc": ["Lavada"], "item_price": ["50000"], "item_qty": ["1"],
                "item_service_id": [""], "item_detail": [""], "item_warranty": [""]})
            with A.app.app_context():
                assert _cot(code).body_amount is None
        finally:
            _borrar(code)


class TestSuma:
    def test_entra_al_subtotal_y_al_total(self, sesion):
        code = _crear(sesion, body_amount="3000000", body_detail=DETALLE,
                      item_desc=["Lavada"], item_price=["50000"], item_qty=["1"],
                      item_service_id=[""], item_detail=[""], item_warranty=[""])
        try:
            with A.app.app_context():
                c = _cot(code)
                assert c.subtotal == 3_050_000
                assert c.total == 3_050_000
        finally:
            _borrar(code)

    def test_el_descuento_le_cae_encima(self, sesion):
        """Es plata que el cliente paga: un 10% de descuento sobre la
        cotización tiene que descontar también la latonería."""
        code = _crear(sesion, body_amount="1000000", body_detail=DETALLE,
                      discount_type="percentage", discount_value="10")
        try:
            with A.app.app_context():
                assert _cot(code).total == 900_000
        finally:
            _borrar(code)

    def test_no_ensucia_el_total_de_servicios(self, sesion):
        """El renglón que dice "Total servicios" no puede traer latonería
        adentro: sería rotular mal una cifra."""
        code = _crear(sesion, body_amount="3000000", body_detail=DETALLE,
                      item_desc=["Lavada"], item_price=["50000"], item_qty=["1"],
                      item_service_id=[""], item_detail=[""], item_warranty=[""])
        try:
            with A.app.app_context():
                c = _cot(code)
                assert c.subtotal_servicios == 50_000
                assert c.subtotal == 3_050_000
        finally:
            _borrar(code)

    def test_convive_con_el_ppf(self, sesion):
        """Con PPF el total sale por marca; la latonería suma en todas."""
        code = _crear(sesion, body_amount="1000000", body_detail=DETALLE,
                      ppf_coverage=["Farolas"])
        try:
            with A.app.app_context():
                c = _cot(code)
                assert c.ppf_items, "la fixture necesita que exista el grupo Farolas"
                for marca, total in c.totales_por_marca.items():
                    assert total == c.ppf_totales[marca] + 1_000_000
        finally:
            _borrar(code)


class TestEnLasPantallas:
    def _token(self, code):
        with A.app.app_context():
            return _cot(code).public_token

    def test_el_detalle_interno_la_muestra(self, sesion):
        code = _crear(sesion, body_amount="3500000", body_detail=DETALLE)
        try:
            cuerpo = sesion.get(f"/quotes/{code}").data.decode()
            assert "Latonería y pintura" in cuerpo
            assert "$3.500.000" in cuerpo
            assert "desabollado" in cuerpo
        finally:
            _borrar(code)

    def test_el_link_del_cliente_la_muestra(self, sesion, client):
        code = _crear(sesion, body_amount="3500000", body_detail=DETALLE)
        try:
            with client.session_transaction() as s:
                s.clear()
            cuerpo = client.get(f"/c/{self._token(code)}").data.decode()
            assert "Latonería y pintura" in cuerpo
            assert "desabollado" in cuerpo
        finally:
            _borrar(code)

    def test_el_pdf_se_arma_y_la_nombra(self, sesion):
        code = _crear(sesion, body_amount="3500000", body_detail=DETALLE)
        try:
            with A.app.app_context():
                pdf = A._construir_pdf_cotizacion(_cot(code))
            assert pdf[:5] == b"%PDF-"
            try:
                from pypdf import PdfReader
                import io
                texto = "\n".join(p.extract_text() or ""
                                  for p in PdfReader(io.BytesIO(pdf)).pages)
            except ImportError:
                pytest.skip("pypdf no instalado")
            assert "LATONER" in texto.upper()
            assert "$3.500.000" in texto
            assert "desabollado" in texto
        finally:
            _borrar(code)

    def test_una_cotizacion_sin_latoneria_no_la_menciona(self, sesion):
        """Contraprueba: si no, los tests de arriba pasarían con la sección
        pintada siempre."""
        code = _crear(sesion, item_desc=["Lavada"], item_price=["50000"],
                      item_qty=["1"], item_service_id=[""], item_detail=[""],
                      item_warranty=[""])
        try:
            assert "Latonería y pintura" not in sesion.get(f"/quotes/{code}").data.decode()
            with A.app.app_context():
                pdf = A._construir_pdf_cotizacion(_cot(code))
            assert b"LATONER" not in pdf.upper()
        finally:
            _borrar(code)


class TestElClienteLaPuedeQuitar:
    """El link promete "marca o desmarca lo que quieras". Una línea de tres
    millones que no se puede desmarcar rompe esa promesa justo donde más pesa."""

    def _token(self, code):
        with A.app.app_context():
            return _cot(code).public_token

    def test_quitarla_baja_el_total_de_la_version(self, sesion, client):
        code = _crear(sesion, body_amount="3000000", body_detail=DETALLE,
                      item_desc=["Lavada"], item_price=["50000"], item_qty=["1"],
                      item_service_id=[""], item_detail=[""], item_warranty=[""])
        try:
            with A.app.app_context():
                ids = [i.id for i in _cot(code).items]
            with client.session_transaction() as s:
                s.clear()
            r = client.post(f"/c/{self._token(code)}/seleccion",
                            json={"items": ids, "ppf": [], "marca": None,
                                  "latoneria": False})
            assert r.get_json()["total"] == 50_000
        finally:
            _borrar(code)

    def test_dejarla_marcada_la_suma(self, sesion, client):
        code = _crear(sesion, body_amount="3000000", body_detail=DETALLE)
        try:
            with client.session_transaction() as s:
                s.clear()
            r = client.post(f"/c/{self._token(code)}/seleccion",
                            json={"items": [], "ppf": [], "marca": None,
                                  "latoneria": True})
            assert r.get_json()["total"] == 3_000_000
        finally:
            _borrar(code)

    def test_queda_registrado_en_la_version(self, sesion, client):
        code = _crear(sesion, body_amount="3000000", body_detail=DETALLE)
        try:
            with client.session_transaction() as s:
                s.clear()
            client.post(f"/c/{self._token(code)}/seleccion",
                        json={"items": [], "ppf": [], "marca": None, "latoneria": False})
            with A.app.app_context():
                assert _cot(code).versiones[-1].incluye_latoneria is False
        finally:
            _borrar(code)

    def test_no_se_puede_marcar_en_una_cotizacion_que_no_la_trae(self, sesion, client):
        """El navegador manda lo que sea; el total lo decide el servidor."""
        code = _crear(sesion, item_desc=["Lavada"], item_price=["50000"],
                      item_qty=["1"], item_service_id=[""], item_detail=[""],
                      item_warranty=[""])
        try:
            with A.app.app_context():
                ids = [i.id for i in _cot(code).items]
            with client.session_transaction() as s:
                s.clear()
            r = client.post(f"/c/{self._token(code)}/seleccion",
                            json={"items": ids, "ppf": [], "marca": None,
                                  "latoneria": True})
            assert r.get_json()["total"] == 50_000
        finally:
            _borrar(code)

    def test_el_pdf_que_baja_el_cliente_la_respeta(self, sesion, client):
        code = _crear(sesion, body_amount="3000000", body_detail=DETALLE,
                      item_desc=["Lavada"], item_price=["50000"], item_qty=["1"],
                      item_service_id=[""], item_detail=[""], item_warranty=[""])
        try:
            with A.app.app_context():
                ids = [str(i.id) for i in _cot(code).items]
            with client.session_transaction() as s:
                s.clear()
            r = client.post(f"/c/{self._token(code)}/pdf",
                            data={"items": ids, "latoneria": "0"})
            assert r.status_code == 200 and r.data[:5] == b"%PDF-"
            with A.app.app_context():
                assert _cot(code).versiones[-1].total == 50_000
        finally:
            _borrar(code)


class TestVersionesViejas:
    def test_una_version_sin_la_columna_imprime_la_latoneria(self, sesion):
        """Las versiones guardadas antes de que existiera esto tienen la
        columna en NULL. Eso no puede leerse como "el cliente la quitó"."""
        code = _crear(sesion, body_amount="3000000", body_detail=DETALLE)
        try:
            with A.app.app_context():
                c = _cot(code)
                v = A.QuoteVersion(quote_id=c.id, numero=2, item_ids=json.dumps([]),
                                   ppf_coverages=json.dumps([]), total=0)
                v.incluye_latoneria = None
                A.db.session.add(v)
                A.db.session.commit()
                pdf = A._construir_pdf_cotizacion(c, version=v)
            assert pdf[:5] == b"%PDF-"
            from pypdf import PdfReader
            import io
            texto = "\n".join(p.extract_text() or ""
                               for p in PdfReader(io.BytesIO(pdf)).pages)
            assert "$3.000.000" in texto
        finally:
            _borrar(code)
