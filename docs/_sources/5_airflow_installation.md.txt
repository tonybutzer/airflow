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
```



### Install Airflow via Helm

#### Airflow Helm Chart Study Key Elements


### Configure Airflow

#### Config Files

#### Managing Airflow Environment Variables
