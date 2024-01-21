import yaml
import logging
from selenium.webdriver.common.by import By
from Logger.Logging_function.logging_UI_func import *
from UI_functions.BaseApp import BasePage
from paths.static_paths import *

class TestSearchLocator:
    # Parse data from yaml files
    with open(yaml_ui_locators()) as f1, open(yaml_ui_logging_text()) as f2:
    ## Parse locators from yaml file to dictionary
        locators = yaml.safe_load(f1)
        logging_txt = yaml.safe_load(f2)
    ids = dict()
    for locator in locators['Xpath'].keys():
        ids[locator] = (By.XPATH, locators['Xpath'][locator])
    for locator in locators['CSS_SELECTOR'].keys():
        ids[locator] = (By.CSS_SELECTOR, locators['CSS_SELECTOR'][locator])
    ## Parse logging text from yaml
    send_text_to_element = logging_txt["send_text_to_element"]
    element_not_found = logging_txt["element_not_found"]
    get_text_from_element = logging_txt["get_text_from_element"]
    click_to_element = logging_txt["click_to_element"]
    cannot_click_to_element = logging_txt["cannot_click_to_element"]
    

class OperationsHelper(BasePage):
    # Func which enter text into fields with curtain locator
    def enter_text(self, locator, word, description=None):
        if description:
            log_debug_ui(TestSearchLocator.send_text_to_element, description)
        else:
            log_debug_ui(TestSearchLocator.send_text_to_element, locator)
        field = self.find_element(locator)
        if field is None:
            if description:
                log_error_ui(TestSearchLocator.element_not_found, description)
            else:
                log_error_ui(TestSearchLocator.element_not_found, locator)
        else:
            field.clear()
            field.send_keys(word)

    # Func which get text from fields with curtain locator
    def get_text(self, locator, description=None):
        if description:
            log_debug_ui(TestSearchLocator.get_text_from_element, description)
        else:
            log_debug_ui(TestSearchLocator.get_text_from_element, locator)     
        try:
            field = self.find_element(locator)
            text = field.text
        except:
            text = None
            if description:
                log_error_ui(TestSearchLocator.element_not_found, description)
            else:
                log_error_ui(TestSearchLocator.element_not_found, locator)
        return text

    # Func which does click to button with curtain locator
    def click_button(self, locator, description=None):
        if description:
            log_debug_ui(TestSearchLocator.click_to_element, description)
        else:
            log_debug_ui(TestSearchLocator.click_to_element, locator)
        field = self.find_element(locator)
        if field:
            try:
                field.click()
            except:
                if description:
                    log_exception_ui(TestSearchLocator.cannot_click_to_element, description)
                else:
                    log_exception_ui(TestSearchLocator.cannot_click_to_element, locator)     
            

    # Functions which use main functions and transfer to them curtain locators
    ## Login functions                
    def enter_login(self, word):
        self.enter_text(TestSearchLocator.ids['LOGIN_FIELD'], word)
    
    def enter_password(self, word):
        self.enter_text(TestSearchLocator.ids['PASS_FIELD'], word)

    def click_login_button(self):
        self.click_button(TestSearchLocator.ids['LOGIN_BUTTON_FIELD'])

    def get_error_text(self):
        text = self.get_text(TestSearchLocator.ids['ERROR_FIELD'])
        return text
        
    def get_auth_text(self):
        return self.get_text(TestSearchLocator.ids['HELLO_USERNAME_SEPECTOR'])

    ## Create Post functions
    def click_ad_post(self):
        self.click_button(TestSearchLocator.ids['NEW_POST_BUTTON'])
    
    def enter_title(self, word):
        self.enter_text(TestSearchLocator.ids['POST_TITLE_FIELD'], word)

    def enter_description(self, word):
        self.enter_text(TestSearchLocator.ids['POST_DESCRIPTION_FIELD'], word)

    def enter_content(self, word):
        self.enter_text(TestSearchLocator.ids['POST_CONTENT_FIELD'], word)

    def click_new_post_button(self):
        self.click_button(TestSearchLocator.ids['POST_SAVE_BUTTON_PATH'])

    def get_new_post_info(self):
        return self.get_text(TestSearchLocator.ids['POST_SAVE_RESULT_FIELD'])
    
    def get_new_post_title(self):
        return self.get_text(TestSearchLocator.ids['POST_TITLE_RESULT_FIELD'])
    
    ## Contact Form functions
    def click_contact_header_button(self):
        self.click_button(TestSearchLocator.ids['CONTACT_HEADER_BUTTON'])

    def get_contact_form_title(self):
        return self.get_text(TestSearchLocator.ids['CONTACT_FORM_TITLE_FIELD'])
    
    def enter_contact_name(self, word):
        self.enter_text(TestSearchLocator.ids['CONTACT_NAME_FIELD'], word)

    def enter_contact_email(self, word):
        self.enter_text(TestSearchLocator.ids['CONTACT_EMAIL_FIELD'], word)

    def enter_contact_content(self, word):
        self.enter_text(TestSearchLocator.ids['CONTACT_CONTENT_FIELD'], word)

    def click_contact_us_button(self):
        self.click_button(TestSearchLocator.ids['CONTACT_US_BUTTON'])

    
    

    