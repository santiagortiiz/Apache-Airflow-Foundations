from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime

def awesome_python():
    print("...Running some python code... (task 1)")

with DAG(dag_id="4_nesting_tasks",
         description="Dependencies between tasks",
         start_date=datetime(2023, 3, 24)) as dag:

    task1 = PythonOperator(task_id="nested_task_1",
                            python_callable=awesome_python)

    task2 = BashOperator(task_id="nested_task_2",
                        bash_command="echo 'Running task 2'")

    task3 = BashOperator(task_id="nested_task_3",
                        bash_command="echo 'Running task 3...'")

    task4 = BashOperator(task_id="nested_task_4",
                        bash_command="echo 'Running task 4...'")

    task1 >> task2 >> [task3, task4]

    # task1.set_downstream(task2)
    # task2.set_downstream([task3, task4])


