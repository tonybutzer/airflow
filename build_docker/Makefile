cat:
	cat Makefile


# builds smartflow container from Adrian Gould Blacksky
build:
	mkdir -p ~/work
	cp -vfr ~/opt/smartflow ~/work
	cp -vfr ./tony ~/work/smartflow/
	cp -v ./tony/smartflow_plugin.py ~/work/smartflow/smartflow/plugins
	(cd ~/work/smartflow; docker build -t smartflowv2 . )
