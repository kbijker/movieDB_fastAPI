FROM ubuntu:latest
RUN apt update && apt upgrade -y
RUN mkdir -p /app
WORKDIR /app

RUN apt install -y -q build-essential python3-pip python3-dev
RUN pip3 install -U pip setuptools wheel
RUN pip3 install gunicorn uvloop httptools

FROM python:3.10
COPY ./app ./app
RUN pip install -r ./app/requirements.txt

CMD ["python3", "./app/main.py"]

#COPY service/ /app

#/usr/;local/bin/gunicorn \
 #  -b 0.0.0.0 80
 #  -w 4 \
