from selenium.webdriver.common.by import By

class LoginLocators:
    USERNAME_INPUT = (By.XPATH, "//input[@placeholder= 'Username']")
    PASSWORD_INPUT = (By.XPATH, "//input[@placeholder= 'Password']")
    LOGIN_BUTTON = (By.XPATH, "//input[@id= 'login-button']")

class InventoryLocators:
    INVENTORY_ITEM_LINK= (By.XPATH, "//div[@class= 'inventory_item_name ']")
    ADD_CART_BUTTON = (By.XPATH, "//button[contains(@id,'add-to-cart')]")
    REMOVE_CART_BUTTON = (By.XPATH, "//button[contains(@id,'remove')]")
    BACK_BUTTON = (By.XPATH, "//button[@id= 'back-to-products']")

class CartLocators:
    CART_BUTTON = (By.XPATH, "//a[@class= 'shopping_cart_link']")

