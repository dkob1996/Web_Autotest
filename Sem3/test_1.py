import yaml
from test_page import OperationsHelper
import time
# pytest --html=report.html; python3 mail.py

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
name = testdata["username"]
passwd = testdata["password"]

test_title = testdata["test_title"]
test_description = testdata["test_description"]
test_content = testdata["test_content"]


def test_step1(browser):
    page = OperationsHelper(address=testdata['address'], driver= browser)
    page.go_to_site()
    page.enter_login('test')
    page.enter_password('test')
    page.click_login_button()
    assert page.get_error_text() == testdata['401_error']

def test_step2(browser):
    page = OperationsHelper(address=testdata['address'], driver= browser)
    page.enter_login(name)
    page.enter_password(passwd)
    page.click_login_button()
    assert page.get_auth_text() == f'{testdata["hello_prefix"]}, {testdata["username"]}'

def test_step3(browser):
    page = OperationsHelper(address=testdata['address'], driver= browser)
    page.click_ad_post()
    page.enter_title(test_title)
    page.enter_description(test_description)
    page.enter_content(test_content)
    page.click_new_post_button()
    time.sleep(3)
    assert page.get_new_post_info() == test_title
    