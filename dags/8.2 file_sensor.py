# External task sensor
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.sensors.filesystem import FileSensor
from datetime import datetime

with DAG(dag_id="8_2_file_sensor",
         description="File sensor testing",
         schedule_interval="@daily",
         start_date=datetime(2023, 4, 20),
         max_active_runs=1) as dag:

    t1 = BashOperator(task_id="creating_file",
                      bash_command="sleep 1 && touch /tmp/file.txt",
                      depends_on_past=True)

    t2 = FileSensor(task_id="waiting_file",
                    filepath="/tmp/file.txt")

    t3 = BashOperator(task_id="end_task",
                      bash_command="echo 'New file detected'",
                      depends_on_past=True)

    t1 >> t2 >> t3