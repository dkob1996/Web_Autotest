import yaml
with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    browser = testdata["browser"]
    wait = testdata["wait"]
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, address, driver):
        self.address = address
        self.driver = driver
    
    def find_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator),
                                               message=f"Can't find element by locator {locator}")
        return element

    def get_element_property(self, mode, path, property):
        element = self.find_element(mode, path)
        return (element.value_of_css_property(property))
    
    def go_to_site(self):
        self.driver.get(self.address)

    def get_current_url(self):
        url = self.driver.current_url
        return url