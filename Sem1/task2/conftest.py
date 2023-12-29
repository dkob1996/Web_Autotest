import pytest
import requests
import yaml

with open('/Users/dmitrii_kobozev/Desktop/Web_Autotests/Sem1/task2/config.yaml', 'r') as f:
    data = yaml.safe_load(f)

@pytest.fixture()
def take_token():
    response = requests.post(data['login_url'], data={'username':data['username'], 'password': data['password']})
    return response.json()['token']

@pytest.fixture()
def postitve_name():
    return 'Котик'