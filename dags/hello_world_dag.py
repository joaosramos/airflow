from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

def say_hello():
    print("👋 Olá, mundo! Airflow está funcionando!")

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='hello_world_dag',
    default_args=default_args,
    description='Uma DAG de teste que diz olá',
    schedule_interval='@hourly',  # roda todo início de hora
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=['teste'],
) as dag:

    tarefa = PythonOperator(
        task_id='dizer_ola',
        python_callable=say_hello
    )

    tarefa
