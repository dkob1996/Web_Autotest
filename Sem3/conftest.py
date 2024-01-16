import pytest
import yaml
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

with open("./testdata.yaml") as f:
   testdata = yaml.safe_load(f)
name = testdata["username"]
browser_name = testdata["browser"]
wait = testdata["wait"]


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
      driver.implicitly_wait(1)
      yield driver
      driver.quit()







