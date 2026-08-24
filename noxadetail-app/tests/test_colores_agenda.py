"""Color del cajón de la cita, configurable por servicio.

Antes vivía en un dict fijo en el código: cambiar un color pedía un deploy y
todo servicio nuevo nacía sin color. Ahora sale del servicio, y el color de la
letra se elige solo por luminancia si no se define uno — que es lo que evita
volver al problema viejo de texto blanco sobre fondo amarillo.
"""
import pytest

from conftest import app_module as A
from conftest import login_as, make_user


@pytest.fixture
def admin(client):
    login_as(client, make_user("admin_colores", role="admin"))
    return client


@pytest.fixture
def servicio():
    with A.app.app_context():
        s = A.Service(name="Servicio Color", duration_minutes=60, is_active=True)
        A.db.session.add(s)
        A.db.session.commit()
        sid = s.id
    yield sid
    with A.app.app_context():
        s = A.Service.query.get(sid)
        if s:
            A.db.session.delete(s)
            A.db.session.commit()


class TestLetraLegible:
    """La regla que hace que un servicio nuevo nazca legible sin configurarlo."""

    @pytest.mark.parametrize("fondo,esperado", [
        ("#FFFFFF", "#111111"),   # blanco
        ("#FFF3B0", "#111111"),   # amarillo claro: con blanco encima no se leía
        ("#7B0000", "#FFFFFF"),   # rojo oscuro
        ("#111111", "#FFFFFF"),   # casi negro
        ("#A0C8FF", "#111111"),   # el azul por defecto
    ])
    def test_elige_el_que_contrasta(self, fondo, esperado):
        assert A.color_texto_legible(fondo) == esperado

    def test_usa_luminancia_y_no_el_promedio(self):
        """Un verde saturado promedia 'oscuro' pero se ve claro: con promedio
        simple saldría letra blanca sobre verde brillante."""
        assert A.color_texto_legible("#00FF00") == "#111111"

    def test_un_color_invalido_no_revienta(self):
        assert A.color_texto_legible("no-es-color") in ("#111111", "#FFFFFF")


class TestValidacionDeHex:
    @pytest.mark.parametrize("valor", ["#AABBCC", "#aabbcc", "  #123456  "])
    def test_acepta_hex_de_seis(self, valor):
        assert A.color_hex_valido(valor) == valor.strip().upper()

    @pytest.mark.parametrize("valor", ["", None, "rojo", "#FFF", "#GGGGGG",
                                       "red; background:url(x)", "#12345678"])
    def test_rechaza_lo_demas(self, valor):
        assert A.color_hex_valido(valor) is None


class TestValoresEfectivos:
    def test_sin_color_cae_al_defecto(self, servicio):
        with A.app.app_context():
            s = A.Service.query.get(servicio)
            assert s.color_fondo_efectivo == A.COLOR_CAJON_DEFECTO
            assert s.color_texto_efectivo == A.color_texto_legible(A.COLOR_CAJON_DEFECTO)

    def test_texto_en_null_se_calcula_del_fondo(self, servicio):
        with A.app.app_context():
            s = A.Service.query.get(servicio)
            s.color_fondo, s.color_texto = "#7B0000", None
            A.db.session.commit()
            assert s.color_texto_efectivo == "#FFFFFF"

    def test_texto_explicito_manda(self, servicio):
        with A.app.app_context():
            s = A.Service.query.get(servicio)
            s.color_fondo, s.color_texto = "#FFFFFF", "#FF0000"
            A.db.session.commit()
            assert s.color_texto_efectivo == "#FF0000"


class TestGuardarDesdeElPanel:
    def _guardar(self, client, sid, **datos):
        base = {"color_fondo": "#123456"}
        base.update(datos)
        return client.post(f"/services/{sid}/colors", data=base, follow_redirects=True)

    def test_guarda_fondo_y_letra(self, admin, servicio):
        self._guardar(admin, servicio, color_fondo="#123456", color_texto="#ABCDEF")
        with A.app.app_context():
            s = A.Service.query.get(servicio)
        assert s.color_fondo == "#123456"
        assert s.color_texto == "#ABCDEF"

    def test_letra_automatica_deja_el_texto_en_null(self, admin, servicio):
        """Guardar NULL y no un color fijo es lo que mantiene la letra legible
        si mañana alguien cambia el fondo."""
        self._guardar(admin, servicio, color_fondo="#000080",
                      color_texto="#ABCDEF", texto_auto="1")
        with A.app.app_context():
            s = A.Service.query.get(servicio)
        assert s.color_texto is None
        assert s.color_texto_efectivo == "#FFFFFF"

    def test_fondo_invalido_no_guarda_nada(self, admin, servicio):
        with A.app.app_context():
            antes = A.Service.query.get(servicio).color_fondo
        r = self._guardar(admin, servicio, color_fondo="javascript:alert(1)")
        assert r.status_code == 200
        with A.app.app_context():
            assert A.Service.query.get(servicio).color_fondo == antes

    def test_letra_invalida_cae_a_automatica(self, admin, servicio):
        self._guardar(admin, servicio, color_fondo="#FFFFFF", color_texto="rojo")
        with A.app.app_context():
            s = A.Service.query.get(servicio)
        assert s.color_texto is None


class TestAgenda:
    def test_el_evento_lleva_los_colores_del_servicio(self, admin, servicio):
        import datetime as dt
        with A.app.app_context():
            s = A.Service.query.get(servicio)
            s.color_fondo, s.color_texto = "#7B0000", None
            vt = A.VehicleType.query.filter_by(is_active=True).first()
            inicio = A.bogota_now() + dt.timedelta(days=1)
            appt = A.Appointment(
                customer_name="Cliente Color", plate="CLR123", phone="3001234567",
                services=s.name, start_datetime=inicio,
                end_datetime=inicio + dt.timedelta(minutes=60),
                vehicle_type_id=vt.id, status="scheduled",
            )
            A.db.session.add(appt)
            A.db.session.commit()
            appt_id = appt.id

        try:
            eventos = admin.get("/api/events").get_json()
            evento = next(e for e in eventos if e["id"] == appt_id)
            assert evento["backgroundColor"] == "#7B0000"
            assert evento["textColor"] == "#FFFFFF", "sobre rojo oscuro la letra tiene que ser blanca"
        finally:
            with A.app.app_context():
                A.db.session.delete(A.Appointment.query.get(appt_id))
                A.db.session.commit()

    def test_la_migracion_sembro_los_colores_historicos(self):
        """Al desplegar, la agenda tiene que verse igual que antes. Si el sembrado
        no corrió, todos los cajones se irían al azul por defecto de golpe."""
        with A.app.app_context():
            for nombre, color in A.COLORS.items():
                s = A.Service.query.filter(A.db.func.lower(A.Service.name) == nombre).first()
                if s:
                    assert s.color_fondo == color.upper(), f"{nombre} perdió su color histórico"
