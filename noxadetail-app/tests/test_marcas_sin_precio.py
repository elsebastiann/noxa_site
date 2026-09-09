"""Una marca sin un solo precio no se le muestra al cliente.

En el link salían las cinco marcas aunque solo una tuviera precios: cuatro
tarjetas en $0 y un "no incluida" en cada fila. Eso no le dice nada al cliente y
parece un error del documento.

Eran tres cosas encadenadas:

1. Las marcas se congelaban SOLO al crear la cotización, así que desmarcarlas al
   editar no las quitaba de ninguna parte.
2. El armador pintaba las casillas contra el catálogo, no contra la cotización,
   así que al editar aparecían marcadas marcas que la cotización no tenía.
3. Nada filtraba al pintar, así que una cotización ya guardada con ese problema
   seguía mostrándolas para siempre.
"""
import itertools
import json

import pytest

from conftest import app_module as A, make_user

_u = itertools.count(1)

NAVEGADOR = "Mozilla/5.0 (iPhone) Safari/604.1"


@pytest.fixture
def sesion(client):
    with A.app.app_context():
        uid = make_user(f"msp{next(_u)}", role="admin").id
    with client.session_transaction() as sess:
        sess["user_id"] = uid
    return client


def _crear(client, marcas, **extra):
    datos = {"customer_name": "Diego", "ppf_coverage": ["Farolas"],
             "ppf_marca": marcas}
    datos.update({f"ppf_garantia::{m}": "5" for m in marcas})
    datos.update(extra)
    r = client.post("/quotes/new", data=datos, follow_redirects=False)
    assert r.status_code == 302
    return r.headers["Location"].rstrip("/").split("/")[-1]


def _marcas(code):
    with A.app.app_context():
        return [m for m, _g in A.Quote.query.filter_by(code=code).first().ppf_marcas]


def _borrar(code):
    with A.app.app_context():
        c = A.Quote.query.filter_by(code=code).first()
        if c:
            A.db.session.delete(c)
            A.db.session.commit()


class TestDesmarcarUnaMarcaAlEditar:
    def test_la_quita_de_la_cotizacion(self, sesion):
        """El caso reportado: se editó dejando una sola marca y el link seguía
        mostrando las otras cuatro en $0."""
        code = _crear(sesion, ["Spectra", "Avery", "Xpel"])
        try:
            assert len(_marcas(code)) == 3
            sesion.post(f"/quotes/{code}/edit", data={
                "customer_name": "Diego", "ppf_coverage": ["Farolas"],
                "ppf_marca": ["Avery"], "ppf_garantia::Avery": "6"})
            assert _marcas(code) == ["Avery"]
        finally:
            _borrar(code)

    def test_y_el_link_deja_de_mostrarlas(self, client, sesion):
        code = _crear(sesion, ["Spectra", "Avery", "Xpel"])
        try:
            sesion.post(f"/quotes/{code}/edit", data={
                "customer_name": "Diego", "ppf_coverage": ["Farolas"],
                "ppf_marca": ["Avery"], "ppf_garantia::Avery": "6"})
            with A.app.app_context():
                token = A.Quote.query.filter_by(code=code).first().public_token
            with client.session_transaction() as sess:
                sess.clear()
            cuerpo = client.get(f"/c/{token}",
                                headers={"User-Agent": NAVEGADOR}).data.decode()
            assert 'data-marca="Avery"' in cuerpo
            assert 'data-marca="Spectra"' not in cuerpo
            assert 'data-marca="Xpel"' not in cuerpo
        finally:
            _borrar(code)

    def test_tambien_se_puede_agregar_una(self, sesion):
        """Recalcular en cada guardado tiene que servir en los dos sentidos."""
        code = _crear(sesion, ["Avery"])
        try:
            sesion.post(f"/quotes/{code}/edit", data={
                "customer_name": "Diego", "ppf_coverage": ["Farolas"],
                "ppf_marca": ["Avery", "Xpel"],
                "ppf_garantia::Avery": "6", "ppf_garantia::Xpel": "10"})
            assert sorted(_marcas(code)) == ["Avery", "Xpel"]
        finally:
            _borrar(code)

    def test_la_garantia_negociada_sobrevive(self, sesion):
        """Es la razón de congelarlas: el papel dice lo que se prometió, no lo
        que diga el catálogo un mes después."""
        code = _crear(sesion, ["Avery"], **{"ppf_garantia::Avery": "9"})
        try:
            with A.app.app_context():
                assert dict(A.Quote.query.filter_by(code=code).first().ppf_marcas)["Avery"] == 9
        finally:
            _borrar(code)


class TestLasQueYaQuedaronMal:
    """Sin esto habría que migrar la base o pedirle a alguien que reabra y
    guarde cada cotización vieja."""

    def test_una_marca_sin_ningun_precio_no_se_pinta(self, sesion):
        code = _crear(sesion, ["Avery"])
        try:
            with A.app.app_context():
                c = A.Quote.query.filter_by(code=code).first()
                # Se fuerza el estado roto: marcas guardadas que ninguna línea
                # cotiza, que es como quedaron las de antes del arreglo.
                c.ppf_brands = json.dumps([["Avery", 6], ["Stark", 7], ["Xpel", 10]])
                c.ppf_items[0].prices_json = json.dumps({"Avery": 830000})
                A.db.session.commit()
                assert [m for m, _g in c.ppf_marcas] == ["Avery"]
        finally:
            _borrar(code)

    def test_si_ninguna_tiene_precio_no_se_queda_sin_columnas(self, sesion):
        """Un documento sin una sola columna es peor que uno con ruido."""
        code = _crear(sesion, ["Avery"])
        try:
            with A.app.app_context():
                c = A.Quote.query.filter_by(code=code).first()
                c.ppf_items[0].prices_json = json.dumps({})
                A.db.session.commit()
                assert c.ppf_marcas, "se quedó sin ninguna marca que mostrar"
        finally:
            _borrar(code)

    def test_una_cotizacion_sin_ppf_no_se_toca(self, sesion):
        """El filtro mira las líneas de PPF; sin líneas no hay nada que filtrar
        y devolver una lista vacía rompería el armador."""
        r = sesion.post("/quotes/new", data={
            "customer_name": "Diego", "item_desc": ["Chrome Delete"],
            "item_price": ["650000"], "item_qty": ["1"], "item_service_id": [""],
            "item_detail": [""], "item_warranty": [""]}, follow_redirects=False)
        code = r.headers["Location"].rstrip("/").split("/")[-1]
        try:
            with A.app.app_context():
                assert A.Quote.query.filter_by(code=code).first().ppf_marcas
        finally:
            _borrar(code)


class TestElArmadorMuestraLasDeLaCotizacion:
    """Pintaba las casillas contra el catálogo: abrir una cotización de dos
    marcas mostraba las cinco marcadas, y guardar así las devolvía todas."""

    def test_al_editar_solo_van_marcadas_las_suyas(self, sesion):
        code = _crear(sesion, ["Avery"])
        try:
            html = sesion.get(f"/quotes/{code}/edit").data.decode()
            import re
            marcadas = re.findall(
                r'name="ppf_marca" value="([^"]+)"\s*\n?\s*checked', html)
            assert marcadas == ["Avery"], f"quedaron marcadas: {marcadas}"
        finally:
            _borrar(code)

    def test_al_crear_se_marcan_las_del_catalogo(self, sesion):
        """En una cotización nueva no hay nada que respetar, así que arranca con
        las que el catálogo ofrece."""
        html = sesion.get("/quotes/new").data.decode()
        assert html.count('name="ppf_marca"') >= 2
