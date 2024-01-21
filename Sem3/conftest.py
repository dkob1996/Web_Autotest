import pytest
import yaml
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Import setting-up data
with open("./yaml_files_UI_tests/testdata.yaml") as f:
   testdata = yaml.safe_load(f)
   browser_name = testdata["browser"]
   sleep_time = testdata["sleep_time"]

# Fuxture to set-up curtain browser where test
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







