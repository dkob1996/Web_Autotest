import yaml
from test_page import OperationsHelper

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
name = testdata["username"]
passwd = testdata["password"]

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

