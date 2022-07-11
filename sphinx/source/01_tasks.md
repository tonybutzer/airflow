# Tasks

## Security Group or a Bunch of ssh port forwards

- https://cloudcasts.io/course/terraform/security-groups
	- https://www.cloudwalker.io/2020/09/13/terraform-security-groups-ec2-instances/
- https://stackoverflow.com/questions/29936948/ssh-l-forward-multiple-ports


## Understand Kubernetes Proxies

```

kubectl create deployment node-hello --image=gcr.io/google-samples/node-hello:1.0 --port=9090
alias k='microk8s kubectl'
k get pods

kubectl proxy --port=9090

curl localhost:9090

curl http://localhost:9090/api/

curl http://localhost:9090/api/v1/namespaces/default/pods


```

#### Proxy 8080

kubectl proxy --port=8080



## Run Airflow on microk8s
- [x] Find Article on Airflow on k8s
	-https://vinayak.io/2020/09/10/day-24-jupyterhub-airflow-microk8s/
- [ ] document steps
	- [ ] get micrk8s running via snap - status helm
		- microk8s status
		- microk8s enable helm
- [ ] airflow helm
	- https://airflow.apache.org/docs/helm-chart/stable/index.html
	- helm repo add apache-airflow https://airflow.apache.org
	-  microk8s helm3 repo add apache-airflow https://airflow.apache.org
	- helm upgrade --install airflow apache-airflow/airflow --namespace airflow --create-namespace
	- get default values for override possibilities
		- microk8s helm3 show values stable/airflow > values.yml
	- [ ]
	- [ ]
	- [ ]
	- [ ]
- [ ]
- [ ]
- [ ]
- [ ]
- [ ]
- [ ]
- [ ]
- [ ]
## Remove Unused Systems From Eccoe -

- [x]  stopped    butzer-mahesh-dev-prototype   10.12.69.99     t3.large        60.736
- [x]  stopped          butzer-eccoe-js-study   10.12.69.74    t3a.large        54.896
- [x]  stopped           butzer-lidar-explore   10.12.69.95  t3a.2xlarge       219.584
- [x]  stopped    butzer-iarpa1-tony-dev-temp  10.12.68.242  t3a.2xlarge       219.584

#### - [ ] butzer-dev - no speak ssh with my pem



## Cleanup smartflow ec2 instance butzer-eccoe-smartflow 

- test butzer-dev
	- [x] install miniconda on efs
	- [x] test jupyter - clone airflow
	- [x] install snapd
	- [x] install microk8s
	- [x] test docker compose airflow-celery
		- [x] install docker compose
