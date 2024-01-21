import yaml
import time
from UI_functions.test_page import OperationsHelper
from paths.static_paths import *

# Test commands:
## Run pytest with sending results to email
### pytest --html=report.html; python3 Mailer/mail.py
## Start current test
## pytest test_2.py -vv

# Import test data
with open(yaml_ui_testdata()) as f:
    testdata = yaml.safe_load(f)
## Auth data
name = testdata["username"]
passwd = testdata["password"]
## Create Post data
test_title = testdata["test_title"]
test_description = testdata["test_description"]
test_content = testdata["test_content"]
## Valid data
valid_user_name = testdata["hello_prefix"]
## Setting-up data
sleep_time = testdata["sleep_time"]
site_address = testdata['address']


## Step 1: Login with VALID data
def test_step1(browser):
    page = OperationsHelper(address=site_address, driver= browser)
    page.go_to_site()
    page.enter_login(name)
    page.enter_password(passwd)
    page.click_login_button()
    assert page.get_auth_text() == f'{valid_user_name}, {name}'

## Step 2: Create post with VALID data
def test_step2(browser):
    page = OperationsHelper(address=site_address, driver= browser)
    page.click_ad_post()
    page.enter_title(test_title)
    page.enter_description(test_description)
    page.enter_content(test_content)
    page.click_new_post_button()
    time.sleep(sleep_time)
    assert page.get_new_post_info() == test_title