import time
import logging

from pages.base_page import BasePage
from config.locators import InventoryLocators
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC

class InventoryPage(BasePage):

    def add_all_products(self):
        buttons = self.driver.find_elements(*InventoryLocators.ADD_CART_BUTTON)

        logging.info(f"finded add buttons: {len(buttons)}")

        for button in buttons:
            button.click()

        logging.info(f"{len(buttons)} products add to cart")


    def remove_all_products(self):
        buttons = self.driver.find_elements(*InventoryLocators.REMOVE_CART_BUTTON)

        logging.info(f"finded remove buttons: {len(buttons)}")

        for button in buttons:
            button.click()

        logging.info(f"{len(buttons)} products removed")


    def add_products_by_name(self, product_name):
        xpath= (By.XPATH,f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button")
        self.wait.until(EC.element_to_be_clickable(xpath)).click()

        logging.info(f"Added {product_name} to cart")
        


    def clickInventory(self):
        self.wait.until(EC.element_to_be_clickable(InventoryLocators.INVENTORY_ITEM_LINK)).click()
        time.sleep(5)

        self.wait.until(EC.element_to_be_clickable(InventoryLocators.ADD_CART_BUTTON)).click()
        logging.info("button add to cart clicked")
        time.sleep(5)

        self.wait.until(EC.element_to_be_clickable(InventoryLocators.BACK_BUTTON)).click()
        logging.info("button back clicked")
        time.sleep(5)
