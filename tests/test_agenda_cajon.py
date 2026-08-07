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
