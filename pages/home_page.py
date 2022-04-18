from pages.base_page import BasePage
from selenium.webdriver.common.by import By


catalog_button = (By.CLASS_NAME, 'side-m')
delivery_button = (By.LINK_TEXT, '/information/delivery')


class HomePage(BasePage):
    def __init__(self, driver):
        # super().__init__(driver)
        self.driver = driver

    def open(self):
        self.driver.get('https://keramazavr.ru/')

    def open_catalog(self):
        self.find_element(catalog_button).click()

    def open_delivery(self):
        self.find_element(delivery_button).click()

