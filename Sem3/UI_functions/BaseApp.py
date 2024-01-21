import yaml
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Logger.Logging_function.logging_UI_func import *

# Import setting-up data
with open("./yaml_files_UI_tests/testdata.yaml") as f1, open("./yaml_files_UI_tests/logging_text.yaml") as f2:
    testdata = yaml.safe_load(f1)
    logging_txt = yaml.safe_load(f2)
    # Setting-up data
    wait = testdata["wait"]

    # Logging errors
    element_not_found = logging_txt["element_not_found"]
    go_to_the_site_error = logging_txt["go_to_the_site_error"]
    # Error Text
    cant_find_element_by_locator = logging_txt["cant_find_element_by_locator"]


class BasePage:
    def __init__(self, address, driver):
        self.address = address
        self.driver = driver
    
    # Func of finding elements by locator
    def find_element(self, locator):
        try:
            element = WebDriverWait(self.driver, wait).until(EC.presence_of_element_located(locator),
                                                message=f"{cant_find_element_by_locator} {locator}")
        except:
            log_exception(element_not_found, '')
            element = None
        return element

    # Func to get element property from element which we found
    def get_element_property(self, mode, path, property):
        element = self.find_element(mode, path)
        if element is None:
            return None
        else:
            return (element.value_of_css_property(property))
    
    # Func which open browser in curtain address
    def go_to_site(self):
        try:
            self.driver.get(self.address)
        except:
            log_exception(go_to_the_site_error, '')
            return False
        return True

    # Func which get current url from open page
    def get_current_url(self):
        return (self.driver.current_url)
    
    # Func which switch from main browser window to alert window
    def swith_to_alert(self):
        return (self.driver.switch_to.alert)
    
    # Func which get text from alert field
    def get_text_from_alert(self):
        return (self.swith_to_alert().text)
    
    # Func which press "accept" in alert window
    def accept_the_alert(self):
        self.swith_to_alert().accept
