from fastapi import APIRouter

router = APIRouter(tags=["health"])


@router.get("/health", summary="Liveness probe")
async def health() -> dict[str, str]:
    """Liveness: процесс жив и отвечает. Ничего не проверяет."""
    return {"status": "ok"}


@router.get("/api/v1/health", summary="Readiness probe", include_in_schema=False)
async def health_v1() -> dict[str, str]:
    """Readiness: алиас для балансировщиков, которые ходят под /api/v1."""
    return {"status": "ok"}