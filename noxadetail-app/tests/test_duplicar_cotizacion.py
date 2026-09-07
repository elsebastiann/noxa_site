"""Duplicar una cotización para usarla de base.

Muchas cotizaciones se parecen: el mismo paquete para otro carro, el mismo
cliente con otro vehículo. Rehacerlas desde cero es volver a elegir servicios,
partes y marcas, y volver a escribir los precios que ya se habían negociado.

Lo que se copia es el TRABAJO —precios congelados, ajuste, descuento, partes—.
Lo que no se copia es lo que pertenece a la cotización original: su código, su
link, las versiones que armó el cliente y su fecha de emisión.
"""
import itertools
from datetime import timedelta

import pytest

from conftest import app_module as A, make_user

_u = itertools.count(1)


@pytest.fixture
def sesion(client):
    with A.app.app_context():
        uid = make_user(f"dup{next(_u)}", role="admin").id
    with client.session_transaction() as sess:
        sess["user_id"] = uid
    return client


def _crear(client, **datos):
    base = {"customer_name": "Laura Ortiz", "customer_phone": "3001234567",
            "plate": "ABC123", "vehicle_label": "Mazda 3 2021"}
    base.update(datos)
    r = client.post("/quotes/new", data=base, follow_redirects=False)
    assert r.status_code == 302
    return r.headers["Location"].rstrip("/").split("/")[-1]


def _duplicar(client, code):
    r = client.post(f"/quotes/{code}/duplicate", follow_redirects=False)
    assert r.status_code == 302, "duplicar debería llevar a editar la copia"
    destino = r.headers["Location"]
    assert destino.endswith("/edit"), f"no abrió la copia para editarla: {destino}"
    return destino.rstrip("/").rsplit("/", 2)[-2]


def _borrar(*codes):
    with A.app.app_context():
        for code in codes:
            c = A.Quote.query.filter_by(code=code).first()
            if c:
                A.db.session.delete(c)
        A.db.session.commit()


class TestLaCopiaEsUnaCotizacionNueva:
    def test_nace_con_codigo_propio(self, sesion):
        code = _crear(sesion, ppf_coverage=["Manijas"])
        copia = _duplicar(sesion, code)
        try:
            assert copia != code
        finally:
            _borrar(code, copia)

    def test_y_con_link_propio(self, sesion):
        """Compartir el link de la copia no puede mostrar la original, ni al
        revés: son dos documentos distintos para dos clientes distintos."""
        code = _crear(sesion, ppf_coverage=["Manijas"])
        copia = _duplicar(sesion, code)
        try:
            with A.app.app_context():
                a = A.Quote.query.filter_by(code=code).first()
                b = A.Quote.query.filter_by(code=copia).first()
                assert a.public_token != b.public_token
        finally:
            _borrar(code, copia)

    def test_la_original_no_se_toca(self, sesion):
        code = _crear(sesion, ppf_coverage=["Manijas"])
        with A.app.app_context():
            antes = A.Quote.query.filter_by(code=code).first()
            token, items, ppf = antes.public_token, len(antes.items), len(antes.ppf_items)
        copia = _duplicar(sesion, code)
        try:
            with A.app.app_context():
                despues = A.Quote.query.filter_by(code=code).first()
                assert despues.public_token == token
                assert len(despues.items) == items
                assert len(despues.ppf_items) == ppf
        finally:
            _borrar(code, copia)

    def test_la_vigencia_se_cuenta_desde_hoy(self, sesion):
        """Heredar la fecha de vencimiento haría nacer vencida una copia de algo
        emitido hace un mes."""
        code = _crear(sesion, ppf_coverage=["Manijas"], valid_days="20")
        with A.app.app_context():
            vieja = A.Quote.query.filter_by(code=code).first()
            vieja.created_at = vieja.created_at - timedelta(days=40)
            vieja.valid_until = A.bogota_today() - timedelta(days=20)
            A.db.session.commit()
        copia = _duplicar(sesion, code)
        try:
            with A.app.app_context():
                assert A.Quote.query.filter_by(code=copia).first().valid_until > A.bogota_today()
        finally:
            _borrar(code, copia)


class TestSeCopiaLoQueCuestaRehacer:
    def test_los_datos_del_cliente_y_el_vehiculo(self, sesion):
        code = _crear(sesion, ppf_coverage=["Manijas"])
        copia = _duplicar(sesion, code)
        try:
            with A.app.app_context():
                b = A.Quote.query.filter_by(code=copia).first()
                assert b.customer_name == "Laura Ortiz"
                assert b.customer_phone == "3001234567"
                assert b.plate == "ABC123"
                assert b.vehicle_label == "Mazda 3 2021"
        finally:
            _borrar(code, copia)

    def test_los_precios_negociados_y_no_los_de_lista(self, sesion):
        """Es la razón de duplicar: partir de lo que ya se acordó. Volver a
        tarifar contra el catálogo dejaría el mismo trabajo que se evitaba."""
        code = _crear(sesion, ppf_coverage=["Manijas"],
                      **{"ppf_precio::Manijas||Xpel": "777000"})
        copia = _duplicar(sesion, code)
        try:
            with A.app.app_context():
                b = A.Quote.query.filter_by(code=copia).first()
                assert b.ppf_items[0].precios["Xpel"] == 777000
        finally:
            _borrar(code, copia)

    def test_el_ajuste_y_el_descuento(self, sesion):
        code = _crear(sesion, ppf_coverage=["Manijas"], ajuste_pct="20",
                      discount_type="percentage", discount_value="15",
                      discount_label="Miembro Silver")
        copia = _duplicar(sesion, code)
        try:
            with A.app.app_context():
                b = A.Quote.query.filter_by(code=copia).first()
                assert b.ajuste_pct == 20
                assert b.discount_type == "percentage"
                assert b.discount_value == 15
                assert b.discount_label == "Miembro Silver"
        finally:
            _borrar(code, copia)

    def test_los_grupos_armados_a_mano_con_sus_partes(self, sesion):
        """Son los que más cuesta rehacer: hay que volver a elegir cada pieza."""
        code = _crear(sesion, libre_nombre=["Interior custom"],
                      libre_partes_0=["Pantalla"],
                      **{"libre_precio_0::Xpel": "500000"})
        copia = _duplicar(sesion, code)
        try:
            with A.app.app_context():
                it = A.Quote.query.filter_by(code=copia).first().ppf_items[0]
                assert it.coverage == "Interior custom"
                assert it.partes == ["Pantalla"]
                assert it.precios["Xpel"] == 500000
                assert it.es_personalizado is True
        finally:
            _borrar(code, copia)


class TestQuienPuede:
    def test_sin_permiso_no_se_duplica(self, client):
        with A.app.app_context():
            uid = make_user(f"dupop{next(_u)}", role="operario").id
        with client.session_transaction() as sess:
            sess["user_id"] = uid
        with A.app.app_context():
            antes = A.Quote.query.count()
        r = client.post("/quotes/CUALQUIERA/duplicate", follow_redirects=False)
        assert r.status_code == 302
        with A.app.app_context():
            assert A.Quote.query.count() == antes

    def test_duplicar_una_que_no_existe_no_revienta(self, sesion):
        r = sesion.post("/quotes/NX-NOEXISTE/duplicate", follow_redirects=True)
        assert r.status_code == 200
        assert "No existe esa cotización" in r.data.decode()
