cat:
	cat Makefile

docker:
	echo hello
	sudo yum update -y
	sudo amazon-linux-extras install docker
	#sudo yum install docker
	sudo service docker start
	sudo usermod -a -G docker ec2-user


dashboard:
	echo token
	kubectl -n kubernetes-dashboard create token admin-user
	kubectl port-forward -n kubernetes-dashboard service/kubernetes-dashboard 8000:443 --address 0.0.0.0 &



helm3:
	curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
	chmod 700 get_helm.sh
	./get_helm.sh


airinfo:
	kubectl get pods -n airflow
	helm ls -n airflow


airpf:
	# port forward
	kubectl port-forward -n airflow service/airflow-webserver 8080:8080 --address 0.0.0.0 &

airval:
	helm show values apache-airflow/airflow > values.yaml


airupdate:
	helm upgrade --install airflow apache-airflow/airflow -n airflow -f values.yaml --debug
	helm ls -n airflow


loadcustom:
	kind load docker-image smartflowv2 --name airflow-cluster


set-ssh-secret:
	echo dag repo secret here
publish:
	(cd ~/opt/airflow; ./gitpush.sh)
