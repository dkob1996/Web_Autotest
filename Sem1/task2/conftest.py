import pytest
import requests
import yaml

with open('/Users/dmitrii_kobozev/Desktop/Web_Autotests/Sem1/task2/config.yaml', 'r') as f:
    data = yaml.safe_load(f)

@pytest.fixture()
def take_token():
    response = requests.post(data['login_url'], data={'username':data['username'], 'password': data['password']})
    token = response.json()['token']
 #   data['token']=token
    return token

@pytest.fixture()
def postitve_name():
    return data['postitve_answer']

@pytest.fixture()
def post_item():
    item_data = requests.post(data['posts_url'], headers={'X-Auth-Token': take_token},data={
        'username': data['username'],
        'password': data['password'],
        'title': data['title'],
        'description': data['description'],
        'content': data['content']})
    return item_data.json()['description']