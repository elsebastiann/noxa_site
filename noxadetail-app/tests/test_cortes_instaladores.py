"""Cortes con instaladores: cerrar cuentas por los polarizados y PPF de un tercero.

La liquidación por periodo ya existía, pero es un informe: se recalcula cada vez
que se abre y no sabe qué se pagó. Un corte es un hecho — estos trabajos, esta
plata, este día.

Lo que estos tests fijan:
  • El corte cobra SOLO lo tercerizado: el lavado de la misma cita no entra.
  • Se ve el descuento y de dónde salió.
  • Un trabajo ya cortado no vuelve a aparecer como pendiente.
  • Los números quedan congelados: editar la cita después no mueve el corte.
"""
import datetime as dt

import pytest

from conftest import app_module as A
from conftest import login_as, make_user


@pytest.fixture
def catalogo():
    """Un polarizado tercerizado, un lavado propio y dos instaladores."""
    with A.app.app_context():
        vt = A.VehicleType.query.filter_by(is_active=True).first()

        polarizado = A.Service(name="Polarizado Corte", duration_minutes=120,
                               is_active=True, is_outsourced=True,
                               default_installer_share=65)
        ppf = A.Service(name="PPF Corte", duration_minutes=180, is_active=True,
                        is_outsourced=True, default_installer_share=65)
        lavado = A.Service(name="Lavado Corte", duration_minutes=60, is_active=True)
        uno = A.Installer(name="Instalador Corte A", default_share=65)
        dos = A.Installer(name="Instalador Corte B", default_share=50)
        A.db.session.add_all([polarizado, ppf, lavado, uno, dos])
        A.db.session.commit()

        A.db.session.add_all([
            A.ServicePrice(service_id=polarizado.id, vehicle_type_id=vt.id,
                           price=1_000_000, duration_minutes=120, is_active=True),
            A.ServicePrice(service_id=ppf.id, vehicle_type_id=vt.id,
                           price=2_000_000, duration_minutes=180, is_active=True),
            A.ServicePrice(service_id=lavado.id, vehicle_type_id=vt.id,
                           price=100_000, duration_minutes=60, is_active=True),
        ])
        A.db.session.commit()
        ids = {"vt": vt.id, "polarizado": polarizado.id, "ppf": ppf.id,
               "lavado": lavado.id, "uno": uno.id, "dos": dos.id}

    yield ids

    with A.app.app_context():
        A.ServicePrice.query.filter(
            A.ServicePrice.service_id.in_([ids["polarizado"], ids["ppf"], ids["lavado"]])
        ).delete(synchronize_session=False)
        A.Service.query.filter(
            A.Service.id.in_([ids["polarizado"], ids["ppf"], ids["lavado"]])
        ).delete(synchronize_session=False)
        A.Installer.query.filter(
            A.Installer.id.in_([ids["uno"], ids["dos"]])
        ).delete(synchronize_session=False)
        A.db.session.commit()


@pytest.fixture(autouse=True)
def _limpiar():
    """Los cortes y las citas de prueba no los borra el conftest, y sobreviven
    al test que los creó: el siguiente vería pendientes que no son suyos."""
    yield
    with A.app.app_context():
        A.InstallerCutLine.query.delete()
        A.InstallerCut.query.delete()
        for appt in A.Appointment.query.filter(A.Appointment.plate.like("COR%")).all():
            A.db.session.delete(appt)
        A.db.session.commit()


def _cita(ids, servicios, outsourcings=(), adjustments=(), placa="COR001", dias=1):
    inicio = dt.datetime.combine(A.bogota_now().date() + dt.timedelta(days=dias),
                                 dt.time(9, 0))
    appt = A.Appointment(
        customer_name="Cliente Corte", plate=placa, services=servicios,
        start_datetime=inicio, end_datetime=inicio + dt.timedelta(hours=2),
        vehicle_type_id=ids["vt"], status="scheduled",
    )
    A.db.session.add(appt)
    A.db.session.commit()
    for o in outsourcings:
        A.db.session.add(A.AppointmentOutsourcing(appointment_id=appt.id, **o))
    for aj in adjustments:
        A.db.session.add(A.AppointmentAdjustment(appointment_id=appt.id, **aj))
    A.db.session.commit()
    return appt


def _terciarizado(ids, quien="uno", pct=65, servicio="Polarizado Corte"):
    return {"service_name": servicio, "installer_id": ids[quien],
            "installer_pct": pct, "material_por": A.MATERIAL_INSTALADOR}


def _admin(client, nombre="admin_corte"):
    login_as(client, make_user(nombre, role="admin"))


def _crear_corte(client, ids, citas, quien="uno", **extra):
    data = {"installer_id": str(ids[quien]),
            "cita": [str(c.id) for c in citas]}
    data.update(extra)
    return client.post("/cortes-instaladores/nuevo", data=data, follow_redirects=True)


def _ultimo_corte():
    return A.InstallerCut.query.order_by(A.InstallerCut.id.desc()).first()


class TestQueEntraAlCorte:
    def test_solo_entra_lo_tercerizado_no_el_lavado_de_la_misma_cita(self, catalogo, client):
        """Es la razón de ser del módulo: el cliente pagó 1.100.000, pero solo
        1.000.000 son del instalador. Cobrarle el lavado sería regalarle
        trabajo propio."""
        _admin(client)
        cita = _cita(catalogo, "Polarizado Corte, Lavado Corte",
                     [_terciarizado(catalogo)])

        _crear_corte(client, catalogo, [cita])

        corte = _ultimo_corte()
        assert corte.total_cobrado == 1_000_000     # NO 1.100.000
        assert corte.total_costo == 650_000
        assert len(corte.lines) == 1

    def test_la_pantalla_de_seleccion_tampoco_suma_el_lavado(self, catalogo, client):
        """El total por cita que se lee al marcar sale por otro camino que el del
        corte guardado: se calcula para la pantalla y no pasa por las líneas.

        Sin este test se puede romper el número que el usuario mira para decidir
        —que es justo lo que pidió ver— sin que nada más falle."""
        _admin(client)
        _cita(catalogo, "Polarizado Corte, Lavado Corte", [_terciarizado(catalogo)])

        with A.app.app_context():
            ofrecidas = A._trabajos_cortables(catalogo["uno"])

        assert len(ofrecidas) == 1
        assert ofrecidas[0]["cobrado"] == 1_000_000    # NO 1.100.000
        assert ofrecidas[0]["lista"] == 1_000_000
        assert ofrecidas[0]["costo"] == 650_000

    def test_solo_entran_las_lineas_del_instalador_elegido(self, catalogo, client):
        """Una cita puede traer el polarizado de uno y el PPF de otro. Cortarle
        a A no puede arrastrar lo de B."""
        _admin(client)
        cita = _cita(catalogo, "Polarizado Corte, PPF Corte", [
            _terciarizado(catalogo, "uno"),
            _terciarizado(catalogo, "dos", pct=50, servicio="PPF Corte"),
        ])

        _crear_corte(client, catalogo, [cita], quien="uno")

        corte = _ultimo_corte()
        assert [l.servicio for l in corte.lines] == ["Polarizado Corte"]
        assert corte.total_costo == 650_000

    def test_lo_que_instalo_noxa_no_genera_corte(self, catalogo, client):
        """Sin comisión no hay cuenta por pagar: en un corte solo estorba."""
        _admin(client)
        _cita(catalogo, "Polarizado Corte", [
            {"service_name": "Polarizado Corte", "installer_id": None,
             "installer_pct": 0, "material_por": A.MATERIAL_NOXA},
        ])

        with A.app.app_context():
            assert A._trabajos_cortables(catalogo["uno"]) == []

    def test_las_citas_canceladas_no_entran(self, catalogo, client):
        _admin(client)
        cita = _cita(catalogo, "Polarizado Corte", [_terciarizado(catalogo)])
        cita.status = "cancelled"
        A.db.session.commit()

        with A.app.app_context():
            assert A._trabajos_cortables(catalogo["uno"]) == []

    def test_el_rango_de_fechas_filtra_lo_que_se_ofrece(self, catalogo, client):
        _admin(client)
        _cita(catalogo, "Polarizado Corte", [_terciarizado(catalogo)],
              placa="COR001", dias=1)
        _cita(catalogo, "Polarizado Corte", [_terciarizado(catalogo)],
              placa="COR002", dias=30)

        hoy = A.bogota_now().date()
        with A.app.app_context():
            solo_cerca = A._trabajos_cortables(
                catalogo["uno"], hoy, hoy + dt.timedelta(days=10))
        assert [t["placa"] for t in solo_cerca] == ["COR001"]


class TestDescuentos:
    def test_el_corte_muestra_el_descuento_y_su_motivo(self, catalogo, client):
        """Sin el motivo, el instalador ve un cobrado más bajo que la lista y no
        hay con qué explicárselo."""
        _admin(client)
        cita = _cita(catalogo, "Polarizado Corte", [_terciarizado(catalogo)],
                     adjustments=[{"kind": "discount", "mode": "fixed",
                                   "value": 200_000,
                                   "description": "Promo lanzamiento"}])

        _crear_corte(client, catalogo, [cita])

        corte = _ultimo_corte()
        assert corte.total_lista == 1_000_000
        assert corte.total_cobrado == 800_000
        assert corte.total_descuento == 200_000
        # La descripción va sola: la pantalla ya pone "Descuento de $200.000"
        # al lado, y repetir la palabra da "Descuento de … — Descuento: …".
        assert corte.lines[0].motivo == "Promo lanzamiento"

    def test_el_instalador_cobra_sobre_lo_realmente_pagado(self, catalogo, client):
        """No puede llevarse el 65% de una plata que nunca entró."""
        _admin(client)
        cita = _cita(catalogo, "Polarizado Corte", [_terciarizado(catalogo)],
                     adjustments=[{"kind": "discount", "mode": "fixed",
                                   "value": 200_000}])

        _crear_corte(client, catalogo, [cita])

        corte = _ultimo_corte()
        assert corte.total_costo == 520_000          # 65% de 800.000, no de 1.000.000
        assert corte.queda_noxa == 280_000

    def test_sin_descuento_el_corte_no_inventa_uno(self, catalogo, client):
        _admin(client)
        cita = _cita(catalogo, "Polarizado Corte", [_terciarizado(catalogo)])

        _crear_corte(client, catalogo, [cita])

        corte = _ultimo_corte()
        assert corte.total_descuento == 0
        assert not corte.lines[0].motivo

    def test_un_recargo_se_ve_como_descuento_negativo(self, catalogo, client):
        """Un recargo sube lo cobrado; esconderlo en un cero perdería plata."""
        _admin(client)
        cita = _cita(catalogo, "Polarizado Corte", [_terciarizado(catalogo)],
                     adjustments=[{"kind": "surcharge", "mode": "fixed",
                                   "value": 100_000, "description": "Vidrio extra"}])

        _crear_corte(client, catalogo, [cita])

        corte = _ultimo_corte()
        assert corte.total_cobrado == 1_100_000
        assert corte.total_descuento == -100_000

    def test_el_descuento_de_convenio_tambien_queda_explicado(self, catalogo, client):
        """El convenio rebaja lo cobrado sin dejar rastro de ajuste en la cita,
        así que es el descuento más fácil de ver como un error de digitación.

        Va sobre PPF y no sobre polarizado a propósito: el polarizado está
        excluido de convenio en el catálogo (AGREEMENT_EXCLUDED_KEYWORDS)."""
        _admin(client)
        with A.app.app_context():
            convenio = A.Agreement(name="Convenio Corte", discount_type="percentage",
                                   value=10, is_active=True)
            A.db.session.add(convenio)
            A.db.session.commit()
            convenio_id = convenio.id

        cita = _cita(catalogo, "PPF Corte",
                     [_terciarizado(catalogo, servicio="PPF Corte")])
        cita.agreement_id = convenio_id
        A.db.session.commit()

        _crear_corte(client, catalogo, [cita])

        corte = _ultimo_corte()
        assert corte.total_lista == 2_000_000
        assert corte.total_cobrado == 1_800_000
        assert corte.total_descuento == 200_000
        assert "Convenio Corte" in corte.lines[0].motivo

        with A.app.app_context():
            A.Agreement.query.filter_by(id=convenio_id).delete()
            A.db.session.commit()


class TestNoPagarDosVeces:
    def test_un_trabajo_ya_cortado_no_vuelve_a_aparecer(self, catalogo, client):
        """Es la única defensa real contra pagar dos veces el mismo polarizado."""
        _admin(client)
        cita = _cita(catalogo, "Polarizado Corte", [_terciarizado(catalogo)])

        with A.app.app_context():
            assert len(A._trabajos_cortables(catalogo["uno"])) == 1

        _crear_corte(client, catalogo, [cita])

        with A.app.app_context():
            assert A._trabajos_cortables(catalogo["uno"]) == []

    def test_mandar_la_misma_cita_dos_veces_no_crea_el_segundo_corte(self, catalogo, client):
        """Dos pestañas abiertas, o un doble clic: el segundo POST no puede
        volver a cobrar lo mismo."""
        _admin(client)
        cita = _cita(catalogo, "Polarizado Corte", [_terciarizado(catalogo)])

        _crear_corte(client, catalogo, [cita])
        _crear_corte(client, catalogo, [cita])

        with A.app.app_context():
            assert A.InstallerCut.query.count() == 1

    def test_borrar_el_corte_devuelve_los_trabajos(self, catalogo, client):
        """Es el único camino de vuelta cuando se arma con la cita equivocada."""
        _admin(client)
        cita = _cita(catalogo, "Polarizado Corte", [_terciarizado(catalogo)])
        _crear_corte(client, catalogo, [cita])
        corte_id = _ultimo_corte().id

        client.post(f"/cortes-instaladores/{corte_id}/borrar", follow_redirects=True)

        with A.app.app_context():
            assert A.InstallerCut.query.count() == 0
            assert A.InstallerCutLine.query.count() == 0      # se va con el corte
            assert len(A._trabajos_cortables(catalogo["uno"])) == 1

    def test_la_segunda_cita_si_puede_cortarse_despues(self, catalogo, client):
        """Cortar una no puede bloquear las demás."""
        _admin(client)
        una = _cita(catalogo, "Polarizado Corte", [_terciarizado(catalogo)],
                    placa="COR001")
        otra = _cita(catalogo, "Polarizado Corte", [_terciarizado(catalogo)],
                     placa="COR002")

        _crear_corte(client, catalogo, [una])
        with A.app.app_context():
            pendientes = A._trabajos_cortables(catalogo["uno"])
        assert [t["appointment_id"] for t in pendientes] == [otra.id]


class TestLosNumerosQuedanCongelados:
    def test_editar_el_descuento_despues_no_mueve_el_corte(self, catalogo, client):
        """Un corte ya cuadrado con el instalador no puede cambiar solo porque
        alguien edite la cita tres semanas después."""
        _admin(client)
        cita = _cita(catalogo, "Polarizado Corte", [_terciarizado(catalogo)])
        _crear_corte(client, catalogo, [cita])
        corte_id = _ultimo_corte().id

        A.db.session.add(A.AppointmentAdjustment(
            appointment_id=cita.id, kind="discount", mode="fixed", value=500_000))
        A.db.session.commit()

        with A.app.app_context():
            corte = A.InstallerCut.query.get(corte_id)
            assert corte.total_cobrado == 1_000_000
            assert corte.total_costo == 650_000

    def test_el_corte_sobrevive_a_que_se_borre_la_cita(self, catalogo, client):
        """La plata salió igual: perder el corte al borrar la cita dejaría al
        instalador cobrado sin respaldo."""
        _admin(client)
        cita = _cita(catalogo, "Polarizado Corte", [_terciarizado(catalogo)])
        _crear_corte(client, catalogo, [cita])
        corte_id = _ultimo_corte().id

        A.db.session.delete(cita)
        A.db.session.commit()

        with A.app.app_context():
            corte = A.InstallerCut.query.get(corte_id)
            assert corte is not None
            assert corte.total_costo == 650_000

    def test_el_total_del_corte_es_la_suma_de_sus_lineas(self, catalogo, client):
        _admin(client)
        una = _cita(catalogo, "Polarizado Corte", [_terciarizado(catalogo)],
                    placa="COR001")
        otra = _cita(catalogo, "PPF Corte",
                     [_terciarizado(catalogo, servicio="PPF Corte")], placa="COR002")

        _crear_corte(client, catalogo, [una, otra])

        corte = _ultimo_corte()
        assert corte.total_cobrado == 3_000_000
        assert corte.total_costo == sum(l.costo for l in corte.lines)
        assert corte.total_costo == 1_950_000


class TestPagoYPantallas:
    def test_nace_pendiente_de_pago(self, catalogo, client):
        """El corte se arma cuando se cuadra y se paga después, a veces días
        después."""
        _admin(client)
        cita = _cita(catalogo, "Polarizado Corte", [_terciarizado(catalogo)])

        _crear_corte(client, catalogo, [cita])

        assert _ultimo_corte().pagado is False

    def test_se_puede_marcar_pagado_y_devolverlo_a_pendiente(self, catalogo, client):
        _admin(client)
        cita = _cita(catalogo, "Polarizado Corte", [_terciarizado(catalogo)])
        _crear_corte(client, catalogo, [cita])
        corte_id = _ultimo_corte().id

        client.post(f"/cortes-instaladores/{corte_id}/pagar",
                    data={"paid_on": A.bogota_today().isoformat()},
                    follow_redirects=True)
        with A.app.app_context():
            assert A.InstallerCut.query.get(corte_id).pagado is True

        client.post(f"/cortes-instaladores/{corte_id}/pagar",
                    data={"deshacer": "1"}, follow_redirects=True)
        with A.app.app_context():
            assert A.InstallerCut.query.get(corte_id).pagado is False

    def test_se_puede_nacer_pagado_de_una(self, catalogo, client):
        """Lo normal cuando se paga en el mismo momento en que se cuadra."""
        _admin(client)
        cita = _cita(catalogo, "Polarizado Corte", [_terciarizado(catalogo)])

        _crear_corte(client, catalogo, [cita],
                     paid_on=A.bogota_today().isoformat())

        assert _ultimo_corte().pagado is True

    def test_la_lista_muestra_el_corte_con_sus_totales(self, catalogo, client):
        _admin(client)
        cita = _cita(catalogo, "Polarizado Corte", [_terciarizado(catalogo)])
        _crear_corte(client, catalogo, [cita])

        html = client.get("/cortes-instaladores").get_data(as_text=True)
        assert "Instalador Corte A" in html
        assert "650.000" in html

    def test_el_detalle_muestra_placa_servicio_y_reparto(self, catalogo, client):
        _admin(client)
        cita = _cita(catalogo, "Polarizado Corte", [_terciarizado(catalogo)],
                     adjustments=[{"kind": "discount", "mode": "fixed",
                                   "value": 200_000, "description": "Promo lanzamiento"}])
        _crear_corte(client, catalogo, [cita])

        html = client.get(
            f"/cortes-instaladores/{_ultimo_corte().id}").get_data(as_text=True)
        assert "COR001" in html
        assert "Polarizado Corte" in html
        assert "Promo lanzamiento" in html
        assert "520.000" in html

    def test_la_pantalla_de_armar_ofrece_las_citas_del_instalador(self, catalogo, client):
        _admin(client)
        _cita(catalogo, "Polarizado Corte", [_terciarizado(catalogo)])

        html = client.get(
            f"/cortes-instaladores/nuevo?installer_id={catalogo['uno']}"
        ).get_data(as_text=True)
        assert "COR001" in html
        assert "Polarizado Corte" in html

    def test_sin_marcar_ninguna_cita_no_crea_corte(self, catalogo, client):
        _admin(client)
        _cita(catalogo, "Polarizado Corte", [_terciarizado(catalogo)])

        client.post("/cortes-instaladores/nuevo",
                    data={"installer_id": str(catalogo["uno"])},
                    follow_redirects=True)

        with A.app.app_context():
            assert A.InstallerCut.query.count() == 0

    def test_la_portada_dice_cuanto_falta_por_cortarle_a_cada_uno(self, catalogo, client):
        """Al entrar la pregunta no es qué pagué, sino a quién le debo."""
        _admin(client)
        _cita(catalogo, "Polarizado Corte", [_terciarizado(catalogo)])

        html = client.get("/cortes-instaladores").get_data(as_text=True)
        assert "Pendiente por cortar" in html
        assert "650.000" in html


class TestAcceso:
    @pytest.mark.parametrize("rol", ["operario", "lider", "marketing"])
    def test_solo_el_admin_entra(self, catalogo, client, rol):
        """Es plata que sale: no es pantalla de consulta general."""
        login_as(client, make_user(f"user_{rol}", role=rol))

        for ruta in ("/cortes-instaladores", "/cortes-instaladores/nuevo"):
            resp = client.get(ruta)
            assert resp.status_code == 302

    def test_un_operario_no_puede_crear_un_corte(self, catalogo, client):
        login_as(client, make_user("operario_corte", role="operario"))
        cita = _cita(catalogo, "Polarizado Corte", [_terciarizado(catalogo)])

        _crear_corte(client, catalogo, [cita])

        with A.app.app_context():
            assert A.InstallerCut.query.count() == 0
