from selenium.webdriver.common.by import By

class LoginLocators:
    USERNAME_INPUT = (By.XPATH, "//input[@placeholder= 'Username']")
    PASSWORD_INPUT = (By.XPATH, "//input[@placeholder= 'Password']")
    LOGIN_BUTTON = (By.XPATH, "//input[@id= 'login-button']")

class InventoryLocators:
    INVENTORY_ITEM_LINK= (By.XPATH, "//div[@class= 'inventory_item_name ']")
    ADD_CART_BUTTON = (By.XPATH, "//button[@class= 'btn btn_primary btn_small btn_inventory']")
