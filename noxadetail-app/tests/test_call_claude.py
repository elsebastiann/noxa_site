"""Cuando Claude no devuelve texto, el error tiene que decir POR QUÉ.

El 2026-08-19 esto falló cuatro veces en una tarde en producción y dejó a un
cliente sin respuesta. El log solo decía "Claude no devolvió texto", que
descarta justo el dato que lo explica: las dos causas posibles —techo de
tokens agotado, o negativa del modelo— se arreglan de forma opuesta, así que
sin el `stop_reason` no se puede decidir nada.
"""
from types import SimpleNamespace
from unittest.mock import MagicMock, patch

import pytest

from conftest import app_module as A


def _bloque(texto):
    return SimpleNamespace(type="text", text=texto)


def _respuesta(texto="", stop_reason="end_turn", tipos=None, output_tokens=42):
    content = [_bloque(texto)] if texto else [
        SimpleNamespace(type=t, text="") for t in (tipos or [])
    ]
    return SimpleNamespace(content=content, stop_reason=stop_reason,
                           usage=SimpleNamespace(output_tokens=output_tokens))


def _cliente(respuestas):
    """Cliente falso que devuelve una respuesta distinta por llamada."""
    cliente = MagicMock()
    cliente.messages.create.side_effect = list(respuestas)
    return cliente


class TestRespuestaNormal:
    def test_devuelve_los_trozos(self):
        with patch.object(A, "_get_claude_client",
                          return_value=_cliente([_respuesta("Hola\n---\n¿Cómo vas?")])):
            with A.app.app_context():
                assert A._call_claude([], "") == ["Hola", "¿Cómo vas?"]

    def test_sin_separador_es_un_solo_mensaje(self):
        with patch.object(A, "_get_claude_client",
                          return_value=_cliente([_respuesta("Un solo mensaje")])):
            with A.app.app_context():
                assert A._call_claude([], "") == ["Un solo mensaje"]


class TestElErrorExplica:
    def test_incluye_stop_reason_bloques_y_tokens(self):
        """Sin estos tres datos el fallo es indiagnosticable, que es exactamente
        lo que pasó en producción."""
        resp = _respuesta("", stop_reason="refusal", tipos=["thinking"], output_tokens=137)
        with patch.object(A, "_get_claude_client", return_value=_cliente([resp])):
            with A.app.app_context():
                with pytest.raises(ValueError) as exc:
                    A._call_claude([], "")
        msg = str(exc.value)
        assert "refusal" in msg
        assert "thinking" in msg
        assert "137" in msg

    def test_una_negativa_no_se_reintenta(self):
        """Reintentar una negativa da lo mismo y gasta llamadas: se falla de una."""
        cliente = _cliente([_respuesta("", stop_reason="refusal")])
        with patch.object(A, "_get_claude_client", return_value=cliente):
            with A.app.app_context():
                with pytest.raises(ValueError):
                    A._call_claude([], "")
        assert cliente.messages.create.call_count == 1


class TestTechoDeTokens:
    def test_vacio_por_max_tokens_reintenta_con_mas_espacio(self):
        cliente = _cliente([
            _respuesta("", stop_reason="max_tokens"),
            _respuesta("Ahora sí alcancé a responder"),
        ])
        with patch.object(A, "_get_claude_client", return_value=cliente):
            with A.app.app_context():
                assert A._call_claude([], "") == ["Ahora sí alcancé a responder"]

        assert cliente.messages.create.call_count == 2
        primero = cliente.messages.create.call_args_list[0].kwargs["max_tokens"]
        segundo = cliente.messages.create.call_args_list[1].kwargs["max_tokens"]
        assert segundo > primero, "el reintento tiene que pedir más espacio, no repetir igual"
        assert segundo == A.CLAUDE_MAX_TOKENS_REINTENTO

    def test_solo_reintenta_una_vez(self):
        """Si con el doble tampoco alcanza, se falla — no se escala sin fin."""
        cliente = _cliente([
            _respuesta("", stop_reason="max_tokens"),
            _respuesta("", stop_reason="max_tokens"),
        ])
        with patch.object(A, "_get_claude_client", return_value=cliente):
            with A.app.app_context():
                with pytest.raises(ValueError) as exc:
                    A._call_claude([], "")
        assert cliente.messages.create.call_count == 2
        assert "max_tokens" in str(exc.value)

    def test_con_texto_truncado_no_reintenta_sino_que_recorta(self):
        """Si alcanzó a escribir algo, se recorta a la última frase completa en
        vez de gastar otra llamada."""
        cliente = _cliente([
            _respuesta("Claro que sí. Te cuento que el cerámi", stop_reason="max_tokens"),
        ])
        with patch.object(A, "_get_claude_client", return_value=cliente):
            with A.app.app_context():
                chunks = A._call_claude([], "")
        assert cliente.messages.create.call_count == 1
        assert chunks == ["Claro que sí."]
