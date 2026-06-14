import time

from config.browser import create_driver

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

driver = create_driver()

login_page = LoginPage(driver)
inventory_page = InventoryPage(driver)

login_page.open()

login_page.login()

time.sleep(5)

inventory_page.clickInventory()
