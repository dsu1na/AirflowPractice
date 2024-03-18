FROM python:3.11-slim
RUN apt-get update
RUN apt-get install sudo
RUN sudo apt-get install -y gcc python3-dev
RUN apt install -y git
RUN mkdir /airflow
ENV AIRFLOW_HOME=/airflow
RUN pip install apache-airflow

# Then follow pip install apache-airflow