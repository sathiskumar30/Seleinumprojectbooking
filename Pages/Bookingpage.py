import time
from selenium.webdriver import Keys
from Pages.Basepage import Basepage


class Bookings(Basepage):
    def __init__(self,driver):
        super().__init__(driver)

    from_xpath = "// input[ @ placeholder = 'Enter city or airport']"
    to_xpath = "//div[@class='dstn u-ib u-v-align-bottom u-text-left']//input[@placeholder='Enter city or airport']"
    cross_xpath = "//div[@class='orgn u-ib u-v-align-bottom u-text-left']//div[@class='clear-input ixi-icon-cross']"
    search_classname = "u-ripple"
    date_by_css_selector = "input[placeholder='Depart']"
    passenger_id = "passenger-list"
    teenager_xpath = "teenager_xpath "
    return_xpath = "//input[@placeholder='Return']"
    book_button_xpath = "//div[@class='book-cta']//button[@class='c-btn u-link  enabled']"
    confirm_book_btn_xpath = "//div[@class='cnfrm-cntnr continue']//button"
    stop = "// div[ @class ='fltr u-pos-rel arln'] // span[@ class ='checkbox-list']// div[@ data-checkboxindex=0]// span[@ class ='ixi-icon-tick check-icon']"
    bus_from_xpath = "//input[@placeholder='From Station']"
    bus_to_xpath = "//input[@placeholder='To Station']"
    tomorrow_linktext = "Tomorrow"
    boarding_arrow_xpath = "//div[contains(text(),'Boarding Point')]"
    dropping_arrow_xpath = "//div[contains(text(),'Dropping Point')]"
    show_seats_xpath = "(//div[@class='text-grey']/preceding-sibling::button[@class='btn bus-info-btn filled primary sm inactive button'])[1]"
    seat_select_xpath = "//*[name()='svg']/*[name()='rect' and position()=1][@fill='white' and @stroke='#BDBDBD']/../parent::button"
    another_boarding_point_xpath = "(//div[@class='scrollable-container place-container primary ']//input[@type='checkbox'])[1]"
    contiune_btn_xpath = "//button[@class='btn btn-shake filled primary md inactive button']"

    def select_from(self,value,drop_value):
        self.drop_down("from_xpath",self.from_xpath,value,drop_value)

    def select_to(self,value,drop_value):
        self.drop_down("to_xpath",self.to_xpath,value,drop_value)

    def cancel_existing(self):
        self.wait_click_a_element("cross_xpath",self.cross_xpath,10)

    def departure_date(self,date):
        self.date("date_by_css_selector",self.date_by_css_selector,date)

    def return_date(self):
        self.click_a_element("return_xpath",self.return_xpath)
        # script = f"document.querySelector(\"input[placeholder='Depart']\").value='{date}';"
        # self.driver.execute_script(script)

    def search_button(self):
        self.click_a_element("search_classname",self.search_classname)

    def passenger_list(self, value1,value2):
        self.adult_selection(value1)
        self.child_selection(value2)

    def adult_selection(self,value):
        self.click_a_element("passenger_id", self.passenger_id)
        value = value
        locator_value = f"//div[@class='passanger-class-input u-pos-rel']//div[1]//div[2]//span[{value}]"
        self.wait_click_a_element("teenager_xpath", locator_value,5)

    def child_selection(self,value):
        self.click_a_element("passenger_id", self.passenger_id)
        value = value
        locator_value = f"//div[@class='u-box passanger-class-list flex-container']//div[2]//div[2]//span[{value}]"
        self.wait_click_a_element("teenager_xpath", locator_value,5)

    # def stop_selection(self):
    #     self.wait_click_a_element("stop_xpath",self.stop_xpath,40)

    def stop_slection_multiple(self):
        for i in range(0,2):
            stop_xpath = "//div[@class='stops']//div[@data-checkboxindex=" +str(i)+ "]//span[@class='ixi-icon-tick check-icon']"
            self.wait_click_a_element("stop_xpath",stop_xpath,20)

    def flight_brand(self):
        for i in range(0,2):
            model_xpath = "//div[@class='fltr u-pos-rel arln']//span[@class='checkbox-list']//div[@data-checkboxindex="+str(i)+"]//span[@class ='ixi-icon-tick check-icon']"
            self.wait_click_a_element("model_xpath",model_xpath,5)

    def booking_button(self):
        self.wait_click_a_element("book_button_xpath",self.book_button_xpath,5)

    def confirm_button(self):
        self.wait_click_a_element("confirm_book_btn_xpath",self.confirm_book_btn_xpath,10)

    def flight_booking(self,fromm,to,dep_date,adult,child):
        self.cancel_existing()
        self.select_from(fromm)
        self.select_to(to)
        self.departure_date(dep_date)
        self.return_date()
        time.sleep(2)
        self.passenger_list(adult,child)
        self.search_button()
        time.sleep(40)
        self.stop_slection_multiple()
        self.flight_brand()
        self.booking_button()
        self.confirm_button()

    def bus_select_from(self ,value, drop_value):
        self.drop_down("bus_from_xpath", self.bus_from_xpath, value, drop_value)

    def bus_select_to(self ,value, drop_value):
        self.drop_down("bus_to_xpath", self.bus_to_xpath, value, drop_value)

    def tomorrow_btn(self):
        self.click_a_element("tomorrow_linktext",self.tomorrow_linktext)

    def selecting_ac(self):
        for i in range(1,3):
            model_xpath = "//div[@id='seat-filter-bus-type']//a["+str(i)+"]"
            self.wait_click_a_element("model_xpath",model_xpath,10)

    def boarding_arrow_click(self):
        self.wait_click_a_element("boarding_arrow_xpath",self.boarding_arrow_xpath,5)

    def dropping_arrow_click(self):
        self.wait_click_a_element("dropping_arrow_xpath",self.dropping_arrow_xpath,5)

    def boarding_point(self,boarding_point):
        label_text_to_select = boarding_point
        boarding_point_xpath = f'//label[text()="{label_text_to_select}"]/preceding-sibling::input[@type="checkbox"]'
        self.click_a_element("boarding_point_xpath",boarding_point_xpath)

    def dropping_point(self,dropping_point):
        label_text_to_select = dropping_point
        dropping_point_xpath = f'//label[text()="{label_text_to_select}"]/preceding-sibling::input[@type="checkbox"]'
        self.click_a_element("dropping_arrow_xpath",dropping_point_xpath)

    def show_seats_btn(self):
        self.wait_click_a_element("show_seats_xpath",self.show_seats_xpath,5)

    def seat_selection_btn(self):
        self.wait_click_a_element("seat_select_xpath",self.seat_select_xpath,10)

    def selecting_another_board(self):
        self.click_a_element("another_boarding_point_xpath",self.another_boarding_point_xpath)

    def continue_btn(self):
        self.click_a_element("contiune_btn_xpath",self.contiune_btn_xpath)

    def bus_booking(self,fromm,to,drop_value,boarding_point,dropping_point):
        time.sleep(2)
        self.bus_select_from(fromm,drop_value)
        self.bus_select_to(to,drop_value)
        self.tomorrow_btn()
        self.selecting_ac()
        self.boarding_arrow_click()
        self.boarding_point(boarding_point)
        # self.dropping_arrow_click()
        # self.dropping_point(dropping_point)
        time.sleep(4)
        self.show_seats_btn()
        self.seat_selection_btn()
        self.selecting_another_board()
        time.sleep(1)
        self.selecting_another_board()
        self.continue_btn()
        time.sleep(3)

