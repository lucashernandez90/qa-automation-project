import time
import logging

from pages.base_page import BasePage
from config.locators import CartLocators
from config.settings import LoginData
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class CartPage(BasePage):

    def clickCart(self):
        self.wait.until(EC.element_to_be_clickable(CartLocators.CART_BUTTON)).click()
        logging.info("cart button clicked")
        time.sleep(5)

        self.wait.until(EC.element_to_be_clickable(CartLocators.CHECKOUT_BUTTON)).click()
        logging.info("checkout button clicked")
        time.sleep(5)

    def fillName(self):
        self.wait.until(EC.visibility_of_element_located(CartLocators.NAME_INPUT)).send_keys(LoginData.NAME)
        self.wait.until(EC.visibility_of_element_located(CartLocators.LAST_NAME_INPUT)).send_keys(LoginData.LAST_NAME)
        self.wait.until(EC.visibility_of_element_located(CartLocators.ZIP_CODE_INPUT)).send_keys(LoginData.ZIP_CODE)
        logging.info("name, last name and zip code filled")
        time.sleep(5)

    def finishCart(self):
        self.wait.until(EC.visibility_of_element_located(CartLocators.CONTINUE_BUTTON)).click()
        logging.info("continue button clicked")
        time.sleep(5)

        self.wait.until(EC.visibility_of_element_located(CartLocators.FINISH_BUTTON)).click()
        logging.info("finish button clicked")
        time.sleep(5)

        self.wait.until(EC.visibility_of_element_located(CartLocators.BACK_HOME_BUTTON)).click()
        logging.info("back home button clicked")
        time.sleep(5)

    def cycleCart(self):
        self.clickCart()
        self.fillName()
        self.finishCart()
