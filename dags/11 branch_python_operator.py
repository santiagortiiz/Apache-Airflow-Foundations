from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import BranchPythonOperator
from datetime import datetime


def _choose():
    flow_A = 'flow_A'
    flob_B = 'flow_B'

    next_task_id = flob_B
    return next_task_id

with DAG(dag_id="11_branch_python_operator",
         description="Branching tasks",
         schedule_interval="@daily",
         start_date=datetime(2023, 4, 23),
         end_date=datetime(2023, 4, 25),
         max_active_runs=1) as dag:

    task_A = BashOperator(task_id="flow_A",
                          bash_command="echo 'Running flow A'")

    task_B = BashOperator(task_id="flow_B",
                          bash_command="echo 'Running flow B'")

    branch = BranchPythonOperator(task_id="branch",
                                  python_callable=_choose)

    branch >> [task_A, task_B]