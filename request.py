# https://www.data.go.kr/
# !pip install xmltodict
import requests
import xmltodict
import json
from pprint import pprint


url = 'target url'
payload = {'ServiceKey': 'serivce key', 
            'param name': 'required params',
           }
columns = ['name', 'key', 'to', 'get value']

def get_api_data(url, payload, columns):
    data = []
    res = requests.get(url, params=payload) 
    
    if res.status_code == 200:
        jt = json.loads(json.dumps(xmltodict.parse(res.text)))
        # pprint(jt)
        
        for item in jt['response']['body']['items']['item']:
            data.append([item[f'{col}'] for col in columns])
    
    return data
