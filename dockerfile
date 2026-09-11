# =============================================================================
# Stage 1: builder
# =============================================================================
FROM python:3.12-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /build

COPY requirements.txt .
RUN pip install --prefix=/install -r requirements.txt


# =============================================================================
# Stage 2: runtime
# =============================================================================
FROM python:3.12-slim AS runtime

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PYTHONPATH=/app

WORKDIR /app

# Runtime-зависимости:
#   libcairo2      — cairosvg
#   fonts-liberation — fallback-шрифты (Arial-совместимые)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libcairo2 \
    fonts-liberation \
    && rm -rf /var/lib/apt/lists/*

# Python-пакеты из builder
COPY --from=builder /install /usr/local

# Non-root пользователь
RUN groupadd --gid 1000 app && \
    useradd --uid 1000 --gid app --shell /bin/bash --create-home app

# Код приложения
COPY --chown=app:app service/ /app/

# Папки для рантайма
RUN mkdir -p /app/output /app/resources /app/fonts && \
    chown -R app:app /app/output /app/resources /app/fonts

USER app

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD python -c "import urllib.request,sys; \
        sys.exit(0 if urllib.request.urlopen('http://127.0.0.1:8000/health', timeout=3).status == 200 else 1)"

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "2"]