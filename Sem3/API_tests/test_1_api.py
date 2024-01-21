import requests
import yaml
from Logger.Logging_function.logging_API_func import *
from paths.static_paths import *

with open(yaml_api_config()) as f1, open(yaml_api_logging_text()) as f2:
    data = yaml.safe_load(f1)
    api_logg = yaml.safe_load(f2)
## API data
api_post_url = data['posts_url']
api_description_answer = data['description_answer']
## Logging text
step_1_name = api_logg['step_1_name']
step_2_name = api_logg['step_2_name']
step_started = api_logg['step_started']
step_ended = api_logg['step_ended']
failed = api_logg['failed']
exception_in = api_logg['exception_in']
expected_result = api_logg['expected_result']

# Test 1 - Check item in collection 
def test_step1(take_token, postitve_name):
    try:
        log_response_api('',step_1_name,step_started)
        header = {'X-Auth-Token': take_token}
        out = requests.get(api_post_url, headers=header, params={'owner': 'notMe'})
        res = [i['title'] for i in out.json()['data']]
        assert postitve_name in res, f'{step_1_name} {failed}'
        log_response_api('',step_1_name,step_ended)
    except AssertionError as e:
        log_exception_api(exception_in,step_1_name,e)

# Test 2: Post item and Check its description.
def test_step2(take_token, post_item):
    try:
        log_response_api('',step_2_name,step_started)
        log_response_api(expected_result,step_2_name,'')
        assert api_description_answer in post_item, f'{step_2_name} {failed}'
        log_response_api('',step_2_name,step_ended)
    except AssertionError as e:
        log_exception_api(exception_in,step_2_name,e)