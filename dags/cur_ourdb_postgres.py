from airflow import DAG
from airflow.operators.dummy import DummyOperator
from datetime import datetime

with DAG(
    dag_id="cur_ourdb_postgres",
    start_date=datetime(2023, 1, 1),
    schedule_interval="* * * * *",  # Roda a cada minuto
    catchup=False
) as dag:
    inicio = DummyOperator(task_id="inicio")
    fim = DummyOperator(task_id="fim")
    inicio >> fim
