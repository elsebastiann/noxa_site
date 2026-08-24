"""Parseo del marcador [META:] que Mariana emite en cada turno.

Un cliente dijo "es para un Hyundai elantra" y el carro nunca quedó registrado.
Investigando salió que el parseo era frágil de una forma traicionera: la regex
tenía el bloque de carro/marca/calificación como OPCIONAL, así que ante
cualquier variante igual DABA MATCH — el estado se leía bien y todo lo demás se
lo tragaba el campo `servicios`. El dato se perdía en silencio y en el panel
solo se veía un lead sin información.

Las tres variantes de abajo son las que un modelo produce de vez en cuando por
más que el prompt fije el formato.
"""
import pytest

from conftest import app_module as A


ESPERADO = {"estado": "En proceso", "servicios": "Cerámico",
            "carro": "Hyundai Elantra", "marca": "Hyundai", "calificacion": "3"}


class TestVariantesQueAntesPerdianElCarro:
    def test_calificacion_con_tilde(self):
        """Es como se escribe en español, así que el modelo lo hace solo."""
        campos = A._parse_meta(
            "estado=En proceso; servicios=Cerámico; carro=Hyundai Elantra; "
            "marca=Hyundai; calificación=3")
        assert campos["carro"] == "Hyundai Elantra"
        assert campos["calificacion"] == "3"

    def test_campos_en_otro_orden(self):
        campos = A._parse_meta(
            "estado=En proceso; servicios=Cerámico; marca=Hyundai; "
            "carro=Hyundai Elantra; calificacion=3")
        assert campos["carro"] == "Hyundai Elantra"
        assert campos["marca"] == "Hyundai"

    def test_falta_un_campo(self):
        """Sin marca, el carro y la calificación se seguían perdiendo."""
        campos = A._parse_meta(
            "estado=En proceso; servicios=Cerámico; carro=Hyundai Elantra; calificacion=3")
        assert campos["carro"] == "Hyundai Elantra"
        assert campos["calificacion"] == "3"
        assert "marca" not in campos


class TestFormatoCanonico:
    def test_el_formato_del_prompt_sigue_funcionando(self):
        campos = A._parse_meta(
            "estado=En proceso; servicios=Cerámico; carro=Hyundai Elantra; "
            "marca=Hyundai; calificacion=3")
        assert campos == ESPERADO

    def test_varios_servicios(self):
        campos = A._parse_meta(
            "estado=En proceso; servicios=Cerámico,PPF; carro=BMW M240i 2022; "
            "marca=BMW; calificacion=5")
        assert campos["servicios"] == "Cerámico,PPF"

    def test_sin_dato_se_conserva_tal_cual(self):
        """Quien decide qué hacer con "Sin dato" es el llamador, no el parseo."""
        campos = A._parse_meta(
            "estado=Iniciado; servicios=; carro=Sin dato; marca=Sin dato; calificacion=Sin dato")
        assert campos["carro"] == "Sin dato"
        assert campos["servicios"] == ""

    def test_espacios_de_sobra(self):
        campos = A._parse_meta(
            "estado = En proceso ;  servicios = Cerámico ; carro = Hyundai Elantra ; "
            "marca = Hyundai ; calificacion = 3 ")
        assert campos == ESPERADO


class TestBasura:
    def test_texto_sin_pares_no_devuelve_nada(self):
        assert A._parse_meta("no hay nada acá") is None

    def test_vacio(self):
        assert A._parse_meta("") is None
        assert A._parse_meta(None) is None


class TestElMarcadorCompleto:
    @pytest.mark.parametrize("texto", [
        "[META: estado=En proceso; servicios=Cerámico; carro=Hyundai Elantra; marca=Hyundai; calificacion=3]",
        "[meta: estado=En proceso; servicios=Cerámico; carro=Hyundai Elantra; marca=Hyundai; calificación=3]",
    ])
    def test_reconoce_el_marcador_y_saca_el_carro(self, texto):
        m = A._META_RE.match(texto)
        assert m is not None
        assert A._parse_meta(m.group(1))["carro"] == "Hyundai Elantra"

    def test_un_mensaje_normal_no_es_un_marcador(self):
        assert A._META_RE.match("Claro, con gusto te cuento.") is None
