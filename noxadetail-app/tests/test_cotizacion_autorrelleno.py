"""Cotizar a un cliente que ya está en el sistema no debería ser volver a
escribirlo todo — igual que en las citas.

Con la placa, el teléfono o el nombre se traen los demás datos, incluido el tipo
de vehículo, que es el que desbloquea el armador.

La regla de oro del autorrelleno: solo llena lo que está VACÍO. Lo que alguien
acaba de escribir suele ser precisamente la corrección, y pisarla convierte una
comodidad en una trampa.
"""
import itertools

import pytest

from conftest import app_module as A, make_user

_u = itertools.count(1)
_placas = itertools.count(1)


@pytest.fixture
def sesion(client):
    with A.app.app_context():
        uid = make_user(f"af{next(_u)}", role="admin").id
    with client.session_transaction() as sess:
        sess["user_id"] = uid
    return client


@pytest.fixture
def cliente():
    """Un cliente conocido, con el teléfono guardado sin formato.

    Teléfono único por test: la búsqueda devuelve el más antiguo que coincida,
    así que un número fijo haría que el test encontrara a cualquier cliente real
    que ya lo tuviera y fallara por un motivo que no es el suyo. Pasó.
    """
    with A.app.app_context():
        tipo = A.VehicleType.query.first()
        n = next(_placas)
        placa, telefono = f"AFT{n:03d}", f"31055{n:05d}"
        c = A.Client(plate=placa, full_name="Carlos Rivera", phone=telefono,
                     vehicle_type_id=tipo.id if tipo else None)
        A.db.session.add(c)
        A.db.session.commit()
        datos = {"plate": placa, "telefono": telefono, "tipo_id": c.vehicle_type_id}
    yield datos
    with A.app.app_context():
        fila = A.Client.query.get(datos["plate"])
        if fila:
            A.db.session.delete(fila)
            A.db.session.commit()


class TestBuscarPorTelefono:
    """El endpoint que faltaba: había por placa y por nombre, no por teléfono."""

    @pytest.mark.parametrize("formato", [
        "{t}",
        "+57 {t0} {t1} {t2}",
        "{t0}-{t1}-{t2}",
        "({t0}) {t1}{t2}",
        "57{t}",
    ])
    def test_lo_encuentra_escrito_de_cualquier_forma(self, sesion, cliente, formato):
        """El mismo número está guardado de varias maneras según por dónde entró
        —el bot, una cita, el panel—. Comparar literal no encontraría ninguna."""
        t = cliente["telefono"]
        escrito = formato.format(t=t, t0=t[:3], t1=t[3:6], t2=t[6:])
        r = sesion.get(f"/api/clients/by-phone?phone={escrito}")
        datos = r.get_json()
        assert datos["found"] is True
        assert datos["full_name"] == "Carlos Rivera"
        assert datos["plate"] == cliente["plate"]

    def test_un_numero_desconocido_no_inventa_nada(self, sesion, cliente):
        assert sesion.get("/api/clients/by-phone?phone=3009999999").get_json()["found"] is False

    def test_pocos_digitos_no_hacen_match_por_casualidad(self, sesion, cliente):
        """Con tres dígitos cualquier cosa coincidiría con alguien."""
        r = sesion.get("/api/clients/by-phone?phone=310")
        assert r.status_code == 400
        assert r.get_json()["found"] is False

    def test_trae_el_tipo_de_vehiculo(self, sesion, cliente):
        """Es la mitad del ahorro: sin tipo el armador está bloqueado."""
        datos = sesion.get(f"/api/clients/by-phone?phone={cliente['telefono']}").get_json()
        assert datos["vehicle_type_id"] == cliente["tipo_id"]


class TestElArmadorPideElTipoPrimero:
    """El precio de cada servicio depende del tipo de vehículo, así que armar la
    cotización antes de elegirlo es cotizar con la tarifa de otro carro."""

    def test_arranca_sin_tipo_elegido(self, sesion):
        cuerpo = sesion.get("/quotes/new").data.decode()
        i = cuerpo.index('id="tipoVeh"')
        # La primera opción del select es la vacía, no un tipo cualquiera.
        assert '<option value="">' in cuerpo[i:i + 400]

    def test_la_pantalla_dice_qué_falta(self, sesion):
        cuerpo = sesion.get("/quotes/new").data.decode()
        assert "Elige el tipo de vehículo para empezar" in cuerpo

    def test_al_editar_llega_con_su_tipo_puesto(self, sesion):
        """El bloqueo es para empezar, no para estorbar al corregir algo."""
        with A.app.app_context():
            tipo = A.VehicleType.query.first()
        r = sesion.post("/quotes/new", data={
            "customer_name": "Laura Ortiz", "ppf_coverage": ["Manijas"],
            "vehicle_type_id": str(tipo.id)}, follow_redirects=False)
        code = r.headers["Location"].rstrip("/").split("/")[-1]
        try:
            cuerpo = sesion.get(f"/quotes/{code}/edit").data.decode()
            assert f'value="{tipo.id}" selected' in cuerpo
        finally:
            with A.app.app_context():
                c = A.Quote.query.filter_by(code=code).first()
                if c:
                    A.db.session.delete(c)
                    A.db.session.commit()
