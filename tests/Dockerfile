FROM python:alpine3.22

LABEL maintainer="Cody Snow"
LABEL version="0.1"
LABEL description="A Docker container to run tests against the Flask API"

WORKDIR /app

COPY tests/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY tests/. /app
COPY api/. /app/api

ENV FLASK_APP=app_test.py

ENV FLASK_ENV=development

CMD ["pytest"]