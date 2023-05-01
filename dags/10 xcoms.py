from datetime import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.utils.trigger_rule import TriggerRule

def print_last_result(**context):
    data = context['ti'].xcom_pull(task_ids='2_second_task')
    print(f'Output of previous task: {data}')

with DAG(dag_id="10_xcoms",
         description="Using bash operator",
         schedule_interval="@daily",
         start_date=datetime(2023, 4, 23),
         end_date=datetime(2023, 4, 25),
         max_active_runs=1) as dag:

    t0 = EmptyOperator(task_id="empty_1",
                       trigger_rule=TriggerRule.ONE_FAILED)

    t1 = BashOperator(task_id="1_first_task",
                      bash_command="sleep 1 && echo $((5*5))")

    t2 = BashOperator(task_id="2_second_task",
                      bash_command="sleep 1 && echo Output of first task {{ ti.xcom_pull(task_ids='1_first_task') }}")

    t3 = PythonOperator(task_id="3_third_task",
                        trigger_rule=TriggerRule.NONE_FAILED,
                        python_callable=print_last_result)

    t4 = EmptyOperator(task_id="empty_2",
                       trigger_rule=TriggerRule.ONE_FAILED)

    t1 >> t2 >> t0 >> t3 >> t4