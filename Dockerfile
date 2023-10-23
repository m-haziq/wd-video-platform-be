FROM python:3.11

# env variable ideally should be in somewhere secure place
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV DB_NAME='db'
#ENV DB_USER='postgres'
#ENV DB_PASSWORD='postgres'
ENV DB_HOST='db'
ENV DB_PORT=5432

ENV CORS_ORIGIN_ALLOW_ALL=True
ENV CORS_ORIGIN_WHITELIST='http://localhost:3000','http://localhost:3001','https://test-assignment-stage.us.aldryn.io'
ENV SECRET_KEY='django-insecure-%z!6&)7%8r$2b1shu6xxo22_no3d1k90stg2k0o9pblkzxmb3&'
ENV CSRF_TRUSTED_ORIGINS='https://test-assignment-stage.us.aldryn.io','http://localhost:3000','https://*.aldryn.io','https://*.io'

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000

CMD uvicorn --host=0.0.0.0 --port=8000 core.asgi:application
