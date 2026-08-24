"""Tablero de seguimiento: leads y clientes pendientes de contactar.

Existe porque los avisos que ya había (WhatsApp a Diana, campanita) son EVENTOS:
suenan una vez y se van. Nada guardaba "a este todavía hay que llamarlo", así que
un día ocupado se llevaba el cliente por delante.

Las dos propiedades que lo hacen funcionar, y que estos tests protegen:
  • Una persona aparece en UNA sola columna — la más urgente. Si apareciera en
    tres, el tablero sería una lista de duplicados que nadie termina de vaciar.
  • Una tarjeta gestionada se calla, pero VUELVE cuando vence el plazo si la
    condición sigue ahí. Eso es lo que la diferencia de una alerta.
"""
import datetime as dt

import pytest

from conftest import app_module as A
from conftest import login_as, make_user


@pytest.fixture(autouse=True)
def _limpio():
    def borrar():
        with A.app.app_context():
            A.SeguimientoGestion.query.delete()
            for c in A.Conversation.query.filter(A.Conversation.phone.like("+5730011%")).all():
                A.Message.query.filter_by(conversation_id=c.id).delete()
                A.db.session.delete(c)
            for a in A.Appointment.query.filter(A.Appointment.plate.like("SEG%")).all():
                A.db.session.delete(a)
            A.db.session.commit()
    borrar()
    yield
    borrar()


def _conv(tel, **kw):
    datos = dict(phone=tel, profile_name="Cliente Seg", status="En proceso",
                 priority="Alta", bot_active=True, calificacion=4)
    datos.update(kw)
    c = A.Conversation(**datos)
    A.db.session.add(c)
    A.db.session.commit()
    return c


def _msg(conv, direction, hace_dias=0):
    m = A.Message(conversation_id=conv.id, direction=direction, body="hola",
                  created_at=A.bogota_now() - dt.timedelta(days=hace_dias))
    A.db.session.add(m)
    A.db.session.commit()
    return m


def _cita(tel, hace_dias, servicios="Wash Essential", placa="SEG001"):
    vt = A.VehicleType.query.filter_by(is_active=True).first()
    inicio = A.bogota_now() - dt.timedelta(days=hace_dias)
    a = A.Appointment(customer_name="Cliente Seg", plate=placa, phone=tel,
                      services=servicios, start_datetime=inicio,
                      end_datetime=inicio + dt.timedelta(hours=1),
                      vehicle_type_id=vt.id, status="completed")
    A.db.session.add(a)
    A.db.session.commit()
    return a


def _columna(tablero, clave):
    return next(c for c in tablero["columnas"] if c["clave"] == clave)


class TestColumnas:
    def test_sin_responder_cuando_el_bot_esta_pausado(self):
        """La fuga más cara: ya escribió y nadie contestó."""
        c = _conv("+573001100001", bot_active=False)
        _msg(c, "in", hace_dias=2)

        col = _columna(A._tablero_seguimiento(), "sin_responder")
        assert [t["telefono"] for t in col["tarjetas"]] == ["+573001100001"]
        assert col["tarjetas"][0]["dias"] == 2

    def test_si_ya_le_respondieron_no_aparece(self):
        c = _conv("+573001100002", bot_active=False)
        _msg(c, "in", hace_dias=2)
        _msg(c, "out", hace_dias=1)

        col = _columna(A._tablero_seguimiento(), "sin_responder")
        assert col["tarjetas"] == []

    def test_caliente_sin_cita(self):
        _conv("+573001100003", priority="Alta", status="En proceso")
        col = _columna(A._tablero_seguimiento(), "caliente")
        assert "+573001100003" in [t["telefono"] for t in col["tarjetas"]]

    def test_con_cita_agendada_sale_del_tablero(self):
        """Si ya agendó, perseguirlo es ruido — y peor, hace desconfiar del panel."""
        _conv("+573001100004", priority="Alta", status="Cita agendada")
        col = _columna(A._tablero_seguimiento(), "caliente")
        assert "+573001100004" not in [t["telefono"] for t in col["tarjetas"]]

    def test_ceramico_cumple_el_trimestre(self):
        _cita("+573001100005", hace_dias=95, servicios="Coating Ceramico 9H", placa="SEG005")
        col = _columna(A._tablero_seguimiento(), "ceramico_mant")
        assert "+573001100005" in [t["telefono"] for t in col["tarjetas"]]

    def test_ceramico_reciente_no_aparece(self):
        _cita("+573001100006", hace_dias=30, servicios="Coating Ceramico 9H", placa="SEG006")
        col = _columna(A._tablero_seguimiento(), "ceramico_mant")
        assert col["tarjetas"] == []

    def test_lavada_premium_pasadas_las_4_semanas(self):
        """Cadencia del negocio: lavada premium cada 3-4 semanas."""
        _cita("+573001100007", hace_dias=40, servicios="Coating Ceramico 9H", placa="SEG007")
        tablero = A._tablero_seguimiento()
        # A 40 días todavía no cumple el trimestre, así que cae en lavada.
        assert "+573001100007" in [t["telefono"] for t in _columna(tablero, "lavada_premium")["tarjetas"]]

    def test_cliente_dormido_a_los_3_meses(self):
        _cita("+573001100008", hace_dias=100, placa="SEG008")
        col = _columna(A._tablero_seguimiento(), "dormido")
        assert "+573001100008" in [t["telefono"] for t in col["tarjetas"]]

    def test_cliente_reciente_no_es_dormido(self):
        _cita("+573001100009", hace_dias=10, placa="SEG009")
        tablero = A._tablero_seguimiento()
        assert tablero["total"] == 0


class TestSinDuplicados:
    def test_una_persona_aparece_en_una_sola_columna(self):
        """Un cliente de cerámico que no viene hace 4 meses califica para tres
        columnas. Verlo tres veces haría el tablero imposible de vaciar."""
        _cita("+573001100010", hace_dias=120, servicios="Coating Ceramico 9H", placa="SEG010")

        tablero = A._tablero_seguimiento()
        apariciones = [c["clave"] for c in tablero["columnas"]
                       for t in c["tarjetas"] if t["telefono"] == "+573001100010"]
        assert len(apariciones) == 1
        assert tablero["total"] == 1

    def test_gana_la_columna_mas_urgente(self):
        """Precedencia: lo de cerámico manda sobre 'dormido' — es una venta
        concreta con motivo concreto, no un 'hace rato no venís'."""
        _cita("+573001100011", hace_dias=120, servicios="Coating Ceramico 9H", placa="SEG011")
        tablero = A._tablero_seguimiento()
        col = [c["clave"] for c in tablero["columnas"]
               for t in c["tarjetas"] if t["telefono"] == "+573001100011"][0]
        assert col == "ceramico_mant"

    def test_sin_responder_le_gana_a_todo(self):
        c = _conv("+573001100012", bot_active=False, priority="Alta")
        _msg(c, "in", hace_dias=1)
        _cita("+573001100012", hace_dias=200, placa="SEG012")

        tablero = A._tablero_seguimiento()
        col = [c2["clave"] for c2 in tablero["columnas"]
               for t in c2["tarjetas"] if t["telefono"] == "+573001100012"][0]
        assert col == "sin_responder"


class TestGestion:
    def test_contactar_esconde_la_tarjeta(self, client):
        login_as(client, make_user("admin_seg", role="admin"))
        _conv("+573001100013", priority="Alta")
        assert A._tablero_seguimiento()["total"] == 1

        r = client.post("/seguimiento/gestionar", json={
            "tipo": "caliente", "telefono": "+573001100013", "accion": "contactado"})

        assert r.get_json()["ok"] is True
        assert A._tablero_seguimiento()["total"] == 0

    def test_la_tarjeta_vuelve_cuando_vence_el_plazo(self):
        """Es la diferencia con una alerta: si no se resolvió de verdad, regresa."""
        _conv("+573001100014", priority="Alta")
        with A.app.app_context():
            A.db.session.add(A.SeguimientoGestion(
                tipo="caliente", telefono="+573001100014", accion="contactado",
                oculta_hasta=A.bogota_now().date() - dt.timedelta(days=1)))
            A.db.session.commit()

        assert A._tablero_seguimiento()["total"] == 1

    def test_posponer_respeta_los_dias_pedidos(self, client):
        login_as(client, make_user("admin_seg2", role="admin"))
        _conv("+573001100015", priority="Alta")

        d = client.post("/seguimiento/gestionar", json={
            "tipo": "caliente", "telefono": "+573001100015",
            "accion": "pospuesto", "dias": 10}).get_json()

        esperado = (A.bogota_now().date() + dt.timedelta(days=10)).isoformat()
        assert d["vuelve"] == esperado

    def test_descartar_no_vuelve(self, client):
        login_as(client, make_user("admin_seg3", role="admin"))
        _conv("+573001100016", priority="Alta")

        client.post("/seguimiento/gestionar", json={
            "tipo": "caliente", "telefono": "+573001100016",
            "accion": "descartado", "motivo": "Vendió el carro"})

        assert A._tablero_seguimiento()["total"] == 0
        with A.app.app_context():
            gest = A.SeguimientoGestion.query.filter_by(telefono="+573001100016").first()
            assert gest.oculta_hasta is None
            assert gest.motivo == "Vendió el carro"

    def test_regestionar_corrige_en_vez_de_acumular(self, client):
        """Dos filas para la misma tarjeta se contradirían entre sí."""
        login_as(client, make_user("admin_seg4", role="admin"))
        _conv("+573001100017", priority="Alta")
        for accion in ("contactado", "descartado"):
            client.post("/seguimiento/gestionar", json={
                "tipo": "caliente", "telefono": "+573001100017", "accion": accion})

        with A.app.app_context():
            filas = A.SeguimientoGestion.query.filter_by(telefono="+573001100017").all()
            assert len(filas) == 1
            assert filas[0].accion == "descartado"

    def test_no_toca_el_estado_de_la_conversacion(self, client):
        """Guardar la decisión humana en `status` la borraría Mariana en el
        siguiente turno del cliente."""
        login_as(client, make_user("admin_seg5", role="admin"))
        _conv("+573001100018", priority="Alta", status="En proceso")

        client.post("/seguimiento/gestionar", json={
            "tipo": "caliente", "telefono": "+573001100018", "accion": "descartado"})

        with A.app.app_context():
            assert A.Conversation.query.filter_by(phone="+573001100018").first().status == "En proceso"


class TestAcceso:
    def test_operario_no_entra(self, client):
        login_as(client, make_user("op_seg", role="operario"))
        assert client.get("/seguimiento").status_code == 302

    def test_lider_si_entra(self, client):
        login_as(client, make_user("lider_seg", role="lider"))
        assert client.get("/seguimiento").status_code == 200

    def test_operario_tampoco_puede_gestionar(self, client):
        """Quedan dos capas: el allowlist global OPERARIO_ENDPOINTS lo rebota
        con un 302 antes de llegar a la vista, y la vista igual comprueba el rol.
        Lo que importa es que no escriba nada."""
        login_as(client, make_user("op_seg2", role="operario"))
        r = client.post("/seguimiento/gestionar", json={
            "tipo": "caliente", "telefono": "+573001100019", "accion": "descartado"})

        assert r.status_code in (302, 403)
        with A.app.app_context():
            assert A.SeguimientoGestion.query.filter_by(telefono="+573001100019").first() is None


class TestPantalla:
    def test_muestra_las_tarjetas_y_el_enlace_de_whatsapp(self, client):
        login_as(client, make_user("admin_seg6", role="admin"))
        _cita("+573001100020", hace_dias=95, servicios="Coating Ceramico 9H", placa="SEG020")

        html = client.get("/seguimiento").get_data(as_text=True)

        assert "Cerámico por mantener" in html
        assert "wa.me/573001100020" in html
        assert "mantenimiento" in html    # el mensaje sugerido va precargado

    def test_tablero_vacio_lo_dice_claro(self, client):
        login_as(client, make_user("admin_seg7", role="admin"))
        html = client.get("/seguimiento").get_data(as_text=True)
        assert "Todo al día" in html


class TestFechas:
    """`updated_at` y `Message.created_at` se guardan en UTC; `start_datetime`
    de las citas, en hora de Bogotá. Restar una contra la otra daba cinco horas
    de desfase y las tarjetas recientes mostraban "hace -1 día(s)"."""

    def test_los_dias_nunca_son_negativos(self):
        import datetime as _dt
        c = _conv("+573001100030", bot_active=False)
        # Mensaje de hace un rato, guardado en UTC como hace la app
        A.db.session.add(A.Message(conversation_id=c.id, direction="in", body="hola",
                                   created_at=_dt.datetime.utcnow()))
        A.db.session.commit()

        col = _columna(A._tablero_seguimiento(), "sin_responder")
        assert col["tarjetas"][0]["dias"] >= 0

    def test_esperando_va_a_su_columna_y_no_a_caliente(self):
        """Un lead 'Esperando' ya agotó los seguimientos de Mariana: su
        conversación es otra. Antes lo capturaba 'Caliente' primero."""
        _conv("+573001100031", status="Esperando", priority="Media", followup_count=4)

        tablero = A._tablero_seguimiento()
        columnas = [c["clave"] for c in tablero["columnas"]
                    for t in c["tarjetas"] if t["telefono"] == "+573001100031"]
        assert columnas == ["enfriado"]


class TestEscribirNoCierraLaVenta:
    """Escribirle a alguien no es cerrar la venta. El botón de WhatsApp escondía
    la tarjeta, y eso hacía perder de vista justo a quien ya mostró interés —
    el peor momento para dejar de verlo."""

    def test_escribir_deja_la_tarjeta_en_el_tablero(self, client):
        login_as(client, make_user("admin_esc", role="admin"))
        _conv("+573001100040", priority="Alta")

        client.post("/seguimiento/gestionar", json={
            "tipo": "caliente", "telefono": "+573001100040", "accion": "escrito"})

        assert A._tablero_seguimiento()["total"] == 1

    def test_pone_el_sello_para_no_escribir_dos_veces(self, client):
        login_as(client, make_user("admin_esc2", role="admin"))
        _conv("+573001100041", priority="Alta")
        client.post("/seguimiento/gestionar", json={
            "tipo": "caliente", "telefono": "+573001100041", "accion": "escrito"})

        col = _columna(A._tablero_seguimiento(), "caliente")
        tarjeta = next(t for t in col["tarjetas"] if t["telefono"] == "+573001100041")
        assert tarjeta["escrita_hace"] == 0

        html = client.get("/seguimiento").get_data(as_text=True)
        assert "Le escribiste hoy" in html

    def test_agendar_de_verdad_saca_la_tarjeta(self):
        """La confirmación objetiva: si tiene una cita por delante, no hay nada
        que perseguir — y no depende de que alguien marque la tarjeta."""
        _conv("+573001100042", priority="Alta")
        assert A._tablero_seguimiento()["total"] == 1

        vt = A.VehicleType.query.filter_by(is_active=True).first()
        inicio = A.bogota_now() + dt.timedelta(days=2)
        A.db.session.add(A.Appointment(
            customer_name="Cliente Seg", plate="SEG042", phone="+573001100042",
            services="Wash Essential", start_datetime=inicio,
            end_datetime=inicio + dt.timedelta(hours=1),
            vehicle_type_id=vt.id, status="scheduled"))
        A.db.session.commit()

        assert A._tablero_seguimiento()["total"] == 0

    def test_una_cita_vieja_no_saca_la_tarjeta(self):
        """Solo cuenta la cita por delante: una de hace meses es justamente el
        motivo por el que la tarjeta existe."""
        _cita("+573001100043", hace_dias=120, placa="SEG043")
        assert A._tablero_seguimiento()["total"] == 1


class TestReactivar:
    def test_devuelve_al_tablero_una_tarjeta_ocultada_por_error(self, client):
        login_as(client, make_user("admin_react", role="admin"))
        _conv("+573001100044", priority="Alta")
        client.post("/seguimiento/gestionar", json={
            "tipo": "caliente", "telefono": "+573001100044", "accion": "contactado"})
        assert A._tablero_seguimiento()["total"] == 0

        client.post("/seguimiento/gestionar", json={
            "tipo": "caliente", "telefono": "+573001100044", "accion": "reactivar"})

        assert A._tablero_seguimiento()["total"] == 1
        with A.app.app_context():
            assert A.SeguimientoGestion.query.filter_by(telefono="+573001100044").first() is None

    def test_las_ocultas_se_pueden_listar(self, client):
        login_as(client, make_user("admin_react2", role="admin"))
        _conv("+573001100045", priority="Alta")
        client.post("/seguimiento/gestionar", json={
            "tipo": "caliente", "telefono": "+573001100045",
            "accion": "descartado", "motivo": "Vendió el carro"})

        html = client.get("/seguimiento?ocultas=1").get_data(as_text=True)
        assert "+573001100045" in html
        assert "Vendió el carro" in html
        assert "Reactivar" in html


class TestFiltroLeadsClientes:
    """Leads y clientes son dos conversaciones distintas: a uno hay que
    convencerlo, al otro hacerlo volver."""

    def test_quien_ya_compro_es_cliente(self):
        _cita("+573001100050", hace_dias=100, placa="SEG050")

        tablero = A._tablero_seguimiento()
        tarjeta = next(t for c in tablero["columnas"] for t in c["tarjetas"]
                       if t["telefono"] == "+573001100050")
        assert tarjeta["es_cliente"] is True

    def test_quien_nunca_compro_es_lead(self):
        _conv("+573001100051", priority="Alta")

        tablero = A._tablero_seguimiento()
        tarjeta = next(t for c in tablero["columnas"] for t in c["tarjetas"]
                       if t["telefono"] == "+573001100051")
        assert tarjeta["es_cliente"] is False

    def test_se_decide_por_persona_y_no_por_columna(self):
        """Un cliente que escribe y nadie le contesta cae en "Sin responder",
        que es una columna de leads — pero sigue siendo seguimiento de cliente."""
        c = _conv("+573001100052", bot_active=False)
        _msg(c, "in", hace_dias=1)
        _cita("+573001100052", hace_dias=200, placa="SEG052")

        tablero = A._tablero_seguimiento()
        col = _columna(tablero, "sin_responder")
        tarjeta = next(t for t in col["tarjetas"] if t["telefono"] == "+573001100052")
        assert tarjeta["es_cliente"] is True

    def test_los_totales_cuadran(self):
        _conv("+573001100053", priority="Alta")
        _cita("+573001100054", hace_dias=100, placa="SEG054")

        t = A._tablero_seguimiento()
        assert t["total_leads"] + t["total_clientes"] == t["total"]
        assert t["total_leads"] >= 1
        assert t["total_clientes"] >= 1

    def test_la_pantalla_trae_el_selector(self, client):
        login_as(client, make_user("admin_filtro", role="admin"))
        _conv("+573001100055", priority="Alta")

        html = client.get("/seguimiento").get_data(as_text=True)
        assert 'data-filtro="leads"' in html
        assert 'data-filtro="clientes"' in html
        assert 'data-grupo="leads"' in html
