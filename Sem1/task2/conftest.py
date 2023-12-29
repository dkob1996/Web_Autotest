import pytest
import requests
import yaml
from logging_fucn import log_response, log_exception
from static_paths import yaml_path

with open(yaml_path(), 'r') as f:
    data = yaml.safe_load(f)

@pytest.fixture()
def take_token():
    name_step = 'AUTH'
    try:
        response = requests.post(data['login_url'], data={'username':data['username'], 'password': data['password']})
        log_response(f'Auth response: {response}')
        token = response.json()['token']
        data['token']=token
        log_response(f'Token: {data["token"]}')
        return token
    except Exception as e:
        log_exception(f'Error in {name_step}: \n{e}')

@pytest.fixture()
def postitve_name():
    return data['postitve_answer']

@pytest.fixture()
def post_item():
    name_step = 'POST ITEM'
    try:
        item_data = requests.post(data['posts_url'], headers={'X-Auth-Token': data['token']},data={
            'username': data['username'],
            'password': data['password'],
            'title': data['title'],
            'description': data['description'],
            'content': data['content']})
        log_response(f'POST DATA: \nTitle: {item_data.json()["title"]}, \nDescription: {item_data.json()["description"]}, \nContent: {item_data.json()["content"]}')
        return item_data.json()['description']
    except Exception as e:
        log_exception(f'Error in {name_step}: \n{e}')