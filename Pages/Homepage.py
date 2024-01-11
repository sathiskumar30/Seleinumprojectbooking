from selenium.webdriver.common.by import By
from Pages.Loginpage import LoginPage
from Pages.Basepage import Basepage
from Pages.Bookingpage import Bookings


class Frontpage(Basepage):
    def __init__(self,driver):
        super().__init__(driver)

    login_xpath= "//span[text()='Login/SignUp']"
    bus_linktext = "Buses"

    def login_button(self):
        self.click_a_element("login_xpath",self.login_xpath)
        return LoginPage(self.driver)

    def bus_booking_btn(self):
        self.click_a_element("bus_linktext",self.bus_linktext)
        return Bookings(self.driver)

    # login_button_xpath = "//div[@class='d-flex']//li[1]//a[1]"
    # def sales_btn(self):
    #     self.click_a_element("link_text_value_linktext",self.link_text_value_linktext)
    #     # self.driver.find_element(By.LINK_TEXT, self.link_text_value).click()
    #     return SalePage(self.driver)