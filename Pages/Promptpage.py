import time
from selenium.common.exceptions import UnexpectedAlertPresentException

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from Pages.Basepage import Basepage


class Prompt(Basepage):
    def __init__(self,driver):
        super().__init__(driver)

    search_name = "q"

    def handle_prompt_and_input(self):
        self.driver.execute_script("setTimeout(function() { prompt('Enter a number:'); }, 2000);")
        time.sleep(5)
        alert = self.driver.switch_to.alert

        prompt_text = alert.text
        alert.accept()
        print("accepted")
        print("Prompt text:", prompt_text)
        # user_input_str = prompt_text.split(":")[1].strip()
        target_element = self.driver.find_element(By.NAME, "q")
        target_element.click
        time.sleep(2)
        target_element.send_keys("hi")
        time.sleep(10)

    def enter_value_in_field(self, user_input):
        target_element = self.driver.find_element(By.NAME,"q")
        target_element.send_keys(user_input)

    def function(self):
        input_value = self.handle_prompt_and_input()
        time.sleep(5)
        self.enter_value_in_field(input_value)
        time.sleep(10)
