import pytest
from selenium import webdriver

@pytest.fixture()
def setup_and_teardown():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.google.com/")
    driver = driver
    yield
    driver.quit()


