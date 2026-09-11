from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse


class MaxBodySizeMiddleware(BaseHTTPMiddleware):
    """Отклоняет запросы, у которых Content-Length больше лимита."""

    def __init__(self, app, max_bytes: int):
        super().__init__(app)
        self.max_bytes = max_bytes

    async def dispatch(self, request: Request, call_next):
        content_length = request.headers.get("content-length")

        if content_length is not None:
            try:
                length = int(content_length)
            except ValueError:
                return JSONResponse(
                    {"detail": "Некорректный Content-Length"},
                    status_code=400,
                )

            if length > self.max_bytes:
                return JSONResponse(
                    {"detail": f"Тело запроса больше {self.max_bytes} байт"},
                    status_code=413,
                )

        return await call_next(request)