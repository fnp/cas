FROM python:3.10-alpine AS base

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app


FROM base AS prod

COPY src src

RUN pip install --no-cache-dir gunicorn psycopg2-binary

RUN src/manage.py collectstatic --no-input
