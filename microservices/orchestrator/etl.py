import requests

def extract():
    url = 'http://extract:80/api/extract/'
    res = requests.get(url)
    return res.json()

def transform(prev_result):
    url = f'http://transform:80/api/transform/?prev_result={prev_result}'
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

def load(data):
    url = 'http://load:80/api/load/'
    res = requests.post(url, json=data)
    return res.json()

def run_etl():
    raw_data = extract()
    transformed_data = transform(raw_data)
    res = load(transformed_data)
    return res

if __name__ == '__main__':
    res = run_etl()
    print(res)
