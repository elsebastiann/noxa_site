"""Registrar un parqueadero crea una venta SIN cita asociada.

Ese es el punto: `service_sales.appointment_id` tiene que aceptar NULL. La
tabla se creó cuando toda venta venía de una cita; el modelo se relajó después
a nullable=True, pero `db.create_all()` no altera tablas existentes, así que la
restricción vieja sobrevivió y cada registro de parqueadero moría con un 500
('NOT NULL constraint failed: service_sales.appointment_id') sin ninguna pista
en pantalla.
"""
import pytest
from sqlalchemy import inspect

from conftest import app_module as A
from conftest import login_as, make_user


@pytest.fixture
def admin(client):
    login_as(client, make_user("admin_parking", role="admin"))
    return client


@pytest.fixture(autouse=True)
def _limpiar():
    yield
    with A.app.app_context():
        A.db.session.execute(A.db.text("DELETE FROM parkings"))
        A.db.session.execute(A.db.text("DELETE FROM service_sales WHERE services = 'Parqueadero'"))
        A.db.session.commit()


class TestEsquema:
    def test_appointment_id_acepta_null_en_la_bd(self):
        """El modelo y la tabla real tienen que coincidir. Sin esto el 500 vuelve."""
        with A.app.app_context():
            cols = inspect(A.db.engine).get_columns("service_sales")
        col = next(c for c in cols if c["name"] == "appointment_id")
        assert col["nullable"], (
            "la tabla real sigue exigiendo appointment_id; "
            "el registro de parqueadero va a fallar con un 500"
        )

    def test_el_modelo_declara_lo_mismo(self):
        assert A.ServiceSale.__table__.c.appointment_id.nullable

    def test_la_migracion_es_idempotente(self):
        """Corre en cada arranque: repetirla no puede perder datos ni fallar."""
        with A.app.app_context():
            antes = A.db.session.execute(A.db.text("SELECT COUNT(*) FROM service_sales")).scalar()
            A._reparar_service_sales_appointment_id()
            A._reparar_service_sales_appointment_id()
            despues = A.db.session.execute(A.db.text("SELECT COUNT(*) FROM service_sales")).scalar()
        assert antes == despues

    def test_no_deja_las_foraneas_activadas(self):
        """El efecto secundario más peligroso de la migración: reconstruir la
        tabla exige foreign_keys=OFF, y la conexión sale del pool y se reutiliza.
        Dejarla en ON activaba la verificación para el resto de la app —que se
        escribió con el default de SQLite, OFF, y tiene flujos que no la
        cumplen— y reventaba nómina con 'FOREIGN KEY constraint failed'."""
        with A.app.app_context():
            antes = A.db.session.execute(A.db.text("PRAGMA foreign_keys")).scalar()
            A._reparar_service_sales_appointment_id()
            despues = A.db.session.execute(A.db.text("PRAGMA foreign_keys")).scalar()
        assert antes == despues, "la migración cambió foreign_keys para el resto de la app"

    def test_no_queda_la_tabla_temporal(self):
        with A.app.app_context():
            sobra = A.db.session.execute(A.db.text(
                "SELECT COUNT(*) FROM sqlite_master WHERE name='service_sales_rebuild'"
            )).scalar()
        assert sobra == 0


class TestRegistro:
    def _registrar(self, client, **extra):
        datos = {"customer_name": "Cliente Parqueo", "plate": "abc 123",
                 "parking_date": "2026-08-18"}
        datos.update(extra)
        return client.post("/parking/new", data=datos)

    def test_registrar_no_revienta(self, admin):
        r = self._registrar(admin)
        assert r.status_code == 302, f"esperaba redirección, llegó {r.status_code}"

    def test_crea_el_parqueadero_con_la_placa_normalizada(self, admin):
        self._registrar(admin)
        with A.app.app_context():
            filas = A.db.session.execute(A.db.text(
                "SELECT plate, customer_name, amount FROM parkings")).fetchall()
        assert len(filas) == 1
        assert filas[0][0] == "ABC123"      # normalizada, sin espacio
        assert filas[0][2] == A.PARKING_AMOUNT

    def test_crea_la_venta_sin_cita(self, admin):
        self._registrar(admin)
        with A.app.app_context():
            venta = A.db.session.execute(A.db.text(
                "SELECT appointment_id, services, final_amount, status "
                "FROM service_sales WHERE services='Parqueadero'")).fetchone()
        assert venta is not None, "no se registró la venta del parqueadero"
        assert venta[0] is None, "la venta del parqueadero no debe apuntar a ninguna cita"
        assert venta[2] == A.PARKING_AMOUNT
        assert venta[3] == "completed"

    def test_sin_placa_no_crea_nada(self, admin):
        r = self._registrar(admin, plate="")
        assert r.status_code == 302
        with A.app.app_context():
            assert A.db.session.execute(A.db.text("SELECT COUNT(*) FROM parkings")).scalar() == 0
            assert A.db.session.execute(A.db.text(
                "SELECT COUNT(*) FROM service_sales WHERE services='Parqueadero'")).scalar() == 0

    def test_fecha_invalida_no_crea_nada(self, admin):
        r = self._registrar(admin, parking_date="no-es-fecha")
        assert r.status_code == 302
        with A.app.app_context():
            assert A.db.session.execute(A.db.text("SELECT COUNT(*) FROM parkings")).scalar() == 0
