from BaseApp import BasePage
from selenium.webdriver.common.by import By
import yaml
import logging

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    address = testdata["address"]

class TestSearchLocator:
    
    LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")

    PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")

    ERROR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")

    LOGIN_BUTTON_FIELD = (By.CSS_SELECTOR, """button""")

    HELLO_USERNAME_SEPECTOR = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[3]/a""")

    NEW_POST_BUTTON = (By.XPATH, """//*[@id="create-btn"]""")   

    POST_TITLE_FIELD = (By.XPATH, """//*[@id="create-item"]/div/div/div[1]/div/label/input""")

    POST_DESCRIPTION_FIELD = (By.XPATH, """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea""")

    POST_CONTENT_FIELD = (By.XPATH, """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea""")

    POST_SAVE_BUTTON_PATH = (By.XPATH, """//*[@id="create-item"]/div/div/div[7]/div/button/span""")

    POST_SAVE_RESULT_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div[1]/h1""")

    POST_TITLE_RESULT_FIELD = (By.XPATH, """ //*[@id="app"]/main/div/div/div[1]/div/div[3]/div[2]/div[1]/table/tbody/tr[1]/td[2]""")

    CONTACT_HEADER_BUTTON = (By.XPATH, """ //*[@id="app"]/main/nav/ul/li[2]/a""")
    
    CONTACT_FORM_TITLE_FIELD = (By.XPATH, """ //*[@id="app"]/main/div/div/h1""")
    
    CONTACT_NAME_FIELD = (By.XPATH, """ //*[@id="contact"]/div[1]/label/input""")

    CONTACT_EMAIL_FIELD = (By.XPATH, """ //*[@id="contact"]/div[2]/label/input""")

    CONTACT_CONTENT_FIELD = (By.XPATH, """ //*[@id="contact"]/div[3]/label/span/textarea""")

    CONTACT_US_BUTTON = (By.XPATH, """ //*[@id="contact"]/div[4]/button""")


class OperationsHelper(BasePage):
    def enter_text(self, locator, word):
        field = self.find_element(locator)
        field.clear()
        field.send_keys(word)
    
    def get_text(self, locator):
        try:
            field = self.find_element(locator)
            text = field.text
        except:
            text = None
            logging.exception(text)
        logging.info(text)
        logging.info('abc')
        return text

    
    def click_button(self, locator):
        field = self.find_element(locator)
        field.click()



    def enter_login(self, word):
        self.enter_text(TestSearchLocator.LOGIN_FIELD, word)
    
    def enter_password(self, word):
        self.enter_text(TestSearchLocator.PASS_FIELD, word)

    def click_login_button(self):
        self.click_button(TestSearchLocator.LOGIN_BUTTON_FIELD)

    def get_error_text(self):
        text = self.get_text(TestSearchLocator.ERROR_FIELD)
        return text
        
    def get_auth_text(self):
        return self.get_text(TestSearchLocator.HELLO_USERNAME_SEPECTOR)

    def click_ad_post(self):
        self.click_button(TestSearchLocator.NEW_POST_BUTTON)
    
    def enter_title(self, word):
        self.enter_text(TestSearchLocator.POST_TITLE_FIELD, word)

    def enter_description(self, word):
        self.enter_text(TestSearchLocator.POST_DESCRIPTION_FIELD, word)

    def enter_content(self, word):
        self.enter_text(TestSearchLocator.POST_CONTENT_FIELD, word)

    def click_new_post_button(self):
        self.click_button(TestSearchLocator.POST_SAVE_BUTTON_PATH)

    def get_new_post_info(self):
        return self.get_text(TestSearchLocator.POST_SAVE_RESULT_FIELD)
    
    def get_new_post_title(self):
        return self.get_text(TestSearchLocator.POST_TITLE_RESULT_FIELD)
    
    def click_contact_header_button(self):
        self.click_button(TestSearchLocator.CONTACT_HEADER_BUTTON)

    def get_contact_form_title(self):
        return self.get_text(TestSearchLocator.CONTACT_FORM_TITLE_FIELD)
    
    def enter_contact_name(self, word):
        self.enter_text(TestSearchLocator.CONTACT_NAME_FIELD, word)

    def enter_contact_email(self, word):
        self.enter_text(TestSearchLocator.CONTACT_EMAIL_FIELD, word)

    def enter_contact_content(self, word):
        self.enter_text(TestSearchLocator.CONTACT_CONTENT_FIELD, word)

    def click_contact_us_button(self):
        self.click_button(TestSearchLocator.CONTACT_US_BUTTON)

    
    

    