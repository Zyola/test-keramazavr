from pages.catalog_page import CatalogPage
from selenium.webdriver.common.by import By


ceramic_granite = (By.XPATH, '//*[@id="__layout"]/div/section/div/div[2]/div[2]')
ceramic_granite_left_menu = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div/div[2]/ul/li[5]/a')
ceramic_granite_by_icon = (By.XPATH, '//*[@id="__layout"]/div/div[2]/div[1]/div/a[5]')
ceramic_granite_by_bottom_menu = (By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/div[1]/div[2]/ul/li[6]')
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
    def ceramic_granite_left_menu_button(self):
        return self.find_element(ceramic_granite_left_menu)

    @property
    def ceramic_granite_by_icon_button(self):
        return self.find_element(ceramic_granite_by_icon)

    @property
    def ceramic_granite_by_bottom_menu(self):
        return self.find_element(ceramic_granite_by_bottom_menu)

    @property
    def ceramic_granite_title_check(self):
        return self.find_element(ceramic_granite_title)

