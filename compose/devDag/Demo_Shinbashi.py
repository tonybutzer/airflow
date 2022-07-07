from datetime import datetime

from airflow import DAG
from airflow.models import Param

from smartflow.operators.pod import create_pod_task
from smartflow.operators.stac import StacItemSearchOperator
from smartflow.utils.constants import REGION_ID_REGEX


with DAG(
    dag_id="Demo_Shinbashi",
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

    search_sentinel = StacItemSearchOperator(
        task_id="search_sentinel",
        search=[
            {
                "url": "https://earth-search.aws.element84.com/v0",
                "intersects": "{{ macros.smartflow.smart_region_aoi(params.region_id) | tojson }}",
                "datetime": "2018-06-01/2018-12-31",
                "query": {"eo:cloud_cover": {"lt": 50}},
                "collections": ["sentinel-s2-l2a-cogs"],
                "sortby": [{"field": "properties.datetime", "direction": "asc"}],
            }
        ],
        aws_conn_id="smartflow_aws_conn",
        output_loc=f"{s3_work}/stac/items.jsonl",
    )

    shinbashi_chip = create_pod_task(
        task_id="shinbashi_chip",
        image="registry.smartgitlab.com/blacksky/shinbashi:latest",
        cmds=["python3", "/infrastructure/shinbashi/bin/shinbashi-cli.py"],
        arguments=[
            "chip",
            "--output-image-directory",
            f"{s3_work}/chipped/",
            "--output-file-list",
            f"{s3_work}/chipped/items.jsonl",
            "--use-region",
            "--sentinel",
            "--stac-list",
            f"{s3_work}/stac/items.jsonl",
            "--asset-name",
            "B04",
            "{{ macros.smartflow.smart_imagery_annotations_s3() }}/region_models/{{ params.region_id }}.geojson",
        ],
        purpose="etl",
        cpu_limit="2",
        memory_limit="8Gi",
    )

    shinbashi_animate = create_pod_task(
        task_id="shinbashi_animate",
        image="registry.smartgitlab.com/blacksky/shinbashi:latest",
        cmds=["python3", "/infrastructure/shinbashi/bin/shinbashi-cli.py"],
        arguments=[
            "animate",
            "--output-image-directory",
            f"{s3_work}/animated/",
            "--output-file-list",
            f"{s3_work}/animated/items.jsonl",
            "--stac-list",
            f"{s3_work}/chipped/items.jsonl",
            "--fps",
            "3",
            "--imsize",
            "640",
            "480",
            "--float-height",
        ],
        purpose="etl",
        cpu_limit="2",
        memory_limit="8Gi",
    )

    search_sentinel >> shinbashi_chip >> shinbashi_animate
