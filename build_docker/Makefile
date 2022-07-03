cat:
	cat Makefile


# builds smartflow container from Adrian Gould Blacksky
build:
	mkdir -p ~/work
	cp -vfr ~/opt/smartflow ~/work
	cp -vfr ./tony ~/work/smartflow/
	(cd ~/work/smartflow; docker build -t smartflowv2 . )
