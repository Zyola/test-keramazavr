from pages.base_page import BasePage
from selenium.webdriver.common.by import By


pay_info_title = (By.CLASS_NAME, 'left-title')


class PayInfoPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        self.driver.get('https://keramazavr.ru/information/payment')

    @property
    def check_pay_info_title(self):
        return self.find_element(pay_info_title)
