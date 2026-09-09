"""Pedirle precios a un instalador antes de cotizarle al cliente.

Para cotizar un PPF hay que saber primero qué cobra el instalador por ESE carro.
Eso se pedía por WhatsApp y volvía como texto suelto que alguien transcribía.
Ahora se manda un link sin login, con la foto y la lista de partes, y la
respuesta queda estructurada.

Dos reglas que sostienen todo lo demás: cada instalador trabaja sus propias
marcas —y eso vive en la tabla, no en un `if` por nombre— y el link vence.
"""
import itertools
import json
from datetime import timedelta

import pytest

from conftest import app_module as A, make_user

_u = itertools.count(1)
_n = itertools.count(1)


@pytest.fixture
def sesion(client):
    with A.app.app_context():
        uid = make_user(f"sp{next(_u)}", role="admin").id
    with client.session_transaction() as sess:
        sess["user_id"] = uid
    return client


@pytest.fixture
def instalador():
    """Uno con marcas propias, como Camilo."""
    with A.app.app_context():
        i = A.Installer(name=f"Instalador {next(_n)}", default_share=65,
                        ppf_brands_json=json.dumps(["Standard", "Avery", "Stark"]))
        A.db.session.add(i)
        A.db.session.commit()
        iid = i.id
    yield iid
    with A.app.app_context():
        for s in A.PriceRequest.query.filter_by(installer_id=iid).all():
            A.db.session.delete(s)
        fila = A.Installer.query.get(iid)
        if fila:
            A.db.session.delete(fila)
        A.db.session.commit()


def _grupo():
    with A.app.app_context():
        return A.PpfPackage.query.filter_by(is_active=True).first().name


def _crear(client, iid, **datos):
    base = {"installer_id": str(iid), "marca": "Mazda", "modelo": "3 Grand Touring",
            "anio": "2021", "cobertura": [_grupo()]}
    base.update(datos)
    r = client.post("/price-requests/new", data=base, follow_redirects=False)
    assert r.status_code == 302, "no se creó la solicitud"
    return r.headers["Location"].rstrip("/").split("/")[-1]


def _sol(code):
    return A.PriceRequest.query.filter_by(code=code).first()


class TestLasMarcasSalenDelInstalador:
    def test_cada_uno_trae_las_suyas(self, instalador):
        with A.app.app_context():
            assert A.Installer.query.get(instalador).ppf_marcas == ["Standard", "Avery", "Stark"]

    def test_sin_marcas_definidas_se_le_preguntan_todas(self):
        """Default ruidoso pero no equivocado: contesta las que maneje y deja
        el resto en blanco. Peor sería no preguntarle por ninguna."""
        with A.app.app_context():
            i = A.Installer(name=f"Sin marcas {next(_n)}")
            A.db.session.add(i)
            A.db.session.commit()
            try:
                assert i.ppf_marcas == [m for m, _g in A.ppf_marcas_activas()]
            finally:
                A.db.session.delete(i)
                A.db.session.commit()

    def test_la_solicitud_las_congela(self, sesion, instalador):
        """Si mañana cambia de proveedor, lo que ya se le preguntó no puede
        reescribirse solo — es el mismo principio de las cotizaciones."""
        code = _crear(sesion, instalador)
        with A.app.app_context():
            assert _sol(code).marcas == ["Standard", "Avery", "Stark"]
            A.Installer.query.get(instalador).ppf_brands_json = json.dumps(["Xpel"])
            A.db.session.commit()
            assert _sol(code).marcas == ["Standard", "Avery", "Stark"]

    def test_no_dependen_del_nombre_del_instalador(self, instalador):
        """Un `if nombre == "Camilo"` se rompe con un cambio de nombre y con el
        tercer instalador que entre. Renombrarlo no le mueve las marcas."""
        with A.app.app_context():
            i = A.Installer.query.get(instalador)
            i.name = "Otro nombre completamente distinto"
            A.db.session.commit()
            assert i.ppf_marcas == ["Standard", "Avery", "Stark"]


class TestQueSeLePide:
    def test_los_grupos_del_catalogo_entran_con_lo_que_incluyen(self, sesion, instalador):
        """Se COPIA lo que incluye, no se referencia: la solicitud queda abierta
        cinco días y el catálogo puede cambiar mientras tanto."""
        code = _crear(sesion, instalador)
        with A.app.app_context():
            it = _sol(code).items[0]
            assert it.cobertura == _grupo()
            assert it.detalle

    def test_tambien_algo_escrito_a_mano(self, sesion, instalador):
        code = _crear(sesion, instalador, cobertura=[],
                      otro_nombre=["Tanque"], otro_detalle=["Solo la cara superior"])
        with A.app.app_context():
            it = _sol(code).items[0]
            assert it.cobertura == "Tanque"
            assert it.detalle == "Solo la cara superior"
            assert it.es_personalizado is True

    def test_una_cobertura_inventada_no_entra(self, sesion, instalador):
        """El nombre viaja por el formulario. Sin validarlo contra el catálogo,
        cualquiera podría meter una línea que no existe."""
        code = _crear(sesion, instalador, cobertura=[_grupo(), "No existe este grupo"])
        with A.app.app_context():
            assert [i.cobertura for i in _sol(code).items] == [_grupo()]

    def test_sin_nada_que_cotizar_no_se_crea(self, sesion, instalador):
        r = sesion.post("/price-requests/new", data={
            "installer_id": str(instalador), "marca": "Mazda", "modelo": "3"},
            follow_redirects=True)
        assert "al menos una cobertura" in r.data.decode()


class TestElLinkDelInstalador:
    def test_lo_abre_sin_login(self, client, sesion, instalador):
        """Pedirle una cuenta a un proveedor externo por una lista de precios
        garantiza que no la llene.

        La sesión se BORRA antes de pedir la página: `client` y `sesion` son el
        mismo objeto, así que sin esto el test pasaba por estar logueado y no
        por ser pública la ruta. Pasó: la ruta redirigía al login y el test
        seguía en verde.
        """
        code = _crear(sesion, instalador)
        with A.app.app_context():
            token = _sol(code).public_token
        with client.session_transaction() as sess:
            sess.clear()
        r = client.get(f"/p/{token}")
        assert r.status_code == 200
        assert "Mazda 3 Grand Touring 2021" in r.data.decode()

    def test_muestra_solo_las_marcas_de_ese_instalador(self, client, sesion, instalador):
        code = _crear(sesion, instalador)
        with A.app.app_context():
            token = _sol(code).public_token
        with client.session_transaction() as sess:
            sess.clear()
        cuerpo = client.get(f"/p/{token}").data.decode()
        assert "Standard" in cuerpo and "Stark" in cuerpo
        assert "Xpel" not in cuerpo

    def test_guarda_los_precios_que_escribe(self, client, sesion, instalador):
        code = _crear(sesion, instalador)
        with A.app.app_context():
            sol = _sol(code)
            token, item_id = sol.public_token, sol.items[0].id
        r = client.post(f"/p/{token}", data={
            f"precio::{item_id}::Standard": "1050000",
            f"precio::{item_id}::Stark": "1750000",
            f"comentario::{item_id}": "Con el rayón hay que corregir antes",
        })
        assert r.status_code == 200
        with A.app.app_context():
            it = _sol(code).items[0]
            assert it.precios == {"Standard": 1050000, "Stark": 1750000}
            assert "corregir antes" in it.comentario
            assert _sol(code).respondida is True

    def test_una_marca_en_blanco_no_queda_en_cero(self, client, sesion, instalador):
        """Vacío significa "no la trabajo" o "no aplica". Un cero diría que la
        regala, y eso terminaría en una cotización al cliente."""
        code = _crear(sesion, instalador)
        with A.app.app_context():
            sol = _sol(code)
            token, item_id = sol.public_token, sol.items[0].id
        client.post(f"/p/{token}", data={f"precio::{item_id}::Standard": "1050000",
                                         f"precio::{item_id}::Avery": ""})
        with A.app.app_context():
            assert "Avery" not in _sol(code).items[0].precios

    def test_puede_volver_y_corregir(self, client, sesion, instalador):
        code = _crear(sesion, instalador)
        with A.app.app_context():
            sol = _sol(code)
            token, item_id = sol.public_token, sol.items[0].id
        client.post(f"/p/{token}", data={f"precio::{item_id}::Standard": "1000000"})
        client.post(f"/p/{token}", data={f"precio::{item_id}::Standard": "1200000"})
        with A.app.app_context():
            assert _sol(code).items[0].precios["Standard"] == 1200000


class TestElLinkVence:
    def test_nace_con_cinco_dias(self, sesion, instalador):
        code = _crear(sesion, instalador)
        with A.app.app_context():
            assert _sol(code).expires_on == A.bogota_today() + timedelta(days=5)

    def test_vencido_ya_no_deja_responder(self, client, sesion, instalador):
        code = _crear(sesion, instalador)
        with A.app.app_context():
            sol = _sol(code)
            sol.expires_on = A.bogota_today() - timedelta(days=1)
            A.db.session.commit()
            token, item_id = sol.public_token, sol.items[0].id
        assert client.get(f"/p/{token}").status_code == 410
        client.post(f"/p/{token}", data={f"precio::{item_id}::Standard": "9999000"})
        with A.app.app_context():
            assert _sol(code).items[0].precios == {}

    def test_el_ultimo_dia_todavia_sirve(self, client, sesion, instalador):
        """Contraprueba del borde: "vence el 14" tiene que incluir el 14."""
        code = _crear(sesion, instalador)
        with A.app.app_context():
            sol = _sol(code)
            sol.expires_on = A.bogota_today()
            A.db.session.commit()
            token = sol.public_token
        assert client.get(f"/p/{token}").status_code == 200

    def test_un_token_que_no_existe_no_revienta(self, client):
        assert client.get("/p/inventado").status_code == 404


class TestQuienPuede:
    def test_un_operario_no_pide_precios(self, client, instalador):
        """Los precios del instalador son el costo del negocio: es el mismo
        criterio por el que un operario no ve cuánto valen los servicios."""
        with A.app.app_context():
            uid = make_user(f"spop{next(_u)}", role="operario").id
        with client.session_transaction() as sess:
            sess["user_id"] = uid
        with A.app.app_context():
            antes = A.PriceRequest.query.count()
        client.post("/price-requests/new", data={
            "installer_id": str(instalador), "marca": "M", "modelo": "3",
            "cobertura": [_grupo()]})
        with A.app.app_context():
            assert A.PriceRequest.query.count() == antes


class TestReplicarUnaSolicitud:
    """Muchas solicitudes se parecen: el mismo carro para el otro instalador, o
    el mismo paquete de partes para otro vehículo.

    Se abre el formulario DILIGENCIADO en vez de crear la copia de una: crear
    una solicitud genera el link que se le manda al instalador, y no hay
    pantalla para editarla después — una copia hecha de golpe habría que
    borrarla y rehacerla para cambiarle una sola cosa.
    """

    def test_el_formulario_llega_con_los_datos_puestos(self, sesion, instalador):
        code = _crear(sesion, instalador, notas="Ojo con el rayón")
        html = sesion.get(f"/price-requests/new?desde={code}").data.decode()
        assert 'value="Mazda"' in html
        assert 'value="3 Grand Touring"' in html
        assert "Ojo con el rayón" in html
        assert "checked" in html          # la cobertura del original

    def test_tambien_los_escritos_a_mano(self, sesion, instalador):
        """Son los que más cuesta rehacer: hay que volver a escribir nombre y
        descripción."""
        code = _crear(sesion, instalador, cobertura=[],
                      otro_nombre=["Tanque"], otro_detalle=["Solo la cara superior"])
        html = sesion.get(f"/price-requests/new?desde={code}").data.decode()
        assert 'name="otro_nombre"' in html and 'value="Tanque"' in html
        assert "Solo la cara superior" in html

    def test_la_copia_nace_con_codigo_y_link_propios(self, sesion, instalador):
        code = _crear(sesion, instalador)
        copia = _crear(sesion, instalador)
        with A.app.app_context():
            a, b = _sol(code), _sol(copia)
            assert a.code != b.code
            assert a.public_token != b.public_token

    def test_no_hereda_las_respuestas(self, client, sesion, instalador):
        """Es otra solicitud: arrastrar los precios de la anterior los daría por
        buenos para un carro que el instalador todavía no ha mirado."""
        code = _crear(sesion, instalador)
        with A.app.app_context():
            sol = _sol(code)
            token, item_id = sol.public_token, sol.items[0].id
        client.post(f"/p/{token}", data={f"precio::{item_id}::Standard": "1000000"})
        html = sesion.get(f"/price-requests/new?desde={code}").data.decode()
        assert "1000000" not in html
        copia = _crear(sesion, instalador)
        with A.app.app_context():
            c = _sol(copia)
            assert c.respondida is False
            assert all(not i.precios for i in c.items)

    def test_un_codigo_que_no_existe_abre_el_formulario_vacio(self, sesion):
        """Sin reventar: es una URL que alguien puede editar a mano."""
        r = sesion.get("/price-requests/new?desde=SP-NOEXISTE")
        assert r.status_code == 200
        assert 'value="Mazda"' not in r.data.decode()


class TestLaVistaPreviaDelLink:
    """Al mandar el link por WhatsApp llegaba solo el título y la URL pelada.
    Con la foto del carro se sabe de un vistazo de qué solicitud se trata cuando
    hay varias en el mismo chat."""

    def test_sin_foto_no_declara_imagen(self, client, sesion, instalador):
        code = _crear(sesion, instalador)
        with A.app.app_context():
            token = _sol(code).public_token
            assert _sol(code).foto_compartir is None
        with client.session_transaction() as sess:
            sess.clear()
        assert 'og:image' not in client.get(f"/p/{token}").data.decode()

    def test_la_url_de_la_imagen_es_absoluta(self, sesion, instalador):
        """La lee el robot de WhatsApp, no el navegador: una ruta relativa no la
        puede resolver y la vista previa sale sin foto."""
        code = _crear(sesion, instalador)
        with A.app.app_context():
            sol = _sol(code)
            sol.foto = "prueba.jpg"
            A.db.session.commit()
            assert sol.foto_compartir.startswith("http")
            assert sol.foto_compartir.endswith("/pr/img/prueba.jpg")

    def test_prefiere_la_miniatura_cuando_existe(self, sesion, instalador):
        """WhatsApp descarta las imágenes pesadas sin decir nada, y una foto de
        celular pesa varios megas."""
        import os
        code = _crear(sesion, instalador)
        with A.app.app_context():
            sol = _sol(code)
            sol.foto = "conmini.jpg"
            A.db.session.commit()
            os.makedirs(A.VEHICULO_UPLOAD_DIR, exist_ok=True)
            mini = os.path.join(A.VEHICULO_UPLOAD_DIR, A._nombre_miniatura("conmini.jpg"))
            open(mini, "wb").write(b"x")
            try:
                assert sol.foto_compartir.endswith("conmini_og.jpg")
            finally:
                os.remove(mini)

    def test_una_foto_pesada_queda_liviana(self):
        """El número es lo que importa: varios megas no sirven de vista previa."""
        import os
        from PIL import Image
        os.makedirs(A.VEHICULO_UPLOAD_DIR, exist_ok=True)
        nombre = "prueba_grande.jpg"
        ruta = os.path.join(A.VEHICULO_UPLOAD_DIR, nombre)
        Image.new("RGB", (4032, 3024), (90, 100, 120)).save(ruta, "JPEG", quality=95)
        try:
            assert A._generar_miniatura(nombre) is True
            mini = os.path.join(A.VEHICULO_UPLOAD_DIR, A._nombre_miniatura(nombre))
            assert os.path.getsize(mini) < 300 * 1024
            with Image.open(mini) as img:
                assert max(img.size) <= 1200
        finally:
            for f in (ruta, os.path.join(A.VEHICULO_UPLOAD_DIR, A._nombre_miniatura(nombre))):
                if os.path.exists(f):
                    os.remove(f)

    def test_si_la_miniatura_falla_no_tumba_la_carga(self):
        """El link tiene que funcionar aunque la vista previa quede fea."""
        assert A._generar_miniatura("no_existe_este_archivo.jpg") is False


class TestEditarUnInstalador:
    """Todo en un solo formulario y un solo Guardar. Con un botón por grupo de
    campos, corregir un teléfono y una marca serían dos guardados, y el segundo
    tendría que acordarse de no pisar lo del primero."""

    @pytest.fixture
    def admin(self, client):
        with A.app.app_context():
            uid = make_user(f"ei{next(_u)}", role="admin").id
        with client.session_transaction() as sess:
            sess["user_id"] = uid
        return client

    def test_guarda_todo_de_una(self, admin, instalador):
        admin.post(f"/installers/{instalador}/edit", data={
            "name": "Camilo León", "phone": "3208288193", "default_share": "70",
            "notes": "Solo PPF", "marca": ["Avery", "Xpel"]})
        with A.app.app_context():
            i = A.Installer.query.get(instalador)
            assert (i.name, i.phone, i.default_share, i.notes) == \
                   ("Camilo León", "3208288193", 70, "Solo PPF")
            assert i.ppf_marcas == ["Avery", "Xpel"]

    def test_renombrarlo_dejandole_el_mismo_nombre_no_choca_consigo_mismo(self, admin, instalador):
        with A.app.app_context():
            nombre = A.Installer.query.get(instalador).name
        admin.post(f"/installers/{instalador}/edit",
                   data={"name": nombre, "default_share": "80"})
        with A.app.app_context():
            assert A.Installer.query.get(instalador).default_share == 80

    def test_no_deja_dos_con_el_mismo_nombre(self, admin, instalador):
        with A.app.app_context():
            otro = A.Installer(name=f"Otro {next(_n)}")
            A.db.session.add(otro)
            A.db.session.commit()
            oid, nombre_otro = otro.id, otro.name
        try:
            admin.post(f"/installers/{instalador}/edit", data={"name": nombre_otro})
            with A.app.app_context():
                assert A.Installer.query.get(instalador).name != nombre_otro
        finally:
            with A.app.app_context():
                fila = A.Installer.query.get(oid)
                if fila:
                    A.db.session.delete(fila)
                    A.db.session.commit()

    def test_un_nombre_vacio_no_lo_borra(self, admin, instalador):
        """Sin nombre, la liquidación histórica se queda sin a quién apuntar."""
        with A.app.app_context():
            antes = A.Installer.query.get(instalador).name
        admin.post(f"/installers/{instalador}/edit", data={"name": "   "})
        with A.app.app_context():
            assert A.Installer.query.get(instalador).name == antes

    def test_desmarcar_todas_las_marcas_vuelve_al_default(self, admin, instalador):
        """Desmarcarlas todas significa "no tiene marcas propias", no "no le
        preguntes por ninguna" — que dejaría solicitudes sin una sola columna."""
        admin.post(f"/installers/{instalador}/edit", data={"name": "Camilo", "marca": []})
        with A.app.app_context():
            i = A.Installer.query.get(instalador)
            assert i.ppf_brands_json is None
            assert i.ppf_marcas == [m for m, _g in A.ppf_marcas_activas()]

    def test_una_marca_inventada_no_entra(self, admin, instalador):
        admin.post(f"/installers/{instalador}/edit",
                   data={"name": "Camilo", "marca": ["Avery", "MarcaFalsa"]})
        with A.app.app_context():
            assert A.Installer.query.get(instalador).ppf_marcas == ["Avery"]

    def test_solo_un_admin_edita(self, client, instalador):
        with A.app.app_context():
            uid = make_user(f"eiop{next(_u)}", role="operario").id
            antes = A.Installer.query.get(instalador).default_share
        with client.session_transaction() as sess:
            sess["user_id"] = uid
        client.post(f"/installers/{instalador}/edit",
                    data={"name": "Cambiado", "default_share": "99"})
        with A.app.app_context():
            i = A.Installer.query.get(instalador)
            assert i.default_share == antes and i.name != "Cambiado"
