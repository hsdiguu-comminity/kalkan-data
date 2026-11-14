"""Kalkan veri servisi.

Dashboard (/stats, /map) ve erken uyarı (/alerts) uç noktaları service/app/routers/ altında
yazılır ve burada include_router ile eklenir. Yalnızca anonimleştirilmiş veri döner.
"""

from fastapi import FastAPI

app = FastAPI(title="Kalkan Data Service", version="0.1.0")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "kalkan-data"}


# Örnek: app.include_router(stats.router, prefix="/stats", tags=["stats"])
