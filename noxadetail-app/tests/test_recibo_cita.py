"""El recibo en PDF de una cita.

El papel que se le entrega al cliente cuando paga o abona. Lo que lo define no
es lo que muestra sino lo que NO muestra: solo precio de lista, descuentos,
abonos y saldo. El costo de tercerización y el ingreso neto son contabilidad del
negocio y no pueden viajar en el bolsillo de un cliente.
"""
import datetime as dt
import itertools
import re

import pytest

from conftest import app_module as A, login_as, make_user

_u = itertools.count(1)


def _texto(pdf: bytes) -> str:
    """Texto del PDF, para poder afirmar sobre lo que de verdad quedó impreso.

    Se lee con pypdf si está; si no, el test se salta en vez de dar por bueno un
    PDF que nadie revisó."""
    try:
        from pypdf import PdfReader
    except ImportError:
        pytest.skip("pypdf no instalado: no se puede leer el texto del PDF")
    import io
    return "\n".join(p.extract_text() or "" for p in PdfReader(io.BytesIO(pdf)).pages)


@pytest.fixture
def cita():
    """Cita con un descuento y un abono, que es el caso que trae el recibo."""
    with A.app.app_context():
        vt = A.VehicleType.query.filter_by(is_active=True).first()
        inicio = A.bogota_now().replace(microsecond=0)
        ap = A.Appointment(
            customer_name="Tatiana Pinzón", plate="NIR849", phone="3105528361",
            services="Wash Shine", start_datetime=inicio,
            end_datetime=inicio + dt.timedelta(hours=2),
            vehicle_type_id=vt.id, status="scheduled",
        )
        A.db.session.add(ap)
        A.db.session.commit()
        A.db.session.add(A.AppointmentPayment(
            appointment_id=ap.id, amount=200000, paid_on=A.bogota_today(),
            description="Anticipo"))
        A.db.session.add(A.AppointmentAdjustment(
            appointment_id=ap.id, kind="discount", mode="fixed", value=50000,
            description="Cliente frecuente"))
        A.db.session.commit()
        ap_id = ap.id
    yield ap_id
    with A.app.app_context():
        A.AppointmentPayment.query.filter_by(appointment_id=ap_id).delete()
        A.AppointmentAdjustment.query.filter_by(appointment_id=ap_id).delete()
        ap = A.Appointment.query.get(ap_id)
        if ap:
            A.db.session.delete(ap)
        A.db.session.commit()


def _pdf(ap_id):
    with A.app.app_context():
        return A._construir_pdf_recibo(A.Appointment.query.get(ap_id))


class TestSeArma:
    def test_sale_un_pdf_de_verdad(self, cita):
        pdf = _pdf(cita)
        assert pdf[:5] == b"%PDF-"
        assert len(pdf) > 3000

    def test_una_cita_pelada_no_lo_revienta(self):
        """Sin teléfono, sin placa, sin tipo de vehículo y sin nada cobrado: es
        como queda una cita agendada a la carrera, y el recibo igual tiene que
        poder imprimirse."""
        with A.app.app_context():
            inicio = A.bogota_now().replace(microsecond=0)
            ap = A.Appointment(services="Wash", start_datetime=inicio,
                               end_datetime=inicio + dt.timedelta(hours=1),
                               status="scheduled")
            A.db.session.add(ap)
            A.db.session.commit()
            try:
                assert A._construir_pdf_recibo(ap)[:5] == b"%PDF-"
            finally:
                A.db.session.delete(ap)
                A.db.session.commit()

    def test_sin_el_archivo_del_logo_igual_sale(self, cita, monkeypatch):
        """La marca de agua es decoración. Un recibo sin logo sirve; uno que
        revienta a la hora de entregárselo a un cliente, no."""
        monkeypatch.setattr(A, "_marca_agua_cache", {})
        monkeypatch.setattr(A.os.path, "exists", lambda *_a, **_k: False)
        assert _pdf(cita)[:5] == b"%PDF-"


class TestElNumeroNoCambia:
    """Reimprimir tiene que dar el MISMO papel. Con un contador propio, volver a
    bajar el recibo de una cita daría otro número y dos documentos distintos
    para un solo pago."""

    def test_es_estable(self, cita):
        with A.app.app_context():
            ap = A.Appointment.query.get(cita)
            assert A.numero_de_recibo(ap) == A.numero_de_recibo(ap)

    def test_lo_lleva_impreso(self, cita):
        with A.app.app_context():
            numero = A.numero_de_recibo(A.Appointment.query.get(cita))
        assert numero in _texto(_pdf(cita))

    def test_dos_citas_no_comparten_numero(self, cita):
        with A.app.app_context():
            a = A.Appointment.query.get(cita)
            inicio = A.bogota_now().replace(microsecond=0)
            otra = A.Appointment(services="Wash", start_datetime=inicio,
                                 end_datetime=inicio + dt.timedelta(hours=1),
                                 status="scheduled")
            A.db.session.add(otra)
            A.db.session.commit()
            try:
                assert A.numero_de_recibo(a) != A.numero_de_recibo(otra)
            finally:
                A.db.session.delete(otra)
                A.db.session.commit()


class TestLasCifrasQueVanYLasQueNo:
    def test_imprime_lista_descuento_abono_y_saldo(self, cita):
        texto = _texto(_pdf(cita))
        assert "Precio de lista" in texto
        assert "Cliente frecuente" in texto      # el descuento, con su nombre
        assert "Abono" in texto
        assert "$50.000" in texto and "$200.000" in texto
        assert re.search(r"Saldo|Pagado en su totalidad", texto)

    def test_no_deja_ver_la_tercerizacion_ni_el_ingreso_neto(self, cita):
        """Lo que le pagamos a un instalador es nuestro costo. En manos del
        cliente es el margen del negocio, impreso y firmado."""
        texto = _texto(_pdf(cita)).lower()
        for prohibido in ("terceriz", "instalador", "ingreso noxa", "ingreso_noxa",
                          "margen", "subtotal", "costo"):
            assert prohibido not in texto, f"el recibo está mostrando {prohibido!r}"

    def test_el_abono_lleva_su_fecha(self, cita):
        """Un abono sin fecha no sirve de comprobante de nada."""
        assert A.bogota_today().strftime("%d/%m/%Y") in _texto(_pdf(cita))

    def test_un_saldo_a_favor_se_dice_asi_y_no_en_negativo(self, cita):
        """Con el precio de lista en cero y un abono encima, el saldo queda
        negativo. "-$200.000" no se entiende; "saldo a favor" sí."""
        texto = _texto(_pdf(cita))
        assert "a favor" in texto.lower()
        assert "-$" not in texto.replace("- $", "")


class TestQuienLoPuedeSacar:
    @pytest.fixture
    def ruta(self, cita):
        return f"/appointments/{cita}/recibo"

    def test_el_admin_si(self, client, ruta):
        login_as(client, make_user(f"rec_adm{next(_u)}", role="admin"))
        r = client.get(ruta)
        assert r.status_code == 200
        assert r.mimetype == "application/pdf"
        assert r.data[:5] == b"%PDF-"

    def test_se_abre_en_el_navegador_y_no_se_descarga(self, client, ruta):
        """Se revisa antes de entregarlo; forzar la descarga obliga a abrir el
        archivo aparte solo para mirarlo."""
        login_as(client, make_user(f"rec_adm{next(_u)}", role="admin"))
        assert "inline" in client.get(ruta).headers["Content-Disposition"]

    @pytest.mark.parametrize("rol", ["operario", "marketing"])
    def test_quien_no_ve_precios_no_saca_recibos(self, client, ruta, rol):
        """El recibo ES plata. Dárselo a quien tiene los precios escondidos en
        pantalla sería devolverle por PDF justo lo que se le ocultó."""
        login_as(client, make_user(f"rec_{rol}{next(_u)}", role=rol))
        assert client.get(ruta).status_code == 302

    def test_una_cita_que_no_existe_no_revienta(self, client):
        login_as(client, make_user(f"rec_adm{next(_u)}", role="admin"))
        assert client.get("/appointments/999999/recibo").status_code == 302


class TestElBotonEnLaCita:
    def test_aparece_al_editar(self, client, cita):
        login_as(client, make_user(f"rec_adm{next(_u)}", role="admin"))
        cuerpo = client.get(f"/appointment/{cita}/edit").data.decode()
        assert f"/appointments/{cita}/recibo" in cuerpo

    def test_no_aparece_al_crear(self, client):
        """Una cita que todavía no existe no tiene de qué dar recibo."""
        login_as(client, make_user(f"rec_adm{next(_u)}", role="admin"))
        assert "/recibo" not in client.get("/appointments/new").data.decode()

    def test_el_operario_no_lo_ve(self, client, cita):
        """Un botón que rebota es peor que un botón que no está."""
        login_as(client, make_user(f"rec_op{next(_u)}", role="operario"))
        cuerpo = client.get(f"/appointment/{cita}/edit").data.decode()
        assert "/recibo" not in cuerpo
