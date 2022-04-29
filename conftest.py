from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='function')
def driver():
    service = Service(executable_path='/home/zyola/chromedriver')
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()
