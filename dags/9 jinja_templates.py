# External task sensor
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime


templated_command = """
{% for file in params.filenames %}
    echo "{{ ds }}"
    echo "{{ file }}"
{% endfor %}
"""

with DAG(dag_id="9_jinja_template",
         description="Trying jinja templates",
         schedule_interval="@daily",
         start_date=datetime(2023, 4, 24)) as dag:

    t1 = BashOperator(task_id="task_1",
                      bash_command=templated_command,
                      params={"filenames": ["file_A.txt", "file_B.txt"]},
                      depends_on_past=True)