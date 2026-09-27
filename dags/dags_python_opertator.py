from airflow.sdk import DAG

import datetime

import pendulum

from airflow.providers.standard.operators.python import PythonOperator

with DAG(
    dag_id="dags_python_operator",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False
) as dag: