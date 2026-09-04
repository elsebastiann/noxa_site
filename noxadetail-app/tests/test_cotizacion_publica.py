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
            # Igual que la ruta real: solo las marcas con precio en alguna de
            # las coberturas elegidas.
            con_precio = set()
            for it in c.ppf_items:
                con_precio.update(m for m, v in json.loads(it.prices_json).items() if v)
            c.ppf_brands = json.dumps(
                [[m, g] for m, g in A.ppf_marcas_activas() if m in con_precio])
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
            assert "Spectra" not in precios, precios
            assert "Avery" in precios and "Xpel" in precios
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

    def test_por_get_baja_la_cotizacion_completa(self, client):
        code, token = _cotizacion(items=[("A", 100000, 1), ("B", 50000, 1)])
        try:
            r = client.get(f"/c/{token}/pdf")
            assert r.data.startswith(b"%PDF")
            assert "-v" not in r.headers["Content-Disposition"], "no es una versión"
        finally:
            _borrar(code)

    def test_por_post_baja_lo_que_el_cliente_tiene_marcado(self, client):
        """Es lo pedido: el papel sale con la combinación que armó, no con la
        cotización entera."""
        code, token = _cotizacion(items=[("A", 100000, 1), ("B", 50000, 1)])
        try:
            with A.app.app_context():
                ids = [i.id for i in A.Quote.query.filter_by(code=code).first().items]
            r = client.post(f"/c/{token}/pdf", data={"items": [str(ids[0])]})
            assert r.status_code == 200
            assert r.data.startswith(b"%PDF")
            with A.app.app_context():
                c = A.Quote.query.filter_by(code=code).first()
                assert len(c.versiones) == 1
                assert c.versiones[0].total == 100000
                assert len(c.items) == 2, "la cotización original no se toca"
        finally:
            _borrar(code)

    def test_el_archivo_de_una_version_lo_dice_en_el_nombre(self, client):
        """Dos PDF con el mismo código en la carpeta de descargas tienen que
        poder distinguirse."""
        code, token = _cotizacion(items=[("A", 100000, 1)])
        try:
            with A.app.app_context():
                ids = [i.id for i in A.Quote.query.filter_by(code=code).first().items]
            cd = client.post(f"/c/{token}/pdf",
                             data={"items": [str(ids[0])]}).headers["Content-Disposition"]
            assert "-v2" in cd, cd
        finally:
            _borrar(code)

    def test_el_pdf_de_la_version_respeta_la_absorcion(self, client):
        """Si el cliente manda el capó junto a Full Car, el PDF no puede
        cobrarlo dos veces solo porque venga marcado del navegador."""
        code, token = _cotizacion(ppf=["Full Car", "Capó"])
        try:
            r = client.post(f"/c/{token}/pdf",
                            data={"ppf": ["Full Car", "Capó"], "marca": "Xpel"})
            assert r.data.startswith(b"%PDF")
            with A.app.app_context():
                assert A.Quote.query.filter_by(code=code).first().versiones[0].total == 15_000_000
        finally:
            _borrar(code)

    def test_una_seleccion_vacia_no_revienta(self, client):
        code, token = _cotizacion(items=[("A", 100000, 1)])
        try:
            r = client.post(f"/c/{token}/pdf", data={})
            assert r.status_code == 200
            assert r.data.startswith(b"%PDF")
        finally:
            _borrar(code)

    def test_vencida_tampoco_por_post(self, client):
        code, token = _cotizacion(items=[("A", 100000, 1)])
        try:
            with A.app.app_context():
                c = A.Quote.query.filter_by(code=code).first()
                c.valid_until = A.bogota_now().date() - dt.timedelta(days=1)
                A.db.session.commit()
            assert client.post(f"/c/{token}/pdf", data={}).status_code == 410
        finally:
            _borrar(code)


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
                              ppf=["Full Car", "Capó"], marca="Xpel")
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


class TestElBotonDePdfMandaLaSeleccion:
    """El PDF personalizado salía VACÍO, en $0.

    El handler del formulario armaba los campos interpolando en una plantilla de
    texto y llamaba a `esc()` — una función que solo existe en la pantalla
    interna, no en la del cliente. Reventaba en la primera cobertura, así que
    los campos nunca se escribían y el POST llegaba sin nada.

    El endpoint estaba bien y sus tests pasaban: se probaba con un POST directo,
    que no ejercita el botón. Estos tests miran el JS que lo llena.
    """

    def _script(self, client, token):
        cuerpo = client.get(f"/c/{token}").data.decode()
        return cuerpo[cuerpo.index("<script>"):]

    def test_no_usa_funciones_que_no_existen_en_esta_pagina(self, client):
        code, token = _cotizacion(items=[("A", 100000, 1)])
        try:
            js = self._script(client, token)
            for fn in ("esc(", "fmtCop("):
                if f"{fn}" in js:
                    assert f"const {fn[:-1]} =" in js or f"function {fn[:-1]}" in js, (
                        f"la página del cliente llama a {fn} sin definirla")
        finally:
            _borrar(code)

    def test_el_formulario_arma_los_campos_con_el_dom(self, client):
        """Creándolos con el DOM no hay nada que escapar, que es de donde vino
        el error."""
        code, token = _cotizacion(items=[("A", 100000, 1)])
        try:
            js = self._script(client, token)
            assert 'createElement("input")' in js
            assert "camposPdf" in js
        finally:
            _borrar(code)

    def test_cada_servicio_lleva_su_id_para_poder_mandarlo(self, client):
        """Sin el id en el marcador, el POST no puede decir cuál se marcó."""
        code, token = _cotizacion(items=[("A", 100000, 1)])
        try:
            with A.app.app_context():
                iid = A.Quote.query.filter_by(code=code).first().items[0].id
            assert f'data-svc="{iid}"' in client.get(f"/c/{token}").data.decode()
        finally:
            _borrar(code)


class TestGarantiasDePolarizado:
    def test_se_siembran_por_marca(self):
        with A.app.app_context():
            A.seed_garantias_polarizado()
            esperado = {"tecnofilm": "5 años", "spectra": "7 años", "ultraoptic": "10 años"}
            for s in A.Service.query.filter(A.Service.name.ilike("%polarizado%")).all():
                import unicodedata
                n = "".join(c for c in unicodedata.normalize("NFD", s.name.lower())
                            if unicodedata.category(c) != "Mn")
                for marca, gar in esperado.items():
                    if marca in n:
                        assert s.garantia == gar, f"{s.name} quedó en {s.garantia}"

    def test_no_pisa_una_garantia_ya_puesta(self):
        """Si un redespliegue revirtiera los ajustes, la pantalla no serviría."""
        with A.app.app_context():
            s = A.Service.query.filter(A.Service.name.ilike("%tecnofilm%")).first()
            if not s:
                import pytest
                pytest.skip("la base de prueba no tiene ese servicio")
            s.garantia = "de por vida"
            A.db.session.commit()
        try:
            A.seed_garantias_polarizado()
            with A.app.app_context():
                assert A.Service.query.filter(
                    A.Service.name.ilike("%tecnofilm%")).first().garantia == "de por vida"
        finally:
            with A.app.app_context():
                A.Service.query.filter(A.Service.name.ilike("%tecnofilm%")).first().garantia = "5 años"
                A.db.session.commit()

    def test_no_le_pone_garantia_a_lo_que_no_es_polarizado(self):
        with A.app.app_context():
            A.seed_garantias_polarizado()
            lavado = A.Service.query.filter(A.Service.name.ilike("%lavado%")).first()
            if lavado:
                assert lavado.garantia in (None, "")


class TestElLinkYElPdfDicenLoMismo:
    """El link sumaba menos que el PDF cuando había fotocromático: el JS no
    conocía el adicional. El cliente veía dos totales distintos del mismo
    código, y el que tuviera a mano sería el que creyera.
    """

    def _con_fotocromatico(self):
        import json
        import secrets
        with A.app.app_context():
            pk = A.PpfPackage.query.filter_by(name="Farolas y Stops").first()
            c = A.Quote(code=A._nuevo_codigo_cotizacion(),
                        public_token=secrets.token_urlsafe(24),
                        customer_name="Coherencia", created_at=A.datetime.utcnow(),
                        valid_until=A.bogota_now().date() + dt.timedelta(days=15),
                        ppf_brands=json.dumps([["Avery", 7], ["Xpel", 10]]))
            c.ppf_items = [A.QuotePpfItem(
                coverage=pk.name, contains=pk.contains, zona="exterior",
                parts_json=json.dumps([x.name for x in pk.parts]), orden=pk.orden,
                prices_json=json.dumps(pk.precios),
                foto_prices_json=json.dumps(pk.precios_fotocromatico))]
            A.db.session.add(c)
            A.db.session.commit()
            return c.code, c.public_token

    def test_el_link_manda_el_adicional_al_navegador(self, client):
        code, token = self._con_fotocromatico()
        try:
            cuerpo = client.get(f"/c/{token}").data.decode()
            assert "FOTO_PPF" in cuerpo, "el navegador no recibe el adicional"
            linea = next(l for l in cuerpo.splitlines() if "const FOTO_PPF" in l)
            assert "100000" in linea and "150000" in linea
        finally:
            _borrar(code)

    def test_el_total_del_servidor_incluye_el_adicional(self, client):
        """Es contra este número que tiene que cuadrar el del navegador."""
        code, _token = self._con_fotocromatico()
        try:
            with A.app.app_context():
                c = A.Quote.query.filter_by(code=code).first()
                assert c.ppf_totales["Avery"] == 400_000 + 100_000
                assert c.ppf_totales["Xpel"] == 450_000 + 150_000
        finally:
            _borrar(code)

    def test_la_pagina_dice_que_lleva_fotocromatico(self, client):
        code, token = self._con_fotocromatico()
        try:
            assert "con fotocromático" in client.get(f"/c/{token}").data.decode()
        finally:
            _borrar(code)


class TestDosPartes:
    """Servicios y PPF salen como dos cotizaciones con su total, y una suma al
    final — en un mismo archivo y un mismo link."""

    def _mixta(self):
        import json
        import secrets
        with A.app.app_context():
            pk = A.PpfPackage.query.filter_by(name="Manijas").first()
            c = A.Quote(code=A._nuevo_codigo_cotizacion(),
                        public_token=secrets.token_urlsafe(24),
                        customer_name="Mixta", created_at=A.datetime.utcnow(),
                        valid_until=A.bogota_now().date() + dt.timedelta(days=15),
                        ppf_brands=json.dumps([["Xpel", 10]]))
            c.items = [A.QuoteItem(description="Lavado", unit_price=90_000, quantity=1)]
            c.ppf_items = [A.QuotePpfItem(
                coverage=pk.name, contains=pk.contains, zona="exterior",
                parts_json=json.dumps([x.name for x in pk.parts]), orden=pk.orden,
                prices_json=json.dumps(pk.precios))]
            A.db.session.add(c)
            A.db.session.commit()
            return c.code, c.public_token

    def test_el_link_numera_las_partes(self, client):
        code, token = self._mixta()
        try:
            cuerpo = client.get(f"/c/{token}").data.decode()
            assert "Parte 1 · Servicios" in cuerpo
            assert "Parte 2 · Protección PPF" in cuerpo
        finally:
            _borrar(code)

    def test_con_una_sola_parte_no_numera(self, client):
        """"Parte 1 de 1" es ruido."""
        code, token = _cotizacion(items=[("Lavado", 90000, 1)])
        try:
            cuerpo = client.get(f"/c/{token}").data.decode()
            assert "Parte 1" not in cuerpo
        finally:
            _borrar(code)

    def test_el_pdf_sale_con_las_dos_partes(self, client):
        code, _token = self._mixta()
        try:
            with A.app.app_context():
                c = A.Quote.query.filter_by(code=code).first()
                assert c.items and c.ppf_items
                assert A._construir_pdf_cotizacion(c).startswith(b"%PDF")
                assert c.totales_por_marca["Xpel"] == 90_000 + 350_000
        finally:
            _borrar(code)
