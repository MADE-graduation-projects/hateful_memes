FROM python:3.6-slim-stretch

RUN apt-get update


COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

ENV API_TOKEN="5838296860:AAG8UTY2WVmQ2TDGX6LjWN65cZTYCOGabGI"

COPY app.py /app.py