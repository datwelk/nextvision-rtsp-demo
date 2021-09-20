FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt update && apt -y upgrade && apt install -y python3.8 python3-pip python3-opencv && \
    pip3 install termcolor && mkdir /app

COPY . /app
CMD python3 /app/test.py