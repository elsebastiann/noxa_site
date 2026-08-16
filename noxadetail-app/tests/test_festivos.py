"""NOXA no atiende domingos ni festivos colombianos.

Los festivos no se pueden escribir en una lista fija: cinco dependen de la
Pascua y siete se corren al lunes siguiente por la Ley Emiliani. Estos tests
fijan el calendario real de varios años contra el cálculo, y verifican que el
bloqueo esté en `get_available_slots()` — el embudo por el que pasan el widget
del club, el panel y el bot de Mariana.
"""
from datetime import date, timedelta

import pytest

from conftest import app_module as A


# Calendario oficial, tomado de años ya publicados.
FESTIVOS_2025 = {
    "2025-01-01", "2025-01-06", "2025-03-24", "2025-04-17", "2025-04-18",
    "2025-05-01", "2025-06-02", "2025-06-23", "2025-06-30", "2025-07-20",
    "2025-08-07", "2025-08-18", "2025-10-13", "2025-11-03", "2025-11-17",
    "2025-12-08", "2025-12-25",
}
FESTIVOS_2026 = {
    "2026-01-01", "2026-01-12", "2026-03-23", "2026-04-02", "2026-04-03",
    "2026-05-01", "2026-05-18", "2026-06-08", "2026-06-15", "2026-06-29",
    "2026-07-20", "2026-08-07", "2026-08-17", "2026-10-12", "2026-11-02",
    "2026-11-16", "2026-12-08", "2026-12-25",
}


class TestCalendario:
    @pytest.mark.parametrize("anio,esperados", [(2025, FESTIVOS_2025), (2026, FESTIVOS_2026)])
    def test_calendario_completo_del_anio(self, anio, esperados):
        calculados = {d.isoformat() for d in A.festivos_colombia(anio)}
        assert calculados == esperados

    @pytest.mark.parametrize("anio,pascua", [
        (2024, "2024-03-31"), (2025, "2025-04-20"),
        (2026, "2026-04-05"), (2027, "2027-03-28"),
    ])
    def test_domingo_de_pascua(self, anio, pascua):
        assert A._domingo_de_pascua(anio).isoformat() == pascua

    def test_ley_emiliani_corre_al_lunes(self):
        # Reyes 2026 cae martes 6 de enero -> se corre al lunes 12.
        assert A.es_festivo(date(2026, 1, 6)) is None
        assert A.es_festivo(date(2026, 1, 12)) == "Reyes Magos"

    def test_festivos_de_fecha_fija_no_se_mueven(self):
        # 20 de julio y Navidad se celebran en su fecha, caiga el día que caiga.
        assert A.es_festivo(date(2025, 12, 25)) == "Navidad"
        assert A.es_festivo(date(2026, 12, 25)) == "Navidad"

    def test_jueves_y_viernes_santo_no_se_mueven(self):
        assert A.es_festivo(date(2026, 4, 2)) == "Jueves Santo"
        assert A.es_festivo(date(2026, 4, 3)) == "Viernes Santo"

    def test_cada_anio_tiene_al_menos_17_festivos(self):
        # Blinda contra un error de cálculo silencioso a futuro. Puede haber 17
        # en vez de 18 cuando dos festivos móviles coinciden en la misma fecha.
        for anio in range(2024, 2036):
            assert 17 <= len(A.festivos_colombia(anio)) <= 18, anio


class TestDiaHabil:
    def test_domingo_no_es_habil(self):
        assert not A.es_dia_habil(date(2026, 8, 16))   # domingo
        assert A.motivo_dia_cerrado(date(2026, 8, 16)) == "es domingo"

    def test_festivo_no_es_habil(self):
        # Lunes 17/08/2026 = Asunción de la Virgen.
        assert not A.es_dia_habil(date(2026, 8, 17))
        assert "Asunción" in A.motivo_dia_cerrado(date(2026, 8, 17))

    def test_sabado_si_es_habil(self):
        assert A.es_dia_habil(date(2026, 8, 22))
        assert A.motivo_dia_cerrado(date(2026, 8, 22)) is None

    def test_dia_normal_es_habil(self):
        assert A.es_dia_habil(date(2026, 8, 18))
        assert A.motivo_dia_cerrado(date(2026, 8, 18)) is None

    def test_acepta_datetime_ademas_de_date(self):
        from datetime import datetime
        assert not A.es_dia_habil(datetime(2026, 8, 17, 10, 30))


@pytest.fixture
def servicio_diagnostico():
    """La BD semilla no trae servicio de diagnóstico, así que se crea uno. Sin
    esto los tests de bloqueo se saltaban en silencio — justo los que importan."""
    with A.app.app_context():
        svc = A._diagnostic_service()
        creado = None
        if not svc:
            creado = A.Service(
                name="Diagnóstico", duration_minutes=30,
                is_active=True, is_diagnostic=True, occupies_single_day=False,
            )
            A.db.session.add(creado)
            A.db.session.commit()
            svc = creado
        yield svc.id, A._availability_vehicle_type_id()
        if creado:
            A.db.session.delete(creado)
            A.db.session.commit()


class TestBloqueoEnLaAgenda:
    """El bloqueo vive en get_available_slots(), no en cada llamador."""

    def test_festivo_no_devuelve_cupos(self, servicio_diagnostico):
        svc_id, vt_id = servicio_diagnostico
        with A.app.app_context():
            slots, _ = A.get_available_slots(date(2026, 8, 17), [svc_id], vt_id)
        assert slots == []

    def test_domingo_no_devuelve_cupos(self, servicio_diagnostico):
        svc_id, vt_id = servicio_diagnostico
        with A.app.app_context():
            slots, _ = A.get_available_slots(date(2026, 8, 16), [svc_id], vt_id)
        assert slots == []

    def test_dia_habil_si_devuelve_cupos(self, servicio_diagnostico):
        # Contraprueba: si un martes normal tampoco diera cupos, los tests de
        # arriba pasarían por la razón equivocada.
        svc_id, vt_id = servicio_diagnostico
        with A.app.app_context():
            slots, _ = A.get_available_slots(date(2026, 8, 18), [svc_id], vt_id)
        assert slots

    def test_get_available_days_omite_domingos_y_festivos(self, servicio_diagnostico):
        svc_id, vt_id = servicio_diagnostico
        with A.app.app_context():
            dias = A.get_available_days(date(2026, 8, 14), date(2026, 8, 22), [svc_id], vt_id)
        assert "2026-08-16" not in dias   # domingo
        assert "2026-08-17" not in dias   # festivo (Asunción)
        assert "2026-08-18" in dias       # martes normal

    def test_disponibilidad_del_bot_nunca_ofrece_dia_cerrado(self, servicio_diagnostico):
        with A.app.app_context():
            disponibilidad = A._diagnostic_availability(days=10)
        assert disponibilidad, "el bot no ofreció ningún día; el test no probaría nada"
        for d, _horas in disponibilidad:
            assert A.es_dia_habil(d), f"ofreció un día cerrado: {d}"


class TestBloqueoAlAgendarDesdeElBot:
    """Mariana revalida contra la agenda antes de crear la cita. Antes de esto,
    `book_diagnostic_from_bot` solo miraba la ventana de 15 días y los cupos, y
    get_available_slots devolvía horarios de 9 a 6 para cualquier fecha — así
    que una cita en domingo o festivo se creaba sin que nada la frenara."""

    def _datos(self, fecha):
        return {
            "nombre": "Prueba Festivos", "celular": "3001234567",
            "vehiculo": "Automovil", "placa": "XTS123",
            "fecha": fecha, "hora": "10:00",
        }

    @pytest.mark.parametrize("fecha,motivo", [
        ("2026-08-16", "domingo"),
        ("2026-08-17", "Asunción"),
    ])
    def test_no_agenda_en_dia_cerrado(self, servicio_diagnostico, fecha, motivo):
        with A.app.app_context():
            conv = A.Conversation(phone="+573009998877")
            A.db.session.add(conv)
            A.db.session.commit()
            try:
                ok, detalle, appt = A.book_diagnostic_from_bot(conv, self._datos(fecha))
            finally:
                A.db.session.delete(conv)
                A.db.session.commit()

        assert ok is False
        assert appt is None
        # El motivo tiene que ser explicable al cliente, no un "no hay cupo" seco.
        assert motivo.lower() in detalle.lower(), detalle


class TestPanelManual:
    """A diferencia de Mariana, un usuario del panel SÍ puede agendar en domingo
    o festivo — pero solo confirmándolo explícitamente. El aviso vive en el
    formulario; esto prueba el guardia del servidor, que es el que de verdad
    manda (el de pantalla se puede saltar apagando el JS o con un POST directo).
    """

    def _payload(self, fecha, **extra):
        with A.app.app_context():
            svc = A.Service.query.filter_by(is_active=True).first()
            vt = A.VehicleType.query.filter_by(is_active=True).first()
        datos = {
            "customer_name": "Cliente Festivo", "plate": "FST123", "phone": "3001234567",
            "date": fecha, "start_time": "10:00", "notes": "",
            "service_ids": str(svc.id), "vehicle_type_id": str(vt.id),
        }
        datos.update(extra)
        return datos

    def _citas_en(self, fecha):
        from datetime import datetime as dtm
        d = dtm.strptime(fecha, "%Y-%m-%d").date()
        return A.Appointment.query.filter(
            A.db.func.date(A.Appointment.start_datetime) == d.isoformat()
        ).count()

    @pytest.mark.parametrize("fecha", ["2026-08-16", "2026-08-17"])  # domingo, festivo
    def test_sin_confirmar_no_se_guarda(self, client, fecha):
        from conftest import make_user, login_as
        login_as(client, make_user("admin_festivos", role="admin"))

        antes = self._citas_en(fecha)
        resp = client.post("/appointments/new", data=self._payload(fecha), follow_redirects=True)

        assert resp.status_code == 200
        assert self._citas_en(fecha) == antes, "creó la cita sin confirmación"
        assert "no atiende" in resp.get_data(as_text=True).lower()

    @pytest.mark.parametrize("fecha", ["2026-08-16", "2026-08-17"])
    def test_confirmando_si_se_guarda(self, client, fecha):
        from conftest import make_user, login_as
        login_as(client, make_user("admin_festivos2", role="admin"))

        antes = self._citas_en(fecha)
        resp = client.post(
            "/appointments/new",
            data=self._payload(fecha, confirmar_dia_cerrado="1"),
            follow_redirects=True,
        )
        assert resp.status_code == 200
        assert self._citas_en(fecha) == antes + 1, "no guardó pese a la confirmación"

    def test_dia_habil_no_pide_confirmacion(self, client):
        from conftest import make_user, login_as
        login_as(client, make_user("admin_festivos3", role="admin"))

        fecha = "2026-08-18"  # martes normal
        antes = self._citas_en(fecha)
        client.post("/appointments/new", data=self._payload(fecha), follow_redirects=True)
        assert self._citas_en(fecha) == antes + 1


class TestApiDiaCerrado:
    def test_reporta_festivo_con_su_nombre(self, client):
        from conftest import make_user, login_as
        login_as(client, make_user("op_festivos", role="operario"))

        data = client.get("/api/dia-cerrado?fecha=2026-08-17").get_json()
        assert data["ok"] and data["closed"]
        assert "Asunción" in data["reason"]

    def test_reporta_domingo(self, client):
        from conftest import make_user, login_as
        login_as(client, make_user("op_festivos2", role="operario"))

        data = client.get("/api/dia-cerrado?fecha=2026-08-16").get_json()
        assert data["closed"] and data["reason"] == "es domingo"

    def test_dia_habil_no_esta_cerrado(self, client):
        from conftest import make_user, login_as
        login_as(client, make_user("op_festivos3", role="operario"))

        data = client.get("/api/dia-cerrado?fecha=2026-08-18").get_json()
        assert data["ok"] and not data["closed"]

    def test_fecha_invalida(self, client):
        from conftest import make_user, login_as
        login_as(client, make_user("op_festivos4", role="operario"))

        assert client.get("/api/dia-cerrado?fecha=nada").status_code == 400


class TestPromptDeMariana:
    def test_el_prompt_nombra_los_festivos_proximos(self):
        with A.app.app_context():
            bloque = A._format_festivos_for_prompt()
        assert "festivo" in bloque.lower()

    def test_los_festivos_listados_caen_en_la_ventana(self):
        with A.app.app_context():
            bloque = A._format_festivos_for_prompt()
        hoy = A.bogota_now().date()
        limite = hoy + timedelta(days=A.BOOKING_WINDOW_DAYS)
        for anio in {hoy.year, limite.year}:
            for d in A.festivos_colombia(anio):
                if hoy <= d <= limite:
                    assert d.isoformat() in bloque
                else:
                    assert d.isoformat() not in bloque
