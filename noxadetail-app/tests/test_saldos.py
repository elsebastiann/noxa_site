"""Vigilancia del saldo de Twilio y del crédito de Anthropic.

Si cualquiera de los dos se agota, Mariana se queda muda y el síntoma es
silencio: nadie se entera hasta que un cliente reclama. Estos tests fijan las
dos decisiones que hacen que el aviso sirva:

  • El aviso de Twilio sale ANTES de llegar a cero — si se esperara al cero,
    el propio aviso tampoco podría salir por WhatsApp.
  • Solo lo que se arregla recargando (crédito/credencial) llega al WhatsApp
    del admin. Un rate limit se normaliza solo; mandarlo por WhatsApp entrena
    a Diana a ignorar los avisos que sí importan.
"""
from unittest.mock import patch

import httpx
import pytest

from conftest import app_module as A
from conftest import login_as, make_user


@pytest.fixture(autouse=True)
def _sin_notificaciones_previas():
    with A.app.app_context():
        A.Notification.query.delete()
        A.db.session.commit()
    yield
    with A.app.app_context():
        A.Notification.query.delete()
        A.db.session.commit()


def _correr_job(saldo_twilio, diagnostico, admin="+573001112233"):
    """Corre el job con los dos servicios simulados. Devuelve (notificaciones, whatsapps)."""
    enviados = []
    with patch.object(A, "_saldo_twilio", return_value=saldo_twilio), \
         patch.object(A, "_diagnostico_anthropic", return_value=diagnostico), \
         patch.dict(A.os.environ, {"ADMIN_WHATSAPP": admin}), \
         patch.object(A, "send_whatsapp",
                      side_effect=lambda to, body, **kw: enviados.append((to, body, kw)) or (True, "")):
        A._job_check_saldos()
    with A.app.app_context():
        notis = A.Notification.query.all()
        return [(n.kind, n.level, n.title) for n in notis], enviados


class TestSaldoTwilio:
    def test_saldo_bajo_avisa_por_campanita_y_whatsapp(self):
        notis, enviados = _correr_job((3.20, "USD", ""), (True, "ok", ""))

        kinds = [k for k, _, _ in notis]
        assert "saldo_twilio_bajo" in kinds
        assert [lvl for k, lvl, _ in notis if k == "saldo_twilio_bajo"] == ["urgent"]
        # El aviso sale mientras TODAVÍA queda saldo: es lo que permite que el
        # propio WhatsApp de alerta se pueda enviar.
        assert len(enviados) == 1
        assert enviados[0][2]["kind"] == "admin_saldo_twilio"
        assert "3.20" in enviados[0][1]

    def test_saldo_suficiente_no_molesta(self):
        notis, enviados = _correr_job((120.0, "USD", ""), (True, "ok", ""))
        assert notis == []
        assert enviados == []

    def test_saldo_ilegible_tambien_es_alerta(self):
        """No poder leer el saldo es un problema por sí mismo: deja al negocio
        ciego justo sobre lo que se quería vigilar."""
        notis, enviados = _correr_job((None, "", "401 Unauthorized"), (True, "ok", ""))
        assert [k for k, _, _ in notis] == ["saldo_twilio_ilegible"]


class TestDiagnosticoAnthropic:
    def test_sin_credito_avisa_por_whatsapp(self):
        notis, enviados = _correr_job(
            (120.0, "USD", ""), (False, "sin_credito", "credit balance is too low"))

        assert [(k, lvl) for k, lvl, _ in notis] == [("anthropic_sin_credito", "urgent")]
        assert len(enviados) == 1
        assert enviados[0][2]["kind"] == "admin_saldo_anthropic"

    def test_rate_limit_queda_en_la_campanita_pero_no_en_whatsapp(self):
        notis, enviados = _correr_job(
            (120.0, "USD", ""), (False, "limite", "429 rate limit"))

        assert [(k, lvl) for k, lvl, _ in notis] == [("anthropic_limite", "info")]
        assert enviados == []

    def test_error_de_credito_se_clasifica_como_sin_credito(self):
        """La API no da un código propio para 'se acabó el crédito': llega como
        un 400 genérico y hay que reconocerlo por el texto."""
        exc = A_bad_request("Your credit balance is too low to access the API.")
        with patch.dict(A.os.environ, {"ANTHROPIC_API_KEY": "sk-ant-de-prueba"}), \
             patch.object(A, "_get_claude_client") as cliente:
            cliente.return_value.messages.create.side_effect = exc
            ok, categoria, _ = A._diagnostico_anthropic()
        assert (ok, categoria) == (False, "sin_credito")

    def test_otro_400_no_se_confunde_con_falta_de_credito(self):
        exc = A_bad_request("max_tokens: must be greater than 0")
        with patch.dict(A.os.environ, {"ANTHROPIC_API_KEY": "sk-ant-de-prueba"}), \
             patch.object(A, "_get_claude_client") as cliente:
            cliente.return_value.messages.create.side_effect = exc
            ok, categoria, _ = A._diagnostico_anthropic()
        assert (ok, categoria) == (False, "otro")


class TestMotivoInfraestructura:
    """El aviso genérico 'Mariana no pudo responderle' se ve igual trátese de un
    bug o de una tarjeta sin fondos, y se arreglan de formas muy distintas."""

    def test_reconoce_credito_agotado(self):
        motivo = A._motivo_infraestructura(
            Exception("Error code: 400 - Your credit balance is too low"))
        assert "CRÉDITO" in motivo

    def test_reconoce_saldo_de_twilio(self):
        motivo = A._motivo_infraestructura(Exception("HTTP 400 error: 20003 Authenticate"))
        assert "Twilio" in motivo

    def test_un_bug_normal_no_manda_a_recargar(self):
        assert A._motivo_infraestructura(ValueError("Claude no devolvió texto")) == ""


class TestPaginaEstado:
    def test_muestra_los_dos_servicios_en_problemas(self, client):
        login_as(client, make_user("admin_estado", role="admin"))
        with patch.object(A, "_saldo_twilio", return_value=(4.5, "USD", "")), \
             patch.object(A, "_diagnostico_anthropic",
                          return_value=(False, "sin_credito", "credit balance is too low")):
            html = client.get("/estado").get_data(as_text=True)

        assert "4.50" in html
        assert "Saldo bajo" in html
        assert "Se acabó el crédito de Anthropic" in html

    def test_muestra_los_dos_servicios_sanos(self, client):
        login_as(client, make_user("admin_estado_ok", role="admin"))
        with patch.object(A, "_saldo_twilio", return_value=(120.0, "USD", "")), \
             patch.object(A, "_diagnostico_anthropic", return_value=(True, "ok", "")):
            html = client.get("/estado").get_data(as_text=True)

        assert "Con saldo" in html
        assert "Respondiendo" in html

    def test_solo_para_admin(self, client):
        """Los saldos son información de la cuenta, no de la operación diaria."""
        login_as(client, make_user("operario_curioso", role="operario"))
        r = client.get("/estado")
        assert r.status_code == 302


def A_bad_request(mensaje):
    """Un BadRequestError real del SDK (necesita una respuesta httpx de verdad)."""
    import anthropic
    respuesta = httpx.Response(400, request=httpx.Request("POST", "https://api.anthropic.com/v1/messages"))
    return anthropic.BadRequestError(mensaje, response=respuesta, body=None)
