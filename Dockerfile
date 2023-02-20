FROM python:3.9

EXPOSE 5000

COPY ./app/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app/ /app

WORKDIR /app

ENTRYPOINT uvicorn run:app --reload --port 5000 --host 0.0.0.0