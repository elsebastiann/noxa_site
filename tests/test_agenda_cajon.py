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

    def test_marketing_no_entra_a_la_agenda(self, client, escenario):
        login_as(client, make_user("agencia", role="marketing"))
        r = client.get("/calendar/diagnosticos")
        assert r.status_code == 302 and "/whatsapp" in r.headers["Location"]
