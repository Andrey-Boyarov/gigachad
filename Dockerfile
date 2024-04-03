FROM python:3.10.14-alpine3.19

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .