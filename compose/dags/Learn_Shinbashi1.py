from datetime import datetime

from airflow import DAG
from airflow.models import Param

from smartflow.operators.pod import create_pod_task
from smartflow.operators.stac import StacItemSearchOperator
from smartflow.utils.constants import REGION_ID_REGEX

from airflow.operators.python_operator import PythonOperator

def my_function(x):
    return x + " This is a Python function."



with DAG(
    dag_id="Learn_Shinbashi1",
    description="Demo DAG for running Shinbashi",
    params={"region_id": Param(default="US_R113", type="string", pattern=REGION_ID_REGEX)},
    start_date=datetime(2022, 3, 1),
    catchup=False,
    schedule_interval=None,
    max_active_runs=1,
    default_view="grid",
    tags=["demo", "shinbashi"],
) as dag:

    s3_work = "{{ var.value.smartflow_s3_work }}/{{ dag.dag_id }}/{{ run_id }}"
    #s3_work = "{{ dag.dag_id }}/{{ run_id }}"
    #s3_work = "{{ macros.smartflow.smart_imagery_s3() }}/{{ dag.dag_id }}/{{ run_id }}"

    search=[
        {
            "url": "https://earth-search.aws.element84.com/v0",
            #"intersects": "{{ macros.smartflow.smart_region_aoi(params.region_id) | tojson }}",
            "datetime": "2018-06-01/2018-12-31",
            "query": {"eo:cloud_cover": {"lt": 50}},
            "collections": ["sentinel-s2-l2a-cogs"],
            "sortby": [{"field": "properties.datetime", "direction": "asc"}],
        }
    ]
    aws_conn_id="smartflow_aws_conn"
    #output_loc=f"{s3_work}/stac/items.jsonl"
    #my_str = s3_work
    #my_str = "{{ macros.smartflow.smart_imagery_s3() }}/{{ dag.dag_id }}/{{ run_id }}"
    #my_str = search[0]['intersects']
    reg = 'US_R113'
    #my_str =  "{{ macros.smartflow.smart_region_aoi('US_R113') | tojson }}"
    my_str = "{{ macros.smartflow.smart_region_aoi(params.region_id) | tojson }}"
    fake_search = PythonOperator(
             task_id="Fake_search_sentinel",
             python_callable = my_function,
             op_kwargs = {"x" : my_str},
             dag=dag,
             )

    fake_search
