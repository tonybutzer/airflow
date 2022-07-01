cat:
	cat Makefile
setuser:
	mkdir -p ./dags ./logs ./plugins
	echo -e "AIRFLOW_UID=1000" > .env


initdb:
	docker-compose up airflow-init
