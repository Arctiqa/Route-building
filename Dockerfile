FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml /

RUN pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi --no-root

COPY . .