from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.trigger_rule import TriggerRule
from datetime import datetime

with DAG(dag_id="7_monitoring",
         description="DAG Monitoring",
         schedule_interval="@daily",
         start_date=datetime(2023, 4, 20),
         end_date=datetime(2023, 4, 25),
         max_active_runs=1) as dag:

    t1 = BashOperator(task_id="scheduled_task_1",
                      bash_command="sleep 1 && echo 'Scheduled task 1'",
                      trigger_rule=TriggerRule.ALL_SUCCESS,
                      retries=2,
                      retry_delay=5, # delay in seconds
                      depends_on_past=True) # Executes if previous tasks succedded

    t2 = BashOperator(task_id="scheduled_task_2",
                      bash_command="sleep 1 && echo 'Scheduled task 2'")
    t3 = BashOperator(task_id="scheduled_task_3",
                      bash_command="sleep 1 && echo 'Scheduled task 3'")
    t4 = BashOperator(task_id="scheduled_task_4",
                      bash_command="sleep 1 && echo 'Scheduled task 4'")

    t1 >> [t2, t3] >> t4