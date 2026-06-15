from selenium.webdriver.common.by import By

class LoginLocators:
    USERNAME_INPUT = (By.XPATH, "//input[@placeholder= 'Username']")
    PASSWORD_INPUT = (By.XPATH, "//input[@placeholder= 'Password']")
    LOGIN_BUTTON = (By.XPATH, "//input[@id= 'login-button']")

class InventoryLocators:
    INVENTORY_ITEM_LINK = (By.XPATH, "//div[@class= 'inventory_item_name ']")
    ADD_CART_BUTTON = (By.XPATH, "//button[contains(@id,'add-to-cart')]")
    REMOVE_CART_BUTTON = (By.XPATH, "//button[contains(@id,'remove')]")
    BACK_BUTTON = (By.XPATH, "//button[@id= 'back-to-products']")
    FILTER_BUTTTON = (By.XPATH, "//span[@class= 'select_container']")
    OPTION_FILTER_ZA = (By.XPATH, "//option[@value = 'za']")

class CartLocators:
    CART_BUTTON = (By.XPATH, "//a[@class= 'shopping_cart_link']")
    CHECKOUT_BUTTON = (By.XPATH, "//button[@id= 'checkout']")
    CONTINUE_BUTTON = (By.XPATH, "//input[@id= 'continue']")
    FINISH_BUTTON = (By.XPATH, "//button[@id= 'finish']")
    CONTINUE_SHOPPING_BUTTON = (By.XPATH, "//button[@id= 'continue-shopping']")
    BACK_HOME_BUTTON = (By.XPATH, "//button[@id= 'back-to-products']")

    NAME_INPUT = (By.XPATH, "//input[@placeholder= 'First Name']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@placeholder= 'Last Name']")
    ZIP_CODE_INPUT = (By.XPATH, "//input[@placeholder= 'Zip/Postal Code']")