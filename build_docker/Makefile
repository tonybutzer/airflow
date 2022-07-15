cat:
	cat Makefile


# builds smartflow container from Adrian Gould Blacksky
build:
	mkdir -p ~/work
	cp -vfr ~/opt/smartflow ~/work
	cp -vfr ./tony ~/work/smartflow/
	cp -v ./tony/smartflow_plugin.py ~/work/smartflow/smartflow/plugins
	cp -v ./tony/Dockerfile ~/work/smartflow/
	cp -v ./tony/s3log_airflow.cfg ~/work/smartflow/airflow.cfg
	(cd ~/work/smartflow; docker build -t smartflowv2 . )
