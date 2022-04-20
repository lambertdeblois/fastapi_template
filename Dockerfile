FROM ubuntu:latest

EXPOSE 5000

RUN apt update && apt upgrade -y

RUN apt install -y -q build-essential python3-pip python3-dev
RUN pip3 install -U pip setuptools wheel

COPY app/requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt

COPY app/ /app

WORKDIR /app

ENTRYPOINT uvicorn run:app --reload --port 5000 --host 0.0.0.0