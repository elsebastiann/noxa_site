"""Los avisos internos salen por plantilla, no por texto libre.

WhatsApp solo deja mandar texto libre dentro de las 24h siguientes al último
mensaje DEL DESTINATARIO. Esa ventana la abre quien recibe, y Diana no le
escribe al WhatsApp de su propia empresa — así que para su número la ventana
está cerrada prácticamente siempre.

O sea que un aviso interno en texto libre no falla "a veces": falla siempre,
con 63016, y el `ok=True` de Twilio hace que se vea como enviado. Así se
perdieron en producción el recordatorio de "cita en 30 min" y el escalamiento
a humano, los dos avisos que más urgen.
"""
import ast
import datetime as dt
import re
from pathlib import Path
from unittest.mock import patch

import pytest

from conftest import app_module as A

SID = "HXplantilladeprueba"

APP_PY = Path(A.__file__).resolve()


@pytest.fixture
def enviados():
    """Captura los envíos con la plantilla y las variables que llevaron."""
    capturados = []

    def fake_send(to, body, **kw):
        capturados.append({"to": to, "body": body, **kw})
        return True, ""

    with patch.object(A, "send_whatsapp", side_effect=fake_send), \
         patch.object(A, "TPL_AVISO_ADMIN", SID), \
         patch.dict(A.os.environ, {"ADMIN_WHATSAPP": "+573001112233"}):
        yield capturados


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


class TestNingunAvisoInternoQuedaEnTextoLibre:
    """Se mira el código y no el comportamiento a propósito: son diez avisos
    repartidos por el archivo, y el que se olvide de la plantilla no falla en
    ningún test — sale, Twilio lo acepta y nadie lo vuelve a ver."""

    def test_ningun_send_whatsapp_manda_un_kind_admin(self):
        arbol = ast.parse(APP_PY.read_text(encoding="utf-8"))
        sueltos = []
        for nodo in ast.walk(arbol):
            if not isinstance(nodo, ast.Call):
                continue
            if getattr(nodo.func, "id", None) != "send_whatsapp":
                continue
            for kw in nodo.keywords:
                if kw.arg != "kind" or not isinstance(kw.value, ast.Constant):
                    continue
                if str(kw.value.value).startswith("admin_"):
                    sueltos.append(f"línea {nodo.lineno}: kind={kw.value.value!r}")
        assert not sueltos, (
            "estos avisos al admin siguen saliendo como texto libre y morirán "
            "con 63016: " + "; ".join(sueltos) + ". Usa avisar_admin_whatsapp()."
        )

    def test_la_prueba_de_whatsapp_tambien_va_por_plantilla(self):
        """Si la prueba usa texto libre, pasa siempre que la ventana esté
        abierta — o sea que decía "todo bien" justo cuando los avisos de verdad
        se estaban perdiendo."""
        fuente = APP_PY.read_text(encoding="utf-8")
        cuerpo = fuente.split("def test_whatsapp()")[1].split("\ndef ")[0]
        assert "avisar_admin_whatsapp(" in cuerpo


class TestLasVariablesQueMetaAcepta:
    """Meta rechaza el mensaje ENTERO —no la variable— si una variable viene
    vacía o trae saltos de línea. Los avisos se venían armando en varias
    líneas, así que pasarlos crudos los rompería igual que hoy."""

    def test_aplana_los_saltos_de_linea(self):
        assert A._var_plantilla("Cliente: Ana\nPlaca: ABC123") == "Cliente: Ana Placa: ABC123"

    def test_aplana_tabs_y_espacios_seguidos(self):
        assert A._var_plantilla("uno\t\tdos     tres") == "uno dos tres"

    @pytest.mark.parametrize("vacio", ["", None, "   ", "\n"])
    def test_nunca_devuelve_vacio(self, vacio):
        assert A._var_plantilla(vacio) == "—"

    def test_se_puede_cambiar_el_relleno(self):
        assert A._var_plantilla("", "NOXA") == "NOXA"

    def test_recorta_lo_muy_largo(self):
        assert len(A._var_plantilla("x" * 5000)) == 900


class TestElEscalamiento:
    """El aviso del caso reportado: un cliente pidió hablar con alguien, el
    aviso salió con 63016 y nadie lo atendió."""

    def test_sale_con_la_plantilla_aprobada(self, enviados, conversacion):
        with A.app.app_context():
            conv = A.Conversation.query.get(conversacion)
            with patch.object(A, "push_notification"):
                A.notify_admin_escalation(conv, "el cliente pide fotos de trabajos previos")
        assert len(enviados) == 1
        assert enviados[0]["content_sid"] == SID

    def test_lleva_los_cuatro_datos_del_aviso(self, enviados, conversacion):
        with A.app.app_context():
            conv = A.Conversation.query.get(conversacion)
            with patch.object(A, "push_notification"):
                A.notify_admin_escalation(conv, "pide hablar con un asesor")
        v = enviados[0]["content_variables"]
        assert v["1"] == "Manu Prueba"
        assert "atención humana" in v["2"]
        assert "pide hablar con un asesor" in v["3"]
        assert v["4"] == "+573159998877"

    def test_ninguna_variable_lleva_saltos_de_linea(self, enviados, conversacion):
        with A.app.app_context():
            conv = A.Conversation.query.get(conversacion)
            with patch.object(A, "push_notification"):
                A.notify_admin_escalation(conv, "quiere pagar\nya mismo")
        for clave, valor in enviados[0]["content_variables"].items():
            assert "\n" not in valor, f"la variable {clave} rompería la plantilla"

    def test_el_panel_guarda_algo_legible(self, enviados, conversacion):
        """Lo que WhatsApp entrega lo define la plantilla, pero en la bandeja de
        salida queda `body` — si ahí quedara un marcador, quien revise por qué
        no llegó un aviso no sabría ni qué decía."""
        with A.app.app_context():
            conv = A.Conversation.query.get(conversacion)
            with patch.object(A, "push_notification"):
                A.notify_admin_escalation(conv, "quiere pagar")
        assert "Manu Prueba" in enviados[0]["body"]
        assert "quiere pagar" in enviados[0]["body"]


class TestLaCitaEnTreintaMinutos:
    @pytest.fixture
    def cita_ya(self):
        with A.app.app_context():
            vt = A.VehicleType.query.filter_by(is_active=True).first()
            inicio = A.bogota_now() + dt.timedelta(minutes=30)
            appt = A.Appointment(
                customer_name="Tatiana Pinzon", plate="NIR849", phone="3105528361",
                services="Wash Shine", start_datetime=inicio,
                end_datetime=inicio + dt.timedelta(hours=1),
                vehicle_type_id=vt.id, status="scheduled",
            )
            A.db.session.add(appt)
            A.db.session.commit()
            appt_id = appt.id
        yield appt_id
        with A.app.app_context():
            appt = A.Appointment.query.get(appt_id)
            if appt:
                A.db.session.delete(appt)
                A.db.session.commit()

    def test_sale_con_la_plantilla_aprobada(self, enviados, cita_ya):
        A._job_admin_reminder()
        mios = [e for e in enviados if e["kind"] == "admin_cita_30min"]
        assert mios, "no salió el recordatorio de la cita"
        assert mios[0]["content_sid"] == SID

    def test_lleva_placa_servicio_y_telefono(self, enviados, cita_ya):
        A._job_admin_reminder()
        v = [e for e in enviados if e["kind"] == "admin_cita_30min"][0]["content_variables"]
        assert v["1"] == "Tatiana Pinzon"
        assert "NIR849" in v["3"] and "Wash Shine" in v["3"]
        assert v["4"] == "3105528361"

    def test_una_cita_sin_telefono_no_manda_una_variable_vacia(self, enviados, cita_ya):
        """Meta rechaza el mensaje entero por una variable vacía, así que la
        cita sin teléfono se llevaría por delante el aviso completo."""
        with A.app.app_context():
            appt = A.Appointment.query.get(cita_ya)
            appt.phone = ""
            A.db.session.commit()
        A._job_admin_reminder()
        v = [e for e in enviados if e["kind"] == "admin_cita_30min"][0]["content_variables"]
        assert all(val.strip() for val in v.values())

    def test_no_se_repite_en_la_siguiente_corrida(self, enviados, cita_ya):
        """Corre cada 5 minutos: sin la marca, la misma cita avisaría seis
        veces antes de empezar."""
        A._job_admin_reminder()
        A._job_admin_reminder()
        assert len([e for e in enviados if e["kind"] == "admin_cita_30min"]) == 1


class TestSinPlantillaConfigurada:
    """Mientras el SID no esté en Railway el envío cae a texto libre. Eso es
    deliberado —es mejor que no mandar nada— pero no puede ser silencioso."""

    def test_cae_a_texto_libre(self, conversacion):
        capturados = []
        with patch.object(A, "send_whatsapp",
                          side_effect=lambda to, body, **kw: capturados.append(kw) or (True, "")), \
             patch.object(A, "TPL_AVISO_ADMIN", ""), \
             patch.dict(A.os.environ, {"ADMIN_WHATSAPP": "+573001112233"}), \
             A.app.app_context():
            conv = A.Conversation.query.get(conversacion)
            with patch.object(A, "push_notification"):
                A.notify_admin_escalation(conv, "quiere pagar")
        assert capturados[0].get("content_sid") in ("", None)

    def test_queda_en_el_log(self, conversacion, caplog):
        with patch.object(A, "send_whatsapp", return_value=(True, "")), \
             patch.object(A, "TPL_AVISO_ADMIN", ""), \
             patch.dict(A.os.environ, {"ADMIN_WHATSAPP": "+573001112233"}), \
             A.app.app_context():
            conv = A.Conversation.query.get(conversacion)
            with patch.object(A, "push_notification"):
                A.notify_admin_escalation(conv, "quiere pagar")
        assert "TWILIO_TPL_AVISO_ADMIN" in caplog.text

    def test_la_bandeja_de_salida_lo_avisa(self, client):
        with A.app.app_context():
            from conftest import make_user
            uid = make_user("outbox_tpl", role="admin").id
        with client.session_transaction() as sess:
            sess["user_id"] = uid
        with patch.object(A, "TPL_AVISO_ADMIN", ""):
            cuerpo = client.get("/whatsapp/outbox").data.decode()
        assert "TWILIO_TPL_AVISO_ADMIN" in cuerpo
        with patch.object(A, "TPL_AVISO_ADMIN", SID):
            cuerpo = client.get("/whatsapp/outbox").data.decode()
        assert "TWILIO_TPL_AVISO_ADMIN" not in cuerpo


class TestLaCampanitaNoDependeDeWhatsApp:
    def test_sin_admin_whatsapp_igual_queda_el_aviso_en_el_panel(self, conversacion):
        """El chequeo de la variable estaba ANTES de la campanita, así que una
        variable sin configurar dejaba a Diana sin los dos canales."""
        with patch.dict(A.os.environ, {"ADMIN_WHATSAPP": ""}), \
             A.app.app_context():
            conv = A.Conversation.query.get(conversacion)
            with patch.object(A, "push_notification") as campanita, \
                 patch.object(A, "_summarize_conversation_for_admin", return_value="preguntó por PPF"):
                A.notify_admin_conversation_error(conv, RuntimeError("se cayó"))
        assert campanita.called


class TestElSeguimientoDeLosSieteDiasLoEscribeDiana:
    """Salía como texto libre 5 a 9 días después del servicio, o sea con la
    ventana de 24h cerrada hace días: no llegó nunca uno solo. Y aunque
    llegara, preguntar cómo le fue viniendo de un automático vale menos que
    viniendo de una persona — es la misma decisión que ya estaba tomada para el
    seguimiento del cerámico."""

    @pytest.fixture
    def cita_de_hace_una_semana(self):
        with A.app.app_context():
            vt = A.VehicleType.query.filter_by(is_active=True).first()
            inicio = dt.datetime.combine(
                A.bogota_today() - dt.timedelta(days=7), dt.time(9, 0))
            appt = A.Appointment(
                customer_name="Ricardo Rendon", plate="ABC123", phone="3214780936",
                services="Cerámico 9H", start_datetime=inicio,
                end_datetime=inicio + dt.timedelta(hours=2),
                vehicle_type_id=vt.id, status="completed",
            )
            A.db.session.add(appt)
            A.db.session.commit()
            appt_id = appt.id
        yield appt_id
        with A.app.app_context():
            appt = A.Appointment.query.get(appt_id)
            if appt:
                A.db.session.delete(appt)
                A.db.session.commit()

    def test_no_se_le_escribe_al_cliente(self, enviados, cita_de_hace_una_semana):
        with patch.object(A, "push_notification"):
            A._job_post_service_followup()
        assert all(e["to"] != "3214780936" for e in enviados), (
            "el mensaje automático al cliente debía desaparecer"
        )

    def test_se_le_avisa_a_diana_con_la_plantilla(self, enviados, cita_de_hace_una_semana):
        with patch.object(A, "push_notification"):
            A._job_post_service_followup()
        mios = [e for e in enviados if e["kind"] == "cliente_seguimiento_post_servicio"]
        assert mios, "Diana se quedó sin el recordatorio"
        assert mios[0]["content_sid"] == SID
        v = mios[0]["content_variables"]
        assert v["1"] == "Ricardo Rendon"
        assert v["4"] == "3214780936"

    def test_no_se_repite_al_dia_siguiente(self, enviados, cita_de_hace_una_semana):
        """La ventana es de 7 ± 2 días: sin la marca, la misma cita le saldría
        cinco veces seguidas."""
        with patch.object(A, "push_notification"):
            A._job_post_service_followup()
            A._job_post_service_followup()
        assert len([e for e in enviados
                    if e["kind"] == "cliente_seguimiento_post_servicio"]) == 1
