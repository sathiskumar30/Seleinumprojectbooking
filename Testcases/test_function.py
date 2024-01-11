import time

import pytest
from Pages.Homepage import Frontpage
from Pages.Loginpage import LoginPage
from Pages.Bookingpage import Bookings
from Testcases.Basetest import BaseTest


class Bookingpage:
    pass


class Test_Website(BaseTest):
    def test_login(self):
        home_page = Frontpage(self.driver)
        login_page = home_page.login_button()
        login_page.signup_funtion("sksathis2002@gmail.com","Sathis kumar","8778164504")

    def test_flight_booking(self):
        booking_page = Bookings(self.driver)
        booking_page.flight_booking("Chennai","Delhi","26/01/2024",3,2)

    def test_bus_booking(self):
        home_page = Frontpage(self.driver)
        bus_booking = home_page.bus_booking_btn()
        bus_booking.bus_booking("Chennai","Coimbatore",1,"Chennai","Gandthipuram")


