# Install Airflow core.

This allows to install and upgrade airflow separately and independently from providers.

https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-no-providers-${PYTHON_VERSION}.txt

https://raw.githubusercontent.com/apache/airflow/constraints-latest/constraints-3.9.txt

pip install "apache-airflow[celery]==2.5.3" --constraint https://raw.githubusercontent.com/apache/airflow/constraints-latest/constraints-no-providers-3.9.txt