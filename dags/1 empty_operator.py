from datetime import datetime
from airflow import DAG
from airflow.operators.empty import EmptyOperator

# Context manager syntax
with DAG(dag_id="1_empty_operator",
         description="first processing",
         start_date=datetime(2023, 4, 24),
         schedule_interval="@once") as dag:

    # Operators should be defined here
    task_1 = EmptyOperator(task_id="dummy")
    task_1
