FROM python:3.13-slim

WORKDIR /app

COPY pyproject.toml .
COPY src/ src/

RUN pip install --no-cache-dir flask

EXPOSE 5000

CMD ["python3", "src/api.py"]
