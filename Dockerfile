FROM python:3.10-alpine AS base

RUN	apk update && apk add --no-cache \
	openssh-keygen
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app/src


FROM base AS dev

RUN pip install --no-cache-dir coverage


FROM base AS prod

RUN pip install --no-cache-dir gunicorn psycopg2-binary

COPY src /app/src
