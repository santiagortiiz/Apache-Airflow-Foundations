# External task sensor
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.sensors.external_task import ExternalTaskSensor
from datetime import datetime

with DAG(dag_id="8_1_external_sensor",
         description="External task sensor testing",
         schedule_interval="@daily",
         start_date=datetime(2023, 4, 20),
         end_date=datetime(2023, 4, 25),
         max_active_runs=1) as dag:

    t1 = ExternalTaskSensor(task_id="waiting_dag",
                            external_dag_id="4_nesting_tasks",
                            external_task_id="nested_task_2",
                            # seconds to ask if the task is finished (other option is reschedule)
                            poke_interval=10)

    t2 = BashOperator(task_id="processing_finished",
                      bash_command="echo 'Processing after ExternalTaskSensor is finished'",
                      depends_on_past=True)

    t1 >> t2