
kubectl create namespace airflow
kubectl get namespaces

helm repo add apache-airflow https://airflow.apache.org
helm repo update
helm search repo airflow
helm install airflow apache-airflow/airflow --namespace airflow --debug
