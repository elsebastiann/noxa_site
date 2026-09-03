"""Lo que existe en el menú de escritorio tiene que existir en el móvil.

Cotizaciones, Precios PPF y "Pregúntale a los datos" se agregaron solo a la
barra de escritorio. En el celular —que es donde se cotiza con el cliente en
frente— no había forma de llegar: la función estaba pero era inalcanzable.
"""
import itertools

import pytest

from conftest import app_module as A, make_user

_u = itertools.count(1)

# El menú de escritorio y el de móvil son bloques distintos del mismo
# base.html, así que se comparan las dos apariciones de cada enlace.
ENLACES = ["/quotes", "/ppf-prices"]


def _pagina(client, rol="admin", usuario=None):
    with A.app.app_context():
        uid = make_user(usuario or f"nav{next(_u)}", role=rol).id
    with client.session_transaction() as sess:
        sess["user_id"] = uid
    return client.get("/calendar").data.decode()


@pytest.mark.parametrize("ruta", ENLACES)
def test_el_enlace_esta_dos_veces(client, ruta):
    """Una vez en la barra de escritorio y otra en el menú del móvil. Con una
    sola aparición, uno de los dos quedó sin el acceso."""
    cuerpo = _pagina(client)
    veces = cuerpo.count(f'href="{ruta}"')
    assert veces >= 2, f"{ruta} aparece {veces} vez/veces; falta en uno de los dos menús"


def test_preguntar_a_los_datos_tambien_esta_en_los_dos(client):
    """Va aparte porque no se restringe por rol sino por nombre de usuario: un
    admin cualquiera no lo ve en ninguno de los dos menús."""
    cuerpo = _pagina(client, usuario="diana")
    assert cuerpo.count('href="/preguntar"') >= 2


def test_el_menu_movil_trae_cotizaciones(client):
    cuerpo = _pagina(client)
    movil = cuerpo[cuerpo.index('class="bn-more-menu"'):]
    assert 'href="/quotes"' in movil


def test_el_operario_no_las_ve_en_el_movil(client):
    """Cotizar es ver precios, y el operario no los ve."""
    cuerpo = _pagina(client, rol="operario")
    movil = cuerpo[cuerpo.index('class="bn-more-menu"'):] if 'class="bn-more-menu"' in cuerpo else cuerpo
    assert 'href="/quotes"' not in movil
    assert 'href="/ppf-prices"' not in movil
