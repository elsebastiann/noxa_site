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
from conftest import login_as, make_user


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


@pytest.fixture(autouse=True)
def _sin_citas_de_otros_tests():
    """Las citas de prueba caen todas en el mismo día, así que si una sobrevive
    al test que la creó se suma a los KPIs del siguiente y los descuadra."""
    yield
    with A.app.app_context():
        for appt in A.Appointment.query.filter(A.Appointment.plate.like("TER%")).all():
            A.db.session.delete(appt)   # cascade se lleva líneas y ajustes
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


class TestAnalitica:
    """El problema original: el tablero mostraba el polarizado completo como
    ingreso de Noxa."""

    def test_el_ingreso_del_periodo_descuenta_al_instalador(self, catalogo):
        appt = _cita(catalogo, "Polarizado Test", [
            {"service_name": "Polarizado Test", "installer_id": catalogo["instalador"],
             "installer_pct": 65, "material_por": A.MATERIAL_INSTALADOR},
        ])
        dia = appt.start_datetime.date()

        kpis = A._kpis_rentabilidad(dia, dia)

        assert kpis["facturado"] == 975_000       # lo que pagó el cliente
        assert kpis["tercerizacion"] == 633_750   # lo que se le debe al instalador
        assert kpis["ingresos"] == 341_250        # lo que de verdad ingresó

    def test_el_margen_se_calcula_sobre_el_ingreso_real(self, catalogo):
        """Si el margen saliera del facturado, un mes lleno de polarizados se
        vería rentabilísimo mientras la caja no crece."""
        appt = _cita(catalogo, "Polarizado Test", [
            {"service_name": "Polarizado Test", "installer_id": catalogo["instalador"],
             "installer_pct": 65, "material_por": A.MATERIAL_INSTALADOR},
        ])
        dia = appt.start_datetime.date()

        kpis = A._kpis_rentabilidad(dia, dia)

        assert kpis["margen"] == kpis["ingresos"] - kpis["gastos"]
        assert kpis["margen"] < 975_000


class TestLiquidacion:
    def test_agrupa_lo_que_se_le_debe_a_cada_instalador(self, catalogo):
        with A.app.app_context():
            otro = A.Installer(name="Segundo Instalador Test", default_share=65)
            A.db.session.add(otro)
            A.db.session.commit()
            otro_id = otro.id

        a1 = _cita(catalogo, "Polarizado Test", [
            {"service_name": "Polarizado Test", "installer_id": catalogo["instalador"],
             "installer_pct": 65, "material_por": A.MATERIAL_INSTALADOR},
        ])
        _cita(catalogo, "PPF a Medida Test", [
            {"service_name": "PPF a Medida Test", "installer_id": otro_id,
             "installer_pct": 65, "material_por": A.MATERIAL_INSTALADOR,
             "amount": 400_000, "description": "Capó"},
        ])
        dia = a1.start_datetime.date()

        liq = A._liquidacion_instaladores(dia, dia)

        por_nombre = {g["instalador"]: g for g in liq}
        assert por_nombre["Instalador Test"]["total"] == 633_750
        assert por_nombre["Segundo Instalador Test"]["total"] == 260_000
        # Ordenada por lo que más se debe: es el orden en que se paga.
        assert liq[0]["instalador"] == "Instalador Test"

        with A.app.app_context():
            A.Installer.query.filter_by(id=otro_id).delete()
            A.db.session.commit()

    def test_el_detalle_permite_revisar_trabajo_por_trabajo(self, catalogo):
        appt = _cita(catalogo, "PPF a Medida Test", [
            {"service_name": "PPF a Medida Test", "installer_id": catalogo["instalador"],
             "installer_pct": 35, "material_por": A.MATERIAL_NOXA,
             "amount": 300_000, "description": "Espejos"},
        ])
        dia = appt.start_datetime.date()

        trabajo = A._liquidacion_instaladores(dia, dia)[0]["trabajos"][0]

        assert trabajo["descripcion"] == "Espejos"
        assert trabajo["material_por"] == A.MATERIAL_NOXA
        assert trabajo["costo"] == 105_000


class TestPantallas:
    def test_liquidacion_lista_los_trabajos(self, catalogo, client):
        login_as(client, make_user("admin_liq", role="admin"))
        appt = _cita(catalogo, "PPF a Medida Test", [
            {"service_name": "PPF a Medida Test", "installer_id": catalogo["instalador"],
             "installer_pct": 65, "material_por": A.MATERIAL_INSTALADOR,
             "amount": 400_000, "description": "Capó y guardabarros"},
        ])
        dia = appt.start_datetime.date().isoformat()

        html = client.get(f"/liquidacion-instaladores?from={dia}&to={dia}").get_data(as_text=True)

        assert "Instalador Test" in html
        assert "Capó y guardabarros" in html
        assert "260.000" in html          # 65% de 400.000

    def test_la_liquidacion_no_es_para_cualquiera(self, catalogo, client):
        login_as(client, make_user("operario_liq", role="operario"))
        assert client.get("/liquidacion-instaladores").status_code == 302

    def test_pagina_de_instaladores(self, catalogo, client):
        login_as(client, make_user("admin_ins", role="admin"))
        html = client.get("/instaladores").get_data(as_text=True)
        assert "Instalador Test" in html

    def test_desactivar_no_borra(self, catalogo, client):
        """Borrarlo dejaría sin nombre la liquidación de las citas viejas."""
        login_as(client, make_user("admin_ins2", role="admin"))
        client.post(f"/instaladores/{catalogo['instalador']}/toggle")

        with A.app.app_context():
            ins = A.Installer.query.get(catalogo["instalador"])
            assert ins is not None
            assert ins.is_active is False
            ins.is_active = True
            A.db.session.commit()


class TestGuardadoDesdeElFormulario:
    def _form_base(self, catalogo, service_id, extra):
        manana = A.bogota_now().date() + dt.timedelta(days=1)
        data = {
            "customer_name": "Cliente Form", "plate": "TERFRM", "phone": "3001112233",
            "date": manana.isoformat(), "start_time": "09:00",
            "service_ids": [str(service_id)],
            "vehicle_type_id": str(catalogo["vt"]),
            "confirmar_dia_cerrado": "1",
        }
        data.update(extra)
        return data

    def test_guarda_el_reparto_al_crear_la_cita(self, catalogo, client):
        login_as(client, make_user("admin_form", role="admin"))
        sid = catalogo["polarizado"]
        client.post("/appointments/new", data=self._form_base(catalogo, sid, {
            f"terc_{sid}_installer": str(catalogo["instalador"]),
            f"terc_{sid}_material": "instalador",
            f"terc_{sid}_pct": "65",
        }), follow_redirects=True)

        with A.app.app_context():
            appt = A.Appointment.query.filter_by(plate="TERFRM").first()
            assert appt is not None
            m = A.appointment_money(appt)
            assert m["costo_tercerizacion"] == 633_750
            assert m["ingreso_noxa"] == 341_250

    def test_sin_porcentaje_valido_cae_al_del_catalogo(self, catalogo, client):
        """Un POST sin JS llegaría con el pct vacío. Sin este respaldo quedaría
        en 0 y el instalador no cobraría nada."""
        login_as(client, make_user("admin_form2", role="admin"))
        sid = catalogo["polarizado"]
        client.post("/appointments/new", data=self._form_base(catalogo, sid, {
            f"terc_{sid}_installer": str(catalogo["instalador"]),
            f"terc_{sid}_material": "noxa",
            f"terc_{sid}_pct": "",
        }), follow_redirects=True)

        with A.app.app_context():
            appt = A.Appointment.query.filter_by(plate="TERFRM").first()
            linea = appt.outsourcings[0]
            assert linea.installer_pct == 35   # material de Noxa => reparto volteado


class TestReclasificacionHistorica:
    """Los polarizados y PPF ya registrados cuentan el ingreso completo como de
    Noxa. Esta pasada les aplica el reparto."""

    def test_encuentra_las_citas_sin_reparto(self, catalogo):
        _cita(catalogo, "Polarizado Test")                  # vieja, sin reparto
        _cita(catalogo, "Lavado Propio Test")               # no se terceriza

        candidatas = A._citas_sin_reclasificar()

        servicios = [c["servicios"] for c in candidatas]
        assert "Polarizado Test" in servicios
        assert "Lavado Propio Test" not in servicios

    def test_no_reofrece_una_cita_ya_reclasificada(self, catalogo):
        """Aplicarla dos veces le duplicaría el costo al instalador."""
        _cita(catalogo, "Polarizado Test", [
            {"service_name": "Polarizado Test", "installer_id": catalogo["instalador"],
             "installer_pct": 65, "material_por": A.MATERIAL_INSTALADOR},
        ])
        assert A._citas_sin_reclasificar() == []

    def test_aplicar_baja_el_ingreso_al_real(self, catalogo, client):
        login_as(client, make_user("admin_rec", role="admin"))
        appt = _cita(catalogo, "Polarizado Test")
        dia = appt.start_datetime.date()

        assert A._kpis_rentabilidad(dia, dia)["ingresos"] == 975_000

        client.post("/tercerizacion/reclasificar", data={
            "aplicar": [str(appt.id)],
            f"installer_{appt.id}": str(catalogo["instalador"]),
            f"material_{appt.id}": "instalador",
            f"pct_{appt.id}": "65",
        }, follow_redirects=True)

        assert A._kpis_rentabilidad(dia, dia)["ingresos"] == 341_250

    def test_permite_marcar_los_de_material_de_noxa(self, catalogo, client):
        """El reparto no siempre fue el mismo: aplicar 65% a ciegas cambiaría
        un error por otro."""
        login_as(client, make_user("admin_rec2", role="admin"))
        appt = _cita(catalogo, "Polarizado Test")

        client.post("/tercerizacion/reclasificar", data={
            "aplicar": [str(appt.id)],
            f"installer_{appt.id}": str(catalogo["instalador"]),
            f"material_{appt.id}": "noxa",
            f"pct_{appt.id}": "35",
        }, follow_redirects=True)

        with A.app.app_context():
            linea = A.AppointmentOutsourcing.query.filter_by(appointment_id=appt.id).first()
            assert linea.installer_pct == 35
            assert linea.material_por == A.MATERIAL_NOXA
