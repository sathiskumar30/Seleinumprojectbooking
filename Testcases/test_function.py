from selenium.webdriver.common.by import By
import pytest

@pytest.mark.usefixtures("setup_and_teardown")
class GoogleSearch:
    def test_search_google(self):
        self.driver.find_element(By.LINK_TEXT, "Gmail").click()


