"""A quién persigue la reactivación de leads, y con qué fecha razona el modelo.

Los dos casos salieron de un incidente en producción (2026-08-10): a un cliente
que ya tenía su diagnóstico agendado le llegó un mensaje de "reactivación
suave", y encima decía "tu diagnóstico de mañana miércoles" cuando la cita era
en dos días. Eran dos fallas distintas: el job no excluía a los que ya
agendaron, y al generar seguimientos el modelo no recibía la fecha de hoy.
"""
import itertools
import re

import app as A

_telefonos = itertools.count(9000)


def _conv(status="En proceso", followup_count=0, bot_active=True):
    conv = A.Conversation(
        phone=f"+5730099{next(_telefonos):05d}", profile_name="Mauricio",
        status=status, followup_count=followup_count, bot_active=bot_active,
    )
    A.db.session.add(conv)
    A.db.session.commit()
    return conv


def _candidatas_del_job():
    """Mismo filtro que usa _job_whatsapp_followup para elegir a quién escribirle."""
    return A.Conversation.query.filter(
        A.Conversation.bot_active == True,  # noqa: E712
        A.Conversation.followup_count < len(A._FOLLOWUP_STAGES),
        A.Conversation.status.notin_(("Diagnóstico agendado", "Servicio agendado")),
    ).all()


class TestAQuienSePersigue:
    def test_al_que_ya_agendo_diagnostico_no_se_le_insiste(self, client):
        agendado = _conv(status="Diagnóstico agendado")
        assert agendado not in _candidatas_del_job()

    def test_al_que_ya_agendo_servicio_tampoco(self, client):
        agendado = _conv(status="Servicio agendado")
        assert agendado not in _candidatas_del_job()

    def test_al_lead_en_proceso_si_se_le_escribe(self, client):
        en_proceso = _conv(status="En proceso")
        assert en_proceso in _candidatas_del_job()

    def test_con_el_bot_pausado_no_se_le_escribe(self, client):
        pausado = _conv(status="En proceso", bot_active=False)
        assert pausado not in _candidatas_del_job()

    def test_agotados_los_intentos_se_deja_de_insistir(self, client):
        agotado = _conv(status="En proceso", followup_count=len(A._FOLLOWUP_STAGES))
        assert agotado not in _candidatas_del_job()


class TestFechaEnElPrompt:
    def test_incluye_el_dia_en_espanol(self):
        texto = A._fecha_hoy_para_prompt()
        assert any(d in texto for d in A._DIAS_ES), texto
        assert any(m in texto for m in A._MESES_ES), texto

    def test_coincide_con_la_hora_de_bogota(self):
        """No con la del servidor, que en Railway corre en UTC."""
        hoy = A.datetime.now(A._BOGOTA)
        texto = A._fecha_hoy_para_prompt()
        assert f"{hoy.day} de {A._MESES_ES[hoy.month - 1]}" in texto
        assert A._DIAS_ES[hoy.weekday()] in texto

    def test_le_dice_al_modelo_contra_que_calcular(self):
        """Sin esta instrucción el modelo toma fechas del historial como si
        fueran de hoy — que es exactamente lo que pasó en producción."""
        texto = A._fecha_hoy_para_prompt()
        assert "historial" in texto.lower()
        assert re.search(r"mañana", texto, re.IGNORECASE)
