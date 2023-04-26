from airflow import DAG
from datetime import datetime
from my_operator import MyOperator

with DAG(dag_id="5_custom_operator",
         description="Custom operator",
         schedule_interval="@once",
         start_date=datetime(2023, 3, 24)) as dag:


    t1 = MyOperator(task_id="custom_operator_task",
                    name="Santiago")

    t1