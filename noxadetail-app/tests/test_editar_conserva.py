"""Abrir una cotización para editarla no puede perderle nada.

El armador se reconstruye entero desde JavaScript con el estado que le pasa el
servidor. Todo lo que ese estado no traiga, la pantalla no lo dibuja — y como al
guardar se vuelve a armar la cotización con lo que hay en el formulario, lo que
no se dibujó se borra. Callado, en una pantalla que dice "Editar".

Por eso estos tests miran el estado embebido en la página y no solo el POST: el
servidor sabe recibir un grupo armado a mano, el problema era que la pantalla
nunca se lo mandaba de vuelta.
"""
import itertools
import json
import re

import pytest

from conftest import app_module as A, make_user

_u = itertools.count(1)


@pytest.fixture
def sesion(client):
    with A.app.app_context():
        uid = make_user(f"ed{next(_u)}", role="admin").id
    with client.session_transaction() as sess:
        sess["user_id"] = uid
    return client


def _crear(client, **datos):
    base = {"customer_name": "Laura Ortiz"}
    base.update(datos)
    r = client.post("/quotes/new", data=base, follow_redirects=False)
    assert r.status_code == 302
    return r.headers["Location"].rstrip("/").split("/")[-1]


def _borrar(code):
    with A.app.app_context():
        c = A.Quote.query.filter_by(code=code).first()
        if c:
            A.db.session.delete(c)
            A.db.session.commit()


def _estado(client, code, variable):
    """Lee una de las variables de estado que el armador embebe en la página."""
    cuerpo = client.get(f"/quotes/{code}/edit").data.decode()
    m = re.search(rf"^let {variable} = (.+);$", cuerpo, re.M)
    assert m, f"la página no embebe «{variable}»"
    return json.loads(m.group(1))


def _grupo_con_fotocromatico():
    with A.app.app_context():
        for p in A.PpfPackage.query.filter_by(is_active=True).all():
            if p.admite_fotocromatico and p.precios_fotocromatico:
                return p.name
    return None


class TestElGrupoArmadoAMano:
    """Uno que no está en el catálogo: lo escribió quien cotizó."""

    def _cotizacion_con_grupo(self, sesion):
        return _crear(sesion, libre_nombre=["Interior custom"],
                      libre_partes_0=["Pantalla"],
                      **{"libre_precio_0::Xpel": "500000"})

    def test_el_armador_lo_trae_de_vuelta(self, sesion):
        """Sin esto la caja de "armar un grupo" abre vacía y no hay manera de
        corregirle el precio ni las partes."""
        code = self._cotizacion_con_grupo(sesion)
        try:
            libres = _estado(sesion, code, "libres")
            assert [g["nombre"] for g in libres] == ["Interior custom"]
            assert libres[0]["partes"] == ["Pantalla"]
            assert libres[0]["precios"]["Xpel"] == 500000
        finally:
            _borrar(code)

    def test_no_lo_manda_como_si_fuera_del_catalogo(self, sesion):
        """Iba en la misma lista que las coberturas del catálogo, así que al
        guardar viajaba como `ppf_coverage`. El servidor lo buscaba en la tabla
        de grupos, no lo encontraba y lo saltaba: editar borraba el grupo."""
        code = self._cotizacion_con_grupo(sesion)
        try:
            assert "Interior custom" not in _estado(sesion, code, "ppfPuestas")
        finally:
            _borrar(code)

    def test_guardar_sin_tocar_nada_no_lo_borra(self, sesion):
        code = self._cotizacion_con_grupo(sesion)
        try:
            sesion.post(f"/quotes/{code}/edit", data={
                "customer_name": "Laura Ortiz",
                "libre_nombre": ["Interior custom"],
                "libre_partes_0": ["Pantalla"],
                "libre_precio_0::Xpel": "500000",
            })
            with A.app.app_context():
                c = A.Quote.query.filter_by(code=code).first()
                assert [it.coverage for it in c.ppf_items] == ["Interior custom"]
                assert c.ppf_items[0].precios["Xpel"] == 500000
        finally:
            _borrar(code)

    def test_sus_precios_no_se_recalculan_solos(self, sesion):
        """El armador sugiere un precio sumando las partes sueltas. Si al
        reabrir no supiera que esa cifra se escribió a mano, la pisaría con la
        suma y cambiaría un precio que el cliente ya vio."""
        code = self._cotizacion_con_grupo(sesion)
        try:
            assert _estado(sesion, code, "libres")[0]["manual"]["Xpel"] is True
        finally:
            _borrar(code)


class TestElFotocromatico:
    def test_sigue_marcado_al_reabrir(self, sesion):
        """Es un adicional que se cobra aparte. Al editar arrancaba en cero, así
        que guardar sin darse cuenta le quitaba el sobrecosto a la cotización."""
        grupo = _grupo_con_fotocromatico()
        if not grupo:
            pytest.skip("ningún grupo del catálogo cobra fotocromático")
        code = _crear(sesion, ppf_coverage=[grupo], **{f"ppf_foto::{grupo}": "1"})
        try:
            with A.app.app_context():
                assert A.Quote.query.filter_by(code=code).first().ppf_items[0].con_fotocromatico
            assert _estado(sesion, code, "ppfFoto").get(grupo) is True
        finally:
            _borrar(code)
