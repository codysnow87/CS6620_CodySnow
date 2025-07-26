FROM python:alpine3.22

LABEL maintainer="Cody Snow"
LABEL version="0.1"
LABEL description="A Docker container to run Flask APIs for storing and retrieving user information"

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN apk add --no-cache curl

COPY app.py .
COPY . .

CMD ["python", "app.py"]