"""El nombre de perfil de WhatsApp casi nunca es un nombre.

Mariana saludaba con "Hola 👍👍☀️☀️" porque se le pasaba el ProfileName tal cual.
El prompt YA decía que no usara emojis como nombre; el problema es que la línea
del perfil se inyecta al final del system prompt, donde más pesa, y un dato
concreto de último momento ("el cliente se llama X") le gana a la regla general.

Por eso el filtro es de código: si no parece un nombre, al modelo no le llega
ninguno.
"""
import pytest

from conftest import app_module as A


class TestNombresQueSeUsan:
    @pytest.mark.parametrize("nombre", [
        "Andrés Rojas",
        "Camila",
        "María José Peña",
        "jorge alvarez pauta",
        "Ana",
    ])
    def test_un_nombre_de_persona_pasa(self, nombre):
        assert A._nombre_perfil_utilizable(nombre) == " ".join(nombre.split())


class TestNombresQueSeDescartan:
    @pytest.mark.parametrize("nombre,por_que", [
        ("👍👍☀️☀️",        "el caso real que disparó esto"),
        ("",                "perfil vacío"),
        (None,              "sin perfil"),
        ("   ",             "solo espacios"),
        ("+573214787284",   "es el teléfono, no un nombre"),
        ("3001234567",      "un número tampoco"),
        ("Carro2020",       "lleva dígitos"),
        ("🔥",              "un solo emoji"),
        ("A",               "una letra no es un nombre"),
        ("🔥🔥🔥 J 🔥🔥🔥",   "mayoría de decorado"),
    ])
    def test_no_se_le_pasa_al_modelo(self, nombre, por_que):
        assert A._nombre_perfil_utilizable(nombre) is None, por_que


class TestLineaDelPrompt:
    def _conv(self, nombre):
        return A.Conversation(phone="+573001199999", profile_name=nombre)

    def test_con_nombre_real_se_lo_pasa(self):
        linea = A._linea_perfil(self._conv("Andrés Rojas"))
        assert "Andrés Rojas" in linea
        assert "no disponible" not in linea

    def test_con_emojis_le_dice_que_no_hay_nombre(self):
        """Y además se lo prohíbe explícitamente: sin esa frase el modelo tiende
        a reutilizar lo que sea que vea del perfil."""
        linea = A._linea_perfil(self._conv("👍👍☀️☀️"))

        assert "no disponible" in linea
        assert "👍" not in linea
        assert "NO inventes un nombre" in linea

    def test_el_telefono_nunca_llega_como_nombre(self):
        linea = A._linea_perfil(self._conv("+573214787284"))
        assert "573214787284" not in linea
        assert "no disponible" in linea
