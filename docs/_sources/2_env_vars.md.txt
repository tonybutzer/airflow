## Env Variables or metastore variables

- example {{ var.value.smartflow_s3_work }}

- env = AIRFLOW_VAR_SMARTFLOW_S3_WORK=s3://eccoe-scratch 

- https://www.youtube.com/watch?v=bRaMAD5vx3g

#### Todo
- write simple dag for displaying any variable



```
aws ssm get-parameters-by-path --recursive --path /smartflow/
```
