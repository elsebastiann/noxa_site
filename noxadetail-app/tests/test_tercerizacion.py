"""Servicios tercerizados: polarizado, PPF y wrap.

Los hace un instalador externo que normalmente pone el material y se queda con
el 65% de lo cobrado. Hasta ahora un polarizado de 975.000 entraba completo
como ingreso de Noxa, cuando en realidad solo entran 341.250.

Lo que estos tests fijan:
  • El cobro al cliente NO cambia — sigue debiendo el total.
  • El ingreso que ve la analítica sí: `ingreso_noxa` descuenta al instalador.
  • El reparto es por servicio, no por cita: un lavado en la misma cita no se
    reparte.
  • Si se dio descuento, el instalador cobra sobre lo realmente pagado.
"""
import datetime as dt

import pytest

from conftest import app_module as A


@pytest.fixture
def catalogo():
    """Un servicio tercerizado con precio de lista, uno a medida y uno propio."""
    with A.app.app_context():
        vt = A.VehicleType.query.filter_by(is_active=True).first()

        polarizado = A.Service(name="Polarizado Test", duration_minutes=120,
                               is_active=True, is_outsourced=True,
                               default_installer_share=65)
        ppf_medida = A.Service(name="PPF a Medida Test", duration_minutes=180,
                               is_active=True, is_outsourced=True,
                               default_installer_share=65, is_custom_price=True)
        lavado = A.Service(name="Lavado Propio Test", duration_minutes=60, is_active=True)
        instalador = A.Installer(name="Instalador Test", default_share=65)
        A.db.session.add_all([polarizado, ppf_medida, lavado, instalador])
        A.db.session.commit()

        A.db.session.add_all([
            A.ServicePrice(service_id=polarizado.id, vehicle_type_id=vt.id,
                           price=975_000, duration_minutes=120, is_active=True),
            A.ServicePrice(service_id=lavado.id, vehicle_type_id=vt.id,
                           price=100_000, duration_minutes=60, is_active=True),
        ])
        A.db.session.commit()
        ids = {"vt": vt.id, "polarizado": polarizado.id, "ppf": ppf_medida.id,
               "lavado": lavado.id, "instalador": instalador.id}

    yield ids

    with A.app.app_context():
        A.ServicePrice.query.filter(
            A.ServicePrice.service_id.in_([ids["polarizado"], ids["ppf"], ids["lavado"]])
        ).delete(synchronize_session=False)
        A.Service.query.filter(
            A.Service.id.in_([ids["polarizado"], ids["ppf"], ids["lavado"]])
        ).delete(synchronize_session=False)
        A.Installer.query.filter_by(id=ids["instalador"]).delete()
        A.db.session.commit()


def _cita(ids, servicios, outsourcings=(), adjustments=()):
    inicio = dt.datetime.combine(A.bogota_now().date() + dt.timedelta(days=1), dt.time(9, 0))
    appt = A.Appointment(
        customer_name="Prueba", plate="TER001", services=servicios,
        start_datetime=inicio, end_datetime=inicio + dt.timedelta(hours=2),
        vehicle_type_id=ids["vt"], status="scheduled",
    )
    A.db.session.add(appt)
    A.db.session.commit()
    for o in outsourcings:
        A.db.session.add(A.AppointmentOutsourcing(appointment_id=appt.id, **o))
    for aj in adjustments:
        A.db.session.add(A.AppointmentAdjustment(appointment_id=appt.id, **aj))
    A.db.session.commit()
    return appt


class TestRepartoBasico:
    def test_el_cliente_sigue_debiendo_el_total(self, catalogo):
        """Tercerizar no cambia lo que se le cobra: cambia a quién le queda."""
        appt = _cita(catalogo, "Polarizado Test", [
            {"service_name": "Polarizado Test", "installer_id": catalogo["instalador"],
             "installer_pct": 65, "material_por": A.MATERIAL_INSTALADOR},
        ])
        m = A.appointment_money(appt)

        assert m["total"] == 975_000          # lo que cobra al cliente
        assert m["costo_tercerizacion"] == 633_750
        assert m["ingreso_noxa"] == 341_250   # lo que de verdad entra

    def test_material_de_noxa_invierte_el_reparto(self, catalogo):
        appt = _cita(catalogo, "Polarizado Test", [
            {"service_name": "Polarizado Test", "installer_id": catalogo["instalador"],
             "installer_pct": 35, "material_por": A.MATERIAL_NOXA},
        ])
        m = A.appointment_money(appt)

        assert m["costo_tercerizacion"] == 341_250
        assert m["ingreso_noxa"] == 633_750

    def test_una_cita_sin_tercerizacion_no_cambia(self, catalogo):
        """La gran mayoría de citas no se reparten: no pueden verse afectadas."""
        appt = _cita(catalogo, "Lavado Propio Test")
        m = A.appointment_money(appt)

        assert m["total"] == 100_000
        assert m["costo_tercerizacion"] == 0
        assert m["ingreso_noxa"] == m["total"]


class TestRepartoPorServicio:
    def test_solo_se_reparte_el_servicio_tercerizado(self, catalogo):
        """Aplicar el % al total de la cita le regalaría al instalador un
        pedazo del lavado, que es trabajo propio de Noxa."""
        appt = _cita(catalogo, "Polarizado Test, Lavado Propio Test", [
            {"service_name": "Polarizado Test", "installer_id": catalogo["instalador"],
             "installer_pct": 65, "material_por": A.MATERIAL_INSTALADOR},
        ])
        m = A.appointment_money(appt)

        assert m["total"] == 1_075_000
        # 65% de 975.000, NO de 1.075.000
        assert m["costo_tercerizacion"] == 633_750
        assert m["ingreso_noxa"] == 441_250   # 341.250 del polarizado + 100.000 del lavado


class TestTrabajosAMedida:
    def test_el_valor_cotizado_entra_al_precio(self, catalogo):
        """Un PPF a medida no tiene fila en ServicePrice: sin esto la cita
        valdría 0 y el trabajo desaparecería de los ingresos."""
        appt = _cita(catalogo, "PPF a Medida Test", [
            {"service_name": "PPF a Medida Test", "installer_id": catalogo["instalador"],
             "installer_pct": 65, "material_por": A.MATERIAL_INSTALADOR,
             "amount": 480_000, "description": "Bomper delantero y retrovisores"},
        ])
        m = A.appointment_money(appt)

        assert m["total"] == 480_000
        assert m["costo_tercerizacion"] == 312_000
        assert m["ingreso_noxa"] == 168_000

    def test_se_guarda_que_se_forro(self, catalogo):
        appt = _cita(catalogo, "PPF a Medida Test", [
            {"service_name": "PPF a Medida Test", "installer_id": catalogo["instalador"],
             "installer_pct": 65, "material_por": A.MATERIAL_INSTALADOR,
             "amount": 480_000, "description": "Bomper delantero y retrovisores"},
        ])
        linea = A.appointment_money(appt)["tercerizado"][0]

        assert linea["descripcion"] == "Bomper delantero y retrovisores"
        assert linea["a_medida"] is True

    def test_a_medida_junto_a_un_servicio_de_lista(self, catalogo):
        appt = _cita(catalogo, "PPF a Medida Test, Lavado Propio Test", [
            {"service_name": "PPF a Medida Test", "installer_id": catalogo["instalador"],
             "installer_pct": 65, "material_por": A.MATERIAL_INSTALADOR, "amount": 480_000},
        ])
        m = A.appointment_money(appt)

        assert m["total"] == 580_000
        assert m["ingreso_noxa"] == 580_000 - 312_000


class TestDescuentos:
    def test_el_instalador_cobra_sobre_lo_realmente_pagado(self, catalogo):
        """Si se descuenta, el instalador no puede llevarse el 65% de una plata
        que nunca entró — quedaría cobrando más de lo que Noxa recibió."""
        appt = _cita(catalogo, "Polarizado Test", [
            {"service_name": "Polarizado Test", "installer_id": catalogo["instalador"],
             "installer_pct": 65, "material_por": A.MATERIAL_INSTALADOR},
        ], adjustments=[
            {"kind": "discount", "mode": "percentage", "value": 10, "base": "lista"},
        ])
        m = A.appointment_money(appt)

        assert m["total"] == 877_500                    # 975.000 − 10%
        assert m["costo_tercerizacion"] == 570_375      # 65% de 877.500
        assert m["ingreso_noxa"] == 307_125

    def test_el_descuento_se_reparte_entre_las_lineas(self, catalogo):
        """El descuento es de la cita, no de un servicio: se prorratea, así que
        el instalador absorbe solo la parte proporcional a su línea."""
        appt = _cita(catalogo, "Polarizado Test, Lavado Propio Test", [
            {"service_name": "Polarizado Test", "installer_id": catalogo["instalador"],
             "installer_pct": 65, "material_por": A.MATERIAL_INSTALADOR},
        ], adjustments=[
            {"kind": "discount", "mode": "fixed", "value": 107_500},   # 10% de 1.075.000
        ])
        m = A.appointment_money(appt)

        assert m["total"] == 967_500
        # El polarizado bajó a 877.500 (su 90%), no absorbió el descuento del lavado.
        assert m["tercerizado"][0]["cobrado"] == 877_500
        assert m["costo_tercerizacion"] == 570_375
