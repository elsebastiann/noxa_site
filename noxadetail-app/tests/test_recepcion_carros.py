"""Ficha de recepción, proceso y entrega de un carro.

Lo que sostiene todo el módulo es una sola regla: una vez que el cliente firma,
la recepción NO se puede modificar por ningún camino. Es lo que responde "ese
rayón ya estaba" el día que alguien diga lo contrario. Por eso buena parte de
estos tests intentan romperla desde cada ruta que escribe.
"""
import base64
import io
import itertools

import pytest

from conftest import app_module as A, login_as, make_user

_u = itertools.count(1)


# ── Utilidades ───────────────────────────────────────────────────────────────
def _jpeg(ancho=800, alto=600, color=(180, 40, 40)) -> bytes:
    from PIL import Image
    buf = io.BytesIO()
    Image.new("RGB", (ancho, alto), color).save(buf, "JPEG")
    return buf.getvalue()


def _firma(trazo=True, otra=False) -> str:
    """Una firma como la manda el lienzo: PNG transparente con tinta.

    `otra` dibuja un trazo distinto: sin eso, un test que compara "la firma de
    antes" con "la de después" pasaría aunque se hubiera reemplazado, porque
    las dos serían idénticas byte a byte."""
    from PIL import Image, ImageDraw
    img = Image.new("RGBA", (400, 180), (0, 0, 0, 0))
    if trazo:
        puntos = ([(30, 40), (200, 150), (370, 30)] if otra
                  else [(20, 120), (120, 40), (220, 140), (360, 60)])
        ImageDraw.Draw(img).line(puntos, fill=(0, 0, 0, 255), width=4)
    buf = io.BytesIO()
    img.save(buf, "PNG")
    return "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()


@pytest.fixture
def cita():
    with A.app.app_context():
        vt = A.VehicleType.query.filter_by(is_active=True).first()
        inicio = A.bogota_now().replace(microsecond=0)
        ap = A.Appointment(customer_name="Tatiana Pinzón", plate="nir849",
                           phone="3105528361", services="Wash Shine",
                           start_datetime=inicio,
                           end_datetime=inicio + A.timedelta(hours=2),
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


@pytest.fixture
def admin(client):
    login_as(client, make_user(f"rc_adm{next(_u)}", role="admin"))
    return client


def _abrir(client, cita_id) -> int:
    r = client.get(f"/appointments/{cita_id}/recepcion")
    assert r.status_code == 302
    return int(r.headers["Location"].rstrip("/").split("/")[-1])


def _ficha(fid):
    return A.VehicleReception.query.get(fid)


def _subir(client, fid, etapa="recepcion", **extra):
    datos = {"foto": (io.BytesIO(_jpeg()), "foto.jpg"), "etapa": etapa}
    datos.update(extra)
    return client.post(f"/recepciones/{fid}/fotos", data=datos,
                       content_type="multipart/form-data")


def _sellar(client, fid, firma=None):
    return client.post(f"/recepciones/{fid}/datos", data={
        "accion": "sellar", "plate": "NIR849", "customer_name": "Tatiana Pinzón",
        "firmado_por": "Tatiana Pinzón", "firma": firma if firma is not None else _firma(),
        "km_entrada": "45.000", "gasolina": "1/2",
    })


# ── Se trae lo que la cita ya sabe ───────────────────────────────────────────
class TestSeAbreDesdeLaCita:
    def test_trae_los_datos_de_la_cita(self, admin, cita):
        f = _ficha(_abrir(admin, cita))
        assert f.customer_name == "Tatiana Pinzón"
        assert f.phone == "3105528361"
        assert f.services == "Wash Shine"
        assert f.appointment_id == cita

    def test_la_placa_queda_en_mayusculas(self, admin, cita):
        """La placa se busca después para traer los datos del carro; con
        mayúsculas y minúsculas mezcladas, la misma placa serían dos carros."""
        assert _ficha(_abrir(admin, cita)).plate == "NIR849"

    def test_abrirla_dos_veces_no_crea_dos_fichas(self, admin, cita):
        """Del cajón se entra varias veces: la segunda no puede empezar de cero
        y dejar la primera huérfana con sus fotos."""
        assert _abrir(admin, cita) == _abrir(admin, cita)
        assert A.VehicleReception.query.filter_by(appointment_id=cita).count() == 1

    def test_un_carro_que_ya_vino_trae_marca_modelo_y_color(self, admin, cita):
        fid = _abrir(admin, cita)
        f = _ficha(fid)
        f.marca, f.modelo, f.color, f.anio = "Mazda", "CX-5", "Rojo", 2021
        A.db.session.commit()
        with A.app.app_context():
            vt = A.VehicleType.query.filter_by(is_active=True).first()
            inicio = A.bogota_now().replace(microsecond=0)
            otra = A.Appointment(customer_name="Tatiana", plate="NIR849", services="Wash",
                                 start_datetime=inicio, end_datetime=inicio + A.timedelta(hours=1),
                                 vehicle_type_id=vt.id, status="scheduled")
            A.db.session.add(otra)
            A.db.session.commit()
            otra_id = otra.id
        try:
            nueva = _ficha(_abrir(admin, otra_id))
            assert (nueva.marca, nueva.modelo, nueva.color, nueva.anio) == ("Mazda", "CX-5", "Rojo", 2021)
            assert nueva.id != fid
        finally:
            A.db.session.delete(A.VehicleReception.query.filter_by(appointment_id=otra_id).first())
            A.db.session.delete(A.Appointment.query.get(otra_id))
            A.db.session.commit()

    def test_los_dos_links_son_distintos(self, admin, cita):
        """Si fueran el mismo, mandarle al cliente su link sería darle permiso de
        subirle fotos a su propia ficha."""
        f = _ficha(_abrir(admin, cita))
        assert f.token_equipo != f.token_cliente
        assert len(f.token_equipo) >= 30 and len(f.token_cliente) >= 30


# ── Fotos ────────────────────────────────────────────────────────────────────
class TestFotos:
    def test_sube_una_foto(self, admin, cita):
        fid = _abrir(admin, cita)
        r = _subir(admin, fid)
        assert r.status_code == 200 and r.get_json()["ok"]
        assert len(_ficha(fid).fotos) == 1

    def test_se_puede_ver_y_su_miniatura_tambien(self, admin, cita):
        fid = _abrir(admin, cita)
        j = _subir(admin, fid).get_json()
        for url in (j["url"], j["mini"]):
            r = admin.get(url)
            assert r.status_code == 200 and r.data[:2] == b"\xff\xd8"

    def test_la_foto_se_achica(self, admin, cita):
        """Una foto de celular pesa megas; guardarla tal cual llena el bucket y
        vuelve lentas las grillas."""
        from PIL import Image
        fid = _abrir(admin, cita)
        datos = {"foto": (io.BytesIO(_jpeg(4000, 3000)), "grande.jpg"), "etapa": "recepcion"}
        j = admin.post(f"/recepciones/{fid}/fotos", data=datos,
                       content_type="multipart/form-data").get_json()
        img = Image.open(io.BytesIO(admin.get(j["url"]).data))
        assert max(img.size) <= A.FOTO_LADO_MAX

    def test_se_le_quita_el_gps(self, admin, cita):
        """Una foto de celular trae en el EXIF dónde se tomó. Estas fotos
        terminan en un link que se le manda a un cliente."""
        from PIL import Image
        buf = io.BytesIO()
        exif = Image.Exif()
        exif[0x010F] = "Apple"            # Make
        exif[0x0110] = "iPhone 15 Pro"    # Model
        Image.new("RGB", (400, 300), (10, 10, 10)).save(buf, "JPEG", exif=exif)
        assert Image.open(io.BytesIO(buf.getvalue())).getexif(), "la foto de prueba no trae EXIF"
        fid = _abrir(admin, cita)
        j = admin.post(f"/recepciones/{fid}/fotos",
                       data={"foto": (io.BytesIO(buf.getvalue()), "gps.jpg"), "etapa": "recepcion"},
                       content_type="multipart/form-data").get_json()
        guardada = Image.open(io.BytesIO(admin.get(j["url"]).data))
        # El GPS vive dentro del EXIF: sin EXIF, sin ubicación.
        assert not guardada.getexif(), "la foto guardada conserva el EXIF"

    def test_algo_que_no_es_una_foto_se_rechaza(self, admin, cita):
        fid = _abrir(admin, cita)
        r = admin.post(f"/recepciones/{fid}/fotos",
                       data={"foto": (io.BytesIO(b"<?php echo 1; ?>"), "foto.jpg"), "etapa": "recepcion"},
                       content_type="multipart/form-data")
        assert r.status_code == 400
        assert _ficha(fid).fotos == []

    def test_una_etapa_inventada_no_entra(self, admin, cita):
        fid = _abrir(admin, cita)
        assert _subir(admin, fid, etapa="cualquiera").status_code == 409


# ── Novedades ────────────────────────────────────────────────────────────────
class TestNovedades:
    def test_se_registra_con_zona_tipo_y_fotos(self, admin, cita):
        fid = _abrir(admin, cita)
        admin.post(f"/recepciones/{fid}/novedades", data={
            "zona": "Puerta delantera izquierda", "tipo": "Rayón",
            "descripcion": "5 cm bajo la manija",
            "fotos": [(io.BytesIO(_jpeg()), "a.jpg"), (io.BytesIO(_jpeg()), "b.jpg")],
        }, content_type="multipart/form-data")
        f = _ficha(fid)
        assert len(f.novedades) == 1
        n = f.novedades[0]
        assert (n.zona, n.tipo, n.descripcion) == ("Puerta delantera izquierda", "Rayón", "5 cm bajo la manija")
        assert len(n.fotos) == 2

    def test_una_zona_inventada_no_entra(self, admin, cita):
        """Las zonas son una lista cerrada para que las novedades se puedan
        comparar entre visitas del mismo carro."""
        fid = _abrir(admin, cita)
        admin.post(f"/recepciones/{fid}/novedades", data={"zona": "El alma", "tipo": "Rayón"})
        assert _ficha(fid).novedades == []

    def test_borrar_una_novedad_se_lleva_sus_fotos(self, admin, cita):
        fid = _abrir(admin, cita)
        admin.post(f"/recepciones/{fid}/novedades", data={
            "zona": "Capó", "tipo": "Picadura",
            "fotos": [(io.BytesIO(_jpeg()), "a.jpg")]}, content_type="multipart/form-data")
        nid = _ficha(fid).novedades[0].id
        admin.post(f"/recepciones/{fid}/novedades/{nid}/borrar")
        f = _ficha(fid)
        assert f.novedades == [] and f.fotos == []


# ── Sellar ───────────────────────────────────────────────────────────────────
class TestSellar:
    def test_sin_firma_no_se_sella(self, admin, cita):
        fid = _abrir(admin, cita)
        _sellar(admin, fid, firma="")
        assert _ficha(fid).etapa == "recepcion"

    def test_un_lienzo_en_blanco_no_es_una_firma(self, admin, cita):
        """Un lienzo vacío llega igual como un PNG válido. Aceptarlo dejaría
        fichas "firmadas" que nadie firmó."""
        fid = _abrir(admin, cita)
        _sellar(admin, fid, firma=_firma(trazo=False))
        assert _ficha(fid).etapa == "recepcion"

    def test_si_falta_la_firma_lo_escrito_no_se_pierde(self, admin, cita):
        """Que falte la firma no puede costar volver a llenar el formulario."""
        fid = _abrir(admin, cita)
        admin.post(f"/recepciones/{fid}/datos", data={
            "accion": "sellar", "plate": "NIR849", "marca": "Mazda", "km_entrada": "45000",
            "firmado_por": "Tatiana", "firma": ""})
        f = _ficha(fid)
        assert f.etapa == "recepcion"
        assert (f.marca, f.km_entrada) == ("Mazda", 45000)

    def test_con_firma_se_sella_y_guarda_quien_y_cuando(self, admin, cita):
        fid = _abrir(admin, cita)
        _sellar(admin, fid)
        f = _ficha(fid)
        assert f.etapa == "proceso"
        assert f.firma_recepcion[:8] == b"\x89PNG\r\n\x1a\n"
        assert f.firmado_por == "Tatiana Pinzón"
        assert f.recibido_por and f.recibido_at
        assert f.km_entrada == 45000

    def test_una_firma_gigante_se_rechaza(self, admin, cita):
        fid = _abrir(admin, cita)
        enorme = "data:image/png;base64," + base64.b64encode(b"\x89PNG" + b"0" * 600_000).decode()
        _sellar(admin, fid, firma=enorme)
        assert _ficha(fid).etapa == "recepcion"


class TestSelladaNoSeToca:
    """LA regla del módulo. Se intenta romper desde cada ruta que escribe."""

    @pytest.fixture
    def sellada(self, admin, cita):
        fid = _abrir(admin, cita)
        admin.post(f"/recepciones/{fid}/novedades", data={
            "zona": "Capó", "tipo": "Rayón",
            "fotos": [(io.BytesIO(_jpeg()), "a.jpg")]}, content_type="multipart/form-data")
        _subir(admin, fid)
        _sellar(admin, fid)
        assert _ficha(fid).etapa == "proceso"
        return fid

    def test_no_se_cambian_los_datos(self, admin, sellada):
        admin.post(f"/recepciones/{sellada}/datos", data={
            "accion": "guardar", "plate": "OTRA99", "km_entrada": "1", "objetos": "nada"})
        f = _ficha(sellada)
        assert (f.plate, f.km_entrada) == ("NIR849", 45000)

    def test_no_se_vuelve_a_sellar_con_otra_firma(self, admin, sellada):
        antes = _ficha(sellada).firma_recepcion
        assert _firma(otra=True) != _firma(), "las dos firmas de prueba son iguales"
        _sellar(admin, sellada, firma=_firma(otra=True))
        assert _ficha(sellada).firma_recepcion == antes

    def test_no_se_agregan_novedades(self, admin, sellada):
        admin.post(f"/recepciones/{sellada}/novedades", data={"zona": "Techo", "tipo": "Golpe / abolladura"})
        assert len(_ficha(sellada).novedades) == 1

    def test_no_se_borran_novedades(self, admin, sellada):
        nid = _ficha(sellada).novedades[0].id
        admin.post(f"/recepciones/{sellada}/novedades/{nid}/borrar")
        assert len(_ficha(sellada).novedades) == 1

    def test_no_se_agregan_fotos_a_la_recepcion(self, admin, sellada):
        antes = len(_ficha(sellada).fotos_de("recepcion"))
        assert _subir(admin, sellada, etapa="recepcion").status_code == 409
        assert len(_ficha(sellada).fotos_de("recepcion")) == antes

    def test_no_se_cuelgan_fotos_de_una_novedad(self, admin, sellada):
        nid = _ficha(sellada).novedades[0].id
        r = _subir(admin, sellada, etapa="proceso", damage_id=str(nid))
        assert r.status_code == 400
        assert len(_ficha(sellada).novedades[0].fotos) == 1

    def test_no_se_borran_fotos_de_la_recepcion_ni_siendo_admin(self, admin, sellada):
        """Ni un admin. Si el dueño puede borrar la foto del rayón, la ficha no
        prueba nada frente al cliente."""
        fotos = _ficha(sellada).fotos_de("recepcion")
        for p in fotos:
            admin.post(f"/recepciones/fotos/{p.id}/borrar")
        assert len(_ficha(sellada).fotos_de("recepcion")) == len(fotos)

    def test_el_link_del_equipo_no_sube_a_la_recepcion(self, client, sellada):
        """El link público solo sube al PROCESO, diga lo que diga el formulario."""
        token = _ficha(sellada).token_equipo
        antes = len(_ficha(sellada).fotos_de("recepcion"))
        client.post(f"/e/{token}/fotos", data={
            "foto": (io.BytesIO(_jpeg()), "x.jpg"), "etapa": "recepcion"},
            content_type="multipart/form-data")
        assert len(_ficha(sellada).fotos_de("recepcion")) == antes


# ── Proceso y link del equipo ────────────────────────────────────────────────
class TestLinkDelEquipo:
    @pytest.fixture
    def en_proceso(self, admin, cita):
        fid = _abrir(admin, cita)
        _sellar(admin, fid)
        with admin.session_transaction() as s:
            s.clear()   # el operario abre el link sin sesión
        return fid

    def _post(self, client, token, contenido=None):
        return client.post(f"/e/{token}/fotos", data={
            "foto": (io.BytesIO(contenido or _jpeg()), "p.jpg"), "nota": "antes del pulido"},
            content_type="multipart/form-data")

    def test_abre_sin_sesion(self, client, en_proceso):
        r = client.get(f"/e/{_ficha(en_proceso).token_equipo}")
        assert r.status_code == 200
        assert "NIR849" in r.data.decode()

    def test_sube_fotos_del_proceso_sin_sesion(self, client, en_proceso):
        r = self._post(client, _ficha(en_proceso).token_equipo)
        assert r.status_code == 200 and r.get_json()["ok"]
        f = _ficha(en_proceso)
        assert len(f.fotos_de("proceso")) == 1
        assert f.fotos_de("proceso")[0].nota == "antes del pulido"

    def test_muestra_las_novedades_de_la_recepcion(self, admin, cita):
        """Quien trabaja el carro tiene que saber qué ya traía antes de tocarlo."""
        fid = _abrir(admin, cita)
        admin.post(f"/recepciones/{fid}/novedades", data={"zona": "Capó", "tipo": "Picadura"})
        _sellar(admin, fid)
        cuerpo = admin.get(f"/e/{_ficha(fid).token_equipo}").data.decode()
        assert "Capó" in cuerpo and "Picadura" in cuerpo

    def test_el_link_del_cliente_no_sube_fotos(self, client, en_proceso):
        r = self._post(client, _ficha(en_proceso).token_cliente)
        assert r.status_code == 404
        assert _ficha(en_proceso).fotos_de("proceso") == []

    def test_un_token_inventado_no_sube_nada(self, client, en_proceso):
        assert self._post(client, "x" * 32).status_code == 404

    def test_antes_de_sellar_el_link_no_sube(self, admin, cita, client):
        fid = _abrir(admin, cita)
        with admin.session_transaction() as s:
            s.clear()
        assert self._post(client, _ficha(fid).token_equipo).status_code == 409

    def test_un_archivo_enorme_se_corta_antes_de_leerlo(self, client, en_proceso):
        """El link es público: sin un tope que se mire ANTES de parsear, cualquiera
        podría llenar el disco del servidor."""
        grande = b"\xff\xd8" + b"0" * (A.FOTO_MAX_BYTES + 200_000)
        assert self._post(client, _ficha(en_proceso).token_equipo, grande).status_code == 413


# ── Link del cliente ─────────────────────────────────────────────────────────
class TestLinkDelCliente:
    def test_antes_de_sellar_no_muestra_la_recepcion_a_medias(self, admin, cita, client):
        fid = _abrir(admin, cita)
        admin.post(f"/recepciones/{fid}/novedades", data={"zona": "Capó", "tipo": "Rayón"})
        token = _ficha(fid).token_cliente
        with admin.session_transaction() as s:
            s.clear()
        cuerpo = client.get(f"/v/{token}").data.decode()
        assert "Estamos recibiendo tu carro" in cuerpo
        assert "Rayón" not in cuerpo

    def test_ni_sus_fotos(self, admin, cita, client):
        fid = _abrir(admin, cita)
        foto_id = _subir(admin, fid).get_json()["id"]
        token = _ficha(fid).token_cliente
        with admin.session_transaction() as s:
            s.clear()
        assert client.get(f"/rf/{token}/{foto_id}").status_code == 404

    def test_ya_sellada_muestra_novedades_y_fotos(self, admin, cita, client):
        fid = _abrir(admin, cita)
        admin.post(f"/recepciones/{fid}/novedades", data={"zona": "Capó", "tipo": "Rayón"})
        foto_id = _subir(admin, fid).get_json()["id"]
        _sellar(admin, fid)
        token = _ficha(fid).token_cliente
        with admin.session_transaction() as s:
            s.clear()
        cuerpo = client.get(f"/v/{token}").data.decode()
        assert "Capó" in cuerpo and "Rayón" in cuerpo
        assert client.get(f"/rf/{token}/{foto_id}").status_code == 200

    def test_no_muestra_el_telefono_del_cliente(self, admin, cita, client):
        """El link se reenvía: el teléfono no tiene por qué viajar con él."""
        fid = _abrir(admin, cita)
        _sellar(admin, fid)
        token = _ficha(fid).token_cliente
        with admin.session_transaction() as s:
            s.clear()
        assert "3105528361" not in client.get(f"/v/{token}").data.decode()

    def test_con_un_token_no_se_ven_fotos_de_otro_carro(self, admin, cita, client):
        """Sin validar que la foto sea de ESA ficha, bastaría cambiar el número
        en la URL para recorrer las fotos de todos los carros."""
        fid = _abrir(admin, cita)
        _sellar(admin, fid)
        token_ajeno = _ficha(fid).token_cliente
        otra = A.VehicleReception(token_equipo="e" * 32, token_cliente="c" * 32,
                                  plate="OTR123", etapa="proceso")
        A.db.session.add(otra)
        A.db.session.commit()
        foto = A.ReceptionPhoto(reception_id=otra.id, etapa="proceso",
                                key="recepciones/x.jpg", thumb_key="recepciones/x_m.jpg")
        A.db.session.add(foto)
        A.db.session.commit()
        with admin.session_transaction() as s:
            s.clear()
        assert client.get(f"/rf/{token_ajeno}/{foto.id}").status_code == 404


# ── Entrega ──────────────────────────────────────────────────────────────────
class TestEntrega:
    @pytest.fixture
    def en_proceso(self, admin, cita):
        fid = _abrir(admin, cita)
        _sellar(admin, fid)
        return fid

    def _entregar(self, client, fid, firma=None):
        return client.post(f"/recepciones/{fid}/entregar", data={
            "km_salida": "45.012", "entregado_a": "Tatiana Pinzón",
            "notas_entrega": "No lavar con presión por 7 días",
            "firma": firma if firma is not None else _firma()})

    def test_no_se_entrega_sin_recepcion_sellada(self, admin, cita):
        fid = _abrir(admin, cita)
        self._entregar(admin, fid)
        assert _ficha(fid).etapa == "recepcion"

    def test_sin_firma_no_se_entrega(self, admin, en_proceso):
        self._entregar(admin, en_proceso, firma="")
        assert _ficha(en_proceso).etapa == "proceso"

    def test_se_entrega_y_guarda_todo(self, admin, en_proceso):
        self._entregar(admin, en_proceso)
        f = _ficha(en_proceso)
        assert f.etapa == "entregado"
        assert f.km_salida == 45012
        assert f.entregado_a == "Tatiana Pinzón"
        assert f.firma_entrega[:4] == b"\x89PNG"
        assert f.entregado_por and f.entregado_at

    def test_entregado_ya_no_se_suben_fotos_ni_por_el_link(self, admin, en_proceso, client):
        self._entregar(admin, en_proceso)
        assert _subir(admin, en_proceso, etapa="proceso").status_code == 409
        token = _ficha(en_proceso).token_equipo
        with admin.session_transaction() as s:
            s.clear()
        r = client.post(f"/e/{token}/fotos", data={"foto": (io.BytesIO(_jpeg()), "p.jpg")},
                        content_type="multipart/form-data")
        assert r.status_code == 409

    def test_no_se_entrega_dos_veces(self, admin, en_proceso):
        self._entregar(admin, en_proceso)
        primera = _ficha(en_proceso).entregado_at
        self._entregar(admin, en_proceso)
        assert _ficha(en_proceso).entregado_at == primera


class TestQuienBorraEvidencias:
    @pytest.fixture
    def foto_proceso(self, admin, cita):
        fid = _abrir(admin, cita)
        _sellar(admin, fid)
        return fid, _subir(admin, fid, etapa="proceso").get_json()["id"]

    def test_un_operario_no_borra_fotos_del_proceso(self, client, foto_proceso):
        """Una vez en proceso, cada foto es una evidencia. Que el mismo operario
        que la subió la pueda desaparecer le quita todo el valor."""
        fid, foto_id = foto_proceso
        login_as(client, make_user(f"rc_op{next(_u)}", role="operario"))
        client.post(f"/recepciones/fotos/{foto_id}/borrar")
        assert len(_ficha(fid).fotos_de("proceso")) == 1

    def test_un_admin_si(self, admin, foto_proceso):
        fid, foto_id = foto_proceso
        admin.post(f"/recepciones/fotos/{foto_id}/borrar")
        assert _ficha(fid).fotos_de("proceso") == []

    def test_en_borrador_quien_recibe_si_borra(self, client, cita):
        """Mientras arma la ficha, quitar una foto movida es corregir, no
        esconder."""
        login_as(client, make_user(f"rc_op{next(_u)}", role="operario"))
        fid = _abrir(client, cita)
        foto_id = _subir(client, fid).get_json()["id"]
        client.post(f"/recepciones/fotos/{foto_id}/borrar")
        assert _ficha(fid).fotos == []


# ── Permisos y puntos de entrada ─────────────────────────────────────────────
class TestPermisos:
    def test_el_operario_recibe_carros(self, client, cita):
        """Es quien está en el taller cuando llega el carro."""
        login_as(client, make_user(f"rc_op{next(_u)}", role="operario"))
        fid = _abrir(client, cita)
        assert client.get(f"/recepciones/{fid}").status_code == 200

    def test_marketing_no(self, client, cita):
        login_as(client, make_user(f"rc_mk{next(_u)}", role="marketing"))
        assert client.get(f"/appointments/{cita}/recepcion").status_code == 302
        assert A.VehicleReception.query.count() == 0

    def test_las_fotos_de_la_app_piden_sesion(self, admin, cita, client):
        fid = _abrir(admin, cita)
        foto_id = _subir(admin, fid).get_json()["id"]
        with admin.session_transaction() as s:
            s.clear()
        assert client.get(f"/recepciones/fotos/{foto_id}").status_code in (302, 403)

    def test_el_cajon_de_la_agenda_sabe_si_ya_hay_ficha(self, admin, cita):
        assert admin.get(f"/appointment/{cita}/json").get_json()["recepcion"] is None
        fid = _abrir(admin, cita)
        j = admin.get(f"/appointment/{cita}/json").get_json()
        assert j["recepcion"] == {"id": fid, "etapa": "recepcion"}

    def test_el_cajon_trae_el_boton(self, admin, cita):
        assert "/recepcion" in admin.get("/calendar").data.decode()

    def test_el_listado_de_citas_trae_el_boton(self, admin, cita):
        assert f"/appointments/{cita}/recepcion" in admin.get("/appointments").data.decode()


class TestNoSeCruzaConLosBackups:
    def test_la_retencion_de_backups_no_ve_las_fotos(self):
        """Comparten bucket. Si la poda de backups listara todo, borraría las
        fotos de las recepciones como si fueran backups viejos."""
        import inspect
        fuente = inspect.getsource(A._backups_existentes)
        assert 'Prefix="agenda/"' in fuente
        assert not A.RECEPCION_PREFIJO.startswith("agenda")

    def test_borrar_la_cita_no_borra_la_ficha(self, admin, cita):
        """La constancia de cómo llegó el carro no puede irse con la cita."""
        fid = _abrir(admin, cita)
        _sellar(admin, fid)
        A.db.session.delete(A.Appointment.query.get(cita))
        A.db.session.commit()
        assert _ficha(fid) is not None


class TestNoSePierdeLoEscrito:
    """Dos formas en que se perdía lo que alguien acababa de escribir, las dos
    encontradas al recorrer el flujo completo en el navegador."""

    def test_el_autoguardado_responde_sin_recargar(self, admin, cita):
        """La página guarda sola mientras se escribe. Sin esto, agregar una
        novedad recargaba la página y se llevaba marca y kilometraje."""
        fid = _abrir(admin, cita)
        r = admin.post(f"/recepciones/{fid}/datos", data={
            "accion": "guardar", "plate": "NIR849", "marca": "Mazda", "km_entrada": "45000"},
            headers={"X-Requested-With": "fetch"})
        assert r.status_code == 200 and r.get_json() == {"ok": True}
        assert (_ficha(fid).marca, _ficha(fid).km_entrada) == ("Mazda", 45000)

    def test_el_autoguardado_tampoco_toca_una_sellada(self, admin, cita):
        """Si la recepción se selló en otra pestaña, el autoguardado de la
        primera no puede reescribirla por detrás."""
        fid = _abrir(admin, cita)
        _sellar(admin, fid)
        r = admin.post(f"/recepciones/{fid}/datos", data={
            "accion": "guardar", "plate": "OTRA99"},
            headers={"X-Requested-With": "fetch"})
        assert r.status_code == 409
        assert _ficha(fid).plate == "NIR849"

    def test_si_falta_la_firma_de_entrega_lo_escrito_sigue_en_pantalla(self, admin, cita):
        fid = _abrir(admin, cita)
        _sellar(admin, fid)
        admin.post(f"/recepciones/{fid}/entregar", data={
            "km_salida": "45012", "entregado_a": "Andrés Pinzón",
            "notas_entrega": "No lavar con presión por 7 días", "firma": ""})
        f = _ficha(fid)
        assert f.etapa == "proceso"
        cuerpo = admin.get(f"/recepciones/{fid}").data.decode()
        assert 'value="45012"' in cuerpo
        assert 'value="Andrés Pinzón"' in cuerpo
        assert "No lavar con presión por 7 días" in cuerpo
