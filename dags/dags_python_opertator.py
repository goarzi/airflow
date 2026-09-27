from airflow.sdk import DAG

import datetime

import pendulum

from airflow.providers.standard.operators.python import PythonOperator

with DAG(
    dag_id="dags_python_operator",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2021, 1, 1, tz="asia/Seoul"),
    catchup=False
) as dag:
    def select_fruit(): 
        fruits = ["apple", "banana", "orange", "berry"]
        rand_int=random.randint(0,3)
        print(fruits[rand_int])

    py_t1=PythonOperator(
        task_id="py_t1",
        python_callable=select_fruit
    )
    py_t1