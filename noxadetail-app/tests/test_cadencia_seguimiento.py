"""A un lead callado se le escribe dos veces. No más.

    1) Al día siguiente a las 12:30. Salvo que a esa hora su último mensaje ya
       pasara de 24 horas; ahí sale a las 23 horas de haber escrito él.
    2) A la semana de ese mismo mensaje. Y ya.

Antes eran cuatro (24h, +2d, +5d, +14d), todos los días de por medio.

El 12:30 y el 23 no son preferencias de horario: WhatsApp solo deja escribir
texto libre dentro de las 24 horas siguientes al último mensaje DEL CLIENTE.
Fuera de esa ventana solo entra plantilla aprobada, y una plantilla no puede
recoger nada de lo que el cliente dijo. La cadencia está armada para que el
primer toque —el único personalizado— caiga dentro.

La franja de atención (9am-6pm) manda sobre ese cálculo: si las 23 horas caen
de madrugada, el mensaje espera. Eso puede sacarlo de la ventana, y entonces
sale como plantilla. Es el precio conocido de no escribirle a nadie a las 2 de
la mañana, y está probado abajo para que se vea cuándo pasa.
"""
from datetime import datetime, timedelta

import pytest

from conftest import app_module as A

VENTANA = timedelta(hours=24)


def cuando(dia, hora, minuto=0):
    return datetime(2026, 9, dia, hora, minuto)


class TestElPrimerToque:
    @pytest.mark.parametrize("escrito, esperado", [
        # Escribió después del mediodía: al otro día a las 12:30 todavía no se
        # cumplen 24 horas, así que va a la hora buena.
        (cuando(1, 14, 0),  cuando(2, 12, 30)),
        (cuando(1, 12, 30), cuando(2, 12, 30)),
        (cuando(1, 23, 45), cuando(2, 12, 30)),
        # Escribió por la mañana: al otro día al mediodía ya se pasó, así que se
        # adelanta a las 23 horas.
        (cuando(1, 12, 0),  cuando(2, 11, 0)),
        (cuando(1, 10, 0),  cuando(2, 9, 0)),
    ])
    def test_al_dia_siguiente_a_las_12_30_o_antes_si_no_alcanza(self, escrito, esperado):
        assert A.momento_de_seguimiento(escrito, 0) == esperado

    @pytest.mark.parametrize("hora", range(0, 24))
    def test_nunca_cae_fuera_de_la_franja_de_atencion(self, hora):
        """Escriba a la hora que escriba, el mensaje sale entre las 9 y las
        17:30. Es lo que impide despertar a un cliente a las 2 de la mañana."""
        momento = A.momento_de_seguimiento(cuando(1, hora), 0)
        assert A.FOLLOWUP_DESDE <= momento.time() <= A.FOLLOWUP_HASTA

    @pytest.mark.parametrize("hora", list(range(10, 24)))
    def test_a_quien_escribe_de_las_10_en_adelante_le_llega_texto_libre(self, hora):
        """El caso normal, y el que justifica toda la regla: dentro de la
        ventana de 24h Mariana escribe personalizado, no plantilla."""
        escrito = cuando(1, hora)
        assert A.momento_de_seguimiento(escrito, 0) - escrito < VENTANA

    @pytest.mark.parametrize("hora", [1, 5, 9])
    def test_a_quien_escribe_de_madrugada_le_toca_plantilla(self, hora):
        """El costo conocido de respetar la franja: a estas horas las 23 horas
        caen antes de las 9 de la mañana, esperar cierra la ventana y el mensaje
        sale como plantilla. Se documenta acá para que sea una decisión y no una
        sorpresa: son los leads que escriben entre la medianoche y las 10."""
        escrito = cuando(1, hora)
        assert A.momento_de_seguimiento(escrito, 0) - escrito >= VENTANA

    def test_pasada_la_medianoche_se_recorta_hacia_atras_y_alcanza(self):
        """Quien escribe a las 00:30 tiene sus 23 horas a las 23:30 del mismo
        día — muy tarde. Recortar a las 17:30 lo deja a 17 horas, todavía
        dentro de la ventana."""
        escrito = cuando(1, 0, 30)
        momento = A.momento_de_seguimiento(escrito, 0)
        assert momento == cuando(1, 17, 30)
        assert momento - escrito < VENTANA


class TestElSegundoToque:
    def test_es_a_la_semana_del_mensaje_del_cliente(self):
        assert A.momento_de_seguimiento(cuando(1, 14, 0), 1) == cuando(8, 14, 0)

    def test_tambien_respeta_la_franja(self):
        assert A.momento_de_seguimiento(cuando(1, 3, 0), 1) == cuando(8, 9, 0)

    def test_se_cuenta_desde_el_cliente_y_no_desde_el_primer_toque(self):
        """Si se contara desde nuestro mensaje, cada toque correría al
        siguiente y la cadencia se iría estirando sola."""
        escrito = cuando(1, 14, 0)
        primero = A.momento_de_seguimiento(escrito, 0)
        segundo = A.momento_de_seguimiento(escrito, 1)
        assert (segundo - escrito).days == A.SEGUNDO_TOQUE_DIAS
        assert segundo > primero


class TestNoHayUnTercero:
    def test_despues_del_segundo_no_le_toca_nada(self):
        assert A.momento_de_seguimiento(cuando(1, 14, 0), 2) is None

    def test_son_exactamente_dos_etapas(self):
        """Eran cuatro. Si alguien agrega una tercera sin querer, el lead vuelve
        a recibir mensajes todos los días — que es lo que esta regla vino a
        quitar."""
        assert A._FOLLOWUP_STAGES == ["primer_toque", "cierre_semana"]

    def test_al_que_ya_recibio_dos_el_job_no_lo_vuelve_a_mirar(self):
        """La otra mitad de la regla: no basta con que no haya tercera etapa, el
        lead tiene que salir de la lista de candidatas. Si no, el job lo
        recorrería cada media hora para siempre."""
        with A.app.app_context():
            usados = A.Conversation(phone="+573003300001", profile_name="Ya le escribimos",
                                    bot_active=True, followup_count=2)
            pendiente = A.Conversation(phone="+573003300002", profile_name="Le falta el segundo",
                                       bot_active=True, followup_count=1)
            A.db.session.add_all([usados, pendiente])
            A.db.session.commit()
            try:
                telefonos = [c.phone for c in A._candidatas_de_seguimiento()]
                assert "+573003300002" in telefonos
                assert "+573003300001" not in telefonos
            finally:
                for c in (usados, pendiente):
                    A.db.session.delete(c)
                A.db.session.commit()


class TestLaFranjaEsUnaFranja:
    @pytest.mark.parametrize("momento, esperado", [
        (cuando(1, 3, 0),   cuando(1, 9, 0)),    # madrugada → al abrir
        (cuando(1, 22, 0),  cuando(1, 17, 30)),  # noche → al último tick
        (cuando(1, 9, 0),   cuando(1, 9, 0)),    # los bordes se quedan quietos
        (cuando(1, 17, 30), cuando(1, 17, 30)),
        (cuando(1, 13, 15), cuando(1, 13, 15)),
    ])
    def test_corre_solo_lo_que_esta_fuera(self, momento, esperado):
        assert A._dentro_de_la_franja(momento) == esperado

    def test_el_tope_deja_pasar_el_ultimo_tick_del_job(self):
        """El job corre cada media hora. Con el tope en las 18:00 en punto, un
        objetivo ahí no lo alcanzaría ningún tick de la franja y el seguimiento
        se quedaría esperando al día siguiente."""
        assert A.FOLLOWUP_HASTA <= A.hora_del_dia(17, 30)
