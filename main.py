import time
from config.browser import create_driver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

driver = create_driver()

login_page = LoginPage(driver)
inventory_page = InventoryPage(driver)
cart_page = CartPage(driver)

login_page.cycle_Login()

inventory_page.cycle_Inventory()

cart_page.cycle_Cart()