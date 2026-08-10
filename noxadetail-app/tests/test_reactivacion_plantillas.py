"""Elección de plantilla en la reactivación de leads fríos.

Todo lo que sale fuera de la ventana de 24h de WhatsApp necesita una plantilla
aprobada por Meta, o se rechaza con 63016 y se pierde en silencio. El SOP de
NOXA pide además que el ángulo cambie en cada intento, y que el segundo intento
se bifurque: reencuadre de valor a quien ya recibió una cotización, diagnóstico
gratuito a quien nunca preguntó precio. Hablarle del costo a alguien que nunca
lo preguntó suena a excusa inventada, así que esa bifurcación es la que se
prueba acá.
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
    def test_segundo_intento_se_bifurca_segun_si_hubo_cotizacion(self, client, monkeypatch):
        monkeypatch.setattr(A, "TPL_REACTIVACION_2_COTIZADO", "HXcotizado")
        monkeypatch.setattr(A, "TPL_REACTIVACION_2_SIN_COTIZAR", "HXsincotizar")

        cotizado = _conversacion([("out", "El cerámico 7H+ queda en $1.099.000.")])
        sin_cotizar = _conversacion([("out", "¿Qué vehículo tienes?")])

        assert A._tpl_reactivacion_para("ancla_de_valor", cotizado) == "HXcotizado"
        assert A._tpl_reactivacion_para("ancla_de_valor", sin_cotizar) == "HXsincotizar"

    def test_las_demas_etapas_no_dependen_de_la_cotizacion(self, client, monkeypatch):
        monkeypatch.setitem(A.TPL_REACTIVACION, "reactivacion_suave", "HXsuave")
        monkeypatch.setitem(A.TPL_REACTIVACION, "check_in_breve", "HXcheckin")
        monkeypatch.setitem(A.TPL_REACTIVACION, "ultima_oportunidad", "HXultima")

        conv = _conversacion([("out", "El cerámico queda en $1.099.000.")])

        assert A._tpl_reactivacion_para("reactivacion_suave", conv) == "HXsuave"
        assert A._tpl_reactivacion_para("check_in_breve", conv) == "HXcheckin"
        assert A._tpl_reactivacion_para("ultima_oportunidad", conv) == "HXultima"

    def test_etapa_desconocida_devuelve_vacio(self, client):
        """Sin SID el envío cae a texto libre en vez de reventar."""
        conv = _conversacion([("out", "hola")])
        assert A._tpl_reactivacion_para("etapa_que_no_existe", conv) == ""
