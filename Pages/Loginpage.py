from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class SalePage:
    def __init__(self,driver):
        self.driver = driver
    full_name ="FullName"
    def enter_username(self,name):
        self.driver.find_element(By.NAME,self.full_name).click()
        self.driver.find_element(By.NAME,self.full_name).send_keys(name)
        print(name,"this is the name mr buddy")

