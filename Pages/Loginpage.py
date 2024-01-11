from Pages.Basepage import Basepage

class LoginPage(Basepage):
    def __init__(self,driver):
        super().__init__(driver)

    email_xpath = "//input[contains(@class,'c-input u-v-align-bottom')]"
    login_classname = "LoginButton_loginText__NDMyN"
    login2_xpath = "//button[normalize-space()='LOGIN']"
    gmail_button_xpath = "//span[text()='email']"
    name_name = "name"
    number_name = "mobile"
    submit_xpath = "//button[normalize-space()='Register']"

    def click_on_gmail(self):
        self.click_a_element("gmail_button_xpath",self.gmail_button_xpath)

    def enter_email(self,email):
        self.enter_a_value("email_xpath",self.email_xpath,email)

    def click_on_login2(self):
        self.click_a_element("login2_xpath", self.login2_xpath)

    def enter_name(self,name):
        self.wait_enter_a_value("name_name",self.name_name,name)

    def enter_number(self, number):
        self.enter_a_value("number_name", self.number_name, number)

    def click_submit_button(self):
        self.click_a_element("submit_xpath",self.submit_xpath)

    def signup_funtion(self,email,name,number):
        self.click_on_gmail()
        self.enter_email(email)
        self.click_on_login2()
        self.enter_name(name)
        self.enter_number(number)
        self.click_submit_button()
