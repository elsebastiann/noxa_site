"""Planes de mantenimiento de cerámico: precio, saldo y plata.

Son bolsas prepagadas: el cliente paga todo al comprar y va gastando lavadas y
mantenimientos. Lo que se prueba acá es lo que duele si sale mal — que el precio
coincida con lo que dice el material comercial, que el saldo no se descuadre al
editar citas, y que la plata no se cuente dos veces.
"""
import itertools
from datetime import date, timedelta

import app as A

_placas = itertools.count(1)


def _placa():
    return f"TST{next(_placas):03d}"


def _tipo_vehiculo(nombre):
    vt = A.VehicleType.query.filter_by(name=nombre).first()
    if not vt:
        vt = A.VehicleType(name=nombre, is_active=True)
        A.db.session.add(vt)
        A.db.session.commit()
    return vt


def _servicio_con_precio(nombre, vt, precio):
    """Servicio activo con precio cargado para ese tipo de vehículo."""
    svc = A.Service.query.filter(A.db.func.lower(A.Service.name) == nombre.lower()).first()
    if not svc:
        svc = A.Service(name=nombre, is_active=True, duration_minutes=60)
        A.db.session.add(svc)
        A.db.session.flush()
    svc.is_active = True
    sp = A.ServicePrice.query.filter_by(service_id=svc.id, vehicle_type_id=vt.id).first()
    if not sp:
        sp = A.ServicePrice(service_id=svc.id, vehicle_type_id=vt.id, price=precio,
                            duration_minutes=60, is_active=True)
        A.db.session.add(sp)
    else:
        sp.price = precio
        sp.is_active = True
    A.db.session.commit()
    return svc


def _plan(nombre="Plan Anual", months=12, pct=25, wash=8, maint=4):
    p = A.MaintenancePlan.query.filter_by(name=nombre).first()
    if not p:
        p = A.MaintenancePlan(name=nombre, months=months, discount_pct=pct,
                              wash_count=wash, maintenance_count=maint, is_active=True)
        A.db.session.add(p)
        A.db.session.commit()
    return p


def _vendido(plan, *, wash=None, maint=None, expira_en_dias=365, plate=None, activo=True):
    cp = A.ClientPlan(
        plan_id=plan.id, plate=plate or _placa(), customer_name="Cliente Test",
        sold_on=A.bogota_now().date(),
        expires_on=A.bogota_now().date() + timedelta(days=expira_en_dias),
        price_paid=1_000_000,
        wash_remaining=plan.wash_count if wash is None else wash,
        maintenance_remaining=plan.maintenance_count if maint is None else maint,
        is_active=activo,
    )
    A.db.session.add(cp)
    A.db.session.commit()
    return cp


class TestPrecioDelPlan:
    """Contra la tabla de precios real del negocio."""

    def test_plan_anual_camioneta_da_el_precio_del_material_comercial(self, client):
        vt = _tipo_vehiculo("Camioneta")
        _servicio_con_precio(A.PLAN_WASH_SERVICE_NAME, vt, 110_000)
        _servicio_con_precio(A.PLAN_MAINT_SERVICE_NAME, vt, 220_000)

        # (8 × 110.000 + 4 × 220.000) × 0,75 = 1.320.000, ahorro 440.000
        assert A.precio_sugerido_plan(_plan(), vt.id) == 1_320_000

    def test_plan_trimestral_automovil(self, client):
        vt = _tipo_vehiculo("Automovil")
        _servicio_con_precio(A.PLAN_WASH_SERVICE_NAME, vt, 70_000)
        _servicio_con_precio(A.PLAN_MAINT_SERVICE_NAME, vt, 180_000)

        plan = _plan("Plan Trimestral", months=3, pct=15, wash=2, maint=1)
        # (2 × 70.000 + 1 × 180.000) × 0,85 = 272.000
        assert A.precio_sugerido_plan(plan, vt.id) == 272_000

    def test_sin_precio_cargado_devuelve_none_en_vez_de_cobrar_de_menos(self, client):
        """calculate_real_price ignora los servicios sin precio y devolvería un
        total incompleto — vender a ese precio sería perder plata en silencio."""
        vt = _tipo_vehiculo("Moto")
        _servicio_con_precio(A.PLAN_WASH_SERVICE_NAME, vt, 40_000)
        # El de mantenimiento existe pero sin precio para Moto.
        maint = A.Service.query.filter(
            A.db.func.lower(A.Service.name) == A.PLAN_MAINT_SERVICE_NAME.lower()).first()
        if maint:
            A.ServicePrice.query.filter_by(service_id=maint.id, vehicle_type_id=vt.id).delete()
            A.db.session.commit()

        assert A.precio_sugerido_plan(_plan(), vt.id) is None

    def test_sin_tipo_de_vehiculo_no_calcula(self, client):
        assert A.precio_sugerido_plan(_plan(), None) is None


class TestSaldo:
    def test_consumir_baja_el_cupo_correcto(self, client):
        cp = _vendido(_plan())
        cp.consumir_cupo("wash")
        assert (cp.wash_remaining, cp.maintenance_remaining) == (7, 4)
        cp.consumir_cupo("maintenance")
        assert (cp.wash_remaining, cp.maintenance_remaining) == (7, 3)

    def test_devolver_no_supera_lo_que_incluye_el_plan(self, client):
        """Guardar la misma cita muchas veces no puede regalar servicios."""
        cp = _vendido(_plan())
        for _ in range(5):
            cp.devolver_cupo("wash")
        assert cp.wash_remaining == cp.plan.wash_count

    def test_sin_cupos_no_se_puede_consumir(self, client):
        cp = _vendido(_plan(), wash=0)
        assert cp.puede_consumir("wash") is False
        assert cp.puede_consumir("maintenance") is True

    def test_plan_vencido_no_se_puede_usar_aunque_le_queden_cupos(self, client):
        cp = _vendido(_plan(), expira_en_dias=-1)
        assert cp.vencido is True
        assert cp.vigente is False
        assert cp.puede_consumir("wash") is False

    def test_plan_desactivado_no_se_puede_usar(self, client):
        cp = _vendido(_plan(), activo=False)
        assert cp.puede_consumir("wash") is False


class TestPlanesDisponiblesParaPlaca:
    def test_solo_devuelve_los_usables(self, client):
        plan = _plan()
        placa = _placa()
        _vendido(plan, plate=placa)
        disponibles = A.planes_vigentes_para_placa(placa)
        assert len(disponibles) == 1

    def test_no_devuelve_agotados_ni_vencidos(self, client):
        plan = _plan()
        agotado = _placa()
        _vendido(plan, plate=agotado, wash=0, maint=0)
        assert A.planes_vigentes_para_placa(agotado) == []

        vencido = _placa()
        _vendido(plan, plate=vencido, expira_en_dias=-5)
        assert A.planes_vigentes_para_placa(vencido) == []

    def test_no_mezcla_placas(self, client):
        plan = _plan()
        mia = _placa()
        _vendido(plan, plate=mia)
        assert A.planes_vigentes_para_placa(_placa()) == []

    def test_normaliza_la_placa_al_buscar(self, client):
        """Que el usuario escriba 'abc 123' no puede esconderle su plan."""
        plan = _plan()
        cp = _vendido(plan, plate=A.normalize_plate("XYZ789"))
        assert A.planes_vigentes_para_placa("xyz 789")[0].id == cp.id


class TestCitaCubiertaPorPlan:
    def _cita(self, plate, vt, servicios, plan=None, kind=None):
        appt = A.Appointment(
            customer_name="Cliente Test", plate=plate, services=servicios,
            start_datetime=A.datetime(2026, 8, 20, 10, 0),
            end_datetime=A.datetime(2026, 8, 20, 11, 0),
            vehicle_type_id=vt.id, status="scheduled",
            client_plan_id=plan.id if plan else None,
            plan_service_kind=kind,
        )
        A.db.session.add(appt)
        A.db.session.commit()
        return appt

    def test_cita_con_plan_vale_cero(self, client):
        """La plata entró el día que se vendió el plan; cobrarla otra vez sería
        contar dos veces la misma venta."""
        vt = _tipo_vehiculo("Camioneta")
        _servicio_con_precio(A.PLAN_WASH_SERVICE_NAME, vt, 110_000)
        cp = _vendido(_plan())

        appt = self._cita(cp.plate, vt, A.PLAN_WASH_SERVICE_NAME, plan=cp, kind="wash")
        assert A.appointment_money(appt)["total"] == 0

    def test_la_misma_cita_sin_plan_si_cobra(self, client):
        vt = _tipo_vehiculo("Camioneta")
        _servicio_con_precio(A.PLAN_WASH_SERVICE_NAME, vt, 110_000)

        appt = self._cita(_placa(), vt, A.PLAN_WASH_SERVICE_NAME)
        assert A.appointment_money(appt)["total"] == 110_000

    def test_liberar_devuelve_el_cupo_y_desvincula(self, client):
        vt = _tipo_vehiculo("Camioneta")
        cp = _vendido(_plan(), wash=3)
        appt = self._cita(cp.plate, vt, "X", plan=cp, kind="wash")

        A.liberar_plan_de_cita(appt)
        assert cp.wash_remaining == 4
        assert appt.client_plan_id is None
        assert appt.plan_service_kind is None

    def test_liberar_una_cita_sin_plan_no_hace_nada(self, client):
        vt = _tipo_vehiculo("Camioneta")
        appt = self._cita(_placa(), vt, "X")
        A.liberar_plan_de_cita(appt)  # no debe reventar
        assert appt.client_plan_id is None


class TestPlanesEnElPromptDeMariana:
    """Lo que Mariana recibe en cada turno para poder hablar de planes.

    Se calcula contra la tabla de precios en vez de escribirse en el prompt,
    porque un catálogo escrito a mano se desactualiza en silencio apenas alguien
    cambia un precio en el panel — el mismo error que ya se corrigió con los
    servicios sueltos.
    """

    def _precios_cargados(self):
        for nombre, (w, m) in {
            "Automovil": (70_000, 180_000), "SUV": (90_000, 200_000),
            "Camioneta": (110_000, 220_000), "Moto": (40_000, 110_000),
        }.items():
            vt = _tipo_vehiculo(nombre)
            _servicio_con_precio(A.PLAN_WASH_SERVICE_NAME, vt, w)
            _servicio_con_precio(A.PLAN_MAINT_SERVICE_NAME, vt, m)

    def test_incluye_los_planes_con_su_precio_por_vehiculo(self, client):
        self._precios_cargados()
        _plan()  # Plan Anual
        bloque = A._format_planes_for_prompt()

        assert "Plan Anual" in bloque
        # El precio que ve Mariana tiene que ser el mismo del material comercial.
        assert "$1.320.000" in bloque, bloque

    def test_le_dice_que_no_cierre_la_venta(self, client):
        """El cobro y el registro los hace una persona; si Mariana cerrara sola,
        quedaría un plan vendido sin plata cobrada ni placa asociada."""
        self._precios_cargados()
        _plan()
        bloque = A._format_planes_for_prompt()
        assert "NO CIERRAS LA VENTA" in bloque
        assert "escala" in bloque.lower()

    def test_singular_bien_escrito(self, client):
        """El modelo copia el fraseo del bloque: un '1 mantenimientos' sale tal
        cual en el chat."""
        self._precios_cargados()
        _plan("Plan Trimestral", months=3, pct=15, wash=2, maint=1)
        bloque = A._format_planes_for_prompt()
        assert "1 mantenimientos" not in bloque, bloque
        assert "1 mantenimiento" in bloque

    def test_sin_planes_activos_no_dice_nada(self, client, monkeypatch):
        """Sin planes vendibles el bloque se omite: mencionar algo que no se
        puede vender es peor que no mencionarlo."""
        class _Vacio:
            def filter_by(self, **kw): return self
            def order_by(self, *a): return self
            def all(self): return []
        monkeypatch.setattr(A.MaintenancePlan, "query", _Vacio())
        assert A._format_planes_for_prompt() == ""
