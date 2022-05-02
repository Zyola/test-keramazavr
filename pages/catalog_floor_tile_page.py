from pages.catalog_page import CatalogPage
from selenium.webdriver.common.by import By


floor_tale = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div/div[2]/ul/li[3]/a')
floor_tale_by_icon_button = (By.XPATH, '//*[@id="__layout"]/div/div[2]/div[1]/div/a[3]')
floor_tale_by_bottom_menu = (By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/div[1]/div[2]/ul/li[4]')
floor_tale_title = (By.XPATH, '//*[@id="__layout"]/div/section/div[2]/div[1]/ul/li[3]')


class FloorTalePage(CatalogPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        CatalogPage.open(self)
        self.floor_tale_button.click()

    @property
    def floor_tale_button(self):
        return self.find_element(floor_tale)

    @property
    def floor_tale_by_icon(self):
        return self.find_element(floor_tale_by_icon_button)

    @property
    def floor_tale_by_bottom_menu(self):
        return self.find_element(floor_tale_by_bottom_menu)

    @property
    def floor_tale_title_check(self):
        return self.find_element(floor_tale_title)
