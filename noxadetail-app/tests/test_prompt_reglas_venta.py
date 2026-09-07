"""Dos reglas de venta que viven en el prompt de Mariana.

Un prompt no se puede testear como código: no se puede afirmar qué va a
responder el modelo. Lo que sí se puede fijar es que la INSTRUCCIÓN esté
presente y no se pierda en una edición futura — que es como se rompen los
prompts largos, borrando un párrafo sin notarlo.

Las dos salieron de una conversación real (2026-08-24): un cliente se enfrió
al ver $1.099.000 / $2.199.000 y no hubo alternativa más barata que ofrecerle
al retomar; y la insistencia con el anticipo estaba cansando a los clientes.
"""
from conftest import app_module as A

PROMPT = A.NOXA_SYSTEM_PROMPT


class TestAlternativaEconomica:
    def test_el_seguimiento_ofrece_una_puerta_mas_barata(self):
        assert "Puerta de entrada más económica" in PROMPT
        assert "corrección de pintura" in PROMPT.lower()

    def test_esta_en_el_seguimiento_y_no_en_la_venta_inmediata(self):
        """Se ofrece AL RETOMAR, no apenas el cliente ve el precio."""
        seguimiento = PROMPT.index("# SEGUIMIENTO A LEADS EN SILENCIO")
        siguiente = PROMPT.index("# TRATO Y TONO")
        bloque = PROMPT[seguimiento:siguiente]
        assert "Puerta de entrada más económica" in bloque
        # Va en el PRIMER toque: es el único que escribe Mariana con el
        # contexto de la conversación. El segundo sale como plantilla fija y no
        # puede adaptarse a que el precio haya sido la objeción.
        assert "primer_toque" in bloque

    def test_se_presenta_como_otro_servicio_y_no_como_descuento(self):
        """Presentarlo como rebaja entrena al cliente a esperar descuentos y
        devalúa el cerámico ya cotizado."""
        assert "NO es un descuento" in PROMPT
        assert "Nunca digas ni insinúes que le vas a bajar el precio" in PROMPT

    def test_el_precio_sale_del_bloque_vigente_y_no_del_prompt(self):
        """La regla existente es 'nunca cotices una cifra que no esté aquí'.
        Escribir el precio de la corrección a mano acá lo desactualizaría en
        silencio apenas alguien lo cambie en el panel."""
        assert "PRECIOS VIGENTES" in PROMPT
        assert "inventar un valor es peor que no darlo" in PROMPT


class TestIntensidadDelAnticipo:
    def test_mariana_no_saca_el_anticipo_por_su_cuenta(self):
        assert "El anticipo es una respuesta, no un gancho" in PROMPT
        assert "No lo saques tú" in PROMPT

    def test_no_se_repite_si_el_cliente_no_lo_tomo(self):
        assert "Una sola vez" in PROMPT
        assert "Que no responda a eso ya es una respuesta" in PROMPT

    def test_no_se_usa_como_condicion_para_avanzar(self):
        assert "Nunca como condición para avanzar" in PROMPT
        assert "El diagnóstico es gratis y no requiere anticipo" in PROMPT

    def test_la_regla_vive_junto_a_los_medios_de_pago(self):
        pagos = PROMPT.index("# MEDIOS DE PAGO")
        siguiente = PROMPT.index("# HORARIO DE ATENCIÓN")
        assert "no un gancho" in PROMPT[pagos:siguiente]


class TestNoSeRompioLoQueYaEstaba:
    def test_estan_las_dos_etapas_de_seguimiento(self):
        """Eran cuatro (24h, +2d, +5d, +14d) y pasaron a dos: al día siguiente
        y a la semana. Si el prompt nombrara etapas que el código ya no manda,
        Mariana escribiría el mensaje de una etapa que no existe."""
        for etapa in A._FOLLOWUP_STAGES:
            assert f"**{etapa}**" in PROMPT, f"el prompt no explica la etapa {etapa}"
        for vieja in ("ancla_de_valor", "check_in_breve", "ultima_oportunidad"):
            assert f"**{vieja}**" not in PROMPT, f"quedó viva la etapa vieja {vieja}"

    def test_sigue_la_regla_de_no_dar_descuentos(self):
        assert "nunca descuento" in PROMPT

    def test_siguen_los_datos_de_transferencia(self):
        for dato in ("Bre-B", "Daviplata", "Nequi"):
            assert dato in PROMPT

    def test_el_cierre_de_la_semana_no_reabre_la_venta(self):
        """El segundo toque cierra el ciclo; no es otra oportunidad de vender.
        Y de todos modos sale como plantilla, así que prometer algo distinto
        acá sería describir un mensaje que Mariana no escribe."""
        i = PROMPT.index("**cierre_semana**")
        bloque = PROMPT[i:i + 600]
        assert "es el último intento automático" in bloque
        assert "Sin presión y sin reproche" in bloque
