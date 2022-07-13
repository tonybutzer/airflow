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

- troubleshooting
	- error: unable to forward port because pod is not running. Current status=Pending
		- maybe waiting for -- storage 
	- https://vinayak.io/2020/09/10/day-24-jupyterhub-airflow-microk8s/


## Airflow YAMLs

- microk8s helm3 show values stable/airflow > values.yml

- understand and possibly override these values - more to come ...


## Shutdown/Nuke Airflow

microk8s kubectl delete airflow


## FAIL Retry these steps tony

```

microk8s helm3 repo add stable https://kubernetes-charts.storage.googleapis.com/
WARNING: Kubernetes configuration file is group-readable. This is insecure. Location: /var/snap/microk8s/3272/credentials/client.config
Error: repo "https://kubernetes-charts.storage.googleapis.com/" is no longer available; try "https://charts.helm.sh/stable" instead


microk8s helm3 repo add stable https://charts.helm.sh/stable


 microk8s helm3 repo update
WARNING: Kubernetes configuration file is group-readable. This is insecure. Location: /var/snap/microk8s/3272/credentials/client.config
Hang tight while we grab the latest from your chart repositories...
...Successfully got an update from the "apache-airflow" chart repository
...Successfully got an update from the "stable" chart repository
Update Complete. ⎈Happy Helming!⎈


```

## more ...
```
[ec2-user@ip-10-12-69-170 ~]$ microk8s kubectl create namespace airflow
namespace/airflow created
[ec2-user@ip-10-12-69-170 ~]$ k get pods -n airflow
No resources found in airflow namespace.
[ec2-user@ip-10-12-69-170 ~]$ microk8s helm3 show values stable/airflow > values.yml
```

---

```
[ec2-user@ip-10-12-69-170 ~]$ microk8s helm3 upgrade --install airflow apache-airflow/airflow --namespace airflow --create-namespace
WARNING: Kubernetes configuration file is group-readable. This is insecure. Location: /var/snap/microk8s/3272/credentials/client.config
Release "airflow" does not exist. Installing it now.

NAME: airflow
LAST DEPLOYED: Wed Jul 13 19:44:40 2022
NAMESPACE: airflow
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
Thank you for installing Apache Airflow 2.3.0!

Your release is named airflow.
You can now access your dashboard(s) by executing the following command(s) and visiting the corresponding port at localhost in your browser:

Airflow Webserver:     kubectl port-forward svc/airflow-webserver 8080:8080 --namespace airflow
Default Webserver (Airflow UI) Login credentials:
    username: admin
    password: admin
Default Postgres connection credentials:
    username: postgres
    password: postgres
    port: 5432

You can get Fernet Key value by running the following:

    echo Fernet Key: $(kubectl get secret --namespace airflow airflow-fernet-key -o jsonpath="{.data.fernet-key}" | base64 --decode)

###########################################################
#  WARNING: You should set a static webserver secret key  #
###########################################################

You are using a dynamically generated webserver secret key, which can lead to
unnecessary restarts of your Airflow components.

Information on how to set a static webserver secret key can be found here:
https://airflow.apache.org/docs/helm-chart/stable/production-guide.html#webserver-secret-key
[ec2-user@ip-10-12-69-170 ~]$
[ec2-user@ip-10-12-69-170 ~]$
```

```
[ec2-user@ip-10-12-69-170 ~]$ k get pods -n airflow
NAME                                   READY   STATUS      RESTARTS   AGE
airflow-statsd-5bcb9dd76-vrhk2         1/1     Running     0          82s
airflow-redis-0                        1/1     Running     0          82s
airflow-postgresql-0                   1/1     Running     0          81s
airflow-webserver-5ddd87bf95-dqgzx     0/1     Running     0          82s
airflow-triggerer-5ddcdcdfd9-wzzdt     1/1     Running     0          82s
airflow-scheduler-75b785f69c-xl2x6     2/2     Running     0          82s
airflow-worker-0                       2/2     Running     0          82s
airflow-run-airflow-migrations-p6ls7   0/1     Completed   0          81s
airflow-create-user-kcjtb              1/1     Running     0          3s
```


