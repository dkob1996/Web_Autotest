import requests
import yaml
from logging_fucn import log_response, log_assert_error, log_exception

with open('/Users/dmitrii_kobozev/Desktop/Web_Autotests/Sem1/task2/config.yaml', 'r') as f:
    data = yaml.safe_load(f)

def test_step1(take_token, postitve_name):
    header = {'X-Auth-Token': take_token}
    out = requests.get(data['posts_url'], headers=header, params={'owner': 'notMe'}).json()['data']
    res = [i['title'] for i in out]
    log_assert_error(res)
    assert postitve_name in res, 'Test1 Fail'

def test_step2(take_token, post_item):
    assert data['description'] in post_item, 'Test2 Fail'