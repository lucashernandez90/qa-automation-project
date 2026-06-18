import pytest
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By

@pytest.fixture
def logged_in_driver(driver):
    login_page = LoginPage(driver)
    login_page.cycle_login() 
    return driver


def test_click_inventory(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    inventory_page.click_Inventory()

    assert "inventory.html" in logged_in_driver.current_url

def test_add_all_products(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    inventory_page.add_all_products()

    assert inventory_page.get_cart_badge_count() == 6

def test_add_products_by_name(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    inventory_page.add_products_by_name("Sauce Labs Bike Light")
    inventory_page.add_products_by_name("Sauce Labs Bolt T-Shirt")

    assert inventory_page.get_cart_badge_count() == 2

def test_filter_button_za(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    inventory_page.filter_Button()
    first_product = inventory_page.get_first_product_name()

    assert first_product == "Test.allTheThings() T-Shirt (Red)"
