from fastapi import FastAPI

from .middleware import setup_cors
from .middleware.body_limit import MaxBodySizeMiddleware
from .middleware.logging import LoggingMiddleware
from .routes import router as generate_router
from .routes.health import router as health_router
from .logging_config import setup_logging


MAX_BODY_BYTES = 10 * 1024 * 1024   # 10 МБ


def create_app() -> FastAPI:
    setup_logging()

    app = FastAPI(
        title="ImageConstructor API",
        description="Сервис сборки изображений.",
        version="1.0.0",
        docs_url="/api/docs",
        redoc_url="/api/redoc",
    )
    
    app.add_middleware(MaxBodySizeMiddleware, max_bytes=MAX_BODY_BYTES)
    setup_cors(app)
    app.add_middleware(LoggingMiddleware)
    app.include_router(health_router)
    app.include_router(generate_router)
    return app
    
app = create_app()