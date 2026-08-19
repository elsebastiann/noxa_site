"""Los avisos al admin no dependen de que el mensaje al cliente salga bien.

Cuando Mariana agenda, mueve una cita o escala, el cambio YA quedó en la
agenda. Si el envío al cliente falla, el admin es justo quien más necesita
enterarse — porque el cliente puede haberse quedado sin la confirmación.
Antes esto hacía `return False` en el bucle de envío y se perdían los tres
avisos, incluida la campanita del panel.
"""
import datetime as dt
from unittest.mock import patch

import pytest

from conftest import app_module as A


@pytest.fixture
def conversacion():
    with A.app.app_context():
        conv = A.Conversation(phone="+573159998877", profile_name="Manu Prueba")
        A.db.session.add(conv)
        A.db.session.commit()
        conv_id = conv.id
    yield conv_id
    with A.app.app_context():
        A.Message.query.filter_by(conversation_id=conv_id).delete()
        A.db.session.delete(A.Conversation.query.get(conv_id))
        A.db.session.commit()


@pytest.fixture
def cita():
    """Cita futura en un día hábil, para que el reagendamiento sea válido."""
    with A.app.app_context():
        vt = A.VehicleType.query.filter_by(is_active=True).first()
        svc = A._diagnostic_service()
        creado = None
        if not svc:
            creado = A.Service(name="Diagnóstico", duration_minutes=30,
                               is_active=True, is_diagnostic=True, occupies_single_day=False)
            A.db.session.add(creado)
            A.db.session.commit()
            svc = creado

        dia = A.bogota_now().date() + dt.timedelta(days=1)
        while not A.es_dia_habil(dia):
            dia += dt.timedelta(days=1)
        inicio = dt.datetime.combine(dia, dt.time(9, 0))

        appt = A.Appointment(
            customer_name="Manu Prueba", plate="QQN399", phone="3159998877",
            services=svc.name, start_datetime=inicio,
            end_datetime=inicio + dt.timedelta(minutes=30),
            vehicle_type_id=vt.id, status="scheduled",
        )
        A.db.session.add(appt)
        A.db.session.commit()
        info = (appt.id, dia, vt.name, creado.id if creado else None)
    yield info
    with A.app.app_context():
        appt = A.Appointment.query.get(info[0])
        if appt:
            A.db.session.delete(appt)
        if info[3]:
            A.db.session.delete(A.Service.query.get(info[3]))
        A.db.session.commit()


def _correr_turno(conv_id, partes, falla_en=None):
    """Corre un turno con el modelo simulado.

    `partes` son los trozos tal como los devuelve get_claude_reply: los
    marcadores ([REAGENDAR:...], [ESCALAR:...]) van como elementos aparte, que
    es como el parser los espera. `falla_en` es el índice del mensaje visible
    cuyo envío al cliente falla (None = todos salen bien).
    """
    enviados = []

    def fake_send(to, body, **kw):
        kind = kw.get("kind")
        visibles = len([e for e in enviados if e["kind"] == "bot_respuesta"])
        enviados.append({"to": to, "body": body, "kind": kind})
        if kind == "bot_respuesta" and falla_en is not None and visibles == falla_en:
            return False, "63016 fuera de la ventana de mensajería"
        return True, ""

    with A.app.app_context():
        conv = A.Conversation.query.get(conv_id)
        with patch.object(A, "send_whatsapp", side_effect=fake_send), \
             patch.object(A, "get_claude_reply", return_value=list(partes)), \
             patch.object(A, "push_notification") as campanita, \
             patch.dict(A.os.environ, {"ADMIN_WHATSAPP": "+573001112233"}):
            ok = A._generate_and_send_reply(conv, conv.phone)
    return ok, enviados, campanita


def _kinds(enviados):
    return [e["kind"] for e in enviados]


class TestAvisoDeReagendamiento:
    def _partes(self, cita, hora="11:00"):
        _appt_id, dia, _vt, _ = cita
        nuevo = dia + dt.timedelta(days=1)
        while not A.es_dia_habil(nuevo):
            nuevo += dt.timedelta(days=1)
        return [
            "Listo, ya te la moví.",
            f"[REAGENDAR: placa=QQN399; fecha={nuevo.isoformat()}; hora={hora}]",
        ]

    def test_avisa_aunque_falle_el_envio_al_cliente(self, conversacion, cita):
        """El caso visto en producción: la cita se movió, el envío al cliente
        falló y Diana no se enteró de nada — ni por WhatsApp ni por campanita."""
        ok, enviados, campanita = _correr_turno(
            conversacion, self._partes(cita), falla_en=0
        )

        assert "admin_cita_movida" in _kinds(enviados), (
            f"no se avisó del reagendamiento al admin; solo salió: {_kinds(enviados)}"
        )
        assert campanita.called, "tampoco quedó la campanita en el panel"
        # Se sigue reportando el turno como fallido para que el webhook reintente.
        assert ok is False

    def test_avisa_cuando_todo_sale_bien(self, conversacion, cita):
        ok, enviados, campanita = _correr_turno(conversacion, self._partes(cita, "14:00"))

        assert ok is True
        assert "admin_cita_movida" in _kinds(enviados)
        assert campanita.called

    def test_la_cita_queda_movida_en_la_agenda(self, conversacion, cita):
        appt_id, _dia, _vt, _ = cita
        _correr_turno(conversacion, self._partes(cita, "15:00"))
        with A.app.app_context():
            assert A.Appointment.query.get(appt_id).start_datetime.strftime("%H:%M") == "15:00"


class TestAvisoDeEscalamiento:
    def test_escala_aunque_falle_el_envio_al_cliente(self, conversacion):
        partes = ["Dame un momento, ya te conecto con un asesor.",
                  "[ESCALAR: el cliente quiere pagar]"]
        ok, enviados, _ = _correr_turno(conversacion, partes, falla_en=0)

        assert "admin_escalacion" in _kinds(enviados), (
            "un fallo de envío dejaba al cliente esperando y al admin sin aviso"
        )
        assert ok is False

    def test_el_bot_queda_pausado(self, conversacion):
        partes = ["Ya te conecto.", "[ESCALAR: pide hablar con un humano]"]
        _correr_turno(conversacion, partes, falla_en=0)
        with A.app.app_context():
            assert A.Conversation.query.get(conversacion).bot_active is False


class TestEnvioNormal:
    def test_sin_fallos_no_se_marca_el_turno_como_fallido(self, conversacion):
        ok, enviados, _ = _correr_turno(conversacion, ["Hola, ¿en qué te ayudo?"])
        assert ok is True
        assert _kinds(enviados).count("bot_respuesta") == 1

    def test_un_fallo_corta_el_resto_de_mensajes_al_cliente(self, conversacion):
        """Si el primero no salió, encimarle los siguientes solo empeora el hilo."""
        ok, enviados, _ = _correr_turno(
            conversacion, ["Primero", "Segundo", "Tercero"], falla_en=0
        )
        assert ok is False
        assert _kinds(enviados).count("bot_respuesta") == 1


class TestTagDeReagendado:
    """Un cliente que ya tenía cita y escribe para moverla no es un lead del
    embudo de ventas: se marca "Reagendado" y no "Diagnóstico agendado"."""

    def _partes(self, cita):
        _appt_id, dia, _vt, _ = cita
        nuevo = dia + dt.timedelta(days=1)
        while not A.es_dia_habil(nuevo):
            nuevo += dt.timedelta(days=1)
        return ["Listo, ya te la moví.",
                f"[REAGENDAR: placa=QQN399; fecha={nuevo.isoformat()}; hora=16:00]"]

    def test_marca_la_conversacion_como_reagendado(self, conversacion, cita):
        _correr_turno(conversacion, self._partes(cita))
        with A.app.app_context():
            assert A.Conversation.query.get(conversacion).status == "Reagendado"

    def test_gana_sobre_el_meta_del_modelo(self, conversacion, cita):
        """La agenda real manda: si el modelo insiste con otro estado, se ignora."""
        partes = self._partes(cita) + ["[META: estado=Diagnóstico agendado; servicios=Cerámico]"]
        _correr_turno(conversacion, partes)
        with A.app.app_context():
            assert A.Conversation.query.get(conversacion).status == "Reagendado"

    def test_reagendado_cuenta_como_lead_con_cita(self):
        """Si se olvida en esta tupla, el job de seguimiento vuelve a perseguir a
        alguien que acaba de confirmar hora, y las analíticas lo dejan de contar."""
        assert "Reagendado" in A.ESTADOS_CON_CITA
        # A propósito NO está en LEAD_STATES: no es una etapa del embudo de ventas
        # que el filtro del panel deba ofrecer aparte — en el panel se ve con el
        # mismo color que "Cita agendada" (ver status_pill_class en whatsapp.html).
        assert "Reagendado" not in A.LEAD_STATES

    def test_el_job_de_seguimiento_no_lo_persigue(self, conversacion, cita):
        _correr_turno(conversacion, self._partes(cita))
        with A.app.app_context():
            perseguibles = A.Conversation.query.filter(
                A.Conversation.status.notin_(A.ESTADOS_CON_CITA),
                A.Conversation.id == conversacion,
            ).count()
        assert perseguibles == 0, "un cliente que acaba de reagendar entraría al seguimiento"

    def test_el_tag_sobrevive_al_turno_siguiente(self, conversacion, cita):
        """En el turno siguiente el modelo vuelve a emitir su [META:] de siempre.
        Si eso pisa el estado, el tag dura un solo mensaje y no sirve de nada."""
        _correr_turno(conversacion, self._partes(cita))
        _correr_turno(conversacion, ["Con gusto, nos vemos.",
                                     "[META: estado=Diagnóstico agendado; servicios=Cerámico]"])
        with A.app.app_context():
            assert A.Conversation.query.get(conversacion).status == "Reagendado"


class TestCalificacionDeLead:
    """carro/marca/calificacion son campos nuevos del [META:] — cubren tanto el
    parseo como que un marcador sin ellos (formato viejo, o un turno donde el
    modelo los olvida) siga reconociéndose como [META:] y no se le cuele al
    cliente como mensaje visible."""

    def test_guarda_carro_marca_y_calificacion(self, conversacion):
        _correr_turno(conversacion, [
            "Con gusto, te cuento.",
            "[META: estado=En proceso; servicios=Cerámico; carro=BMW M240i 2022; marca=BMW; calificacion=5]",
        ])
        with A.app.app_context():
            conv = A.Conversation.query.get(conversacion)
            assert conv.carro == "BMW M240i 2022"
            assert conv.marca == "BMW"
            assert conv.calificacion == 5
            assert conv.priority == "Alta"

    def test_formato_viejo_sin_carro_marca_ni_calificacion_no_se_filtra_al_cliente(self, conversacion):
        """Antes de tolerar el formato viejo, este [META:] sin los campos nuevos
        no matcheaba _META_RE y se mandaba tal cual al cliente como si fuera un
        mensaje normal — justo lo que un marcador interno nunca debe hacer."""
        ok, enviados, _ = _correr_turno(conversacion, [
            "Claro que sí.",
            "[META: estado=En proceso; servicios=Cerámico]",
        ])
        assert ok is True
        visibles = [e["body"] for e in enviados if e["kind"] == "bot_respuesta"]
        assert visibles == ["Claro que sí."], (
            f"el marcador [META:] sin carro/marca/calificacion se coló como mensaje visible: {visibles}"
        )
        with A.app.app_context():
            conv = A.Conversation.query.get(conversacion)
            assert conv.carro == ""
            assert conv.marca == ""
            assert conv.calificacion is None

    def test_marca_no_reconocida_se_ignora_y_no_rompe_el_turno(self, conversacion):
        ok, enviados, _ = _correr_turno(conversacion, [
            "Listo.",
            "[META: estado=En proceso; servicios=; carro=Lada Niva 1990; marca=Lada; calificacion=1]",
        ])
        assert ok is True
        with A.app.app_context():
            conv = A.Conversation.query.get(conversacion)
            assert conv.marca == ""
            assert conv.calificacion == 1  # la calificación sí es válida aunque la marca no

    def test_calificacion_fuera_de_rango_se_ignora(self, conversacion):
        ok, enviados, _ = _correr_turno(conversacion, [
            "Listo.",
            "[META: estado=En proceso; servicios=; carro=Sin dato; marca=Sin dato; calificacion=9]",
        ])
        assert ok is True
        with A.app.app_context():
            assert A.Conversation.query.get(conversacion).calificacion is None

    def test_estado_no_lo_puede_poner_esperando_directamente(self, conversacion):
        """'Esperando' solo lo pone el job de seguimiento, nunca Mariana en vivo —
        si el modelo lo emite, se ignora como estado no reconocido."""
        _correr_turno(conversacion, [
            "Hola.",
            "[META: estado=Esperando; servicios=; carro=Sin dato; marca=Sin dato; calificacion=Sin dato]",
        ])
        with A.app.app_context():
            assert A.Conversation.query.get(conversacion).status == "En proceso"  # default del modelo, sin cambiar

    def test_no_interesado_con_calificacion_alta_va_a_remarketing(self, conversacion):
        """El caso que pidió el negocio: alguien que dijo que no, pero cuyo carro
        y servicio de interés son del perfil bueno, no se descarta — se separa
        para poder mandarle promociones más adelante."""
        _correr_turno(conversacion, [
            "Entendido.",
            "[META: estado=No interesado; servicios=Polarizado; carro=Audi Q5 2023; marca=Audi; calificacion=4]",
        ])
        with A.app.app_context():
            assert A.Conversation.query.get(conversacion).priority == "Remarketing"

    def test_no_interesado_con_calificacion_baja_es_baja_no_remarketing(self, conversacion):
        _correr_turno(conversacion, [
            "Entendido.",
            "[META: estado=No interesado; servicios=Lavada / mantenimiento; carro=Renault Logan 2015; marca=Renault; calificacion=0]",
        ])
        with A.app.app_context():
            assert A.Conversation.query.get(conversacion).priority == "Baja"

    def test_calificacion_media_es_prioridad_media(self, conversacion):
        _correr_turno(conversacion, [
            "Ok.",
            "[META: estado=En proceso; servicios=; carro=Mazda 3 2023; marca=Mazda; calificacion=3]",
        ])
        with A.app.app_context():
            assert A.Conversation.query.get(conversacion).priority == "Media"

    def test_sin_calificacion_todavia_la_prioridad_es_baja(self, conversacion):
        _correr_turno(conversacion, [
            "Hola.",
            "[META: estado=Iniciado; servicios=; carro=Sin dato; marca=Sin dato; calificacion=Sin dato]",
        ])
        with A.app.app_context():
            assert A.Conversation.query.get(conversacion).priority == "Baja"


class TestComputePriority:
    """Unitarios directos sobre _compute_priority, sin pasar por un turno completo."""

    def test_calificacion_alta_es_prioridad_alta(self):
        assert A._compute_priority("En proceso", 5) == "Alta"
        assert A._compute_priority("En proceso", 4) == "Alta"

    def test_calificacion_media_es_prioridad_media(self):
        assert A._compute_priority("En proceso", 2) == "Media"
        assert A._compute_priority("En proceso", 3) == "Media"

    def test_calificacion_baja_es_prioridad_baja(self):
        assert A._compute_priority("En proceso", 0) == "Baja"
        assert A._compute_priority("En proceso", 1) == "Baja"

    def test_sin_calificacion_es_baja(self):
        assert A._compute_priority("En proceso", None) == "Baja"

    def test_no_interesado_con_calificacion_4_o_5_es_remarketing(self):
        assert A._compute_priority("No interesado", 4) == "Remarketing"
        assert A._compute_priority("No interesado", 5) == "Remarketing"

    def test_no_interesado_con_calificacion_baja_es_baja(self):
        assert A._compute_priority("No interesado", 3) == "Baja"
        assert A._compute_priority("No interesado", None) == "Baja"
