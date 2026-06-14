import time
import logging

from pages.base_page import BasePage
from config.settings import Buttons

from selenium.webdriver.support import expected_conditions as EC

from config.settings import InventoryItem

class InventoryPage(BasePage):

    def clickInventory(self):
        self.wait.until(EC.element_to_be_clickable(Buttons.BUTTON_INVENTORY_ITEM)).click()
        time.sleep(5)

        self.wait.until(EC.element_to_be_clickable(Buttons.BUTTON_ADD_CART)).click()
        logging.info("button add to cart clicked")
        
