from pages.base_page import BasePage
from selenium.webdriver.common.by import By


chapter_catalog = (By.CLASS_NAME, 'active')


class CatalogPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @property
    def chapter_catalog(self):
        return self.find_element(chapter_catalog)

