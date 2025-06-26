FROM python:alpine3.22

LABEL maintainer="Cody Snow"
LABEL version="0.1"
LABEL description="A Docker container to serve a simple Python Flask API for assignment submission"

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

ENV FLASK_ENV=development

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
