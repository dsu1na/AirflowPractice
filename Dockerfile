FROM python:3.11-slim

ENV AIRFLOW_HOME=/airflow
COPY requirements.txt .

RUN apt-get update \
    && apt-get install sudo \
    && sudo apt-get install -y gcc python3-dev \
    && apt install -y git \
    && mkdir /airflow \
    && pip3 install --no-cache-dir -r requirements.txt

# Then follow pip install apache-airflow