import json

from fastapi import APIRouter, Depends, HTTPException, Request
from starlette.concurrency import run_in_threadpool

from api.dependencies import get_image_manager
from image_manager import ImageManager

router = APIRouter()


async def _read_json(request: Request):
    """Читает JSON из тела запроса. Бросает 400 при некорректном JSON."""
    try:
        return await request.json()
    except json.JSONDecodeError as e:
        raise HTTPException(status_code=400, detail=f"Некорректный JSON: {e}")


@router.post("/api/v1/create_from_static_patterns")
async def create_from_static_patterns(
    request: Request,
    manager: ImageManager = Depends(get_image_manager),
):
    data = await _read_json(request)
    if not data:
        raise HTTPException(status_code=400, detail="Нет данных для генерации")

    result = await run_in_threadpool(manager.create_from_pattern, data)

    if not result:
        raise HTTPException(status_code=400, detail="Не удалось сгенерировать изображения")

    return {"success": True, "total": len(result), "images": result}


@router.post("/api/v1/create_custom")
async def create_custom(
    request: Request,
    manager: ImageManager = Depends(get_image_manager),
):
    data = await _read_json(request)
    if not data:
        raise HTTPException(status_code=400, detail="Нет данных для генерации")

    result = await run_in_threadpool(manager.create_custom, data)

    if not result:
        raise HTTPException(status_code=400, detail="Не удалось сгенерировать изображения")

    return {"success": True, "total": len(result), "images": result}