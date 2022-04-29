from pages.base_page import BasePage
from selenium.webdriver.common.by import By


delivery_title = (By.CLASS_NAME, 'left-title')


class DeliveryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        self.driver.get('https://keramazavr.ru/information/delivery')

    @property
    def check_delivery_title(self):
        return self.find_element(delivery_title)
