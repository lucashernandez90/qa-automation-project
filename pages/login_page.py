import time
import logging
from config.settings import LoginData
from config.locators import LoginLocators
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(level=logging.INFO)

class LoginPage(BasePage):

    def open(self):
        self.driver.get(LoginData.URL_SITE)
    
    def login(self, username=LoginData.USERNAME, password=LoginData.PASSWORD):
        # REMOVIDOS OS ASTERISCOS DAQUI DE DENTRO:
        self.wait.until(EC.visibility_of_element_located(LoginLocators.USERNAME_INPUT)).send_keys(username)
        self.wait.until(EC.visibility_of_element_located(LoginLocators.PASSWORD_INPUT)).send_keys(password)
        logging.info("username and password filled")
        time.sleep(5)

        self.wait.until(EC.element_to_be_clickable(LoginLocators.LOGIN_BUTTON)).click()
        logging.info("login button clicked")
    
    def is_logged(self):
        return "inventory" in self.driver.current_url

    def cycle_Login(self):
        self.open()
        self.login()