# ELK on k8s manually 

## Video

- https://www.youtube.com/watch?v=SU--XMhbWoY

- Filebeat + Elk Stack Tutorial With Kubernetes

## Steps

https://artifacthub.io/packages/search?kind=0

### git Michael Guays repo

- cd ~/opt
- https://github.com/mguay22/elk-filebeat.git

### test redis in k8s

```
kubectl run redis --image=redis
alias k='kubectl'
k get logs redis
```


### bring up each item in ELK

- create namespace elk and set context elk

```
k get ns
k create namespace elk

kubectl config set-context --current --namespace=elk

kubectl run redis --image=redis

k get pods

```

go to logstash folder from Michael

```
cd /home/ec2-user/opt/elk-filebeat/logstash

grep port values.yaml


```

#### Filebeat

```
cd /home/ec2-user/opt/elk-filebeat/filebeat

grep logstash values.yaml
```


#### Elastic - helm from elastic

```
/home/ec2-user/opt/elk-filebeat/elasticsearch

grep log values.yaml
```

#### Kibana - same

### Install


```
cd /home/ec2-user/opt/elk-filebeat/filebeat
helm install filebeat .

kubectl get pods --namespace=elk -l app=filebeat-filebeat -w


cd ../logstash
helm install logstash .
kubectl get pods --namespace=elk -l app=logstash-logstash -w

cd ../elasticisearch
helm install elasticsearch  . 


cd ../kibana
### disable ingress service first
helm install kibana .

```

### Inspect




