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
        time.sleep(5)


    def remove_all_products(self):
        buttons = self.driver.find_elements(*InventoryLocators.REMOVE_CART_BUTTON)

        logging.info(f"finded remove buttons: {len(buttons)}")

        for button in buttons:
            button.click()

        logging.info(f"{len(buttons)} products removed")
        time.sleep(5)


    def add_products_by_name(self, product_name):
        xpath= (By.XPATH,f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button")
        self.wait.until(EC.element_to_be_clickable(xpath)).click()

        logging.info(f"Added {product_name} to cart")
        time.sleep(5)
        

    def click_Inventory(self):
        self.wait.until(EC.element_to_be_clickable(InventoryLocators.INVENTORY_ITEM_LINK)).click()
        logging.info("linked of the product cliked")
        time.sleep(5)

        self.wait.until(EC.element_to_be_clickable(InventoryLocators.ADD_CART_BUTTON)).click()
        logging.info("button add to cart clicked")
        time.sleep(5)

        self.wait.until(EC.element_to_be_clickable(InventoryLocators.BACK_BUTTON)).click()
        logging.info("button back clicked")
        time.sleep(5)

    def filter_Button(self):
        self.wait.until(EC.element_to_be_clickable(InventoryLocators.FILTER_BUTTTON)).click()
        logging.info("filter button clicked")
        time.sleep(5)

        self.wait.until(EC.element_to_be_clickable(InventoryLocators.OPTION_FILTER_ZA)).click()
        logging.info("option button za clicked")
        time.sleep(5)

    def get_cart_badge_count(self):

        CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
        
        try:
            text_counter = self.driver.find_element(*CART_BADGE).text
            return int(text_counter) 
        except:
            return 0

    def get_first_product_name(self):

        PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
        first_item = self.wait.until(EC.visibility_of_element_located(PRODUCT_NAME))
        return first_item.text

    def cycle_Inventory(self):
        self.click_Inventory()
        self.filter_Button()
        self.add_all_products()
        self.remove_all_products()

        self.add_products_by_name("Sauce Labs Bike Light")
        self.add_products_by_name("Test.allTheThings() T-Shirt (Red)")
        self.add_products_by_name("Sauce Labs Bolt T-Shirt")