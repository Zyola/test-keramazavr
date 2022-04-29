from pages.base_page import BasePage
from selenium.webdriver.common.by import By


cart_title = (By.XPATH, '//*[@id="__layout"]/div/section/div/div/ul/li[2]')


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        self.driver.get('https://keramazavr.ru/cart/')

    @property
    def check_cart_title(self):
        return self.find_element(cart_title)
