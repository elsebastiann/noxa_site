"""Listado de servicios: inactivos ocultos y borrado con candados.

Borrar un servicio es irreversible y se lleva su lista de precios. Los tres
candados —quién, en qué estado, y si tiene citas futuras— son el grueso de lo
que hay que probar; la agrupación por categoría reusa `agrupar_servicios()`,
que ya usaba el formulario de citas.
"""
import datetime as dt

import pytest

from conftest import app_module as A
from conftest import login_as, make_user


@pytest.fixture
def servicio():
    with A.app.app_context():
        s = A.Service(name="Servicio Borrable", duration_minutes=60, is_active=True)
        A.db.session.add(s)
        A.db.session.commit()
        sid = s.id
    yield sid
    with A.app.app_context():
        A.ServicePrice.query.filter_by(service_id=sid).delete()
        s = A.Service.query.get(sid)
        if s:
            A.db.session.delete(s)
        A.db.session.commit()


def _desactivar(sid):
    with A.app.app_context():
        A.Service.query.get(sid).is_active = False
        A.db.session.commit()


def _borrar(client, sid):
    return client.post(f"/services/{sid}/delete", follow_redirects=True)


def _existe(sid):
    with A.app.app_context():
        return A.Service.query.get(sid) is not None


class TestOcultarInactivos:
    def test_por_defecto_no_se_listan_los_inactivos(self, client, servicio):
        login_as(client, make_user("sa", role="admin"))
        _desactivar(servicio)
        html = client.get("/services").get_data(as_text=True)
        assert "Servicio Borrable" not in html

    def test_con_el_filtro_si_aparecen(self, client, servicio):
        login_as(client, make_user("sa", role="admin"))
        _desactivar(servicio)
        html = client.get("/services?inactivos=1").get_data(as_text=True)
        assert "Servicio Borrable" in html

    def test_los_activos_siempre_se_ven(self, client, servicio):
        login_as(client, make_user("sa", role="admin"))
        html = client.get("/services").get_data(as_text=True)
        assert "Servicio Borrable" in html


class TestQuienPuedeBorrar:
    def test_sa_si_puede(self, client, servicio):
        login_as(client, make_user("sa", role="admin"))
        _desactivar(servicio)
        _borrar(client, servicio)
        assert not _existe(servicio)

    def test_diana_si_puede(self, client, servicio):
        login_as(client, make_user("diana", role="admin"))
        _desactivar(servicio)
        _borrar(client, servicio)
        assert not _existe(servicio)

    def test_otro_admin_no_puede(self, client, servicio):
        """Ser admin no alcanza: el catálogo lo responden dos personas."""
        login_as(client, make_user("otro_admin", role="admin"))
        _desactivar(servicio)
        r = _borrar(client, servicio)
        assert _existe(servicio)
        assert "Solo sa o Diana" in r.get_data(as_text=True)

    def test_el_boton_no_se_le_muestra_a_quien_no_puede(self, client, servicio):
        login_as(client, make_user("otro_admin2", role="admin"))
        _desactivar(servicio)
        html = client.get("/services?inactivos=1").get_data(as_text=True)
        assert f"/services/{servicio}/delete" not in html


class TestCandadosDeBorrado:
    def test_un_servicio_activo_no_se_borra(self, client, servicio):
        """Obliga a desactivarlo primero: es el paso que evita el clic accidental."""
        login_as(client, make_user("sa", role="admin"))
        r = _borrar(client, servicio)
        assert _existe(servicio)
        assert "Primero desactiva" in r.get_data(as_text=True)

    def test_con_citas_futuras_no_se_borra(self, client, servicio):
        login_as(client, make_user("sa", role="admin"))
        _desactivar(servicio)
        with A.app.app_context():
            vt = A.VehicleType.query.filter_by(is_active=True).first()
            inicio = A.bogota_now() + dt.timedelta(days=3)
            appt = A.Appointment(
                customer_name="Cliente", plate="FUT123", phone="3001234567",
                services="Servicio Borrable", start_datetime=inicio,
                end_datetime=inicio + dt.timedelta(minutes=60),
                vehicle_type_id=vt.id, status="scheduled",
            )
            A.db.session.add(appt)
            A.db.session.commit()
            appt_id = appt.id
        try:
            r = _borrar(client, servicio)
            assert _existe(servicio)
            assert "cita" in r.get_data(as_text=True).lower()
        finally:
            with A.app.app_context():
                A.db.session.delete(A.Appointment.query.get(appt_id))
                A.db.session.commit()

    def test_una_cita_pasada_no_lo_impide(self, client, servicio):
        """El historial guarda el nombre como texto y sobrevive al borrado."""
        login_as(client, make_user("sa", role="admin"))
        _desactivar(servicio)
        with A.app.app_context():
            vt = A.VehicleType.query.filter_by(is_active=True).first()
            inicio = A.bogota_now() - dt.timedelta(days=30)
            appt = A.Appointment(
                customer_name="Cliente Viejo", plate="OLD123", phone="3001234567",
                services="Servicio Borrable", start_datetime=inicio,
                end_datetime=inicio + dt.timedelta(minutes=60),
                vehicle_type_id=vt.id, status="completed",
            )
            A.db.session.add(appt)
            A.db.session.commit()
            appt_id = appt.id
        try:
            _borrar(client, servicio)
            assert not _existe(servicio)
            with A.app.app_context():
                vieja = A.Appointment.query.get(appt_id)
                assert vieja is not None
                assert vieja.services == "Servicio Borrable", "el historial perdió el nombre"
        finally:
            with A.app.app_context():
                a = A.Appointment.query.get(appt_id)
                if a:
                    A.db.session.delete(a)
                    A.db.session.commit()


class TestArrastreDePrecios:
    def test_borrar_se_lleva_los_precios(self, client, servicio):
        """Dejarlos huérfanos ensucia la lista de precios con filas que apuntan
        a un servicio que ya no existe."""
        login_as(client, make_user("sa", role="admin"))
        with A.app.app_context():
            vt = A.VehicleType.query.filter_by(is_active=True).first()
            A.db.session.add(A.ServicePrice(service_id=servicio, vehicle_type_id=vt.id,
                                            price=150000, duration_minutes=60,
                                            is_active=True))
            A.db.session.commit()
            assert A.ServicePrice.query.filter_by(service_id=servicio).count() == 1

        _desactivar(servicio)
        _borrar(client, servicio)

        with A.app.app_context():
            assert A.ServicePrice.query.filter_by(service_id=servicio).count() == 0


class TestAgrupacion:
    def test_la_pagina_agrupa_por_categoria(self, client, servicio):
        login_as(client, make_user("sa", role="admin"))
        html = client.get("/services").get_data(as_text=True)
        assert "svc-cat-titulo" in html

    def test_usa_la_misma_funcion_que_el_formulario_de_citas(self):
        """Si mañana se agrega una categoría, las dos pantallas la heredan."""
        with A.app.app_context():
            svcs = A.Service.query.filter_by(is_active=True).all()
            grupos = A.agrupar_servicios(svcs)
        assert sum(len(g[1]) for g in grupos) == len(svcs)
