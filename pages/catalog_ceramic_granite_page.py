from pages.catalog_page import CatalogPage
from selenium.webdriver.common.by import By


ceramic_granite = (By.XPATH, '//*[@id="__layout"]/div/section/div/div[2]/div[2]')
ceramic_granite_title = (By.XPATH, '//*[@id="__layout"]/div/section/div[2]/div[1]/ul/li[3]')


class CeramicGranitePage(CatalogPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        CatalogPage.open(self)
        self.ceramic_granite_button.click()

    @property
    def ceramic_granite_button(self):
        return self.find_element(ceramic_granite)

    @property
    def ceramic_granite_title_check(self):
        return self.find_element(ceramic_granite_title)

