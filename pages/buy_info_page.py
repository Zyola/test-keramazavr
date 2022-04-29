from pages.base_page import BasePage
from selenium.webdriver.common.by import By


buy_info_title = (By.CLASS_NAME, 'left-title')


class BuyInfoPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        self.driver.get('https://keramazavr.ru/information/kak-sdelat-pokupku')

    @property
    def check_buy_info_title(self):
        return self.find_element(buy_info_title)
