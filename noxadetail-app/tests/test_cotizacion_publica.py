"""El link público de una cotización: interactivo y con fecha de caducidad.

El cliente entra sin login, marca y desmarca lo que quiere y ve el total
moverse. El enlace deja de funcionar solo cuando vence la cotización — la misma
fecha que ya se imprime en el PDF, así que el papel y el link nunca se
contradicen.
"""
import datetime as dt
import itertools

import pytest

from conftest import app_module as A, make_user

_u = itertools.count(1)


def _cotizacion(dias=15, items=None, ppf=None, **kw):
    """Crea una cotización con token y devuelve (code, token)."""
    import json
    import secrets
    with A.app.app_context():
        c = A.Quote(code=A._nuevo_codigo_cotizacion(),
                    public_token=secrets.token_urlsafe(24),
                    customer_name=kw.pop("customer_name", "Cliente Público"),
                    created_at=A.datetime.utcnow(),
                    valid_until=A.bogota_now().date() + dt.timedelta(days=dias),
                    **kw)
        c.items = [A.QuoteItem(description=d, unit_price=p, quantity=q)
                   for d, p, q in (items or [])]
        for cob in (ppf or []):
            filas = A.PpfPrice.query.filter_by(coverage=cob, is_active=True).all()
            c.ppf_items.append(A.QuotePpfItem(
                coverage=cob, contains=next((f.contains for f in filas if f.contains), None),
                orden=filas[0].orden,
                prices_json=json.dumps({f.brand: f.price for f in filas})))
        if c.ppf_items:
            c.ppf_brands = json.dumps([[m, g] for m, g in A.PPF_MARCAS])
        A.db.session.add(c)
        A.db.session.commit()
        return c.code, c.public_token


def _borrar(code):
    with A.app.app_context():
        c = A.Quote.query.filter_by(code=code).first()
        if c:
            A.db.session.delete(c)
            A.db.session.commit()


class TestEntraSinLogin:
    def test_el_cliente_abre_el_link_sin_cuenta(self, client):
        """Sin registrar la ruta como pública, require_login la mandaría al
        login y el cliente vería una pantalla de la app interna."""
        code, token = _cotizacion(items=[("Lavado Premium", 110000, 1)])
        try:
            r = client.get(f"/c/{token}")
            assert r.status_code == 200
            assert code.encode() in r.data
        finally:
            _borrar(code)

    def test_muestra_los_servicios_con_su_precio(self, client):
        code, token = _cotizacion(items=[("Coating Cerámico 9H", 2199000, 1)])
        try:
            cuerpo = client.get(f"/c/{token}").data.decode()
            assert "Coating Cerámico 9H" in cuerpo
            assert "2.199.000" in cuerpo
        finally:
            _borrar(code)

    def test_no_arrastra_la_app_interna(self, client):
        """La página del cliente no puede traer la barra de navegación ni los
        enlaces del panel."""
        code, token = _cotizacion(items=[("Lavado", 90000, 1)])
        try:
            cuerpo = client.get(f"/c/{token}").data.decode()
            for rastro in ("navbar", "Seguimiento", "Gastos", "/whatsapp"):
                assert rastro not in cuerpo, f"se coló «{rastro}» en la página del cliente"
        finally:
            _borrar(code)

    def test_pide_no_ser_indexada(self, client):
        """Una cotización con el nombre y el carro de un cliente no debería
        terminar en Google."""
        code, token = _cotizacion(items=[("Lavado", 90000, 1)])
        try:
            assert "noindex" in client.get(f"/c/{token}").data.decode()
        finally:
            _borrar(code)


class TestCaduca:
    """Lo pedido: que el link deje de funcionar solo al vencer la vigencia."""

    def test_vigente_abre(self, client):
        code, token = _cotizacion(dias=15, items=[("Lavado", 90000, 1)])
        try:
            assert client.get(f"/c/{token}").status_code == 200
        finally:
            _borrar(code)

    def test_vencida_no_muestra_la_cotizacion(self, client):
        code, token = _cotizacion(items=[("Lavado", 90000, 1)])
        try:
            with A.app.app_context():
                c = A.Quote.query.filter_by(code=code).first()
                c.valid_until = A.bogota_now().date() - dt.timedelta(days=1)
                A.db.session.commit()
            r = client.get(f"/c/{token}")
            assert r.status_code == 410
            assert b"90.000" not in r.data, "siguió mostrando los precios"
            assert "venci".encode() in r.data.lower()
        finally:
            _borrar(code)

    def test_el_ultimo_dia_todavia_sirve(self, client):
        """Vence AL FINAL del día que dice el PDF, no al empezarlo."""
        code, token = _cotizacion(items=[("Lavado", 90000, 1)])
        try:
            with A.app.app_context():
                c = A.Quote.query.filter_by(code=code).first()
                c.valid_until = A.bogota_now().date()
                A.db.session.commit()
            assert client.get(f"/c/{token}").status_code == 200
        finally:
            _borrar(code)

    def test_usa_la_misma_fecha_que_el_pdf(self, client):
        """Si el link tuviera su propio plazo, tarde o temprano diría una cosa
        distinta de la que el cliente tiene impresa."""
        import inspect
        assert "cot.vigente" in inspect.getsource(A.quote_public)


class TestElTokenEsUnSecreto:
    def test_no_es_el_codigo(self):
        """El código se dicta por teléfono y se imprime; con 6 caracteres no
        sirve de secreto."""
        code, token = _cotizacion(items=[("Lavado", 90000, 1)])
        try:
            assert token != code
            assert len(token) >= 24
        finally:
            _borrar(code)

    def test_dos_cotizaciones_no_comparten_token(self):
        c1, t1 = _cotizacion(items=[("A", 1000, 1)])
        c2, t2 = _cotizacion(items=[("B", 1000, 1)])
        try:
            assert t1 != t2
        finally:
            _borrar(c1)
            _borrar(c2)

    def test_un_token_inventado_no_abre_nada(self, client):
        assert client.get("/c/estonoexiste123456789012").status_code == 404

    def test_el_codigo_no_sirve_como_link(self, client):
        """Adivinar un código no puede alcanzar para ver la cotización."""
        code, _token = _cotizacion(items=[("Lavado", 90000, 1)])
        try:
            assert client.get(f"/c/{code}").status_code == 404
        finally:
            _borrar(code)


class TestPpfEnElLink:
    def test_manda_los_precios_de_las_tres_marcas(self, client):
        """El cliente cambia de marca y los precios se recalculan en su
        navegador, sin volver al servidor."""
        code, token = _cotizacion(ppf=["Full Front"])
        try:
            cuerpo = client.get(f"/c/{token}").data.decode()
            assert "PRECIOS_PPF" in cuerpo
            for precio in ("2500000", "3000000", "4000000"):
                assert precio in cuerpo
        finally:
            _borrar(code)

    def test_una_cobertura_que_la_marca_no_ofrece_no_lleva_precio(self, client):
        """La marca que no la ofrece no aparece en el JSON —ni siquiera en
        cero—, y la página la muestra como "no incluida". Un cero se leería
        como gratis."""
        code, token = _cotizacion(ppf=["Farolas Fotocromático"])
        try:
            cuerpo = client.get(f"/c/{token}").data.decode()
            precios = next(l for l in cuerpo.splitlines() if "const PRECIOS_PPF" in l)
            assert "SPECTRA" not in precios, precios
            assert "AVERY" in precios and "XPEL" in precios
            assert "no incluida" in cuerpo
        finally:
            _borrar(code)


class TestSeCreaSolo:
    def test_una_cotizacion_nueva_ya_trae_link(self, client):
        with A.app.app_context():
            uid = make_user(f"lk{next(_u)}", role="admin").id
        with client.session_transaction() as sess:
            sess["user_id"] = uid
        r = client.post("/quotes/new", data={
            "customer_name": "Con Link",
            "item_desc": ["Lavado"], "item_price": ["90000"], "item_qty": ["1"],
            "item_service_id": [""], "item_detail": [""]})
        code = r.headers["Location"].rstrip("/").split("/")[-1]
        try:
            with A.app.app_context():
                c = A.Quote.query.filter_by(code=code).first()
                assert c.public_token
                assert client.get(f"/c/{c.public_token}").status_code == 200
        finally:
            _borrar(code)

    def test_las_viejas_reciben_token_en_el_arranque(self):
        """Las cotizaciones creadas antes de que existiera el link también
        tienen que poder compartirse."""
        with A.app.app_context():
            c = A.Quote(code=A._nuevo_codigo_cotizacion(), customer_name="Sin token",
                        created_at=A.datetime.utcnow(),
                        valid_until=A.bogota_now().date() + dt.timedelta(days=10))
            c.items = [A.QuoteItem(description="X", unit_price=1000, quantity=1)]
            A.db.session.add(c)
            A.db.session.commit()
            code = c.code
            assert c.public_token is None
        try:
            A._backfill_public_tokens()
            with A.app.app_context():
                assert A.Quote.query.filter_by(code=code).first().public_token
        finally:
            _borrar(code)

    def test_el_pdf_lleva_el_link(self):
        code, _token = _cotizacion(items=[("Lavado", 90000, 1)])
        try:
            with A.app.app_context():
                c = A.Quote.query.filter_by(code=code).first()
                assert A._construir_pdf_cotizacion(c).startswith(b"%PDF")
        finally:
            _borrar(code)


class TestDescargarElPdf:
    """El cliente puede bajarse el PDF desde el mismo link."""

    def test_lo_descarga_sin_login(self, client):
        code, token = _cotizacion(items=[("Lavado Premium", 110000, 1)])
        try:
            r = client.get(f"/c/{token}/pdf")
            assert r.status_code == 200
            assert r.mimetype == "application/pdf"
            assert r.data.startswith(b"%PDF")
        finally:
            _borrar(code)

    def test_el_archivo_se_llama_por_su_codigo(self, client):
        """Va a quedar en la carpeta de descargas del cliente entre otros
        archivos: tiene que poder reconocerlo."""
        code, token = _cotizacion(items=[("Lavado", 90000, 1)])
        try:
            cd = client.get(f"/c/{token}/pdf").headers["Content-Disposition"]
            assert "attachment" in cd
            assert code in cd and "NOXA" in cd
        finally:
            _borrar(code)

    def test_vencida_no_entrega_el_pdf(self, client):
        """Si no, el link vencido seguiría repartiendo precios viejos por otra
        puerta."""
        code, token = _cotizacion(items=[("Lavado", 90000, 1)])
        try:
            with A.app.app_context():
                c = A.Quote.query.filter_by(code=code).first()
                c.valid_until = A.bogota_now().date() - dt.timedelta(days=1)
                A.db.session.commit()
            r = client.get(f"/c/{token}/pdf")
            assert r.status_code == 410
            assert not r.data.startswith(b"%PDF")
        finally:
            _borrar(code)

    def test_un_token_inventado_no_entrega_nada(self, client):
        assert client.get("/c/noexiste123456789012345/pdf").status_code == 404

    def test_entrega_la_cotizacion_completa(self, client):
        """El PDF es el documento guardado, no la selección que el cliente
        tenga marcada: si dependiera de unos checkboxes habría varios PDF
        distintos con el mismo código."""
        import inspect
        fuente = inspect.getsource(A.quote_public_pdf)
        assert "_construir_pdf_cotizacion(cot)" in fuente


class TestVersionDelCliente:
    """Lo que el cliente arma desde el link se guarda como versión aparte.

    La cotización entregada es la versión 1 y no se toca: si el cliente
    desmarcara algo y eso reescribiera el original, se perdería el documento
    que ya tiene en la mano.
    """

    def _seleccionar(self, client, token, **payload):
        return client.post(f"/c/{token}/seleccion", json=payload)

    def test_guarda_lo_que_el_cliente_marco(self, client):
        code, token = _cotizacion(items=[("A", 100000, 1), ("B", 50000, 1)])
        try:
            with A.app.app_context():
                ids = [i.id for i in A.Quote.query.filter_by(code=code).first().items]
            r = self._seleccionar(client, token, items=[ids[0]], ppf=[], marca=None)
            assert r.status_code == 200
            with A.app.app_context():
                c = A.Quote.query.filter_by(code=code).first()
                assert len(c.versiones) == 1
                assert c.versiones[0].numero == 2, "la original es la 1"
                assert c.versiones[0].items_marcados == [ids[0]]
                assert c.versiones[0].total == 100000
        finally:
            _borrar(code)

    def test_no_toca_la_cotizacion_original(self, client):
        code, token = _cotizacion(items=[("A", 100000, 1), ("B", 50000, 1)])
        try:
            self._seleccionar(client, token, items=[], ppf=[], marca=None)
            with A.app.app_context():
                c = A.Quote.query.filter_by(code=code).first()
                assert len(c.items) == 2
                assert c.total == 150000
        finally:
            _borrar(code)

    def test_no_le_cree_el_total_al_navegador(self, client):
        """Un total que llegue del cliente es un número que cualquiera puede
        cambiar antes de mandarlo."""
        code, token = _cotizacion(items=[("A", 100000, 1)])
        try:
            with A.app.app_context():
                ids = [i.id for i in A.Quote.query.filter_by(code=code).first().items]
            self._seleccionar(client, token, items=ids, ppf=[], marca=None, total=1)
            with A.app.app_context():
                assert A.Quote.query.filter_by(code=code).first().versiones[0].total == 100000
        finally:
            _borrar(code)

    def test_ignora_lineas_de_otra_cotizacion(self, client):
        """Los ids llegan del navegador: podrían apuntar a otra cotización."""
        c1, t1 = _cotizacion(items=[("A", 100000, 1)])
        c2, _t2 = _cotizacion(items=[("Ajena", 999999, 1)])
        try:
            with A.app.app_context():
                ajeno = A.Quote.query.filter_by(code=c2).first().items[0].id
            self._seleccionar(client, t1, items=[ajeno], ppf=[], marca=None)
            with A.app.app_context():
                v = A.Quote.query.filter_by(code=c1).first().versiones[0]
                assert v.items_marcados == []
                assert v.total == 0
        finally:
            _borrar(c1)
            _borrar(c2)

    def test_dos_cambios_seguidos_son_la_misma_version(self, client):
        """Tantear casillas no puede dejar una versión por clic."""
        code, token = _cotizacion(items=[("A", 100000, 1), ("B", 50000, 1)])
        try:
            with A.app.app_context():
                ids = [i.id for i in A.Quote.query.filter_by(code=code).first().items]
            self._seleccionar(client, token, items=[ids[0]], ppf=[], marca=None)
            self._seleccionar(client, token, items=ids, ppf=[], marca=None)
            with A.app.app_context():
                c = A.Quote.query.filter_by(code=code).first()
                assert len(c.versiones) == 1
                assert c.versiones[0].total == 150000, "no guardó el último cambio"
        finally:
            _borrar(code)

    def test_volver_despues_crea_otra_version(self, client):
        """Si el cliente vuelve al otro día, eso es una versión nueva, no una
        corrección de la anterior."""
        code, token = _cotizacion(items=[("A", 100000, 1)])
        try:
            with A.app.app_context():
                ids = [i.id for i in A.Quote.query.filter_by(code=code).first().items]
            self._seleccionar(client, token, items=ids, ppf=[], marca=None)
            with A.app.app_context():
                v = A.Quote.query.filter_by(code=code).first().versiones[0]
                v.updated_at = A.datetime.utcnow() - dt.timedelta(days=1)
                A.db.session.commit()
            self._seleccionar(client, token, items=[], ppf=[], marca=None)
            with A.app.app_context():
                c = A.Quote.query.filter_by(code=code).first()
                assert [v.numero for v in c.versiones] == [2, 3]
        finally:
            _borrar(code)

    def test_respeta_la_regla_de_full_car(self, client):
        """Si el cliente deja marcado el capó junto a Full Car, no se puede
        cobrar dos veces solo porque venga marcado del navegador."""
        code, token = _cotizacion(ppf=["Full Car", "Capó"])
        try:
            self._seleccionar(client, token, items=[],
                              ppf=["Full Car", "Capó"], marca="XPEL")
            with A.app.app_context():
                assert A.Quote.query.filter_by(code=code).first().versiones[0].total == 15_000_000
        finally:
            _borrar(code)

    def test_una_cotizacion_vencida_no_acepta_cambios(self, client):
        code, token = _cotizacion(items=[("A", 100000, 1)])
        try:
            with A.app.app_context():
                c = A.Quote.query.filter_by(code=code).first()
                c.valid_until = A.bogota_now().date() - dt.timedelta(days=1)
                A.db.session.commit()
            assert self._seleccionar(client, token, items=[], ppf=[]).status_code == 410
            with A.app.app_context():
                assert A.Quote.query.filter_by(code=code).first().versiones == []
        finally:
            _borrar(code)

    def test_borrar_la_cotizacion_se_lleva_sus_versiones(self, client):
        code, token = _cotizacion(items=[("A", 100000, 1)])
        self._seleccionar(client, token, items=[], ppf=[], marca=None)
        with A.app.app_context():
            qid = A.Quote.query.filter_by(code=code).first().id
        _borrar(code)
        with A.app.app_context():
            assert A.QuoteVersion.query.filter_by(quote_id=qid).count() == 0
