"""Plata de una cita: descuentos/recargos contra abonos.

La regla que estos tests protegen es una sola y es la razón de ser del módulo:
un abono NO cambia lo que vale el servicio, solo lo que falta por cobrar. Antes
los abonos se registraban como descuentos y eso bajaba los ingresos reportados
e inventaba descuentos que nadie otorgó.
"""

from datetime import date, datetime

import pytest

from conftest import db, flask_app, login_as, make_user
import app as app_module


@pytest.fixture
def catalogo():
    """Un servicio con precio real para un tipo de vehículo, del seed."""
    precio = (
        app_module.ServicePrice.query
        .filter(app_module.ServicePrice.is_active == True,      # noqa: E712
                app_module.ServicePrice.price > 0)
        .first()
    )
    assert precio, "el seed debería traer al menos un precio de servicio"
    servicio = db.session.get(app_module.Service, precio.service_id)
    return servicio, precio.vehicle_type_id, precio.price


@pytest.fixture
def cita(catalogo):
    servicio, vehiculo_id, _ = catalogo
    appt = app_module.Appointment(
        customer_name="Cliente Test",
        plate="TST999",
        services=servicio.name,
        start_datetime=datetime(2026, 6, 10, 9, 0),
        end_datetime=datetime(2026, 6, 10, 10, 0),
        vehicle_type_id=vehiculo_id,
        status="scheduled",
    )
    db.session.add(appt)
    db.session.commit()
    yield appt
    db.session.delete(appt)
    db.session.commit()


def _ajuste(kind, mode, value, description=None, base="lista"):
    return app_module.AppointmentAdjustment(
        kind=kind, mode=mode, value=value, base=base, description=description
    )


def _abono(amount, dia=None):
    return app_module.AppointmentPayment(amount=amount, paid_on=dia or date(2026, 6, 1))


class TestAbonoVsDescuento:
    def test_el_abono_no_baja_el_valor_del_servicio(self, cita, catalogo):
        _, _, lista = catalogo
        cita.payments.append(_abono(lista // 2))
        db.session.commit()

        plata = app_module.appointment_money(cita)
        assert plata["total"] == lista
        assert plata["abonado"] == lista // 2
        assert plata["saldo"] == lista - lista // 2
        # Lo que mira la analítica es el total, nunca el saldo.
        assert app_module.calculate_estimated_amount_for_appointment(cita) == lista

    def test_el_descuento_si_baja_el_valor_del_servicio(self, cita, catalogo):
        _, _, lista = catalogo
        cita.adjustments.append(_ajuste("discount", "fixed", 5000))
        db.session.commit()

        plata = app_module.appointment_money(cita)
        assert plata["total"] == lista - 5000
        assert app_module.calculate_estimated_amount_for_appointment(cita) == lista - 5000

    def test_abonar_de_mas_deja_saldo_a_favor(self, cita, catalogo):
        _, _, lista = catalogo
        cita.payments.append(_abono(lista + 10000))
        db.session.commit()

        plata = app_module.appointment_money(cita)
        assert plata["saldo"] == -10000, "un saldo a favor tiene que verse, no volverse cero"
        assert plata["total"] == lista


class TestVariosAjustes:
    def test_se_acumulan_descuentos_y_recargos(self, cita, catalogo):
        _, _, lista = catalogo
        cita.adjustments.append(_ajuste("discount", "fixed", 3000))
        cita.adjustments.append(_ajuste("discount", "fixed", 2000))
        cita.adjustments.append(_ajuste("surcharge", "fixed", 10000))
        db.session.commit()

        plata = app_module.appointment_money(cita)
        assert plata["descuentos"] == 5000
        assert plata["recargos"] == 10000
        assert plata["total"] == lista - 5000 + 10000

    def test_los_porcentajes_no_se_encadenan(self, cita, catalogo):
        _, _, lista = catalogo
        cita.adjustments.append(_ajuste("discount", "percentage", 10))
        cita.adjustments.append(_ajuste("discount", "percentage", 10))
        db.session.commit()

        # Dos veces 10% de la misma base, no 10% y luego 10% del resto.
        esperado = lista - 2 * round(lista * 0.10)
        assert app_module.appointment_money(cita)["total"] == esperado

    def test_el_orden_no_cambia_el_total(self, cita):
        ajustes = [_ajuste("discount", "percentage", 10),
                   _ajuste("surcharge", "fixed", 20000),
                   _ajuste("discount", "fixed", 5000)]
        total, _ = app_module.apply_adjustments(100000, ajustes)
        invertido, _ = app_module.apply_adjustments(100000, list(reversed(ajustes)))
        assert total == invertido == 100000 - 10000 + 20000 - 5000

    def test_los_descuentos_no_dejan_el_total_en_negativo(self, cita):
        total, _ = app_module.apply_adjustments(10000, [_ajuste("discount", "fixed", 999999)])
        assert total == 0

    def test_se_ignoran_las_filas_vacias_o_invalidas(self, cita):
        basura = [_ajuste("discount", "fixed", 0),
                  _ajuste("recargo_inventado", "fixed", 5000),
                  _ajuste("surcharge", "fixed", -100)]
        total, detalle = app_module.apply_adjustments(50000, basura)
        assert total == 50000
        assert detalle == []


class TestBaseDelPorcentaje:
    """Con convenio de por medio, un 10% sobre lista y un 10% sobre subtotal
    son plata distinta. Cada línea elige su base."""

    @pytest.fixture
    def con_convenio(self, cita):
        convenio = app_module.Agreement.query.filter_by(
            discount_type="percentage", is_active=True).first()
        assert convenio, "el seed debería traer un convenio en porcentaje"
        cita.agreement_id = convenio.id
        db.session.commit()
        return cita, convenio

    def test_sobre_lista_ignora_el_convenio(self, con_convenio, catalogo):
        cita, _ = con_convenio
        _, _, lista = catalogo
        subtotal = app_module.appointment_money(cita)["subtotal"]
        assert subtotal < lista, "el convenio debería estar rebajando algo"

        cita.adjustments.append(_ajuste("discount", "percentage", 10, base="lista"))
        db.session.commit()

        plata = app_module.appointment_money(cita)
        assert plata["descuentos"] == round(lista * 0.10)
        assert plata["total"] == subtotal - round(lista * 0.10)

    def test_sobre_subtotal_usa_el_valor_ya_con_convenio(self, con_convenio, catalogo):
        cita, _ = con_convenio
        subtotal = app_module.appointment_money(cita)["subtotal"]

        cita.adjustments.append(_ajuste("discount", "percentage", 10, base="subtotal"))
        db.session.commit()

        plata = app_module.appointment_money(cita)
        assert plata["descuentos"] == round(subtotal * 0.10)
        assert plata["total"] == subtotal - round(subtotal * 0.10)

    def test_las_dos_bases_dan_montos_distintos(self, con_convenio, catalogo):
        cita, _ = con_convenio
        _, _, lista = catalogo
        subtotal = app_module.appointment_money(cita)["subtotal"]

        sobre_lista, _ = app_module.apply_adjustments(
            subtotal, [_ajuste("discount", "percentage", 10, base="lista")], lista)
        sobre_sub, _ = app_module.apply_adjustments(
            subtotal, [_ajuste("discount", "percentage", 10, base="subtotal")], lista)
        assert sobre_lista < sobre_sub, "sobre lista descuenta más porque la base es mayor"

    def test_en_valor_fijo_la_base_no_cambia_nada(self, con_convenio):
        cita, _ = con_convenio
        subtotal = app_module.appointment_money(cita)["subtotal"]
        a, _ = app_module.apply_adjustments(
            subtotal, [_ajuste("discount", "fixed", 5000, base="lista")], 999999)
        b, _ = app_module.apply_adjustments(
            subtotal, [_ajuste("discount", "fixed", 5000, base="subtotal")], 999999)
        assert a == b == subtotal - 5000

    def test_sin_precio_de_lista_cae_al_subtotal(self):
        """apply_adjustments se puede llamar sin lista (cierres viejos): en ese
        caso la única referencia posible es el subtotal, y no debe reventar."""
        total, detalle = app_module.apply_adjustments(
            50000, [_ajuste("discount", "percentage", 10, base="lista")])
        assert total == 45000
        assert detalle[0]["amount"] == 5000

    def test_el_detalle_reporta_la_base_solo_en_porcentaje(self, cita):
        _, detalle = app_module.apply_adjustments(
            100000,
            [_ajuste("discount", "percentage", 10, base="subtotal"),
             _ajuste("discount", "fixed", 5000, base="lista")],
            100000)
        assert detalle[0]["base"] == "subtotal"
        assert detalle[1]["base"] is None, "en valor fijo la base no significa nada"


class TestFormulario:
    """El formulario manda listas paralelas; acá se prueba el parseo."""

    def _post(self, client, cita, catalogo, extra):
        servicio, vehiculo_id, _ = catalogo
        datos = {
            "customer_name": cita.customer_name,
            "plate": cita.plate,
            "phone": "",
            "date": "2026-06-10",
            "start_time": "09:00",
            "notes": "",
            "service_ids": [str(servicio.id)],
            "vehicle_type_id": str(vehiculo_id),
            "agreement_id": "",
        }
        datos.update(extra)
        return client.post(f"/appointment/{cita.id}/edit", data=datos)

    def test_guarda_varias_filas_de_cada_tipo(self, client, cita, catalogo):
        login_as(client, make_user("admin_test", role="admin"))
        self._post(client, cita, catalogo, {
            "adj_kind": ["discount", "surcharge"],
            "adj_mode": ["percentage", "fixed"],
            "adj_base": ["subtotal", "lista"],
            "adj_value": ["10", "20000"],
            "adj_desc": ["Frecuente", "Domicilio"],
            "pay_amount": ["50000", "30000"],
            "pay_date": ["2026-06-01", "2026-06-05"],
            "pay_desc": ["Abono inicial", ""],
        })
        db.session.refresh(cita)
        assert [(a.kind, a.mode, a.base, a.value) for a in cita.adjustments] == [
            ("discount", "percentage", "subtotal", 10),
            ("surcharge", "fixed", "lista", 20000)]
        assert [(p.amount, p.paid_on) for p in cita.payments] == [
            (50000, date(2026, 6, 1)), (30000, date(2026, 6, 5))]

    def test_sin_base_en_el_form_queda_sobre_lista(self, client, cita, catalogo):
        """El default acordado con la operación: si nadie elige, es sobre lista."""
        login_as(client, make_user("admin_test", role="admin"))
        self._post(client, cita, catalogo, {
            "adj_kind": ["discount"], "adj_mode": ["percentage"],
            "adj_value": ["10"], "adj_desc": [""],
        })
        db.session.refresh(cita)
        assert cita.adjustments[0].base == "lista"

    def test_una_base_inventada_cae_a_lista(self, client, cita, catalogo):
        login_as(client, make_user("admin_test", role="admin"))
        self._post(client, cita, catalogo, {
            "adj_kind": ["discount"], "adj_mode": ["percentage"],
            "adj_base": ["lo_que_sea"], "adj_value": ["10"], "adj_desc": [""],
        })
        db.session.refresh(cita)
        assert cita.adjustments[0].base == "lista"

    def test_una_fila_sin_valor_se_descarta(self, client, cita, catalogo):
        login_as(client, make_user("admin_test", role="admin"))
        self._post(client, cita, catalogo, {
            "adj_kind": ["discount", "discount"],
            "adj_mode": ["fixed", "fixed"],
            "adj_value": ["", "7000"],       # la primera quedó vacía
            "adj_desc": ["", ""],
            "pay_amount": ["", "1000"],
            "pay_date": ["", ""],
            "pay_desc": ["", ""],
        })
        db.session.refresh(cita)
        assert [a.value for a in cita.adjustments] == [7000]
        assert [p.amount for p in cita.payments] == [1000]

    def test_un_abono_sin_fecha_queda_con_la_de_hoy(self, client, cita, catalogo):
        login_as(client, make_user("admin_test", role="admin"))
        self._post(client, cita, catalogo, {
            "pay_amount": ["1000"], "pay_date": [""], "pay_desc": [""],
        })
        db.session.refresh(cita)
        assert cita.payments[0].paid_on == app_module.bogota_now().date()

    def test_editar_reemplaza_lo_que_habia(self, client, cita, catalogo):
        cita.adjustments.append(_ajuste("discount", "fixed", 9999))
        cita.payments.append(_abono(9999))
        db.session.commit()

        login_as(client, make_user("admin_test", role="admin"))
        self._post(client, cita, catalogo, {
            "adj_kind": ["surcharge"], "adj_mode": ["fixed"],
            "adj_value": ["1234"], "adj_desc": [""],
            "pay_amount": [], "pay_date": [], "pay_desc": [],
        })
        db.session.refresh(cita)
        assert [(a.kind, a.value) for a in cita.adjustments] == [("surcharge", 1234)]
        assert cita.payments == []


class TestBorrado:
    def test_borrar_la_cita_arrastra_ajustes_y_abonos(self, catalogo):
        servicio, vehiculo_id, _ = catalogo
        appt = app_module.Appointment(
            customer_name="Se borra", plate="DEL001", services=servicio.name,
            start_datetime=datetime(2026, 6, 11, 9, 0),
            end_datetime=datetime(2026, 6, 11, 10, 0),
            vehicle_type_id=vehiculo_id, status="scheduled",
        )
        appt.adjustments.append(_ajuste("discount", "fixed", 1000))
        appt.payments.append(_abono(2000))
        db.session.add(appt)
        db.session.commit()
        appt_id = appt.id

        db.session.delete(appt)
        db.session.commit()

        assert app_module.AppointmentAdjustment.query.filter_by(appointment_id=appt_id).count() == 0
        assert app_module.AppointmentPayment.query.filter_by(appointment_id=appt_id).count() == 0


class TestAnalitica:
    def test_el_abono_no_mueve_ingresos_ni_descuentos(self, cita, catalogo):
        _, _, lista = catalogo
        desde, hasta = date(2026, 6, 1), date(2026, 6, 30)

        antes = app_module._kpis_rentabilidad(desde, hasta)
        cita.payments.append(_abono(lista))
        db.session.commit()
        despues = app_module._kpis_rentabilidad(desde, hasta)

        assert antes["ingresos"] == despues["ingresos"]
        assert antes["descuentos"] == despues["descuentos"]

    def test_un_recargo_no_borra_los_descuentos_del_kpi(self, cita, catalogo):
        """El bug que aparece si se calcula `lista − cobrado`: un recargo grande
        deja la resta en negativo y los descuentos se ven como cero."""
        desde, hasta = date(2026, 6, 1), date(2026, 6, 30)
        base = app_module._kpis_rentabilidad(desde, hasta)["descuentos"]

        cita.adjustments.append(_ajuste("discount", "fixed", 5000))
        cita.adjustments.append(_ajuste("surcharge", "fixed", 500000))
        db.session.commit()

        kpis = app_module._kpis_rentabilidad(desde, hasta)
        assert kpis["descuentos"] == base + 5000
        assert kpis["recargos"] >= 500000
        assert kpis["descuentos_pct"] >= 0, "el porcentaje de descuento no puede ser negativo"


class TestMigracionDelAjusteViejo:
    def test_pasa_la_columna_vieja_a_una_fila_y_no_se_repite(self, catalogo):
        servicio, vehiculo_id, lista = catalogo
        appt = app_module.Appointment(
            customer_name="Legado", plate="OLD001", services=servicio.name,
            start_datetime=datetime(2026, 6, 12, 9, 0),
            end_datetime=datetime(2026, 6, 12, 10, 0),
            vehicle_type_id=vehiculo_id, status="scheduled",
            booking_adjustment_type="discount",
            booking_adjustment_mode="fixed",
            booking_adjustment_value=5000,
        )
        db.session.add(appt)
        db.session.commit()
        appt_id = appt.id

        app_module.migrate_booking_adjustments_to_rows()
        db.session.expire_all()
        appt = db.session.get(app_module.Appointment, appt_id)
        assert [(a.kind, a.value) for a in appt.adjustments] == [("discount", 5000)]
        assert appt.booking_adjustment_type is None, "la columna vieja debe quedar limpia"
        assert app_module.appointment_money(appt)["total"] == lista - 5000

        # Correrla de nuevo no puede duplicar el ajuste...
        app_module.migrate_booking_adjustments_to_rows()
        db.session.expire_all()
        appt = db.session.get(app_module.Appointment, appt_id)
        assert len(appt.adjustments) == 1

        # ...ni resucitar uno que alguien borró a mano.
        appt.adjustments.clear()
        db.session.commit()
        app_module.migrate_booking_adjustments_to_rows()
        db.session.expire_all()
        appt = db.session.get(app_module.Appointment, appt_id)
        assert appt.adjustments == []

        db.session.delete(appt)
        db.session.commit()
