from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(dag_id="6_scheduling",
         description="Using bash operator",
         schedule_interval="@daily",
         start_date=datetime(2023, 4, 20),
         end_date=datetime(2023, 4, 25),
         max_active_runs=1) as dag:

    t1 = BashOperator(task_id="scheduled_task_1",
                      bash_command="sleep 1 && echo 'Scheduled task 1'")
    t2 = BashOperator(task_id="scheduled_task_2",
                      bash_command="sleep 1 && echo 'Scheduled task 2'")
    t3 = BashOperator(task_id="scheduled_task_3",
                      bash_command="sleep 1 && echo 'Scheduled task 3'")
    t4 = BashOperator(task_id="scheduled_task_4",
                      bash_command="sleep 1 && echo 'Scheduled task 4'")

    t1 >> [t2, t3] >> t4