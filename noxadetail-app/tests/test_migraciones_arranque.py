"""Las migraciones de arranque no pueden tumbar la app.

Caso real (2026-09-02): producción quedó caída con
`no such column: services.is_outsourced`, lanzado desde el sembrado de COLORES
—una función que nada tiene que ver con tercerización—. Dos fallas encadenadas:

1. `ensure_service_colors_schema()` usaba `Service.query`, y una consulta del
   ORM trae TODAS las columnas del modelo, incluidas las que agregan
   migraciones que corren MÁS ABAJO en el mismo arranque. Cualquier base a la
   que le faltara una de esas tumbaba el import entero.

2. Las migraciones de `services` no hacían rollback tras el SELECT fallido. En
   SQLAlchemy 2 esa sesión queda inutilizable, así que el primer ALTER reventaba
   y NINGUNA de las tres columnas se agregaba — que es como la base terminó sin
   `is_outsourced` para empezar.
"""
import sqlite3

import pytest

from conftest import app_module as A


def _codigo(fn) -> str:
    """El cuerpo de la función sin comentarios: los comentarios citan el patrón
    que se está prohibiendo y harían pasar (o fallar) el test por la razón
    equivocada."""
    import inspect
    return "\n".join(
        l for l in inspect.getsource(fn).splitlines()
        if not l.strip().startswith("#")
    )


COLUMNAS_QUE_AGREGA_UNA_MIGRACION = [
    "is_outsourced", "default_installer_share", "is_custom_price",
    "is_online_bookable",
]


@pytest.fixture
def base_sin_columnas(tmp_path):
    """Copia la base de pruebas y le quita columnas de `services`, dejándola en
    el mismo estado en el que quedó producción."""
    import os
    import shutil

    destino = tmp_path / "sin_columnas.db"
    shutil.copyfile(os.environ["DB_PATH"], destino)

    con = sqlite3.connect(destino)
    cols = [r[1] for r in con.execute("PRAGMA table_info(services)")]
    quedan = [c for c in cols if c not in COLUMNAS_QUE_AGREGA_UNA_MIGRACION]
    assert "color_fondo" in quedan, "el test necesita que color_fondo siga"
    con.execute("ALTER TABLE services RENAME TO services_old")
    con.execute(f"CREATE TABLE services ({', '.join(quedan)})")
    con.execute(f"INSERT INTO services SELECT {', '.join(quedan)} FROM services_old")
    con.execute("DROP TABLE services_old")
    con.commit()
    con.close()
    return destino


def _columnas(ruta):
    con = sqlite3.connect(ruta)
    try:
        return {r[1] for r in con.execute("PRAGMA table_info(services)")}
    finally:
        con.close()


class TestArranqueConColumnasFaltantes:
    def test_la_base_de_prueba_arranca_sin_las_columnas(self, base_sin_columnas):
        """Contraprueba del montaje: si las columnas siguieran ahí, el test de
        abajo pasaría sin probar nada."""
        assert not (_columnas(base_sin_columnas) & set(COLUMNAS_QUE_AGREGA_UNA_MIGRACION))

    def test_la_app_arranca_y_repone_las_columnas(self, base_sin_columnas):
        """El caso de producción, de punta a punta.

        Corre en un proceso aparte porque acá `app` ya está importado y el fallo
        ocurría justamente al importarlo.
        """
        import os
        import subprocess
        import sys

        raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        entorno = {**os.environ, "DB_PATH": str(base_sin_columnas)}
        r = subprocess.run(
            [sys.executable, "-c", "import app; print('ARRANCO')"],
            cwd=raiz, env=entorno, capture_output=True, text=True, timeout=120,
        )
        assert "ARRANCO" in r.stdout, (
            "la app no arrancó con columnas faltantes:\n" + r.stderr[-1500:]
        )
        assert set(COLUMNAS_QUE_AGREGA_UNA_MIGRACION) <= _columnas(base_sin_columnas)


class TestElSembradoDeColoresNoUsaElORM:
    """La causa raíz. Una función de migración no puede consultar por el ORM:
    el modelo describe el esquema FINAL, no el que hay a mitad del arranque."""

    def test_no_consulta_services_por_el_orm(self):
        assert "Service.query" not in _codigo(A.ensure_service_colors_schema), (
            "vuelve a depender del orden de las migraciones: Service.query trae "
            "todas las columnas del modelo, incluidas las que aún no existen"
        )

    def test_pide_solo_las_columnas_que_necesita(self):
        assert "SELECT id, name FROM services" in _codigo(A.ensure_service_colors_schema)

    def test_sigue_sembrando_el_color_historico(self):
        """El arreglo no puede haberse llevado por delante lo que la función
        hace: sin el sembrado, todos los cajones pasarían al azul por defecto."""
        fuente = _codigo(A.ensure_service_colors_schema)
        assert "COLORS.get" in fuente
        assert "UPDATE services SET color_fondo" in fuente


class TestTodasLasMigracionesHacenRollback:
    """Sin rollback tras el SELECT fallido, la sesión queda inutilizable y el
    ALTER que viene detrás no corre."""

    @pytest.mark.parametrize("fn", [
        "ensure_service_colors_schema",
        "ensure_service_outsourcing_schema",
        "ensure_service_widget_schema",
        "ensure_quote_item_detail_schema",
        "ensure_quote_ppf_brands_schema",
        "ensure_quote_updated_schema",
    ])
    def test_hace_rollback(self, fn):
        fuente = _codigo(getattr(A, fn))
        if "ALTER TABLE" not in fuente:
            pytest.skip("no agrega columnas")
        assert "rollback" in fuente, f"{fn} no hace rollback tras el SELECT fallido"
