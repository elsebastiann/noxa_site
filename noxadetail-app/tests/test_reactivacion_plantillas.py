"""Elección de plantilla en la reactivación de leads fríos.

Todo lo que sale fuera de la ventana de 24h de WhatsApp necesita una plantilla
aprobada por Meta, o se rechaza con 63016 y se pierde en silencio. Con la cadencia de dos toques solo se usan dos plantillas, y cada una por una
razón distinta: el SEGUNDO toque va siempre fuera de la ventana, así que su
plantilla es el camino normal; la del primero es un plan B que solo entra
cuando la franja de atención (9am-6pm) lo empuja fuera de las 24 horas.

`_ya_se_cotizo` sigue probándose acá aunque ya no elija plantilla: la usa el
prompt de Mariana para decidir el ángulo del primer toque.
"""
import itertools

import app as A

# `phone` es único en whatsapp_conversations y estos tests no limpian esa tabla,
# así que cada conversación necesita su propio número.
_telefonos = itertools.count(1)


def _conversacion(mensajes):
    """Conversación con los mensajes dados, como (direccion, texto)."""
    conv = A.Conversation(phone=f"+5730011{next(_telefonos):05d}", profile_name="Andrés")
    A.db.session.add(conv)
    A.db.session.flush()
    for direction, body in mensajes:
        A.db.session.add(A.Message(conversation_id=conv.id, direction=direction, body=body))
    A.db.session.commit()
    return conv


class TestYaSeCotizo:
    def test_detecta_precio_que_mando_mariana(self, client):
        conv = _conversacion([
            ("in", "hola, cuánto vale el cerámico?"),
            ("out", "Para tu SUV el cerámico 9H queda en $2.199.000 con 5 años de garantía."),
        ])
        assert A._ya_se_cotizo(conv) is True

    def test_sin_precio_no_lo_da_por_cotizado(self, client):
        conv = _conversacion([
            ("in", "hola, quiero cuidar mi carro"),
            ("out", "Claro que sí, ¿qué vehículo tienes?"),
        ])
        assert A._ya_se_cotizo(conv) is False

    def test_un_numero_suelto_no_cuenta_como_precio(self, client):
        """'3 años' o '15 minutos' no son cotizaciones."""
        conv = _conversacion([
            ("out", "El diagnóstico toma 15 minutos y la garantía es de 3 años."),
        ])
        assert A._ya_se_cotizo(conv) is False

    def test_precio_que_escribio_el_cliente_no_cuenta(self, client):
        """Que el cliente diga 'me cobraron $800.000 en otro lado' no significa
        que nosotros le hayamos cotizado."""
        conv = _conversacion([
            ("in", "en otro lado me cobraron $800.000, ustedes cuánto?"),
        ])
        assert A._ya_se_cotizo(conv) is False


class TestPlantillaPorEtapa:
    def test_el_cierre_de_la_semana_usa_la_de_ultima_oportunidad(self, client, monkeypatch):
        """Es el texto aprobado que dice "este es el último por ahora", que es
        exactamente lo que este mensaje es."""
        monkeypatch.setitem(A.TPL_REACTIVACION, "ultima_oportunidad", "HXultima")
        conv = _conversacion([("out", "El cerámico queda en $1.099.000.")])

        sid, clave = A._tpl_reactivacion_para("cierre_semana", conv)
        assert sid == "HXultima"
        assert clave == "ultima_oportunidad"

    def test_el_primer_toque_tiene_plan_b(self, client, monkeypatch):
        """Casi siempre sale como texto libre, pero cuando la franja de
        atención lo empuja fuera de las 24h tiene que haber una plantilla: sin
        SID el mensaje se rechaza con 63016 y el lead no recibe nada."""
        monkeypatch.setitem(A.TPL_REACTIVACION, "reactivacion_suave", "HXsuave")
        conv = _conversacion([("out", "¿Qué vehículo tienes?")])

        assert A._tpl_reactivacion_para("primer_toque", conv)[0] == "HXsuave"

    def test_ninguna_etapa_se_queda_sin_plantilla(self, client, monkeypatch):
        """Cada etapa que el job pueda mandar tiene que resolver a un SID y a un
        texto. Una etapa sin plantilla no falla: manda vacío y el cliente no
        recibe nada."""
        monkeypatch.setitem(A.TPL_REACTIVACION, "reactivacion_suave", "HXsuave")
        monkeypatch.setitem(A.TPL_REACTIVACION, "ultima_oportunidad", "HXultima")
        conv = _conversacion([("out", "hola")])

        for etapa in A._FOLLOWUP_STAGES:
            sid, clave = A._tpl_reactivacion_para(etapa, conv)
            assert sid, f"{etapa} se quedó sin SID"
            assert A._TEXTO_REACTIVACION.get(clave), f"{etapa} se quedó sin texto"


class TestTextoQueQuedaEnElPanel:
    """Lo que se guarda tiene que ser lo que el cliente leyó.

    Al principio se guardaba un marcador tipo '[Plantilla de reactivación: X]',
    y eso dejaba ciegos a los dos que necesitan el contexto: quien atiende desde
    el panel, y Mariana misma —que recibe el historial y podría repetirse o
    contradecir lo que ya dijo.
    """

    def test_cada_etapa_tiene_su_texto(self, client):
        conv = _conversacion([("out", "hola")])
        for stage in A._FOLLOWUP_STAGES:
            _, clave = A._tpl_reactivacion_para(stage, conv)
            assert clave in A._TEXTO_REACTIVACION, f"falta el texto de {stage}"

    def test_el_texto_lleva_el_nombre_del_cliente(self, client):
        for clave, plantilla in A._TEXTO_REACTIVACION.items():
            texto = plantilla.format(nombre="Andrés")
            assert "Andrés" in texto, f"{clave} no usa el nombre"
            assert "{nombre}" not in texto, f"{clave} quedó sin sustituir"

    def test_ningun_texto_parece_un_marcador_interno(self, client):
        """Un '[algo]' suelto es señal de que volvió el placeholder."""
        for clave, plantilla in A._TEXTO_REACTIVACION.items():
            assert not plantilla.strip().startswith("["), f"{clave} parece un marcador"
            assert "Mariana" in plantilla, f"{clave} no se presenta"
