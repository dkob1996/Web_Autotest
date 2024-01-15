import pytest
import yaml
from module import Site

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
site = Site(testdata["address"])

def test_color(div_cookies, er1):
    assert site.get_element_property("css", div_cookies, "background-color") == er1, "Test 1 fail"

def test_height(div_cookies, er2):
    assert site.get_element_property("css", div_cookies, "height") == er2, "Test 2 fail"

def teardown():
    site.close()