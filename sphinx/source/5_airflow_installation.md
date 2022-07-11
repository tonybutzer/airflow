# Airflow Installion Steps

## Airflow and Microk8s

### Create Base System via Terraform

- /home/ec2-user/opt/airflow/tfinfra/butzer-sf-incubator
- make init
- make apply
- costs       # pinstance

```
[ec2-user@ip-10-12-68-177 butzer-sf-incubator]$ costs | grep sf
6  running            butzer-sf-incubator  10.12.69.170  t3a.2xlarge       219.584
6  running            butzer-sf-incubator  10.12.69.170  t3a.2xlarge       219.584
```

### Install Microk8s


#### Install SNAP/SNAPD
- NOTE: snapd does not like  symlinks

- cd pkg
- ./install_snap_amazon_linux.sh

- sudo systemctl enable --now snapd.socket

- [x] test of snap on incubator complete?

#### Install Microk8s via SNAPD

-  sudo snap install microk8s --classic

```
sudo usermod -a -G microk8s ec2-user
sudo chown -f -R ec2-user ~/.kube

#### Logoff and on to add group

microk8s status

```

#### Enable Kubernetes Key Services

```
microk8s enable dns
microk8s enable dashboard
microk8s enable helm3
microk8s status
```


#### Test k8s Dashboard Access

> This is sort of complicated and annoying -- tony.

- alias k='microk8s kubectl'

```
 k get namespaces

k get svc -n kube-system 

```

---
```
[ec2-user@ip-10-12-69-170 ~]$ k get svc -n kube-system
NAME                        TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)                  AGE
kube-dns                    ClusterIP   10.152.183.10    <none>        53/UDP,53/TCP,9153/TCP   5m34s
metrics-server              ClusterIP   10.152.183.65    <none>        443/TCP                  5m5s
kubernetes-dashboard        ClusterIP   10.152.183.19    <none>        443/TCP                  4m57s
dashboard-metrics-scraper   ClusterIP   10.152.183.173   <none>        8000/TCP                 4m57s
```

##### Port Forward The Dashboard

- microk8s kubectl port-forward -n kube-system service/kubernetes-dashboard 8000:443 --address 0.0.0.0





### Install Airflow via Helm

#### Airflow Helm Chart Study Key Elements


### Configure Airflow

#### Config Files

#### Managing Airflow Environment Variables
