# Airflow on Kubernetes

## Step 1 Read this:
- https://bhavaniravi.com/blog/deploying-airflow-on-kubernetes/


## Default Helm3 Approach 

- microk8s helm3 repo add apache-airflow https://airflow.apache.org
- microk8s helm3 upgrade --install airflow apache-airflow/airflow --namespace airflow --create-namespace


## Contact the Airflow Webserver

### Port Forward

```
[ec2-user@ip-10-12-69-170 ~]$ k get svc -n airflow
NAME                          TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)             AGE
airflow-worker                ClusterIP   None             <none>        8793/TCP            95s
airflow-postgresql-headless   ClusterIP   None             <none>        5432/TCP            95s
airflow-postgresql            ClusterIP   10.152.183.185   <none>        5432/TCP            95s
airflow-redis                 ClusterIP   10.152.183.127   <none>        6379/TCP            95s
airflow-statsd                ClusterIP   10.152.183.106   <none>        9125/UDP,9102/TCP   95s
airflow-webserver             ClusterIP   10.152.183.218   <none>        8080/TCP            95s
```

- port forward command

```bash
k -n airflow port-forward service/airflow-webserver 8080:8080 --address 0.0.0.0
```

