"""Leads que llegan del formulario instantáneo de Meta (pauta de encuesta).

Lo que importa acá es doble: que el endpoint no se pueda falsificar —es público
y dispara WhatsApps con plantilla, que cuestan— y que las respuestas de la
encuesta terminen en el historial de la conversación, porque de ahí es de donde
Mariana las lee para no volver a preguntar lo mismo.
"""
import hashlib
import hmac
import json
from unittest.mock import patch

import pytest

from conftest import app_module as A

SECRET = "secreto_de_prueba"
TELEFONO = "+573001239876"


def _firmar(cuerpo: bytes) -> str:
    return "sha256=" + hmac.new(SECRET.encode(), cuerpo, hashlib.sha256).hexdigest()


def _payload(leadgen_id="LEAD123"):
    return {"entry": [{"changes": [{"field": "leadgen",
                                    "value": {"leadgen_id": leadgen_id}}]}]}


def _lead_de_meta(**extra):
    campos = [
        {"name": "full_name", "values": ["Camila Rojas"]},
        {"name": "phone_number", "values": [TELEFONO]},
        {"name": "que_servicio_te_interesa", "values": ["Cerámico"]},
        {"name": "que_carro_tienes", "values": ["Mazda CX-5 2023"]},
    ]
    campos.extend(extra.get("campos", []))
    return {"id": "LEAD123", "field_data": campos}


@pytest.fixture(autouse=True)
def _entorno():
    with patch.dict(A.os.environ, {"META_APP_SECRET": SECRET,
                                   "META_VERIFY_TOKEN": "token_verificacion",
                                   "META_PAGE_TOKEN": "token_pagina"}):
        yield
    with A.app.app_context():
        conv = A.Conversation.query.filter_by(phone=TELEFONO).first()
        if conv:
            A.Message.query.filter_by(conversation_id=conv.id).delete()
            A.db.session.delete(conv)
            A.db.session.commit()


def _postear(client, payload, firma=None, lead=None):
    cuerpo = json.dumps(payload).encode()
    headers = {"Content-Type": "application/json",
               "X-Hub-Signature-256": firma if firma is not None else _firmar(cuerpo)}
    with patch.object(A, "_meta_traer_lead", return_value=lead or _lead_de_meta()), \
         patch.object(A, "_send_whatsapp_opening_for_lead", return_value=(True, "")), \
         patch.object(A, "notify_admin_new_web_lead"):
        return client.post("/api/public/meta-lead", data=cuerpo, headers=headers)


class TestSeguridad:
    def test_sin_firma_no_entra(self, client):
        r = _postear(client, _payload(), firma="")
        assert r.status_code == 403
        with A.app.app_context():
            assert A.Conversation.query.filter_by(phone=TELEFONO).first() is None

    def test_firma_incorrecta_no_entra(self, client):
        r = _postear(client, _payload(), firma="sha256=" + "0" * 64)
        assert r.status_code == 403
        with A.app.app_context():
            assert A.Conversation.query.filter_by(phone=TELEFONO).first() is None

    def test_firma_de_otro_secreto_no_entra(self, client):
        cuerpo = json.dumps(_payload()).encode()
        ajena = "sha256=" + hmac.new(b"otro_secreto", cuerpo, hashlib.sha256).hexdigest()
        assert _postear(client, _payload(), firma=ajena).status_code == 403

    def test_firma_valida_si_entra(self, client):
        assert _postear(client, _payload()).status_code == 200


class TestVerificacionDelWebhook:
    def test_devuelve_el_challenge_con_el_token_correcto(self, client):
        r = client.get("/api/public/meta-lead?hub.mode=subscribe"
                       "&hub.verify_token=token_verificacion&hub.challenge=12345")
        assert r.status_code == 200
        assert r.get_data(as_text=True) == "12345"

    def test_token_equivocado_se_rechaza(self, client):
        r = client.get("/api/public/meta-lead?hub.mode=subscribe"
                       "&hub.verify_token=malo&hub.challenge=12345")
        assert r.status_code == 403


class TestLeadRegistrado:
    def test_crea_la_conversacion_con_el_nombre(self, client):
        _postear(client, _payload())
        with A.app.app_context():
            conv = A.Conversation.query.filter_by(phone=TELEFONO).first()
        assert conv is not None
        assert conv.profile_name == "Camila Rojas"

    def test_mariana_recibe_las_respuestas_de_la_encuesta(self, client):
        """El punto de toda la función: que no vuelva a preguntar lo que ya contestó."""
        _postear(client, _payload())
        with A.app.app_context():
            conv = A.Conversation.query.filter_by(phone=TELEFONO).first()
            historial = A._build_message_history(conv)
        texto = " ".join(m["content"] for m in historial)
        assert "Cerámico" in texto
        assert "Mazda CX-5 2023" in texto

    def test_el_contexto_entra_como_mensaje_del_cliente(self, client):
        # Si entrara como "assistant", Claude lo leería como algo que dijo
        # Mariana y no como información del cliente.
        _postear(client, _payload())
        with A.app.app_context():
            conv = A.Conversation.query.filter_by(phone=TELEFONO).first()
            primero = A.Message.query.filter_by(conversation_id=conv.id).order_by(A.Message.id).first()
        assert primero.direction == "in"

    def test_telefono_invalido_no_crea_conversacion(self, client):
        lead = _lead_de_meta()
        lead["field_data"][1] = {"name": "phone_number", "values": ["no-es-un-numero"]}
        r = _postear(client, _payload(), lead=lead)
        # Responde 200 igual: reintentar no lo va a arreglar y Meta reenviaría el lote.
        assert r.status_code == 200
        with A.app.app_context():
            assert A.Conversation.query.filter_by(phone=TELEFONO).first() is None

    def test_un_lead_roto_no_tumba_el_lote(self, client):
        """Meta manda varios leads juntos; uno malo no puede perder los buenos."""
        payload = {"entry": [{"changes": [
            {"field": "leadgen", "value": {"leadgen_id": "ROTO"}},
            {"field": "leadgen", "value": {"leadgen_id": "BUENO"}},
        ]}]}
        cuerpo = json.dumps(payload).encode()

        def traer(leadgen_id):
            if leadgen_id == "ROTO":
                raise RuntimeError("Graph API respondió 400")
            return _lead_de_meta()

        with patch.object(A, "_meta_traer_lead", side_effect=traer), \
             patch.object(A, "_send_whatsapp_opening_for_lead", return_value=(True, "")), \
             patch.object(A, "notify_admin_new_web_lead"), \
             patch.object(A, "push_notification"):
            r = client.post("/api/public/meta-lead", data=cuerpo,
                            headers={"Content-Type": "application/json",
                                     "X-Hub-Signature-256": _firmar(cuerpo)})
        assert r.status_code == 200
        with A.app.app_context():
            assert A.Conversation.query.filter_by(phone=TELEFONO).first() is not None

    def test_avisa_al_admin_si_un_lead_falla(self, client):
        cuerpo = json.dumps(_payload("ROTO")).encode()
        with patch.object(A, "_meta_traer_lead", side_effect=RuntimeError("token vencido")), \
             patch.object(A, "push_notification") as campanita:
            client.post("/api/public/meta-lead", data=cuerpo,
                        headers={"Content-Type": "application/json",
                                 "X-Hub-Signature-256": _firmar(cuerpo)})
        assert campanita.called, "un lead pagado que se pierde en silencio es plata perdida"


class TestParseo:
    def test_separa_nombre_telefono_y_respuestas(self):
        nombre, telefono, contexto = A._meta_parsear_lead(_lead_de_meta())
        assert nombre == "Camila Rojas"
        assert telefono == TELEFONO
        assert "Cerámico" in contexto and "Mazda CX-5 2023" in contexto
        # El nombre y el teléfono no se repiten dentro del texto de la encuesta.
        assert "Camila Rojas" not in contexto

    def test_sin_respuestas_igual_devuelve_contexto(self):
        lead = {"field_data": [{"name": "full_name", "values": ["Ana"]},
                               {"name": "phone_number", "values": [TELEFONO]}]}
        _n, _t, contexto = A._meta_parsear_lead(lead)
        assert contexto.strip()
