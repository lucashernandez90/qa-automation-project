from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Login:
    URL_SITE = 'https://www.saucedemo.com/' 
    USERNAME = 'standard_user'
    PASSWORD = 'secret_sauce'
    
    PLACE_HOLDER_USERNAME = (By.XPATH, "//input[@placeholder= 'Username']")
    PLACE_HOLDER_PASSWORD = (By.XPATH, "//input[@placeholder= 'Password']")
    LOGIN_BUTTON = (By.XPATH, "//input[@id= 'login-button']")

class Buttons:
    BUTTON_INVENTORY_ITEM = (By.XPATH, "//div[@class= 'inventory_item_name ']")
    BUTTON_ADD_CART = (By.XPATH, "//button[@class= 'btn btn_primary btn_small btn_inventory']")

    



