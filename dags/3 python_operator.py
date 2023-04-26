from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def awesome_python():
    print("...Running some python code...")

with DAG(dag_id="3_python_operator",
         description="Using bash operator",
         schedule_interval="@once",
         start_date=datetime(2023, 4, 24)) as dag:

    t1 = PythonOperator(task_id="hello_with_python",
                        python_callable=awesome_python)

    t1