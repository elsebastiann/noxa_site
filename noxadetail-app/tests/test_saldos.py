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
from datetime import date, timedelta
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

    def test_muestra_el_costo_de_railway_y_la_comparacion(self, client):
        login_as(client, make_user("admin_costos", role="admin"))
        corte = A.SERVERLESS_APAGADO
        periodo = corte - timedelta(days=20)
        with A.app.app_context():
            A.RailwayCostSnapshot.query.delete()
            A.db.session.add(A.RailwayCostSnapshot(
                fecha=corte, usage_usd=4.00, periodo_inicio=periodo))
            A.db.session.commit()

        datos = {"workspace": "NOXA", "usage_usd": 6.50, "credito_usd": 0.0,
                 "periodo_inicio": periodo, "periodo_fin": None}
        with patch.object(A, "_saldo_twilio", return_value=(50.0, "USD", "")), \
             patch.object(A, "_diagnostico_anthropic", return_value=(True, "ok", "")), \
             patch.object(A, "_costo_railway", return_value=(datos, "")):
            html = client.get("/estado").get_data(as_text=True)

        with A.app.app_context():
            A.RailwayCostSnapshot.query.delete()
            A.db.session.commit()

        assert "Costo de Railway" in html
        assert "6.50" in html          # acumulado del periodo
        assert "corte" in html          # la marca del día en que se apagó Serverless

    def test_sin_token_de_railway_explica_como_activarlo(self, client):
        login_as(client, make_user("admin_sin_token", role="admin"))
        with patch.object(A, "_saldo_twilio", return_value=(50.0, "USD", "")), \
             patch.object(A, "_diagnostico_anthropic", return_value=(True, "ok", "")), \
             patch.object(A, "_costo_railway", return_value=(None, "Falta configurar RAILWAY_API_TOKEN")):
            html = client.get("/estado").get_data(as_text=True)

        assert "RAILWAY_API_TOKEN" in html
        assert "railway.com/account/tokens" in html

    def test_solo_para_admin(self, client):
        """Los saldos son información de la cuenta, no de la operación diaria."""
        login_as(client, make_user("operario_curioso", role="operario"))
        r = client.get("/estado")
        assert r.status_code == 302


class TestCostoRailway:
    """Railway solo publica el gasto como acumulado del periodo. El costo por día
    sale de restar dos fotos, y esa resta tiene una trampa: cuando arranca un
    ciclo de facturación nuevo el acumulado vuelve a cero."""

    @pytest.fixture(autouse=True)
    def _limpio(self):
        with A.app.app_context():
            A.RailwayCostSnapshot.query.delete()
            A.db.session.commit()
        yield
        with A.app.app_context():
            A.RailwayCostSnapshot.query.delete()
            A.db.session.commit()

    def _snap(self, dia, usd, periodo):
        A.db.session.add(A.RailwayCostSnapshot(
            fecha=dia, usage_usd=usd, periodo_inicio=periodo))
        A.db.session.commit()

    def test_costo_diario_es_la_diferencia_entre_fotos(self):
        p = date(2026, 8, 1)
        self._snap(date(2026, 8, 20), 4.00, p)
        self._snap(date(2026, 8, 21), 4.30, p)
        self._snap(date(2026, 8, 22), 4.75, p)

        serie = A._serie_costos_railway()
        assert [s["costo"] for s in serie] == [None, 0.30, 0.45]

    def test_el_primer_dia_de_un_ciclo_nuevo_no_se_resta(self):
        """Sin esto, el reinicio del acumulado se vería como un día de gasto
        negativo — y arrastraría el promedio a un número sin sentido."""
        self._snap(date(2026, 8, 30), 9.00, date(2026, 8, 1))
        self._snap(date(2026, 9, 1), 0.35, date(2026, 9, 1))

        serie = A._serie_costos_railway()
        assert serie[-1]["costo"] is None

    def test_compara_promedio_antes_y_despues_del_corte(self):
        corte = A.SERVERLESS_APAGADO
        periodo = corte - timedelta(days=20)
        # En el corte llevaba 4 USD en 20 días dormida => 0.20 USD/día.
        self._snap(corte, 4.00, periodo)
        self._snap(corte + timedelta(days=1), 4.50, periodo)
        self._snap(corte + timedelta(days=2), 5.00, periodo)

        comp = A._comparacion_serverless()

        assert comp["antes_diario"] == 0.20
        assert comp["despues_diario"] == 0.50
        assert comp["incremento_pct"] == 150
        assert comp["dias_despues"] == 2

    def test_la_comparacion_sobrevive_al_cambio_de_ciclo(self):
        """Antes esto se calculaba restando el acumulado de hoy menos el del
        corte, así que al facturar (acumulado de vuelta a cero) la comparación
        desaparecía justo cuando ya había más días de datos."""
        corte = A.SERVERLESS_APAGADO
        p1 = corte - timedelta(days=20)
        p2 = corte + timedelta(days=2)
        self._snap(corte, 4.00, p1)
        self._snap(corte + timedelta(days=1), 4.50, p1)
        # Empieza un ciclo nuevo: el acumulado se reinicia.
        self._snap(p2, 0.00, p2)
        self._snap(p2 + timedelta(days=1), 0.60, p2)

        comp = A._comparacion_serverless()

        # Promedia los días medibles (0.50 y 0.60), ignorando el día del
        # reinicio, que no tiene contra qué restarse.
        assert comp["despues_diario"] == 0.55
        assert comp["dias_despues"] == 2

    def test_sin_foto_del_corte_no_inventa_comparacion(self):
        assert A._comparacion_serverless() is None

    def test_la_foto_del_dia_es_idempotente(self):
        """Abrir /estado varias veces el mismo día no puede duplicar filas: la
        serie se calcula restando días consecutivos."""
        datos = {"usage_usd": 5.0, "periodo_inicio": date(2026, 8, 1)}
        A._tomar_snapshot_costo_railway(datos)
        A._tomar_snapshot_costo_railway({**datos, "usage_usd": 5.4})

        snaps = A.RailwayCostSnapshot.query.all()
        assert len(snaps) == 1
        assert snaps[0].usage_usd == 5.4


class TestConsultaRailway:
    def test_sin_token_lo_dice_en_vez_de_fallar(self):
        with patch.dict(A.os.environ, {"RAILWAY_API_TOKEN": "", "RAILWAY_WORKSPACE_ID": ""}):
            datos, err = A._costo_railway()
        assert datos is None and "RAILWAY_API_TOKEN" in err

    def test_un_error_de_graphql_no_pasa_como_exito(self):
        """GraphQL responde 200 aunque la consulta falle — el error viene en el
        cuerpo. Mirar solo el código HTTP daría un costo de 0 dólares."""
        respuesta = type("R", (), {"json": lambda self: {"errors": [{"message": "Not Authorized"}]}})()
        with patch.dict(A.os.environ, {"RAILWAY_API_TOKEN": "t", "RAILWAY_WORKSPACE_ID": "w"}), \
             patch.object(A.requests, "post", return_value=respuesta):
            datos, err = A._costo_railway()
        assert datos is None and "Not Authorized" in err

    def test_lee_el_consumo_y_el_periodo(self):
        cuerpo = {"data": {"workspace": {"name": "NOXA", "customer": {
            "currentUsage": 7.42, "creditBalance": 1.5,
            "billingPeriod": {"start": "2026-08-01T00:00:00Z", "end": "2026-09-01T00:00:00Z"}}}}}
        respuesta = type("R", (), {"json": lambda self: cuerpo})()
        with patch.dict(A.os.environ, {"RAILWAY_API_TOKEN": "t", "RAILWAY_WORKSPACE_ID": "w"}), \
             patch.object(A.requests, "post", return_value=respuesta):
            datos, err = A._costo_railway()

        assert err == ""
        assert datos["usage_usd"] == 7.42
        assert datos["periodo_inicio"] == date(2026, 8, 1)


def A_bad_request(mensaje):
    """Un BadRequestError real del SDK (necesita una respuesta httpx de verdad)."""
    import anthropic
    respuesta = httpx.Response(400, request=httpx.Request("POST", "https://api.anthropic.com/v1/messages"))
    return anthropic.BadRequestError(mensaje, response=respuesta, body=None)
