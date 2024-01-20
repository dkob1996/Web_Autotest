import yaml
from test_page import OperationsHelper
import time

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
name = testdata["username"]
passwd = testdata["password"]

test_contact_name = testdata["test_contact_name"]
test_contact_valid_email = testdata["test_contact_valid_email"]
test_contact_invalid_email = testdata["test_contact_invalid_email"]
test_contact_content = testdata["test_contact_content"]
test_contact_valid_answer = testdata["test_contact_valid_answer"]

# Start Test
## pytest test_2.py -vv


## auth
def test_step1(browser):
    page = OperationsHelper(address= testdata['address'], driver= browser)
    page.go_to_site()
    page.enter_login(name)
    page.enter_password(passwd)
    page.click_login_button()
    assert page.get_auth_text() == f'{testdata["hello_prefix"]}, {testdata["username"]}'

## open contact form
def test_step2(browser):
    page = OperationsHelper(address=testdata['address'], driver= browser)
    page.click_contact_header_button()
    time.sleep(3)
    assert page.get_contact_form_title() == testdata['contact_form_title']

## sign contact form with VALID email
def test_step3(browser):
    page = OperationsHelper(address=testdata['contact_us_url'], driver= browser)
    page.enter_contact_name(test_contact_name)
    page.enter_contact_email(test_contact_valid_email)
    page.enter_contact_content(test_contact_content)
    page.click_contact_us_button()
    time.sleep(3)
    page.swith_to_alert()
    assert page.get_text_from_alert() == testdata["test_contact_valid_answer"]
