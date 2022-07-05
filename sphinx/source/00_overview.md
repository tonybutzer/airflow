# Overview


## Purpose

This project will explore airflow as a workflow manager - used by IARPA/SMART project and potrentially used by EROS for projects such as LCMAP/NLCD.

## Mission

1. Get smart on Airflow
2. Implement sample DAGS

## Objectives

1. Run GAASS-PY as a DAG Flow and contrast this with simple docker (python module) based orchestration

### Prerequsite steps

1. Get airflow running in CHS as a docker-compose cluster of containers
2. Pass compentancy tests such as running our fisrt Shinbashi DAG
3. Explore providers notably:
	- Celery
	- Kubernetes

## Quests

### Get Docker Airflow Running in CHS

1. Create airflow repo GIT
2. Create test machine EC2-instance terraform etc
3. Install Docker
4. Build Docs for web page
5. Start Quest

#### References
https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html

- BOOK: 
	- Data Pipelines with Apache Airflow
	- by Bas P. Harenslak (Author), Julian Rutger de Ruiter (Author)

