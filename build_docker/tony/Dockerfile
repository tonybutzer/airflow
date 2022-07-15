FROM apache/airflow:2.3.2-python3.8
ARG DEBIAN_FRONTEND=noninteractive
ARG EXTRA_REQUIRES=test

COPY --chown=airflow:root . /app

COPY ./airflow.cfg /opt/airflow

RUN pip install  -c /app/constraints.txt --user "/app[$EXTRA_REQUIRES]"

ENV PYTHONFAULTHANDLER=1
