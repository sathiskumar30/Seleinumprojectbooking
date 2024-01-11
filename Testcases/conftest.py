import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from Utilities import Configuration
@pytest.fixture()
def setup_and_teardown(request):
    driver = None
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)
    options.add_argument("--disable-notifications")
    options.add_argument("--start-maximized")
    options.add_experimental_option("detach",True)
    driver.maximize_window()
    url = Configuration.read_configuration("base info", "url")
    print(url)
    driver.get(url)
    request.cls.driver = driver
    # yield
    # driver.quit()




