import yaml
import time
from UI_functions.test_page import OperationsHelper
from paths.static_paths import *

# Test commands:
## Run pytest with sending results to email
### pytest --html=report.html; python3 Mailer/mail.py
## Start current test
## pytest test_3.py -vv

# Import test data
with open(yaml_ui_testdata()) as f:
    testdata = yaml.safe_load(f)
## Auth data
name = testdata["username"]
passwd = testdata["password"]
## Contact us page data
test_contact_name = testdata["test_contact_name"]
test_contact_valid_email = testdata["test_contact_valid_email"]
test_contact_content = testdata["test_contact_content"]
test_contact_valid_answer = testdata["test_contact_valid_answer"]
## Valid data
valid_user_name = testdata["hello_prefix"]
contact_us_page_title = testdata['contact_form_title']
contact_us_answer_valid = testdata["test_contact_valid_answer"]
## Setting-up data
sleep_time = testdata["sleep_time"]
site_address = testdata['address']
contact_us_address = testdata['contact_us_url']


## Step 1: Login with VALID data
def test_step1(browser):
    page = OperationsHelper(address= site_address, driver= browser)
    page.go_to_site()
    page.enter_login(name)
    page.enter_password(passwd)
    page.click_login_button()
    assert page.get_auth_text() == f'{valid_user_name}, {name}'

## Step 2: Open contact form page
def test_step2(browser):
    page = OperationsHelper(address=site_address, driver= browser)
    page.click_contact_header_button()
    time.sleep(sleep_time)
    assert page.get_contact_form_title() == contact_us_page_title

## Step 3: Sign contact form with VALID email
def test_step3(browser):
    page = OperationsHelper(address=contact_us_address, driver= browser)
    page.enter_contact_name(test_contact_name)
    page.enter_contact_email(test_contact_valid_email)
    page.enter_contact_content(test_contact_content)
    page.click_contact_us_button()
    time.sleep(sleep_time)
    page.swith_to_alert()
    assert page.get_text_from_alert() == contact_us_answer_valid
