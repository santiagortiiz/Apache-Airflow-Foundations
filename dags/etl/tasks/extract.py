import requests

def extract():
    url = 'http://extract:80/api/extract/'
    res = requests.get(url)
    return res.json()