# Kalkan – Veri Bilimi

Verinin toplanması, anonimleştirilmesi, analizi; dolandırıcılık dashboard'u, erken uyarı sistemi ve Türkçe dolandırıcılık veri seti.

**Sorumlu:** *(belirlenecek)* · **Diller:** Python, SQL

## Klasör yapısı

```
pipelines/etl/            Veri toplama & temizleme
pipelines/anonymization/  Kişisel veri maskeleme
sql/schema/  sql/queries/ PostgreSQL / DuckDB
analysis/notebooks/       Jupyter analizleri
early-warning/            Anomali tespiti (z-skoru, Prophet/STL, Isolation Forest)
dataset/guidelines/       Etiketleme kılavuzu
dataset/labeling/         Label Studio yapılandırması
dataset/raw/  processed/  Yerel – repoya eklenmez
dashboards/superset/      Herkese açık dashboard
reports/monthly/          Aylık "Kalkan Dolandırıcılık Raporu"
service/                  Veri servisi (FastAPI)
tests/                    pytest
```

> Dashboard'da 5'ten az ihbar içeren gruplar gösterilmez. Ham veriye yalnızca yetkili kişiler erişir.

## Çalışma kuralları

- `main` korumalıdır; her değişiklik ayrı bir branch ve pull request ile gelir, en az 1 onay gerekir.
- Branch adları: `feature/<alan>-<kısa-açıklama>`, `fix/<alan>-<kısa-açıklama>`
- Commit mesajları: Conventional Commits (`feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`)
- `.env` dosyaları repoya eklenmez; örnek değerler `.env.example` içinde tutulur.
- Projenin tamamı için bkz. [`CLAUDE.md`](CLAUDE.md).
