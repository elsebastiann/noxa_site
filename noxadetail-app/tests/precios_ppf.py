"""Precios del catálogo, leídos de la base en vez de escritos en los tests.

Los precios de PPF se mueven: cambian de proveedor, de temporada y de
negociación. Un test que los tenga escritos se rompe cada vez que la
administración ajusta la lista, y el que lo arregla termina cambiando el número
sin mirar si la LÓGICA sigue bien — que es lo que el test debía cuidar.

Acá se leen del catálogo. Así estos tests solo fallan cuando se rompe una
regla: la absorción, el adicional de fotocromático, el total por marca.
"""
from conftest import app_module as A


def precio(grupo, marca):
    """Lo que vale ese grupo en esa marca, según el catálogo de ahora."""
    with A.app.app_context():
        g = A.PpfPackage.query.filter_by(name=grupo).first()
        assert g, f"el catálogo no tiene el grupo «{grupo}»"
        p = g.precios.get(marca)
        assert p, f"«{grupo}» no tiene precio en {marca}"
        return p


def foto(grupo, marca):
    """El adicional de fotocromático, o 0 si esa marca no lo ofrece."""
    with A.app.app_context():
        g = A.PpfPackage.query.filter_by(name=grupo).first()
        return (g.precios_fotocromatico or {}).get(marca, 0)


def marca_sin_precios():
    """Una marca activa que no tiene precio en ningún grupo, para probar que
    no entra a las cotizaciones. Si algún día todas tienen precio, el test que
    la use se salta en vez de fallar por la razón equivocada."""
    with A.app.app_context():
        con_precio = set()
        for g in A.PpfPackage.query.all():
            con_precio.update(m for m, v in g.precios.items() if v)
        for nombre, _g in A.ppf_marcas_activas():
            if nombre not in con_precio:
                return nombre
    return None
