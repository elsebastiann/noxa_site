"""Entrega programada, barra de avance y plazos de las evidencias.

Tres cosas que el cliente lee en su link y que tienen que ser verdad:
  - cuánto va el trabajo, contra la fecha que se le prometió;
  - hasta cuándo puede ver sus fotos (30 días después de la entrega);
  - y que pasado ese plazo el registro de verdad se cierra.
Internamente las fotos se guardan 90 días y después se borran solas.
"""
import base64
import io
import itertools
from datetime import timedelta
from unittest.mock import patch

import pytest

from conftest import app_module as A, login_as, make_user

_u = itertools.count(1)


def _jpeg() -> bytes:
    from PIL import Image
    buf = io.BytesIO()
    Image.new("RGB", (300, 200), (90, 30, 30)).save(buf, "JPEG")
    return buf.getvalue()


def _firma() -> str:
    from PIL import Image, ImageDraw
    img = Image.new("RGBA", (400, 180), (0, 0, 0, 0))
    ImageDraw.Draw(img).line([(20, 120), (120, 40), (220, 140), (360, 60)],
                             fill=(0, 0, 0, 255), width=4)
    buf = io.BytesIO()
    img.save(buf, "PNG")
    return "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()


@pytest.fixture
def admin(client):
    login_as(client, make_user(f"pl_adm{next(_u)}", role="admin"))
    return client


@pytest.fixture
def cita():
    """Cita que empezó hace 1 hora y cuyo fin calculado es en 9 horas."""
    with A.app.app_context():
        vt = A.VehicleType.query.filter_by(is_active=True).first()
        ahora = A.bogota_now().replace(microsecond=0)
        ap = A.Appointment(customer_name="Santiago Bernal", plate="KYK963", phone="3001234567",
                           services="PPF Full Front", start_datetime=ahora - timedelta(hours=1),
                           end_datetime=ahora + timedelta(hours=9),
                           vehicle_type_id=vt.id, status="scheduled")
        A.db.session.add(ap)
        A.db.session.commit()
        ap_id = ap.id
    yield ap_id
    with A.app.app_context():
        for f in A.VehicleReception.query.all():
            A.db.session.delete(f)
        ap = A.Appointment.query.get(ap_id)
        if ap:
            A.db.session.delete(ap)
        A.db.session.commit()


def _ficha_sellada(client, cita_id) -> int:
    r = client.get(f"/appointments/{cita_id}/recepcion")
    fid = int(r.headers["Location"].rstrip("/").split("/")[-1])
    client.post(f"/recepciones/{fid}/datos", data={
        "accion": "sellar", "plate": "KYK963", "firmado_por": "Santiago Bernal",
        "firma": _firma()})
    assert A.VehicleReception.query.get(fid).etapa == "proceso"
    return fid


def _entregar(client, fid):
    client.post(f"/recepciones/{fid}/entregar", data={
        "entregado_a": "Santiago Bernal", "firma": _firma()})
    assert A.VehicleReception.query.get(fid).etapa == "entregado"


def _mover_entrega(fid, dias_atras: int):
    """Simula que la entrega fue hace N días."""
    f = A.VehicleReception.query.get(fid)
    f.entregado_at = A.datetime.utcnow() - timedelta(days=dias_atras)
    A.db.session.commit()


# ── Entrega programada en la cita ────────────────────────────────────────────
class TestEntregaProgramada:
    def _form(self, **extra):
        vt = A.VehicleType.query.filter_by(is_active=True).first()
        svc = A.Service.query.filter_by(is_active=True).first()
        datos = {"customer_name": "Santiago Bernal", "plate": "KYK963", "phone": "3001234567",
                 "date": "2030-03-04", "start_time": "09:00",
                 "service_ids": [str(svc.id)], "vehicle_type_id": str(vt.id), "notes": ""}
        datos.update(extra)
        return datos

    def _ultima(self):
        return A.Appointment.query.filter_by(plate="KYK963").order_by(A.Appointment.id.desc()).first()

    def _limpiar(self):
        for a in A.Appointment.query.filter_by(plate="KYK963").all():
            A.db.session.delete(a)
        A.db.session.commit()

    def test_se_guarda_al_crear_la_cita(self, admin):
        try:
            admin.post("/appointments/new", data=self._form(entrega_programada="2030-03-06T17:00"))
            ap = self._ultima()
            assert ap.entrega_programada == A.datetime(2030, 3, 6, 17, 0)
            assert ap.entrega_estimada == A.datetime(2030, 3, 6, 17, 0)
        finally:
            self._limpiar()

    def test_es_opcional_y_sin_ella_manda_el_fin_de_la_cita(self, admin):
        """Sin fecha prometida, la entrega estimada es lo que el sistema calcula
        con la duración de los servicios, que es el fin de la cita."""
        try:
            admin.post("/appointments/new", data=self._form())
            ap = self._ultima()
            assert ap.entrega_programada is None
            assert ap.entrega_estimada == ap.end_datetime
        finally:
            self._limpiar()

    def test_una_entrega_antes_del_inicio_no_se_guarda(self, admin):
        """Es un error de dedo, no una promesa: guardarla haría arrancar la
        barra del cliente ya vencida."""
        try:
            admin.post("/appointments/new", data=self._form(entrega_programada="2030-03-01T10:00"))
            assert self._ultima().entrega_programada is None
        finally:
            self._limpiar()

    def test_se_puede_cambiar_al_editar(self, admin):
        try:
            admin.post("/appointments/new", data=self._form())
            ap = self._ultima()
            admin.post(f"/appointment/{ap.id}/edit", data=self._form(entrega_programada="2030-03-07T12:30"))
            assert self._ultima().entrega_programada == A.datetime(2030, 3, 7, 12, 30)
        finally:
            self._limpiar()

    def test_el_formulario_trae_el_campo(self, admin):
        assert 'name="entrega_programada"' in admin.get("/appointments/new").data.decode()


# ── Barra de avance ──────────────────────────────────────────────────────────
class TestAvance:
    def test_antes_de_sellar_no_hay_barra(self, admin, cita):
        r = admin.get(f"/appointments/{cita}/recepcion")
        fid = int(r.headers["Location"].rstrip("/").split("/")[-1])
        assert A.VehicleReception.query.get(fid).progreso is None

    def test_recien_recibido_va_cerca_de_cero(self, admin, cita):
        """Arranca al SELLAR la recepción, no a la hora de la cita: el carro de
        verdad empieza a trabajarse cuando se recibe. La cita de la fixture
        empezó hace una hora; si contara desde ahí, esto marcaría ~10%."""
        fid = _ficha_sellada(admin, cita)
        av = A.VehicleReception.query.get(fid).progreso
        assert av["pct"] <= 2, f"marcó {av['pct']}%: ¿cuenta desde la hora de la cita y no desde que se recibió?"
        assert not av["entregado"] and not av["atrasado"]

    def test_usa_la_entrega_programada_si_la_hay(self, admin, cita):
        fid = _ficha_sellada(admin, cita)
        f = A.VehicleReception.query.get(fid)
        prometida = A.bogota_now().replace(microsecond=0) + timedelta(days=3)
        f.appointment.entrega_programada = prometida
        A.db.session.commit()
        assert A.VehicleReception.query.get(fid).progreso["fin"] == prometida

    def test_sin_programada_usa_el_fin_de_la_cita(self, admin, cita):
        fid = _ficha_sellada(admin, cita)
        f = A.VehicleReception.query.get(fid)
        assert f.progreso["fin"] == f.appointment.end_datetime

    def test_a_mitad_de_camino_marca_la_mitad(self, admin, cita):
        """Es la prueba de la zona horaria. `recibido_at` se guarda en UTC y la
        cita en hora de Bogotá. Sin convertir, el inicio queda cinco horas en el
        FUTURO y la barra se clava en 0% hasta pasada la mitad del trabajo.
        Verificado: quitando la conversión, este test falla y el de "recién
        recibido" no — por eso la regla vive acá."""
        fid = _ficha_sellada(admin, cita)
        f = A.VehicleReception.query.get(fid)
        # Recibido hace 5 horas, entrega en 5 horas.
        f.recibido_at = A.datetime.utcnow() - timedelta(hours=5)
        f.appointment.entrega_programada = A.bogota_now() + timedelta(hours=5)
        A.db.session.commit()
        assert 48 <= A.VehicleReception.query.get(fid).progreso["pct"] <= 52

    def test_nunca_marca_100_antes_de_entregar(self, admin, cita):
        """Un 100% con el carro en el taller le dice al cliente que vaya por él."""
        fid = _ficha_sellada(admin, cita)
        f = A.VehicleReception.query.get(fid)
        f.appointment.entrega_programada = A.bogota_now() - timedelta(hours=2)
        A.db.session.commit()
        av = A.VehicleReception.query.get(fid).progreso
        assert av["pct"] == A.PROGRESO_TOPE_EN_PROCESO
        assert av["atrasado"]

    def test_atrasado_el_cliente_lee_ultimos_detalles_y_no_una_fecha_vencida(self, admin, cita, client):
        fid = _ficha_sellada(admin, cita)
        f = A.VehicleReception.query.get(fid)
        f.appointment.entrega_programada = A.bogota_now() - timedelta(hours=2)
        A.db.session.commit()
        cuerpo = client.get(f"/v/{f.token_cliente}").data.decode()
        assert "últimos detalles" in cuerpo
        assert "Entrega estimada" not in cuerpo

    def test_entregado_marca_100(self, admin, cita):
        fid = _ficha_sellada(admin, cita)
        _entregar(admin, fid)
        av = A.VehicleReception.query.get(fid).progreso
        assert av["pct"] == 100 and av["entregado"]

    def test_el_cliente_ve_la_barra_con_su_porcentaje(self, admin, cita, client):
        fid = _ficha_sellada(admin, cita)
        f = A.VehicleReception.query.get(fid)
        cuerpo = client.get(f"/v/{f.token_cliente}").data.decode()
        assert "Avance del trabajo" in cuerpo
        assert f'{f.progreso["pct"]}%' in cuerpo


# ── Mensaje de entrega y plazo del cliente ───────────────────────────────────
class TestPlazoDelCliente:
    def test_al_entregar_se_le_dice_el_plazo_y_la_fecha(self, admin, cita, client):
        fid = _ficha_sellada(admin, cita)
        _entregar(admin, fid)
        f = A.VehicleReception.query.get(fid)
        cuerpo = client.get(f"/v/{f.token_cliente}").data.decode()
        assert "30 días" in cuerpo
        assert f.link_cliente_vence.strftime("%d/%m/%Y") in cuerpo
        assert "reclamaciones" in cuerpo

    def test_vence_30_dias_despues_de_la_entrega(self, admin, cita):
        fid = _ficha_sellada(admin, cita)
        _entregar(admin, fid)
        f = A.VehicleReception.query.get(fid)
        dias = (f.link_cliente_vence - A.hora_bogota_naive(f.entregado_at)).days
        assert dias == A.RETENCION_CLIENTE_DIAS == 30

    def test_el_dia_29_todavia_abre(self, admin, cita, client):
        fid = _ficha_sellada(admin, cita)
        _entregar(admin, fid)
        _mover_entrega(fid, 29)
        assert client.get(f"/v/{A.VehicleReception.query.get(fid).token_cliente}").status_code == 200

    def test_pasados_30_dias_el_link_se_cierra_amablemente(self, admin, cita, client):
        fid = _ficha_sellada(admin, cita)
        _entregar(admin, fid)
        _mover_entrega(fid, 31)
        r = client.get(f"/v/{A.VehicleReception.query.get(fid).token_cliente}")
        assert r.status_code == 410
        cuerpo = r.data.decode()
        assert "ya cerró" in cuerpo and "Gracias" in cuerpo
        assert "KYK963" in cuerpo

    def test_y_una_url_de_foto_guardada_tampoco_se_salta_el_cierre(self, admin, cita, client):
        """El cliente pudo guardar el enlace directo a una foto. Si ese enlace
        siguiera abriendo, el cierre sería solo de fachada."""
        fid = _ficha_sellada(admin, cita)
        foto_id = admin.post(f"/recepciones/{fid}/fotos", data={
            "foto": (io.BytesIO(_jpeg()), "p.jpg"), "etapa": "proceso"},
            content_type="multipart/form-data").get_json()["id"]
        _entregar(admin, fid)
        token = A.VehicleReception.query.get(fid).token_cliente
        assert client.get(f"/rf/{token}/{foto_id}").status_code == 200
        _mover_entrega(fid, 31)
        assert client.get(f"/rf/{token}/{foto_id}").status_code == 404
        assert client.get(f"/rf/{token}/firma/entrega").status_code == 404

    def test_el_equipo_sigue_viendo_todo_despues_de_los_30(self, admin, cita):
        """Los 30 días son del cliente. Adentro la evidencia sigue: justo para
        la conversación que llega tarde."""
        fid = _ficha_sellada(admin, cita)
        foto_id = admin.post(f"/recepciones/{fid}/fotos", data={
            "foto": (io.BytesIO(_jpeg()), "p.jpg"), "etapa": "proceso"},
            content_type="multipart/form-data").get_json()["id"]
        _entregar(admin, fid)
        _mover_entrega(fid, 45)
        assert admin.get(f"/recepciones/fotos/{foto_id}").status_code == 200


# ── Borrado a los 90 días ────────────────────────────────────────────────────
class TestBorradoDeFotos:
    def _con_foto(self, admin, cita) -> int:
        fid = _ficha_sellada(admin, cita)
        admin.post(f"/recepciones/{fid}/fotos", data={
            "foto": (io.BytesIO(_jpeg()), "p.jpg"), "etapa": "proceso"},
            content_type="multipart/form-data")
        return fid

    def test_a_los_90_dias_se_borran_las_fotos(self, admin, cita):
        fid = self._con_foto(admin, cita)
        _entregar(admin, fid)
        _mover_entrega(fid, 91)
        keys = [p.key for p in A.VehicleReception.query.get(fid).fotos]
        with patch.object(A, "_almacen_borrar") as borrar:
            assert A._depurar_fotos_vencidas() == 1
        borradas = [c.args[0] for c in borrar.call_args_list]
        assert set(keys) <= set(borradas), "no se borró el archivo del almacén"
        f = A.VehicleReception.query.get(fid)
        assert f.fotos == [] and f.fotos_depuradas_at

    def test_la_ficha_con_sus_firmas_y_novedades_se_queda(self, admin, cita):
        """Solo se van las fotos, que son lo que pesa. Lo que se firmó sigue."""
        fid = self._con_foto(admin, cita)
        _entregar(admin, fid)
        _mover_entrega(fid, 91)
        A._depurar_fotos_vencidas()
        f = A.VehicleReception.query.get(fid)
        assert f is not None
        assert f.firma_recepcion and f.firma_entrega
        assert f.plate == "KYK963"

    def test_antes_de_los_90_no_se_toca(self, admin, cita):
        fid = self._con_foto(admin, cita)
        _entregar(admin, fid)
        _mover_entrega(fid, 89)
        assert A._depurar_fotos_vencidas() == 0
        assert len(A.VehicleReception.query.get(fid).fotos) == 1

    def test_un_carro_sin_entregar_nunca_se_depura(self, admin, cita):
        """Un carro que lleva meses en el taller es justo el que más necesita
        sus fotos."""
        fid = self._con_foto(admin, cita)
        f = A.VehicleReception.query.get(fid)
        f.recibido_at = A.datetime.utcnow() - timedelta(days=200)
        A.db.session.commit()
        assert A._depurar_fotos_vencidas() == 0
        assert len(A.VehicleReception.query.get(fid).fotos) == 1

    def test_no_se_depura_dos_veces(self, admin, cita):
        fid = self._con_foto(admin, cita)
        _entregar(admin, fid)
        _mover_entrega(fid, 91)
        A._depurar_fotos_vencidas()
        assert A._depurar_fotos_vencidas() == 0

    def test_el_trabajo_esta_programado(self):
        assert A._scheduler.get_job("depurar_fotos_recepciones") is not None


# ── Orden de la página del cliente ───────────────────────────────────────────
class TestOrdenDeLaPagina:
    def test_recepcion_firma_novedades_avance_entrega_firma(self, admin, cita, client):
        fid = _ficha_sellada(admin, cita)
        _entregar(admin, fid)
        cuerpo = client.get(f"/v/{A.VehicleReception.query.get(fid).token_cliente}").data.decode()
        orden = ["<h2>Recepción</h2>", "<h2>Firma de recepción</h2>", "Novedades que ya traía",
                 "Avance del trabajo <span", "<h2>Entrega</h2>", "<h2>Firma de entrega</h2>"]
        posiciones = [cuerpo.find(t) for t in orden]
        assert all(p >= 0 for p in posiciones), dict(zip(orden, posiciones))
        assert posiciones == sorted(posiciones), dict(zip(orden, posiciones))
