import requests
import json

Url = "https://ru.yougile.com/api-v2/"
payload = {"login": "jjiqcbr451@ramvv.com", "password": "Gfhjkm@024"}
headers = {'Content-Type': 'application/json'}


# Получаем ID компании
def get_company_id(name):
    payload['name'] = name
    response = requests.post(Url + 'auth/companies',
                             json=payload,
                             headers=headers
                             )
    filtered_list = response.json()
    return filtered_list['content'][0]['id']


# Получаем API для компании
def get_api_key(company_id):
    payload['companyId'] = company_id
    api_response = requests.post(Url + 'auth/keys',
                                 json=payload,
                                 headers=headers
                                 )
    key_data = api_response.json()
    return key_data['key']


