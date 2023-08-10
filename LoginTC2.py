# This file provides the main code to the automation for OrangeHRM
 
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from Test_Data_1 import data_login2
from Test_Locators_1 import locators_login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginTest2:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)
   
    def login(self):
        self.driver.find_element(by=By.NAME, value=locators_login.Locators_login1().username_input_box).send_keys(data_login2.Data_login2().username)
        self.driver.find_element(by=By.NAME, value=locators_login.Locators_login1().password_input_box).send_keys(data_login2.Data_login2().password)
        self.driver.find_element(by=By.XPATH, value=locators_login.Locators_login1().submit_button).click()

        # Wait for error message to appear
        error_message = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p"))
        
        )
        expected_message = "Invalid credentials"
        actual_message = error_message.text
        if expected_message == actual_message:
            print("Invalid credentials")
           
    def shutdown(self):
        self.driver.quit()


N = LoginTest2(data_login2.Data_login2().url)
N.login()
N.shutdown()