import time
import logging

from pages.base_page import BasePage
from config.locators import InventoryLocators

from selenium.webdriver.support import expected_conditions as EC

class InventoryPage(BasePage):

    def clickInventory(self):
        self.wait.until(EC.element_to_be_clickable(InventoryLocators.INVENTORY_ITEM_LINK)).click()
        time.sleep(5)

        self.wait.until(EC.element_to_be_clickable(InventoryLocators.ADD_CART_BUTTON)).click()
        logging.info("button add to cart clicked")
        
