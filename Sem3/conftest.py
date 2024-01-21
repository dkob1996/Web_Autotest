import pytest
import yaml
import requests
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from paths.static_paths import *
from Logger.Logging_function.logging_API_func import *


# Import setting-up data
with open(yaml_ui_testdata()) as f1, open(yaml_api_config()) as f2, open(yaml_api_logging_text()) as f3:
   testdata = yaml.safe_load(f1)
   data = yaml.safe_load(f2)
   api_logg = yaml.safe_load(f3)

## UI data
browser_name = testdata["browser"]
sleep_time = testdata["sleep_time"]
## API data
api_login_url = data['login_url']
api_username = data['username']
api_password = data['password']
api_post_url = data['posts_url']
api_post_title = data['title']
api_post_description = data['description']
api_post_content = data['content']
api_valid_answer = data['postitve_answer']
## API Logging text
token_text = api_logg['token_text']
error_in = api_logg['error_in']
step_auth = api_logg['step_auth']
step_post_item = api_logg['step_post_item']
## API Long logging response
post_data = api_logg['post_data']
post_data_title = api_logg['post_data_title']
post_data_description = api_logg['post_data_description']
post_data_contact = api_logg['post_data_contact']



# Fixtures for UI testing
## Fuxture to set-up curtain browser where test
@pytest.fixture(scope='session')
def browser():
      if browser_name == "firefox":
         service = Service(executable_path=GeckoDriverManager().install())
         options = webdriver.FirefoxOptions()
         driver = webdriver.Firefox(service=service, options=options)
      elif browser_name == "chrome":
         service = Service(executable_path=ChromeDriverManager().install())
         options = webdriver.ChromeOptions()
         driver = webdriver.Chrome(service=service, options=options)
      driver.implicitly_wait(sleep_time)
      yield driver
      driver.quit()

# Fixtures for API testing
## Fixture which get authorization token and remembered it
@pytest.fixture()
def take_token():
    try:
        response = requests.post(api_login_url, data={'username':api_username, 'password': api_password})
        log_response_api(f'Auth response: {response}')
        token = response.json()['token']
        data['token']=token
        log_response_api(token_text,data["token"],'')
        return token
    except Exception as e:
        log_exception_api(error_in,step_auth,e)

## Fuxture which return valid answer
@pytest.fixture()
def postitve_name():
    return api_valid_answer

## Fixture which create post
@pytest.fixture()
def post_item():
    try:
        item_data = requests.post(api_post_url, headers={'X-Auth-Token': data['token']},data={
            'username': api_username,
            'password': api_password,
            'title': api_post_title,
            'description': api_post_description,
            'content':api_post_content})
        log_long_response_api(post_data,post_data_title,item_data.json()["title"],post_data_description,item_data.json()["description"],post_data_contact,item_data.json()["content"])
        return item_data.json()['description']
    except Exception as e:
        log_exception_api(error_in,step_post_item,e)


