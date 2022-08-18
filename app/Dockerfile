FROM ubuntu:latest
RUN apt update && apt upgrade -y

WORKDIR /movieDB

RUN apt install -y -q build-essential python3-pip python3-dev
RUN pip3 install -U pip setuptools wheel
RUN pip3 install gunicorn uvloop httptools

COPY requirements.txt .
RUN pip3 install -r requirements.txt
FROM python:3.10
COPY ./app ./app
CMD ["python3", "main.py"]

#COPY service/ /app

#/usr/;local/bin/gunicorn \
 #  -b 0.0.0.0 80
 #  -w 4 \
