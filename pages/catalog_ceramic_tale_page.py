from pages.catalog_page import CatalogPage
from selenium.webdriver.common.by import By


ceramic_tale = (By.LINK_TEXT, '/catalog/ceramic-tile')


class CeramicTalePage(CatalogPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        CatalogPage.open(self)
        self.ceramic_tale_button.click()

    @property
    def ceramic_tale_button(self):
        return self.find_element(ceramic_tale)
