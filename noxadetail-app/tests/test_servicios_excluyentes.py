"""Servicios excluyentes en el link del cliente.

Cotizar dos niveles del mismo servicio es normal: se le muestran al cliente
para que compare. Dejarlos marcados los dos no, porque suma un coating de 3
años ENCIMA de uno de 5 — y eso no es nada que se le pueda prestar a un carro.

Lo que fijan estos tests:
  • Nace marcado el mejor del grupo; los demás quedan a un clic.
  • Marcar uno desmarca el otro (en el navegador, y también en el servidor).
  • Lo que NO es excluyente sigue pudiéndose comprar junto: Detallado agrupa
    áreas distintas, no niveles.
"""
import itertools

import pytest

from conftest import app_module as A
from conftest import login_as, make_user

_u = itertools.count(1)


@pytest.fixture
def sesion(client):
    with A.app.app_context():
        uid = make_user(f"exc{next(_u)}", role="admin").id
    with client.session_transaction() as sess:
        sess["user_id"] = uid
    return client


def _crear(client, descripciones, precios, garantias=None):
    n = len(descripciones)
    garantias = garantias or [""] * n
    r = client.post("/quotes/new", data={
        "customer_name": "Cliente Excluyente",
        "item_desc": descripciones,
        "item_price": [str(p) for p in precios],
        "item_qty": ["1"] * n,
        "item_service_id": [""] * n,
        "item_detail": [""] * n,
        "item_warranty": garantias,
    }, follow_redirects=False)
    assert r.status_code == 302, r.data[:300]
    return r.headers["Location"].rstrip("/").split("/")[-1]


def _cot(code):
    return A.Quote.query.filter_by(code=code).first()


def _borrar(code):
    with A.app.app_context():
        c = _cot(code)
        if c:
            A.db.session.delete(c)
            A.db.session.commit()


COATINGS = (["Coating Ceramico 7H+", "Coating Ceramico 9H"],
            [1_099_000, 2_199_000],
            ["3 años", "5 años"])


class TestCualNaceMarcado:
    def test_manda_el_de_mas_garantia(self, sesion):
        """Lo que el cliente compara es la garantía, no el precio."""
        code = _crear(sesion, *COATINGS)
        try:
            with A.app.app_context():
                filas = {f["item"].description: f["marcado"]
                         for f in _cot(code).servicios_del_link}
            assert filas == {"Coating Ceramico 7H+": False,
                             "Coating Ceramico 9H": True}
        finally:
            _borrar(code)

    def test_el_orden_en_que_se_cotizaron_no_decide(self, sesion):
        """Si el de 5 años se digitó primero, sigue mandando él."""
        code = _crear(sesion,
                      ["Coating Ceramico 9H", "Coating Ceramico 7H+"],
                      [2_199_000, 1_099_000],
                      ["5 años", "3 años"])
        try:
            with A.app.app_context():
                marcados = [f["item"].description
                            for f in _cot(code).servicios_del_link if f["marcado"]]
            assert marcados == ["Coating Ceramico 9H"]
        finally:
            _borrar(code)

    def test_sin_garantia_escrita_desempata_el_precio(self, sesion):
        """La garantía es texto libre y a veces no la ponen."""
        code = _crear(sesion, ["Coating Ceramico 7H+", "Coating Ceramico 9H"],
                      [1_099_000, 2_199_000], ["", ""])
        try:
            with A.app.app_context():
                marcados = [f["item"].description
                            for f in _cot(code).servicios_del_link if f["marcado"]]
            assert marcados == ["Coating Ceramico 9H"]
        finally:
            _borrar(code)

    def test_una_garantia_de_dos_digitos_no_pierde_contra_una_de_un_digito(self, sesion):
        """Comparadas como texto, "10 años" < "5 años"."""
        code = _crear(sesion, ["Coating Ceramico 7H+", "Coating Ceramico 9H"],
                      [2_199_000, 1_099_000], ["5 años", "10 años"])
        try:
            with A.app.app_context():
                marcados = [f["item"].description
                            for f in _cot(code).servicios_del_link if f["marcado"]]
            assert marcados == ["Coating Ceramico 9H"]
        finally:
            _borrar(code)

    def test_uno_solo_del_grupo_no_es_una_eleccion(self, sesion):
        """Con un solo coating no hay disyuntiva: va marcado y sin grupo, o el
        cliente vería un radio que no lleva a ninguna parte."""
        code = _crear(sesion, ["Coating Ceramico 9H"], [2_199_000], ["5 años"])
        try:
            with A.app.app_context():
                fila = _cot(code).servicios_del_link[0]
            assert fila["marcado"] is True and fila["grupo"] is None
        finally:
            _borrar(code)


class TestLoQueNoEsExcluyente:
    def test_los_detallados_se_compran_juntos(self, sesion):
        """Detallado agrupa ÁREAS distintas, no niveles: interior y exterior es
        un combo normal. Volverlas excluyentes le quitaría la venta."""
        code = _crear(sesion, ["Detallado Interior", "Detallado Exterior",
                               "Detallado de Motor"],
                      [400_000, 500_000, 200_000])
        try:
            with A.app.app_context():
                filas = _cot(code).servicios_del_link
            assert all(f["marcado"] for f in filas)
            assert all(f["grupo"] is None for f in filas)
        finally:
            _borrar(code)

    def test_polichado_y_porcelanizado_son_complementarios(self, sesion):
        code = _crear(sesion, ["Polichado", "Porcelanizado"], [300_000, 250_000])
        try:
            with A.app.app_context():
                filas = _cot(code).servicios_del_link
            assert all(f["marcado"] for f in filas)
        finally:
            _borrar(code)

    def test_un_coating_y_un_detallado_no_se_estorban(self, sesion):
        """Grupos distintos: el coating elige uno, el detallado va aparte."""
        code = _crear(sesion, ["Coating Ceramico 7H+", "Coating Ceramico 9H",
                               "Detallado Interior"],
                      [1_099_000, 2_199_000, 400_000], ["3 años", "5 años", ""])
        try:
            with A.app.app_context():
                filas = {f["item"].description: f for f in _cot(code).servicios_del_link}
            assert filas["Detallado Interior"]["marcado"] is True
            assert filas["Detallado Interior"]["grupo"] is None
            assert filas["Coating Ceramico 9H"]["marcado"] is True
            assert filas["Coating Ceramico 7H+"]["marcado"] is False
        finally:
            _borrar(code)


class TestElLinkDelCliente:
    def test_solo_uno_nace_con_el_chulito(self, sesion):
        code = _crear(sesion, *COATINGS)
        try:
            with A.app.app_context():
                token = _cot(code).public_token
            with sesion.session_transaction() as s:
                s.clear()
            html = sesion.get(f"/c/{token}").get_data(as_text=True)
            import re
            # Las dos líneas del grupo están, con UNA sola marcada.
            filas = re.findall(
                r'data-grupo="Protección Cerámica">\s*<input type="checkbox"( checked)?',
                html)
            assert len(filas) == 2
            assert sum(1 for f in filas if f) == 1
        finally:
            _borrar(code)

    def test_el_total_de_apertura_no_suma_los_dos(self, sesion):
        code = _crear(sesion, *COATINGS)
        try:
            with A.app.app_context():
                c = _cot(code)
                marcados = [f["item"].total for f in c.servicios_del_link if f["marcado"]]
            assert sum(marcados) == 2_199_000        # no 3.298.000
        finally:
            _borrar(code)


class TestElServidorTambienLoImpone:
    """El navegador ya lo impide, pero el PDF y el total salen del servidor.
    Una pestaña abierta desde antes del cambio mandaría los dos."""

    def test_si_llegan_los_dos_se_queda_el_de_mas_garantia(self, sesion):
        code = _crear(sesion, *COATINGS)
        try:
            with A.app.app_context():
                c = _cot(code)
                ambos = [i.id for i in c.items_de_servicio]
                ids, *_ = A._limpiar_seleccion(c, {"items": ambos})
                quedan = [i.description for i in c.items_de_servicio if i.id in ids]
            assert quedan == ["Coating Ceramico 9H"]
        finally:
            _borrar(code)

    def test_el_total_impreso_no_cobra_los_dos(self, sesion):
        code = _crear(sesion, *COATINGS)
        try:
            with A.app.app_context():
                c = _cot(code)
                ambos = [i.id for i in c.items_de_servicio]
                v = A._version_en_memoria(c, {"items": ambos})
            assert v.total == 2_199_000               # no 3.298.000
        finally:
            _borrar(code)

    def test_el_cliente_puede_quedarse_con_el_de_menos_garantia(self, sesion):
        """Es su decisión: si marca el de 3 años, se respeta."""
        code = _crear(sesion, *COATINGS)
        try:
            with A.app.app_context():
                c = _cot(code)
                barato = [i.id for i in c.items_de_servicio
                          if i.description == "Coating Ceramico 7H+"]
                ids, *_ = A._limpiar_seleccion(c, {"items": barato})
                quedan = [i.description for i in c.items_de_servicio if i.id in ids]
            assert quedan == ["Coating Ceramico 7H+"]
        finally:
            _borrar(code)

    def test_puede_no_querer_ninguno(self, sesion):
        code = _crear(sesion, *COATINGS)
        try:
            with A.app.app_context():
                c = _cot(code)
                ids, *_ = A._limpiar_seleccion(c, {"items": []})
            assert ids == []
        finally:
            _borrar(code)

    def test_lo_que_no_es_excluyente_pasa_completo(self, sesion):
        code = _crear(sesion, ["Detallado Interior", "Detallado Exterior"],
                      [400_000, 500_000])
        try:
            with A.app.app_context():
                c = _cot(code)
                todos = [i.id for i in c.items_de_servicio]
                ids, *_ = A._limpiar_seleccion(c, {"items": todos})
            assert len(ids) == 2
        finally:
            _borrar(code)


class TestLaRegla:
    def test_que_categorias_son_excluyentes(self):
        assert A.grupo_excluyente("Coating Ceramico 9H") == "Protección Cerámica"
        assert A.grupo_excluyente("Wash Essential") == "Lavado & Mantenimiento"
        assert A.grupo_excluyente("Detallado Interior") is None
        assert A.grupo_excluyente("Polichado") is None

    def test_lee_los_anios_de_una_garantia_escrita_a_mano(self):
        assert A._anios_de_garantia("5 años") == 5
        assert A._anios_de_garantia("10 años con certificado de la marca") == 10
        assert A._anios_de_garantia("") == 0
        assert A._anios_de_garantia(None) == 0
