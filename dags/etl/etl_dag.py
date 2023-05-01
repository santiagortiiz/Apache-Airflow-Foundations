from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.trigger_rule import TriggerRule

from etl.tasks import extract, transform, load

with DAG(dag_id="12_NEW_ETL",
         description="Run an ETL based on microservices",
         schedule_interval="@daily",
         start_date=datetime(2023, 4, 23),
         end_date=datetime(2023, 4, 25),
         max_active_runs=1) as dag:

    t1 = PythonOperator(task_id="1_extract",
                        python_callable=extract,
                       trigger_rule=TriggerRule.ALL_SUCCESS)

    t2 = PythonOperator(task_id="2_transform",
                        python_callable=transform,
                       trigger_rule=TriggerRule.ALL_SUCCESS)

    t3 = PythonOperator(task_id="3_load",
                        python_callable=load,
                       trigger_rule=TriggerRule.ALL_SUCCESS)

    t1 >> t2 >> t3