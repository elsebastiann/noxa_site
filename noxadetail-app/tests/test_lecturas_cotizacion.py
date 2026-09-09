"""¿El cliente abrió la cotización que le mandamos?

Antes no se podía saber. Una cotización sin respuesta y una que el cliente nunca
abrió se veían exactamente igual, y son dos problemas distintos: la primera es
de precio o de producto, la segunda es de que el mensaje no llegó.

Lo que sostiene toda la métrica es el filtro de robots: cuando el link se pega
en WhatsApp, el robot de la vista previa entra ANTES que el cliente. Sin
filtrarlo, toda cotización aparecería como "abierta" en el segundo en que se
manda, y el dato diría exactamente lo contrario de lo que pasó.
"""
import itertools

import pytest

from conftest import app_module as A, make_user

_u = itertools.count(1)

NAVEGADOR = ("Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) "
             "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile Safari/604.1")


@pytest.fixture
def sesion(client):
    with A.app.app_context():
        uid = make_user(f"lec{next(_u)}", role="admin").id
    with client.session_transaction() as sess:
        sess["user_id"] = uid
    return client


@pytest.fixture
def cotizacion(sesion):
    r = sesion.post("/quotes/new", data={"customer_name": "Laura Ortiz",
                                         "ppf_coverage": ["Manijas"]},
                    follow_redirects=False)
    code = r.headers["Location"].rstrip("/").split("/")[-1]
    with A.app.app_context():
        token = A.Quote.query.filter_by(code=code).first().public_token
    yield {"code": code, "token": token}
    with A.app.app_context():
        c = A.Quote.query.filter_by(code=code).first()
        if c:
            A.db.session.delete(c)
            A.db.session.commit()


def _lecturas(code):
    with A.app.app_context():
        return A.Quote.query.filter_by(code=code).first().lecturas


def _abrir(client, token, agente=NAVEGADOR):
    with client.session_transaction() as sess:
        sess.clear()          # el cliente no tiene sesión
    return client.get(f"/c/{token}", headers={"User-Agent": agente})


class TestLosRobotsNoCuentanComoCliente:
    """Es la diferencia entre una métrica útil y una que siempre dice que sí."""

    @pytest.mark.parametrize("agente", [
        "WhatsApp/2.23.20.0 A",
        "facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)",
        "Mozilla/5.0 (compatible; Twitterbot/1.0)",
        "TelegramBot (like TwitterBot)",
        "Slackbot-LinkExpanding 1.0",
        "Mozilla/5.0 (compatible; Googlebot/2.1)",
        "curl/8.4.0",
        "python-requests/2.31.0",
    ])
    def test_una_vista_previa_no_es_una_apertura(self, client, cotizacion, agente):
        _abrir(client, cotizacion["token"], agente)
        assert _lecturas(cotizacion["code"])["abierta"] is False

    def test_sin_user_agent_tampoco(self, client, cotizacion):
        """Un cliente real siempre manda uno; lo que no lo manda es un script."""
        _abrir(client, cotizacion["token"], "")
        assert _lecturas(cotizacion["code"])["abierta"] is False

    def test_un_navegador_de_verdad_si_cuenta(self, client, cotizacion):
        """Contraprueba: si no, el filtro podría estar descartándolo todo y los
        tests de arriba pasarían igual."""
        _abrir(client, cotizacion["token"])
        assert _lecturas(cotizacion["code"])["abierta"] is True


class TestQueSePuedeSaberDeCadaCotizacion:
    def test_recien_creada_no_la_ha_visto_nadie(self, cotizacion):
        l = _lecturas(cotizacion["code"])
        assert l == {"abierta": False, "veces": 0, "primera": None,
                     "ultima": None, "pdfs": 0, "versiones": 0}

    def test_cuenta_cuantas_veces_la_abrieron(self, client, cotizacion):
        """Volver a abrirla es señal: la está pensando o se la está mostrando a
        alguien."""
        for _ in range(3):
            _abrir(client, cotizacion["token"])
        assert _lecturas(cotizacion["code"])["veces"] == 3

    def test_guarda_la_primera_y_la_ultima(self, client, cotizacion):
        _abrir(client, cotizacion["token"])
        _abrir(client, cotizacion["token"])
        l = _lecturas(cotizacion["code"])
        assert l["primera"] is not None and l["ultima"] is not None
        assert l["ultima"] >= l["primera"]

    def test_descargar_el_pdf_se_cuenta_aparte(self, client, cotizacion):
        """Bajar el PDF es más fuerte que abrir: se guarda para enseñárselo a
        alguien o para decidir con calma."""
        with client.session_transaction() as sess:
            sess.clear()
        client.get(f"/c/{cotizacion['token']}/pdf", headers={"User-Agent": NAVEGADOR})
        l = _lecturas(cotizacion["code"])
        assert l["pdfs"] == 1
        assert l["veces"] == 0, "una descarga no es una apertura del link"

    def test_no_se_guarda_nada_que_identifique_a_la_persona(self, client, cotizacion):
        """Para responder "¿la abrió?" basta la marca de tiempo. Guardar la IP
        de un cliente es un dato personal que después hay que cuidar."""
        _abrir(client, cotizacion["token"])
        columnas = {c.name for c in A.QuoteView.__table__.columns}
        assert not (columnas & {"ip", "ip_address", "user_agent", "email", "phone"})
        assert columnas == {"id", "quote_id", "viewed_at", "kind"}


class TestLaMetricaNoPuedeRomperElDocumento:
    def test_si_el_registro_falla_la_cotizacion_igual_abre(self, client, cotizacion):
        """Es telemetría. Que se caiga la métrica es un problema nuestro; que no
        cargue el documento es un problema del cliente."""
        from unittest.mock import patch
        with client.session_transaction() as sess:
            sess.clear()
        with patch.object(A.db.session, "commit", side_effect=RuntimeError("db caída")):
            r = client.get(f"/c/{cotizacion['token']}", headers={"User-Agent": NAVEGADOR})
        assert r.status_code == 200
        assert "Laura Ortiz" in r.data.decode()

    def test_borrar_la_cotizacion_se_lleva_sus_vistas(self, client, sesion, cotizacion):
        """Sin el cascade quedarían filas huérfanas apuntando a una cotización
        que ya no existe."""
        _abrir(client, cotizacion["token"])
        with A.app.app_context():
            qid = A.Quote.query.filter_by(code=cotizacion["code"]).first().id
            assert A.QuoteView.query.filter_by(quote_id=qid).count() == 1
            A.db.session.delete(A.Quote.query.filter_by(code=cotizacion["code"]).first())
            A.db.session.commit()
            assert A.QuoteView.query.filter_by(quote_id=qid).count() == 0


class TestSeVeEnLaPantalla:
    def test_el_detalle_dice_que_no_la_han_abierto(self, sesion, cotizacion):
        cuerpo = sesion.get(f"/quotes/{cotizacion['code']}").data.decode()
        assert "Todavía no la ha abierto" in cuerpo

    def test_y_cuando_si_muestra_las_cifras(self, client, sesion, cotizacion):
        _abrir(client, cotizacion["token"])
        with client.session_transaction() as sess:
            sess["user_id"] = A.User.query.filter(
                A.User.username.like("lec%")).first().id
        cuerpo = sesion.get(f"/quotes/{cotizacion['code']}").data.decode()
        assert "Todavía no la ha abierto" not in cuerpo
        assert "Primera vez" in cuerpo

    def test_el_listado_marca_las_que_nadie_abrio(self, sesion, cotizacion):
        """Es lo que se quiere ver de un vistazo: cuáles ni siquiera se
        miraron."""
        assert "sin abrir" in sesion.get("/quotes").data.decode()
