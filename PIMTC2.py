# This file provides the main code to the automation for OrangeHRM for PIMTC2


from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from Test_Data_2 import data_pim1
from Test_Locators_2 import locators_pim1
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains



class Pimtest2:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)
   
    def login(self):
            self.driver.find_element(by=By.NAME, value=locators_pim1.Locators_login1().username_input_box).send_keys(data_pim1.Data_login1().username)
            self.driver.find_element(by=By.NAME, value=locators_pim1.Locators_login1().password_input_box).send_keys(data_pim1.Data_login1().password)
            self.driver.find_element(by=By.XPATH, value=locators_pim1.Locators_login1().submit_button).click()

            pimbtn = self.driver.find_element(by=By.XPATH, value=locators_pim1.newadd().pim_box).click()
            
            add1 = self.driver.find_element(by=By.XPATH, value=locators_pim1.newadd().addbutn_box).click()
                
            self.driver.find_element(by=By.NAME, value=locators_pim1.newadd().firstname_input_box).send_keys(data_pim1.Employeeinfo().firstname)
            self.driver.find_element(by=By.NAME, value=locators_pim1.newadd().middlename_input_box).send_keys(data_pim1.Employeeinfo().middlename)
            self.driver.find_element(by=By.NAME, value=locators_pim1.newadd().lastname_input_box).send_keys(data_pim1.Employeeinfo().lastname)
            self.driver.find_element(by=By.XPATH, value=locators_pim1.newadd().EmployeeID_input_box).send_keys(data_pim1.Employeeinfo().EmployeeID)
            image_input = self.driver.find_element(By.XPATH, locators_pim1.newadd().image_input_box)
            self.driver.execute_script("arguments[0].setAttribute('value', arguments[1]);", image_input,r'C:\Users\HP\Desktop\Workspace\AT-17\Guvi Project1\empimage.png')
            wait = WebDriverWait(self.driver, 15)
            sbtn= self.driver.find_element(by=By.XPATH, value=locators_pim1.newadd().savebtn_box).click()
            wait = WebDriverWait(self.driver, 30)
            nickname2 = self.driver.find_element(by=By.XPATH, value=locators_pim1.newadd().nickname_input_box).send_keys(data_pim1.Employeeinfo().nickname)
            self.driver.execute_script("document.getElementsByClassName('oxd-input oxd-input--active')[0].value = arguments[0]", nickname2)
            wait = WebDriverWait(self.driver, 30)
            savbutn=    self.driver.find_element(by=By.XPATH, value=locators_pim1.newadd().savebtn2_box).click()
            self.driver.execute_script("document.getElementsByClassName('oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space')[0].click()", savbutn)     
            
            action = ActionChains(self.driver)
            action.click(on_element=pimbtn).perform()
            action.click(on_element=add1).perform()
                
            wait = WebDriverWait(self.driver, 15)    
        
    def shutdown(self):
        self.driver.quit() 
        

u = Pimtest2(data_pim1.Data_login1().url)
u.login()
u.shutdown()
print('Employee update successful')
