from pages.base_page import BasePage
from selenium.webdriver.common.by import By


catalog_title = (By.XPATH, '//*[@id="__layout"]/div/section/div/div[1]/ul/li[2]')


class CatalogPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        self.driver.get('https://keramazavr.ru/catalog')

    @property
    def check_catalog_title(self):
        return self.find_element(catalog_title)


