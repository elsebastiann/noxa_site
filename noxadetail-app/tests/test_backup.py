"""Backup diario de la base.

Dos cosas que tienen que estar bien sí o sí: que la copia sea una base SQLite
válida y completa (un backup que no se puede abrir no es un backup), y que la
retención no borre de más — es el único código del sistema que borra archivos
solo, y si se equivoca se lleva la única copia que había.
"""
import gzip
import io
import itertools
import sqlite3

import app as A

_dias = itertools.count(1)


class TestDumpDeLaBase:
    def test_la_copia_es_una_base_sqlite_valida(self, tmp_path):
        datos = A._dump_sqlite_gz()
        destino = tmp_path / "restaurada.db"
        destino.write_bytes(gzip.decompress(datos))

        # Si el dump quedó a medias, esto revienta.
        conn = sqlite3.connect(destino)
        tablas = {r[0] for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table'")}
        conn.close()
        assert "appointments" in tablas
        assert "users" in tablas

    def test_conserva_los_datos_no_solo_el_esquema(self, client, tmp_path):
        conv = A.Conversation(phone="+573001234599", profile_name="Backup Test")
        A.db.session.add(conv)
        A.db.session.commit()

        destino = tmp_path / "restaurada.db"
        destino.write_bytes(gzip.decompress(A._dump_sqlite_gz()))
        conn = sqlite3.connect(destino)
        encontrado = conn.execute(
            "SELECT profile_name FROM whatsapp_conversations WHERE phone = ?",
            ("+573001234599",),
        ).fetchone()
        conn.close()
        assert encontrado == ("Backup Test",)

    def test_comprimir_reduce_el_tamano(self):
        import os
        crudo = os.path.getsize(A.db_path)
        assert len(A._dump_sqlite_gz()) < crudo


class _S3Falso:
    """Bucket en memoria, para probar la retención sin tocar Railway."""

    def __init__(self, claves):
        self.objetos = {k: {"Key": k, "Size": 100} for k in claves}
        self.borrados = []

    def get_paginator(self, _op):
        objetos = list(self.objetos.values())

        class _P:
            def paginate(self, **_kw):
                return [{"Contents": objetos}]

        return _P()

    def delete_object(self, Bucket=None, Key=None):  # noqa: N803
        self.borrados.append(Key)
        self.objetos.pop(Key, None)


def _keys(*fechas):
    return [f"agenda/{f}.db.gz" for f in fechas]


class TestRetencion:
    def test_con_pocos_backups_no_borra_nada(self, monkeypatch):
        monkeypatch.setattr(A, "BACKUP_BUCKET", "b")
        s3 = _S3Falso(_keys("2026-08-01", "2026-08-02", "2026-08-03"))
        assert A._aplicar_retencion(s3) == 0
        assert s3.borrados == []

    def test_conserva_los_ultimos_30_dias(self, monkeypatch):
        monkeypatch.setattr(A, "BACKUP_BUCKET", "b")
        # 40 días seguidos del mismo mes+siguiente: sobran 10.
        fechas = [f"2026-07-{d:02d}" for d in range(1, 32)] + [f"2026-08-{d:02d}" for d in range(1, 10)]
        s3 = _S3Falso(_keys(*fechas))
        A._aplicar_retencion(s3)

        vivos = set(s3.objetos)
        # Los 30 más recientes siguen ahí.
        for f in sorted(fechas, reverse=True)[:30]:
            assert f"agenda/{f}.db.gz" in vivos

    def test_conserva_el_primero_de_cada_mes_aunque_sea_viejo(self, monkeypatch):
        monkeypatch.setattr(A, "BACKUP_BUCKET", "b")
        # Un año de backups: el 1 y el 15 de cada mes.
        fechas = [f"2026-{m:02d}-{d:02d}" for m in range(1, 13) for d in (1, 15)]
        s3 = _S3Falso(_keys(*fechas))
        A._aplicar_retencion(s3)

        vivos = set(s3.objetos)
        # El primero de cada mes sobrevive aunque tenga meses de antigüedad.
        for m in range(1, 13):
            assert f"agenda/2026-{m:02d}-01.db.gz" in vivos, f"se borró el mensual de {m:02d}"

    def test_nunca_borra_el_backup_mas_reciente(self, monkeypatch):
        monkeypatch.setattr(A, "BACKUP_BUCKET", "b")
        fechas = [f"2026-{m:02d}-{d:02d}" for m in range(1, 13) for d in range(1, 29)]
        s3 = _S3Falso(_keys(*fechas))
        A._aplicar_retencion(s3)
        assert "agenda/2026-12-28.db.gz" in s3.objetos


class TestDescargaSegura:
    def test_no_deja_pedir_objetos_fuera_de_la_carpeta_de_backups(self, client, monkeypatch):
        """Un `key` manipulado no puede sacar otra cosa del bucket."""
        for key in ("otra-cosa/secreto.txt", "agenda/../otro/x.gz", ""):
            resp = client.get(f"/backups/download?key={key}", follow_redirects=False)
            assert resp.status_code in (302, 303)
            assert "/backups" in resp.headers.get("Location", "") or "/login" in resp.headers.get("Location", "")
