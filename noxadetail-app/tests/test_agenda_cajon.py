"""Lo que va dentro del cajón de una cita en la agenda.

El recorte por alto lo hace el navegador (no se puede medir desde acá), pero sí
se puede fijar QUÉ se manda y en qué orden: nombre, placa, servicio abreviado,
saldo y notas.
"""

from datetime import datetime

import pytest

from conftest import db, login_as, make_user
import app as app_module


class TestAbreviarServicios:
    @pytest.mark.parametrize("nombre, esperado", [
        ("Wash Essential", "Wash Ess"),
        ("Coating Ceramico 9H", "Cerámico 9H"),
        ("Detallado Llanta a Llanta", "Det. L a L"),
        ("Porcelanizado", "Porcelanizado"),          # corto, se deja igual
        ("Instalación PPF Completa", "Inst PPF Comp"),
    ])
    def test_nombres_conocidos_y_regla_general(self, nombre, esperado):
        assert app_module.abreviar_servicios(nombre) == esperado

    def test_las_siglas_no_se_cortan(self):
        assert "PPF" in app_module.abreviar_servicios("Instalación PPF Completa")

    def test_un_nombre_larguisimo_termina_en_puntos(self):
        corto = app_module.abreviar_servicios(
            "Instalacion fibra de carbono en paneles y puertas")
        assert corto.endswith("…")
        assert len(corto) <= 20

    def test_dos_servicios_van_los_dos(self):
        assert app_module.abreviar_servicios("Wash Chasis, Wash Motor") == "Chasis + Motor"

    def test_de_tres_en_adelante_se_cuenta_el_resto(self):
        assert app_module.abreviar_servicios(
            "Wash Chasis, Wash Motor, Polichado, Porcelanizado") == "Chasis +3"

    def test_sin_servicios_no_revienta(self):
        assert app_module.abreviar_servicios("") == ""
        assert app_module.abreviar_servicios(None) == ""


class TestLineasDelEvento:
    @pytest.fixture
    def cita(self):
        precio = (app_module.ServicePrice.query
                  .filter(app_module.ServicePrice.is_active == True,   # noqa: E712
                          app_module.ServicePrice.price > 0).first())
        servicio = db.session.get(app_module.Service, precio.service_id)
        appt = app_module.Appointment(
            customer_name="Fabián Restrepo Gómez", plate="qrs123",
            services=servicio.name,
            start_datetime=datetime(2026, 6, 20, 9, 0),
            end_datetime=datetime(2026, 6, 20, 10, 0),
            notes="Instalar ppf\n  completo,  revisar farolas",
            vehicle_type_id=precio.vehicle_type_id, status="scheduled",
        )
        db.session.add(appt)
        db.session.commit()
        yield appt, precio.price
        db.session.delete(appt)
        db.session.commit()

    def _lineas(self, client, appt):
        eventos = client.get("/api/events").get_json()
        evento = next(e for e in eventos if e["id"] == appt.id)
        return evento["extendedProps"]["lineas"]

    def test_manda_las_cinco_lineas(self, client, cita):
        appt, precio = cita
        login_as(client, make_user("admin_test", role="admin"))
        lineas = self._lineas(client, appt)

        # El ORDEN en que se pintan lo decide calendar.html (jsonify entrega las
        # claves alfabéticas); acá se fija que estén las cinco y con qué valor.
        assert set(lineas) == {"nombre", "placa", "servicio", "saldo", "notas"}
        assert lineas["nombre"] == "Fabián", "solo el primer nombre, el cajón es angosto"
        assert lineas["placa"] == "QRS123"
        assert lineas["saldo"] == "$" + f"{precio:,}".replace(",", ".")

    def test_las_notas_van_en_una_sola_linea(self, client, cita):
        appt, _ = cita
        login_as(client, make_user("admin_test", role="admin"))
        notas = self._lineas(client, appt)["notas"]
        assert "\n" not in notas
        assert "  " not in notas, "los espacios de más desperdician ancho"

    def test_sin_abonos_la_cifra_va_sola(self, client, cita):
        appt, precio = cita
        login_as(client, make_user("admin_test", role="admin"))
        # Sin abonos el saldo ES el valor del servicio: la palabra sobra.
        assert not self._lineas(client, appt)["saldo"].startswith("Saldo")

    def test_con_abono_se_dice_que_es_un_saldo(self, client, cita):
        appt, precio = cita
        appt.payments.append(app_module.AppointmentPayment(
            amount=precio // 2, paid_on=datetime(2026, 6, 19).date()))
        db.session.commit()

        login_as(client, make_user("admin_test", role="admin"))
        saldo = self._lineas(client, appt)["saldo"]
        assert saldo.startswith("Saldo "), "con un abono de por medio hay que decir qué es la cifra"
        assert f"{precio - precio // 2:,}".replace(",", ".") in saldo

    def test_si_abonaron_de_mas_dice_a_favor(self, client, cita):
        appt, precio = cita
        appt.payments.append(app_module.AppointmentPayment(
            amount=precio + 10000, paid_on=datetime(2026, 6, 19).date()))
        db.session.commit()

        login_as(client, make_user("admin_test", role="admin"))
        assert self._lineas(client, appt)["saldo"] == "A favor $10.000"


class TestAgendaDeDiagnosticos:
    """Dos agendas con la misma pantalla: la que factura y la de diagnósticos."""

    @pytest.fixture
    def escenario(self):
        # El catálogo semilla no siempre trae el servicio de diagnóstico; se
        # crea acá y se borra al final para no ensuciar los demás tests.
        diag = app_module._diagnostic_service()
        diag_creado = False
        if not diag:
            diag = app_module.Service(name=app_module.DIAGNOSTIC_SERVICE_NAME,
                                      duration_minutes=30, is_active=True,
                                      is_diagnostic=True)
            db.session.add(diag)
            db.session.commit()
            diag_creado = True

        precio = (app_module.ServicePrice.query
                  .filter(app_module.ServicePrice.is_active == True,   # noqa: E712
                          app_module.ServicePrice.price > 0)
                  .filter(app_module.ServicePrice.service_id != diag.id).first())
        otro = db.session.get(app_module.Service, precio.service_id)

        def crear(placa, servicios, hora):
            ini = datetime(2026, 6, 25, hora, 0)
            a = app_module.Appointment(
                customer_name="Cliente " + placa, plate=placa, services=servicios,
                start_datetime=ini, end_datetime=ini + app_module.timedelta(minutes=60),
                vehicle_type_id=precio.vehicle_type_id, status="scheduled")
            db.session.add(a)
            return a

        creadas = [
            crear("SOLODIAG", diag.name, 9),
            crear("SOLOCITA", otro.name, 11),
            crear("MIXTA001", f"{diag.name}, {otro.name}", 13),
        ]
        db.session.commit()
        yield {a.plate: a for a in creadas}
        for a in creadas:
            db.session.delete(a)
        if diag_creado:
            db.session.delete(diag)
        db.session.commit()

    def _placas(self, client, modo):
        eventos = client.get(f"/api/events?modo={modo}").get_json()
        return {e["extendedProps"]["lineas"]["placa"] for e in eventos}

    def test_cada_agenda_ve_lo_suyo(self, client, escenario):
        login_as(client, make_user("admin_test", role="admin"))
        assert "SOLODIAG" in self._placas(client, "diagnosticos")
        assert "SOLODIAG" not in self._placas(client, "citas")
        assert "SOLOCITA" in self._placas(client, "citas")
        assert "SOLOCITA" not in self._placas(client, "diagnosticos")

    def test_una_cita_mixta_cuenta_como_cita(self, client, escenario):
        """Si el cliente aprovechó y agendó también un servicio, ya factura."""
        login_as(client, make_user("admin_test", role="admin"))
        assert "MIXTA001" in self._placas(client, "citas")
        assert "MIXTA001" not in self._placas(client, "diagnosticos")

    def test_sin_modo_se_asume_la_agenda_de_citas(self, client, escenario):
        login_as(client, make_user("admin_test", role="admin"))
        eventos = client.get("/api/events").get_json()
        placas = {e["extendedProps"]["lineas"]["placa"] for e in eventos}
        assert "SOLOCITA" in placas and "SOLODIAG" not in placas

    def test_en_diagnosticos_no_se_repite_la_palabra_diagnostico(self, client, escenario):
        """Todos los cajones dirían lo mismo; el renglón rinde más con las notas."""
        login_as(client, make_user("admin_test", role="admin"))
        eventos = client.get("/api/events?modo=diagnosticos").get_json()
        assert all(e["extendedProps"]["lineas"]["servicio"] == "" for e in eventos)

    def test_un_diagnostico_gratis_no_muestra_cero(self, client, escenario):
        login_as(client, make_user("admin_test", role="admin"))
        eventos = client.get("/api/events?modo=diagnosticos").get_json()
        evento = next(e for e in eventos
                      if e["extendedProps"]["lineas"]["placa"] == "SOLODIAG")
        assert evento["extendedProps"]["lineas"]["saldo"] == "", \
            "un '$0' no informa y le quita el renglón a las notas"

    def test_marketing_si_entra_a_la_agenda(self, client, escenario):
        """Se le abrió a pedido del negocio: la agencia necesita ver qué hay
        agendado para planear contenido y campañas."""
        login_as(client, make_user("agencia", role="marketing"))
        assert client.get("/calendar/diagnosticos").status_code == 200
        assert client.get("/calendar").status_code == 200

    def test_pero_no_ve_la_plata_de_cada_cita(self, client, escenario):
        """"Marketing ve conversión y comportamiento de clientes, no la caja."
        Antes no se notaba porque no llegaba a ninguna pantalla con precios; con
        la agenda sí llega, y cada cita mostraría lo que factura."""
        login_as(client, make_user("agencia2", role="marketing"))
        eventos = client.get("/api/events?modo=citas").get_json()
        assert eventos, "sin eventos el test no probaría nada"
        assert all(e["extendedProps"]["lineas"]["saldo"] == "" for e in eventos)

    def test_y_no_puede_operar_la_agenda(self, client, escenario):
        """Mirar no es operar: crear, editar o borrar citas siguen fuera."""
        login_as(client, make_user("agencia3", role="marketing"))
        for ruta in ("/appointments/new", "/appointments"):
            r = client.get(ruta)
            assert r.status_code == 302, f"{ruta} quedó abierta para marketing"


class TestDondeAterrizaCadaRol:
    """Al abrirle la agenda a marketing dejó de existir el rebote que lo mandaba
    al inbox, así que la pantalla de aterrizaje pasó a ser explícita."""

    def test_marketing_sigue_cayendo_en_mensajes(self, client):
        with app_module.app.app_context():
            u = make_user("agencia_land", role="marketing")
            u.set_password("clave-larga-1234")
            u.must_change_password = False
            db.session.commit()
        r = client.post("/login", data={"username": "agencia_land",
                                        "password": "clave-larga-1234"})
        assert r.status_code == 302 and "/whatsapp" in r.headers["Location"]

    def test_los_demas_siguen_cayendo_en_la_agenda(self, client):
        with app_module.app.app_context():
            u = make_user("admin_land", role="admin")
            u.set_password("clave-larga-1234")
            u.must_change_password = False
            db.session.commit()
        r = client.post("/login", data={"username": "admin_land",
                                        "password": "clave-larga-1234"})
        assert r.status_code == 302 and "calendar" in r.headers["Location"]


class TestMarketingYLasCotizaciones:
    """Se le abrió a pedido del negocio: la agencia necesita ver qué se le
    cotizó a cada cliente para hacerle seguimiento a la conversación.

    Solo LEER. Lo que de verdad la limita es la lista blanca de endpoints, no
    `puede_cotizar()` — esa dejó de ser un alias de `puede_ver_precios` porque
    son dos preguntas distintas: si se entra a una pantalla, y si dentro de ella
    se muestran cifras.
    """

    @pytest.fixture
    def agencia(self, client):
        login_as(client, make_user("agencia_cot", role="marketing"))
        return client

    def test_entra_al_listado_y_al_detalle(self, agencia):
        # La cotización se inserta directo: crearla por la ruta necesitaría un
        # segundo cliente logueado como admin, y el usuario se desprende de la
        # sesión al salir del contexto.
        import secrets
        with app_module.app.app_context():
            c = app_module.Quote(
                code=app_module._nuevo_codigo_cotizacion(),
                public_token=secrets.token_urlsafe(24),
                customer_name="Laura Ortiz",
                created_at=app_module.datetime.utcnow(),
                valid_until=app_module.bogota_today())
            db.session.add(c)
            db.session.commit()
            code = c.code
        try:
            assert agencia.get("/quotes").status_code == 200
            assert agencia.get(f"/quotes/{code}").status_code == 200
        finally:
            with app_module.app.app_context():
                c = app_module.Quote.query.filter_by(code=code).first()
                if c:
                    db.session.delete(c)
                    db.session.commit()

    @pytest.mark.parametrize("ruta", [
        "/quotes/new",
        "/ppf-prices",
        "/price-requests",
    ])
    def test_pero_no_puede_crear_ni_ver_los_costos(self, agencia, ruta):
        """Los precios de PPF y lo que cobra un instalador son el costo del
        negocio, no la conversación con el cliente."""
        r = agencia.get(ruta)
        assert r.status_code == 302, f"{ruta} quedó abierta para marketing"

    def test_un_operario_sigue_sin_entrar(self, client):
        """La regla que no cambió: el operario no ve cuánto valen las cosas."""
        login_as(client, make_user("operario_cot", role="operario"))
        assert client.get("/quotes").status_code == 302


class TestMarketingYElTableroDeSeguimiento:
    """Se le abrió a pedido del negocio. Encaja con lo que ya hacía: la agencia
    contesta la bandeja de WhatsApp, y el tablero es la lista de a quién le toca
    hoy. No muestra plata — sus números son cuántos faltan, no cuánto valen."""

    @pytest.fixture
    def agencia(self, client):
        login_as(client, make_user("agencia_seg", role="marketing"))
        return client

    def test_entra_al_tablero(self, agencia):
        assert agencia.get("/seguimiento").status_code == 200

    def test_puede_marcar_una_tarjeta(self, agencia):
        """Un tablero de "a quién contactar hoy" donde no se puede marcar lo ya
        contactado se llena de tarjetas viejas y se deja de mirar."""
        r = agencia.post("/seguimiento/gestionar",
                         json={"tipo": "sin_responder", "telefono": "+573001234567",
                               "accion": "contactado"})
        assert r.status_code == 200

    def test_el_menu_le_muestra_el_enlace(self, agencia):
        """Si la ruta abre pero el menú no lo pinta, la pantalla existe y nadie
        llega a ella."""
        cuerpo = agencia.get("/whatsapp").data.decode()
        assert 'href="/seguimiento"' in cuerpo

    def test_el_operario_sigue_afuera(self, client):
        login_as(client, make_user("operario_seg", role="operario"))
        assert client.get("/seguimiento").status_code == 302

    def test_el_menu_no_le_ofrece_lo_que_no_puede_abrir(self, client):
        """Contraprueba del enlace: si el menú lo pintara siempre, el test de
        arriba pasaría sin probar nada."""
        login_as(client, make_user("operario_seg2", role="operario"))
        cuerpo = client.get("/").data.decode()
        assert 'href="/seguimiento"' not in cuerpo
