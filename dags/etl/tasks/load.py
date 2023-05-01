import requests

def load(**context):
    transformed_data = context['ti'].xcom_pull(task_ids='2_transform')

    url = 'http://load:80/api/load/'
    res = requests.post(url, json=transformed_data)
    return res.json()