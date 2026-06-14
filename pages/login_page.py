import time
import logging

from pages.base_page import BasePage

from config.settings import Login

from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(level=logging.INFO)

class LoginPage(BasePage):

    def open(self):

        self.driver.get(Login.URL_SITE)
    
    def login(self):

        self.wait.until(EC.visibility_of_element_located(Login.PLACE_HOLDER_USERNAME)).send_keys(Login.USERNAME)
        self.wait.until(EC.visibility_of_element_located(Login.PLACE_HOLDER_PASSWORD)).send_keys(Login.PASSWORD)
        logging.info("username and password filled")

        time.sleep(5)

        self.wait.until(EC.element_to_be_clickable(Login.LOGIN_BUTTON)).click()
        logging.info("login button clicked")