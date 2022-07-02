from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
        'owner': 'airflow',
        'retries':5,
        'retry_delay': timedelta(minutes=2)
        }

with DAG(
        dag_id='1_our_first_dag',
        default_args=default_args,
        description='This is from the tutorial',
        start_date=datetime(2022, 7, 4, 2),
        schedule_interval='@daily'
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command="echo hello world, this is the first task in my DAG"
    )

    task2 = BashOperator(
            task_id='second_task',
            bash_command="echo hello from two"
            )

    task1 >> task2

#dag.cli()
