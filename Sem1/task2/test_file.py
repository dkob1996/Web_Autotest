import requests
import yaml

with open('/Users/dmitrii_kobozev/Desktop/Web_Autotests/Sem1/task2/config.yaml', 'r') as f:
    data = yaml.safe_load(f)

def test_step1(take_token, postitve_name):
    header = {'X-Auth-Token': take_token}
    out = requests.get(data['posts_url'], headers=header, params={'owner': 'notMe'}).json()['data']
    res = [i['title'] for i in out]
    assert postitve_name in res, 'Test1 Fail'