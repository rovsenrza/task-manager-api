# ════════════════════════════════════════════════════════
#  Stage 1 – Builder
# ════════════════════════════════════════════════════════
FROM python:3.11-slim AS builder

WORKDIR /build

# Install dependencies into an isolated prefix
COPY requirements.txt .
RUN pip install --prefix=/install --no-cache-dir -r requirements.txt


# ════════════════════════════════════════════════════════
#  Stage 2 – Runtime (small, production-ready image)
# ════════════════════════════════════════════════════════
FROM python:3.11-slim AS runtime

LABEL org.opencontainers.image.title="Task Manager API"
LABEL org.opencontainers.image.version="1.0.0"
LABEL org.opencontainers.image.authors="DevOps Student"

# Copy installed packages from builder stage
COPY --from=builder /install /usr/local

WORKDIR /app

# Copy application source
COPY app/ ./app/
COPY run.py .

# ── Environment-based configuration ──────────────────────
ENV APP_VERSION=1.0.0 \
    MAX_TASKS=100 \
    PORT=5000

# Expose port
EXPOSE 5000

# ── Health check ──────────────────────────────────────────
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/health')"

# Run with gunicorn (production WSGI server)
CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:${PORT} --workers 2 run:app"]
