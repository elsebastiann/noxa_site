"""La lista de precios como matriz (servicio × tipo de vehículo).

Antes era una fila por combinación, que es la misma matriz aplanada: cuatro
filas para ver un servicio y, peor, los huecos invisibles — un precio que falta
simplemente no tenía fila.

Un hueco no es inofensivo: `calculate_real_price` cuenta como $0 el servicio sin
precio para ese vehículo, así que la cita se factura de menos sin avisar. Por eso
la matriz los marca.
"""
import pytest

from conftest import app_module as A
from conftest import login_as, make_user


@pytest.fixture
def catalogo_precios():
    with A.app.app_context():
        tipos = {}
        for nombre in ("Automovil", "SUV", "Camioneta", "Moto", "Jet Ski"):
            vt = A.VehicleType.query.filter(
                A.db.func.lower(A.VehicleType.name) == nombre.lower()).first()
            if vt is None:
                vt = A.VehicleType(name=nombre, is_active=True)
                A.db.session.add(vt)
                A.db.session.commit()
            vt.is_active = True
            tipos[nombre] = vt.id

        svc = A.Service(name="Polarizado Matriz Test", duration_minutes=120, is_active=True)
        A.db.session.add(svc)
        A.db.session.commit()

        # Precio solo para Automóvil: quedan huecos en SUV, Camioneta y Moto.
        A.db.session.add(A.ServicePrice(
            service_id=svc.id, vehicle_type_id=tipos["Automovil"],
            price=900_000, duration_minutes=120, is_active=True))
        A.db.session.commit()
        ids = {"svc": svc.id, **tipos}

    yield ids

    with A.app.app_context():
        A.ServicePrice.query.filter_by(service_id=ids["svc"]).delete()
        A.Service.query.filter_by(id=ids["svc"]).delete()
        A.db.session.commit()


class TestMatriz:
    def test_un_servicio_es_una_sola_fila(self, catalogo_precios, client):
        login_as(client, make_user("admin_precios", role="admin"))
        html = client.get("/service-prices").get_data(as_text=True)

        # El nombre aparece una vez como fila, no una por tipo de vehículo.
        assert html.count('data-nombre="polarizado matriz test"') == 1

    def test_marca_los_huecos_de_los_tipos_que_se_cobran(self, catalogo_precios, client):
        login_as(client, make_user("admin_precios2", role="admin"))
        html = client.get("/service-prices").get_data(as_text=True)

        # SUV, Camioneta y Moto sin precio; Jet Ski no cuenta como hueco.
        assert 'data-huecos="3"' in html
        assert "poner precio" in html

    def test_jet_ski_no_cuenta_como_hueco(self, catalogo_precios):
        """Que no haya precio de Jet Ski para un polarizado no es un error;
        marcarlo llenaría la pantalla de falsas alarmas."""
        with A.app.app_context():
            assert "jet ski" not in A.VEHICULOS_PRINCIPALES

    def test_agrupa_por_la_misma_categoria_del_formulario(self, catalogo_precios, client):
        """Reusa categoria_de_servicio para no obligar a aprender dos
        organizaciones distintas del mismo catálogo."""
        login_as(client, make_user("admin_precios3", role="admin"))
        html = client.get("/service-prices").get_data(as_text=True)

        assert A.categoria_de_servicio("Polarizado Matriz Test") == "Polarizados"
        assert 'data-cat="Polarizados"' in html


class TestEdicionDeCelda:
    def test_llenar_un_hueco_crea_el_precio(self, catalogo_precios, client):
        """Es la razón de que exista el endpoint aparte: /update exige un
        ServicePrice que ya exista, y el hueco es justo donde no hay fila."""
        login_as(client, make_user("admin_celda", role="admin"))
        r = client.post("/service-prices/cell", json={
            "service_id": catalogo_precios["svc"],
            "vehicle_type_id": catalogo_precios["SUV"],
            "price": 1_050_000,
        })

        assert r.get_json()["ok"] is True
        with A.app.app_context():
            sp = A.ServicePrice.query.filter_by(
                service_id=catalogo_precios["svc"],
                vehicle_type_id=catalogo_precios["SUV"]).first()
            assert sp.price == 1_050_000
            assert sp.is_active is True

    def test_editar_una_celda_existente_no_duplica(self, catalogo_precios, client):
        login_as(client, make_user("admin_celda2", role="admin"))
        for valor in (950_000, 980_000):
            client.post("/service-prices/cell", json={
                "service_id": catalogo_precios["svc"],
                "vehicle_type_id": catalogo_precios["Automovil"],
                "price": valor,
            })

        with A.app.app_context():
            filas = A.ServicePrice.query.filter_by(
                service_id=catalogo_precios["svc"],
                vehicle_type_id=catalogo_precios["Automovil"]).all()
            assert len(filas) == 1
            assert filas[0].price == 980_000

    def test_cambiar_solo_la_duracion_no_borra_el_precio(self, catalogo_precios, client):
        login_as(client, make_user("admin_celda3", role="admin"))
        client.post("/service-prices/cell", json={
            "service_id": catalogo_precios["svc"],
            "vehicle_type_id": catalogo_precios["Automovil"],
            "duration_minutes": 180,
        })

        with A.app.app_context():
            sp = A.ServicePrice.query.filter_by(
                service_id=catalogo_precios["svc"],
                vehicle_type_id=catalogo_precios["Automovil"]).first()
            assert sp.duration_minutes == 180
            assert sp.price == 900_000

    def test_un_valor_no_numerico_no_rompe_la_fila(self, catalogo_precios, client):
        login_as(client, make_user("admin_celda4", role="admin"))
        r = client.post("/service-prices/cell", json={
            "service_id": catalogo_precios["svc"],
            "vehicle_type_id": catalogo_precios["Automovil"],
            "price": "carísimo",
        })

        assert r.status_code == 400
        with A.app.app_context():
            sp = A.ServicePrice.query.filter_by(
                service_id=catalogo_precios["svc"],
                vehicle_type_id=catalogo_precios["Automovil"]).first()
            assert sp.price == 900_000   # intacto

    def test_una_celda_nueva_hereda_la_duracion_del_servicio(self, catalogo_precios, client):
        """Un precio con duración 0 hace que la cita no ocupe tiempo en el
        calendario, y al llenar un hueco solo se escribe el precio."""
        login_as(client, make_user("admin_dur", role="admin"))
        client.post("/service-prices/cell", json={
            "service_id": catalogo_precios["svc"],
            "vehicle_type_id": catalogo_precios["Camioneta"],
            "price": 1_100_000,
        })

        with A.app.app_context():
            sp = A.ServicePrice.query.filter_by(
                service_id=catalogo_precios["svc"],
                vehicle_type_id=catalogo_precios["Camioneta"]).first()
            assert sp.duration_minutes == 120   # la del servicio, no 0
