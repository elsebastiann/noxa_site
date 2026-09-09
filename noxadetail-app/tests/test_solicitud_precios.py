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
