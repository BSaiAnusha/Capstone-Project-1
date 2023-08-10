# This file provides the main code to the automation for OrangeHRM
 
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from Test_Data_1 import data_login1
from Test_Locators_1 import locators_login
from selenium.webdriver.common.by import By


class LoginTest1:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)
   
    def login(self):
        self.driver.find_element(by=By.NAME, value=locators_login.Locators_login1().username_input_box).send_keys(data_login1.Data_login1().username)
        self.driver.find_element(by=By.NAME, value=locators_login.Locators_login1().password_input_box).send_keys(data_login1.Data_login1().password)
        self.driver.find_element(by=By.XPATH, value=locators_login.Locators_login1().submit_button).click()
   
    def shutdown(self):
        self.driver.quit()


a = LoginTest1(data_login1.Data_login1().url)
a.login()
a.shutdown()
print("The user is logged in successfully")
