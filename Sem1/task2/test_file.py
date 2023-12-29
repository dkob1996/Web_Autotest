import requests
import yaml
from logging_fucn import log_response, log_assert_error, log_exception
from static_paths import yaml_path

with open(yaml_path(), 'r') as f:
    data = yaml.safe_load(f)

# Test 1 - Check item in collection 
def test_step1(take_token, postitve_name):
    name_step = 'Test 1: Check item in collection.'
    try:
        log_response(f'  Test: {name_step} - STARTED')
        header = {'X-Auth-Token': take_token}
        out = requests.get(data['posts_url'], headers=header, params={'owner': 'notMe'})
        res = [i['title'] for i in out.json()['data']]
        assert postitve_name in res, f'{name_step} Fail'
        log_response(f'  Test: {name_step} - ENDED')
    except AssertionError as e:
        log_exception(f'EXCEPTION in {name_step}: \n{e}')

# Test 2: Post item and Check its description.
def test_step2(take_token, post_item):
    name_step = 'Test 2: Post item and Check its description.'
    try:
        log_response(f'  Test: {name_step} - STARTED')
        log_response(f'Expected result: {data["description_answer"]}')
        assert data['description_answer'] in post_item, f'{name_step} Fail'
        log_response(f'  Test: {name_step} - ENDED')
    except AssertionError as e:
        log_exception(f'EXCEPTION in {name_step}: \n{e}')