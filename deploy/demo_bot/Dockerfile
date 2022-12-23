FROM python:3.6-slim-stretch

RUN apt-get update

COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

ENV API_TOKEN=""

COPY app.py /app.py
