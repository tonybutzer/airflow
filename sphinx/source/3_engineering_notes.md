# Engineering Notes

# smartflow references

- https://blacksky.smartgitlab.com/smartflow/markdown/Framework/Getting-Started.html
- https://app.slack.com/client/TN3QR7WAH/C03KCBSUMC0/thread/C03KCBSUMC0-1654795666.581149
- https://blacksky.smartgitlab.com/smartflow/markdown/Administration/Deployment.html#installation

- Repository Link: https://smartgitlab.com/blacksky/smartflow
- Documentation Link: https://blacksky.smartgitlab.com/smartflow

> This channel is to be used for:
SmartFlow Announcements
General SmartFlow questions
To coordinate specific tech support (most likely to be moved off channel for resolution) 

## Airflow Tutorial Videos - document good to bad

- https://www.youtube.com/watch?v=AHMm1wfGuHE


## Airflow Operators

- bash
- noop
- SimpleHttpOperator
- EmailOperator


    BashOperator - executes a bash command

    PythonOperator - calls an arbitrary Python function

    EmailOperator - sends an email

- https://stackoverflow.com/questions/62660347/airflow-send-email-with-aws-ses



## Running Airflow with Docker Compose

- https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html
- https://airflow.apache.org/docs/apache-airflow/stable/tutorial.html


```
docker-compose --profile flower up
# put in a makefile - tony

```


## Docker Simple Orcherstration - python docker starts

### Rylie Notes

>


## Airflow Scaling Celery

- https://airflow.apache.org/docs/apache-airflow/1.10.1/howto/executor/use-celery.html


## Just Celery

https://www.youtube.com/watch?v=mcX_4EvYka4

## Terraform

- https://medium.com/typeforms-engineering-blog/deploy-airflow-1-10-10-in-kubernetes-using-terraform-and-helm-2476f03f07d0


## TroubleShooting

- https://stackoverflow.com/questions/45534535/airflow-not-loading-dags-in-usr-local-airflow-dags
- https://zero-to-jupyterhub.readthedocs.io/en/latest/jupyterhub/installation.html
- https://zero-to-jupyterhub.readthedocs.io/en/latest/jupyterhub/customizing/user-storage.html
- https://github.com/jupyterhub/zero-to-jupyterhub-k8s/issues/1597
- https://aws.amazon.com/about-aws/whats-new/2019/12/run-serverless-kubernetes-pods-using-amazon-eks-and-aws-fargate/
- https://platform9.com/blog/fargate-vs-upstream-kubernetes/
- https://aws.amazon.com/blogs/containers/running-airflow-on-aws-fargate/
- https://microk8s.io/docs/addon-dashboard
- https://k9scli.io/
- https://vinayak.io/2020/09/10/day-24-jupyterhub-airflow-microk8s/
- https://jupyterhub.readthedocs.io/en/0.7.1/getting-started.html
- https://jamesdefabia.github.io/docs/user-guide/kubectl/kubectl_proxy/
