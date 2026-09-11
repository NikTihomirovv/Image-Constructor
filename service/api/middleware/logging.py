# service/api/middleware/logging.py
import logging
import time
import uuid

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

logger = logging.getLogger("api.access")


class LoggingMiddleware(BaseHTTPMiddleware):
    """Логирует входящие запросы и ответы с длительностью и request_id."""

    async def dispatch(self, request: Request, call_next):
        request_id = request.headers.get("X-Request-ID") or uuid.uuid4().hex[:12]
        start = time.perf_counter()

        logger.info(
            "→ %s %s | client=%s | req_id=%s",
            request.method,
            request.url.path,
            request.client.host if request.client else "unknown",
            request_id,
        )

        try:
            response = await call_next(request)
        except Exception:
            elapsed_ms = (time.perf_counter() - start) * 1000
            logger.exception(
                "✗ %s %s | %.1fms | req_id=%s",
                request.method,
                request.url.path,
                elapsed_ms,
                request_id,
            )
            raise

        elapsed_ms = (time.perf_counter() - start) * 1000
        response.headers["X-Request-ID"] = request_id

        logger.info(
            "← %s %s | %d | %.1fms | req_id=%s",
            request.method,
            request.url.path,
            response.status_code,
            elapsed_ms,
            request_id,
        )
        return response