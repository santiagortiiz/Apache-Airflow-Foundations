import requests

def transform(**context):
    extracted_data = context['ti'].xcom_pull(task_ids='1_extract')

    url = f'http://transform:80/api/transform/?prev_result={extracted_data}'
    data = {
        "source_data": {
            "some_field": "some_value"
        },
        "some_schema": {
            "some_field": "target_field"
        }
    }
    res = requests.post(url, json=data)
    return res.json()