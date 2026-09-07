FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
PYTHONUNBUFFERED=1 \
PIP_NO_CACHE_DIR=1

WORKDIR /app

# Install dependencies first so this layer is cached between code changes.
COPY pyproject.toml README.md ./
COPY src ./src
RUN pip install --no-cache-dir . gunicorn

# Run as a non-root user.
RUN useradd --create-home --uid 10001 appuser
USER appuser

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "2", "src.api:app"]