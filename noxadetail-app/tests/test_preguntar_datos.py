"""Preguntarle a los datos en lenguaje natural.

Acá el modelo escribe SQL que se ejecuta contra la base del negocio, así que
lo que hay que probar no es que las respuestas sean bonitas sino que el diseño
NO dependa de que el modelo se porte bien: la conexión es de solo lectura, hay
tablas vetadas, y el permiso es de dos personas.
"""
import json
from types import SimpleNamespace
from unittest.mock import MagicMock, patch

import pytest

from conftest import app_module as A
from conftest import login_as, make_user


def _claude_responde(payload):
    """Cliente falso que devuelve el JSON que normalmente arma el modelo."""
    cli = MagicMock()
    texto = payload if isinstance(payload, str) else json.dumps(payload)
    cli.messages.create.return_value = SimpleNamespace(
        content=[SimpleNamespace(type="text", text=texto)],
        stop_reason="end_turn",
        usage=SimpleNamespace(output_tokens=50),
    )
    return cli


class TestQuienPuedeEntrar:
    def test_sa_entra(self, client):
        login_as(client, make_user("sa", role="admin"))
        assert client.get("/preguntar").status_code == 200

    def test_diana_entra(self, client):
        login_as(client, make_user("diana", role="admin"))
        assert client.get("/preguntar").status_code == 200

    def test_otro_admin_no(self, client):
        """Preguntarle a la data da acceso a toda la plata de una forma que
        ningún tablero permite: no basta con ser admin."""
        login_as(client, make_user("otro_admin_pg", role="admin"))
        assert client.get("/preguntar", follow_redirects=False).status_code == 302

    def test_la_api_le_responde_403_a_un_admin_no_autorizado(self, client):
        """Un admin pasa el allowlist global, así que llega hasta la ruta y es
        MI candado el que lo frena. Es el caso que de verdad prueba el permiso."""
        login_as(client, make_user("otro_admin_api", role="admin"))
        r = client.post("/api/preguntar", json={"pregunta": "cuánto entró"})
        assert r.status_code == 403

    def test_al_operario_lo_frena_el_allowlist_global(self, client):
        """Queda fuera antes de llegar a la ruta: dos capas, y la de afuera
        actúa primero (302 al calendario, no 403)."""
        login_as(client, make_user("op_pg", role="operario"))
        r = client.post("/api/preguntar", json={"pregunta": "cuánto entró"})
        assert r.status_code in (302, 403)

    def test_el_menu_no_lo_muestra_a_quien_no_puede(self, client):
        login_as(client, make_user("otro_admin_pg2", role="admin"))
        html = client.get("/calendar").get_data(as_text=True)
        assert "Pregúntale a los datos" not in html


class TestValidacionDelSQL:
    @pytest.mark.parametrize("sql,fragmento", [
        ("DELETE FROM services", "SELECT"),
        ("UPDATE services SET name='x'", "SELECT"),
        ("DROP TABLE appointments", "SELECT"),
        ("SELECT 1; DROP TABLE x", "más de una sentencia"),
        ("SELECT * FROM users", "no está disponible"),
        ("PRAGMA table_info(users)", "SELECT"),
        ("", "vacía"),
    ])
    def test_rechaza_lo_peligroso(self, sql, fragmento):
        motivo = A._sql_es_de_lectura(sql)
        assert motivo is not None, f"dejó pasar: {sql!r}"
        assert fragmento.lower() in motivo.lower()

    @pytest.mark.parametrize("sql", [
        "SELECT COUNT(*) FROM appointments",
        "WITH x AS (SELECT 1 AS n) SELECT n FROM x",
        "SELECT name FROM services LIMIT 10;",
    ])
    def test_acepta_lecturas(self, sql):
        assert A._sql_es_de_lectura(sql) is None


class TestSoloLectura:
    """La validación se podría burlar; la conexión no. Este es el candado real."""

    @pytest.mark.parametrize("sql", [
        "DELETE FROM services",
        "UPDATE services SET name='x'",
        "DROP TABLE services",
    ])
    def test_el_motor_bloquea_la_escritura(self, sql):
        with A.app.app_context():
            antes = A.db.session.execute(A.db.text("SELECT COUNT(*) FROM services")).scalar()
            with pytest.raises(Exception) as exc:
                A._ejecutar_consulta_lectura(sql)   # saltándose la validación a propósito
            assert "readonly" in str(exc.value).lower()
            despues = A.db.session.execute(A.db.text("SELECT COUNT(*) FROM services")).scalar()
        assert antes == despues

    def test_leer_sí_funciona(self):
        with A.app.app_context():
            cols, filas = A._ejecutar_consulta_lectura("SELECT COUNT(*) AS n FROM services")
        assert cols == ["n"] and len(filas) == 1


class TestEsquema:
    def test_no_expone_las_tablas_vetadas(self):
        """`users` tiene los hashes de contraseñas: no entra ni al prompt."""
        with A.app.app_context():
            esquema = A._esquema_para_preguntas()
        for tabla in A.TABLAS_VETADAS:
            assert f"{tabla}(" not in esquema

    def test_si_expone_las_del_negocio(self):
        with A.app.app_context():
            esquema = A._esquema_para_preguntas()
        for tabla in ("appointments(", "service_sales(", "clients("):
            assert tabla in esquema

    def test_se_lee_de_la_base_y_no_de_una_lista_a_mano(self):
        """Escrito a mano se desactualizaría con la próxima migración y el
        modelo empezaría a inventar columnas."""
        with A.app.app_context():
            esquema = A._esquema_para_preguntas()
        assert "seguimiento_pausado_hasta" in esquema, "no refleja el esquema real"


class TestFlujoCompleto:
    def _preguntar(self, client, plan, pregunta="cuántos servicios hay"):
        login_as(client, make_user("sa", role="admin"))
        with patch.object(A, "_get_claude_client", return_value=_claude_responde(plan)):
            return client.post("/api/preguntar", json={"pregunta": pregunta}).get_json()

    def test_devuelve_datos_y_el_sql(self, client):
        r = self._preguntar(client, {
            "sql": "SELECT COUNT(*) AS total FROM services",
            "gráfica": "kpi", "titulo": "Servicios", "explicacion": "Cuántos hay.",
        })
        assert "error" not in r
        assert r["grafica"] == "kpi"
        assert r["columnas"] == ["total"]
        assert r["sql"].startswith("SELECT")

    def test_un_sql_peligroso_no_se_ejecuta(self, client):
        r = self._preguntar(client, {"sql": "DELETE FROM services", "gráfica": "tabla"})
        assert "error" in r
        assert "rechaz" in r["error"].lower()

    def test_json_malo_devuelve_error_entendible(self, client):
        r = self._preguntar(client, "esto no es json")
        assert "error" in r
        assert "reformular" in r["error"].lower()

    def test_tolera_el_json_envuelto_en_bloque_de_codigo(self, client):
        """El modelo a veces lo envuelve pese a la instrucción; se limpia en vez
        de fallar."""
        plan = json.dumps({"sql": "SELECT COUNT(*) AS n FROM services",
                           "gráfica": "kpi", "titulo": "T", "explicacion": ""})
        r = self._preguntar(client, f"```json\n{plan}\n```")
        assert "error" not in r
        assert r["columnas"] == ["n"]

    def test_sin_pregunta_no_llama_al_modelo(self, client):
        login_as(client, make_user("sa", role="admin"))
        r = client.post("/api/preguntar", json={"pregunta": "   "})
        assert r.status_code == 400


class TestCosto:
    """El costo se calcula del uso REAL que reporta la API, no de una
    estimación. Lo delicado es el caché: el prompt del sistema va cacheado, así
    que la mayor parte de la entrada se paga a un décimo a partir de la segunda
    pregunta seguida."""

    def _uso(self, entrada=0, escritura=0, lectura=0, salida=0):
        return SimpleNamespace(input_tokens=entrada, cache_creation_input_tokens=escritura,
                               cache_read_input_tokens=lectura, output_tokens=salida)

    def test_entrada_y_salida_a_tarifa_plena(self):
        # 1M de entrada = $2 ; 1M de salida = $10
        c = A._costo_de_la_llamada(self._uso(entrada=1_000_000), "claude-sonnet-5")
        assert round(c["usd"], 2) == 2.00
        c = A._costo_de_la_llamada(self._uso(salida=1_000_000), "claude-sonnet-5")
        assert round(c["usd"], 2) == 10.00

    def test_escribir_al_cache_cuesta_25_por_ciento_mas(self):
        c = A._costo_de_la_llamada(self._uso(escritura=1_000_000), "claude-sonnet-5")
        assert round(c["usd"], 2) == 2.50

    def test_leer_del_cache_cuesta_una_decima_parte(self):
        c = A._costo_de_la_llamada(self._uso(lectura=1_000_000), "claude-sonnet-5")
        assert round(c["usd"], 2) == 0.20

    def test_el_total_de_entrada_suma_los_tres_campos(self):
        """`input_tokens` es SOLO el remanente no cacheado. Contarlo solo a él
        subestima el tamaño justo cuando el caché está funcionando."""
        c = A._costo_de_la_llamada(self._uso(entrada=100, escritura=200, lectura=300), "claude-sonnet-5")
        assert c["tokens_entrada"] == 600
        assert c["tokens_de_cache"] == 300

    def test_leer_del_cache_sale_mucho_mas_barato_que_escribirlo(self):
        mismo = 5000
        escribe = A._costo_de_la_llamada(self._uso(escritura=mismo), "claude-sonnet-5")["usd"]
        lee = A._costo_de_la_llamada(self._uso(lectura=mismo), "claude-sonnet-5")["usd"]
        assert lee < escribe / 10

    def test_tolera_un_usage_incompleto(self):
        """No todas las respuestas traen los campos de caché."""
        c = A._costo_de_la_llamada(SimpleNamespace(input_tokens=10, output_tokens=5), "claude-sonnet-5")
        assert c["usd"] > 0

    def test_la_respuesta_de_la_api_incluye_el_costo(self, client):
        login_as(client, make_user("sa", role="admin"))
        plan = {"sql": "SELECT COUNT(*) AS n FROM services", "gráfica": "kpi",
                "titulo": "T", "explicacion": ""}
        with patch.object(A, "_get_claude_client", return_value=_claude_responde(plan)):
            r = client.post("/api/preguntar", json={"pregunta": "x"}).get_json()
        assert "costo" in r
        assert r["costo"]["usd"] >= 0 and "cop" in r["costo"]

    def test_tambien_se_cobra_cuando_el_sql_se_rechaza(self, client):
        """La llamada al modelo ya se pagó aunque después se rechace el SQL:
        ocultarlo haría que el acumulado mienta."""
        login_as(client, make_user("sa", role="admin"))
        with patch.object(A, "_get_claude_client",
                          return_value=_claude_responde({"sql": "DELETE FROM services", "gráfica": "tabla"})):
            r = client.post("/api/preguntar", json={"pregunta": "x"}).get_json()
        assert "error" in r and "costo" in r


class TestPromptExigeDosColumnas:
    """Con tres columnas la gráfica salía con TODAS las barras en cero: el
    frontend tomaba la segunda columna como valor, ahí venía texto,
    Number("Gustavo Pauta") daba NaN y el `|| 0` lo volvía cero sin un solo
    error. Visto en producción el 2026-08-28.

    El arreglo real es que el frontend busque la última columna numérica (no se
    puede probar desde acá, es JavaScript). Esto cubre la otra mitad: que el
    prompt lo pida explícito, para que el caso raro sea aún más raro."""

    # El prompt viene envuelto a 79 columnas, así que las frases se parten en
    # varias líneas: se compara con los espacios normalizados y no crudo.
    PROMPT = " ".join(A.PROMPT_CONSULTAS.split())

    def test_pide_exactamente_dos_columnas_para_graficar(self):
        assert "EXACTAMENTE DOS columnas" in self.PROMPT

    def test_explica_como_evitar_la_tercera(self):
        assert "únelos en una sola columna" in self.PROMPT
        assert "una tercera columna rompe la gráfica" in self.PROMPT

    def test_ofrece_la_tabla_como_salida_para_mas_columnas(self):
        assert 'Si de verdad necesitas más columnas, usa "tabla"' in self.PROMPT

    def test_tres_columnas_igual_se_ejecutan_y_devuelven(self, client):
        """El backend no debe rechazarlas: son un SQL válido, y la tabla las
        muestra bien. El problema era solo cómo las graficaba el navegador."""
        login_as(client, make_user("sa", role="admin"))
        plan = {"sql": "SELECT name AS a, name AS b, COUNT(*) AS n FROM services GROUP BY name",
                "gráfica": "barras", "titulo": "T", "explicacion": ""}
        with patch.object(A, "_get_claude_client", return_value=_claude_responde(plan)):
            r = client.post("/api/preguntar", json={"pregunta": "x"}).get_json()
        assert "error" not in r
        assert len(r["columnas"]) == 3


class TestDefinicionDeIngresos:
    """Reglas de negocio que el prompt tiene que seguir declarando.

    La versión anterior de esta clase probaba una redacción que pedía calcular
    la plata en SQL — se reemplazó cuando esa vía resultó inviable (ver
    TestTablaDeIngresos). Lo que sobrevive son las reglas que siguen vigentes.
    """
    PROMPT = " ".join(A.PROMPT_CONSULTAS.split())

    def test_los_diagnosticos_no_son_ingreso(self):
        assert "Los diagnósticos son GRATIS y no son ingreso" in self.PROMPT

    def test_toda_cita_en_agenda_cuenta_sin_importar_su_estado(self):
        """La regla del negocio: si quedó en la agenda, se asume ejecutada."""
        assert "las canceladas no entran" in self.PROMPT
        assert "'scheduled' cuenta igual que una 'completed'" in self.PROMPT

    def test_sigue_la_regla_del_abono(self):
        assert "Un ABONO (appointment_payments) NO es un descuento" in self.PROMPT

    def test_distingue_lo_que_cobra_de_lo_que_le_queda_al_negocio(self):
        assert "`ingreso_noxa` = lo que queda para NOXA" in self.PROMPT

    def test_los_gastos_siguen_saliendo_de_expenses(self):
        assert "Los GASTOS sí viven en `expenses`" in self.PROMPT


class TestTablaDeIngresos:
    """El monto de una cita NO está en la base: se calcula en Python con
    service_prices, el convenio y los ajustes, y una cita sin venta cerrada
    vale su estimado.

    Pedirle al modelo que lo resolviera en SQL era imposible: las citas sin
    venta salían en 0, y en la práctica eran casi todas — una pregunta por
    ventas de cerámico daba 14 días en cero. Ahora el cálculo lo hace
    `_transacciones_citas()`, la misma que alimenta Analítica, y se materializa
    en una tabla temporal que el modelo solo agrega.
    """

    def test_la_tabla_existe_en_la_consulta(self):
        with A.app.app_context():
            cols, _ = A._ejecutar_consulta_lectura("SELECT * FROM ingresos LIMIT 1")
        for c in ("fecha", "monto", "servicios", "es_diagnostico", "ingreso_noxa"):
            assert c in cols

    def test_una_cita_sin_venta_cerrada_igual_trae_su_monto(self):
        """El caso exacto que fallaba en producción."""
        import datetime as dt
        with A.app.app_context():
            vt = A.VehicleType.query.filter_by(is_active=True).first()
            svc = A.Service(name="Servicio Sin Venta", duration_minutes=60, is_active=True)
            A.db.session.add(svc)
            A.db.session.commit()
            A.db.session.add(A.ServicePrice(service_id=svc.id, vehicle_type_id=vt.id,
                                            price=777000, duration_minutes=60, is_active=True))
            ini = A.bogota_now().replace(hour=9, minute=0, second=0, microsecond=0)
            appt = A.Appointment(customer_name="C", plate="SVT001", phone="3001112233",
                                 services=svc.name, start_datetime=ini,
                                 end_datetime=ini + dt.timedelta(hours=1),
                                 vehicle_type_id=vt.id, status="scheduled")
            A.db.session.add(appt)
            A.db.session.commit()
            ids = (appt.id, svc.id)
        try:
            with A.app.app_context():
                assert A.ServiceSale.query.filter_by(plate="SVT001").count() == 0
                _c, filas = A._ejecutar_consulta_lectura(
                    "SELECT monto FROM ingresos WHERE placa = 'SVT001'")
            assert filas and filas[0][0] == 777000, "una cita sin venta volvió a salir en cero"
        finally:
            with A.app.app_context():
                A.db.session.delete(A.Appointment.query.get(ids[0]))
                A.ServicePrice.query.filter_by(service_id=ids[1]).delete()
                A.db.session.delete(A.Service.query.get(ids[1]))
                A.db.session.commit()

    def test_la_tabla_temporal_no_puede_escribir_en_la_base_real(self):
        """Montarla no puede haber abierto un hueco: la conexión sigue siendo
        de solo lectura para todo lo demás."""
        with A.app.app_context():
            with pytest.raises(Exception) as exc:
                A._ejecutar_consulta_lectura("DELETE FROM services")
            assert "readonly" in str(exc.value).lower()

    def test_la_tabla_aparece_en_el_esquema_del_modelo(self):
        with A.app.app_context():
            assert "ingresos(" in A._esquema_para_preguntas()

    def test_el_prompt_manda_usarla_para_plata(self):
        prompt = " ".join(A.PROMPT_CONSULTAS.split())
        assert "Para TODA pregunta de plata usa la tabla `ingresos`" in prompt
        assert "No la calcules desde `appointments` ni desde `service_sales`" in prompt

    def test_el_prompt_explica_excluir_diagnosticos(self):
        prompt = " ".join(A.PROMPT_CONSULTAS.split())
        assert "es_diagnostico = 0" in prompt


class TestVentasSinCita:
    """El parqueadero se vende sin cita. `_transacciones_citas()` solo recorre
    citas, así que sin agregarlas aparte quedaría fuera del total y nada lo
    advertiría — un ingreso real desapareciendo en silencio."""

    def test_una_venta_sin_cita_entra_a_ingresos(self):
        import datetime as dt
        with A.app.app_context():
            v = A.ServiceSale(appointment_id=None, service_date=dt.date(2026, 8, 20),
                              vehicle_type="N/A", plate="PKG999", customer_name="Parqueo",
                              services="Parqueadero", base_amount=7000, discount_amount=0,
                              final_amount=7000, status="completed")
            A.db.session.add(v)
            A.db.session.commit()
            vid = v.id
        try:
            with A.app.app_context():
                _c, filas = A._ejecutar_consulta_lectura(
                    "SELECT monto, servicios FROM ingresos WHERE placa = 'PKG999'")
            assert filas, "la venta sin cita no llegó a ingresos"
            assert filas[0][0] == 7000
        finally:
            with A.app.app_context():
                A.db.session.delete(A.ServiceSale.query.get(vid))
                A.db.session.commit()

    def test_no_se_cuenta_como_diagnostico(self):
        """Si entrara con es_diagnostico=1 se filtraría fuera de las cifras."""
        import datetime as dt
        with A.app.app_context():
            v = A.ServiceSale(appointment_id=None, service_date=dt.date(2026, 8, 20),
                              vehicle_type="N/A", plate="PKG998", customer_name="P",
                              services="Parqueadero", base_amount=7000, discount_amount=0,
                              final_amount=7000, status="completed")
            A.db.session.add(v)
            A.db.session.commit()
            vid = v.id
        try:
            with A.app.app_context():
                _c, filas = A._ejecutar_consulta_lectura(
                    "SELECT es_diagnostico FROM ingresos WHERE placa = 'PKG998'")
            assert filas[0][0] == 0
        finally:
            with A.app.app_context():
                A.db.session.delete(A.ServiceSale.query.get(vid))
                A.db.session.commit()
