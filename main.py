import time

from config.browser import create_driver

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

driver = create_driver()

login_page = LoginPage(driver)
inventory_page = InventoryPage(driver)
cart_page = CartPage(driver)

login_page.open()
login_page.login()

inventory_page.clickInventory()
inventory_page.add_all_products()
inventory_page.remove_all_products()
inventory_page.add_products_by_name("Sauce Labs Bike Light")
inventory_page.add_products_by_name("Test.allTheThings() T-Shirt (Red)")
inventory_page.add_products_by_name("Sauce Labs Bolt T-Shirt")

cart_page.cycleCart()