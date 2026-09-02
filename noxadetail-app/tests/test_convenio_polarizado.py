"""El convenio no descuenta polarizados.

Se cobran a precio completo aunque el cliente tenga convenio. Va por palabra en
el nombre y no por nombre exacto: hay un polarizado por marca de película
—Tecnofilm, Spectra, UltraOptic, Nanocerámica HD— y entra una nueva cada tanto.
Con la lista de nombres exactos, el que se olvidaran de agregar se habría
descontado en silencio.
"""
import itertools

import pytest

from conftest import app_module as A

_n = itertools.count(1)


@pytest.fixture
def convenio():
    with A.app.app_context():
        a = A.Agreement(name=f"Convenio Prueba {next(_n)}", discount_type="percentage",
                        value=10, is_active=True)
        A.db.session.add(a)
        A.db.session.commit()
        aid = a.id
    yield aid
    with A.app.app_context():
        A.db.session.delete(A.Agreement.query.get(aid))
        A.db.session.commit()


@pytest.fixture
def servicio():
    """Crea un servicio con precio y lo borra al final."""
    creados = []

    def _crear(nombre, precio=1_000_000, vt=1):
        with A.app.app_context():
            s = A.Service(name=f"{nombre} {next(_n)}", duration_minutes=60, is_active=True)
            A.db.session.add(s)
            A.db.session.flush()
            A.db.session.add(A.ServicePrice(service_id=s.id, vehicle_type_id=vt,
                                            price=precio, duration_minutes=60, is_active=True))
            A.db.session.commit()
            creados.append(s.id)
            return s.id

    yield _crear
    with A.app.app_context():
        for sid in creados:
            A.ServicePrice.query.filter_by(service_id=sid).delete()
            s = A.Service.query.get(sid)
            if s:
                A.db.session.delete(s)
        A.db.session.commit()


def _con_convenio(sids, aid, vt=1):
    with A.app.app_context():
        a = A.Agreement.query.get(aid)
        final, base = A.apply_agreement_discount_split(sids, vt, a)
        return final, base


class TestElPolarizadoNoSeDescuenta:
    @pytest.mark.parametrize("nombre", [
        "Polarizado Nanocerámica Tecnofilm",
        "Polarizado Nanocerámica Spectra",
        "Polarizado Nanocerámica UltraOptic",
        "Polarizado Nanoceramica HD",
        "POLARIZADO ULTRAOPTIC",
    ])
    def test_se_cobra_completo(self, servicio, convenio, nombre):
        """Con y sin tildes, y en mayúsculas: el nombre lo escribe una persona."""
        sid = servicio(nombre, 800_000)
        final, base = _con_convenio([sid], convenio)
        assert final == 800_000, f"le aplicó el convenio a «{nombre}»"
        assert base == 800_000

    def test_contraprueba_otro_servicio_si_se_descuenta(self, servicio, convenio):
        """Sin esto, el test de arriba pasaría aunque el convenio no funcionara
        para nada."""
        sid = servicio("Coating Cerámico 9H", 1_000_000)
        final, _base = _con_convenio([sid], convenio)
        assert final == 900_000

    def test_en_una_cita_mixta_solo_descuenta_lo_otro(self, servicio, convenio):
        """El caso real: el cliente lleva coating y polarizado el mismo día."""
        coating = servicio("Coating Cerámico", 1_000_000)
        polar = servicio("Polarizado Spectra", 800_000)
        final, base = _con_convenio([coating, polar], convenio)
        assert base == 1_800_000
        assert final == 900_000 + 800_000

    def test_tambien_con_convenio_de_monto_fijo(self, servicio):
        """El descuento absoluto se come el total si no se separa la base."""
        with A.app.app_context():
            a = A.Agreement(name=f"Fijo {next(_n)}", discount_type="absolute",
                            value=200_000, is_active=True)
            A.db.session.add(a)
            A.db.session.commit()
            aid = a.id
        try:
            polar = servicio("Polarizado Tecnofilm", 800_000)
            final, _ = _con_convenio([polar], aid)
            assert final == 800_000
        finally:
            with A.app.app_context():
                A.db.session.delete(A.Agreement.query.get(aid))
                A.db.session.commit()


class TestLoQueYaEstabaExcluidoSigueExcluido:
    @pytest.mark.parametrize("nombre", ["Wash Essential", "Wash Shine",
                                        "Detallado Exterior", "Detallado Llanta a Llanta"])
    def test_los_nombres_exactos_siguen(self, nombre):
        with A.app.app_context():
            s = A.Service(name=nombre, duration_minutes=60)
            assert A.excluido_de_convenio(s), f"{nombre} dejó de estar excluido"

    def test_un_servicio_cualquiera_no_esta_excluido(self):
        with A.app.app_context():
            assert not A.excluido_de_convenio(A.Service(name="Lavado Premium", duration_minutes=60))

    def test_none_no_revienta(self):
        with A.app.app_context():
            assert not A.excluido_de_convenio(None)
