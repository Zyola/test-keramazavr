from pages.catalog_page import CatalogPage
from selenium.webdriver.common.by import By


ceramic_tale = (By.XPATH, '//*[@id="__layout"]/div/section/div/div[2]/div[1]')
ceramic_tale_left_menu = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div/div[2]/ul/li[4]/a')
ceramic_tale_by_icon_button = (By.XPATH, '//*[@id="__layout"]/div/div[2]/div[1]/div/a[4]')
ceramic_tale_by_bottom_menu = (By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/div[1]/div[2]/ul/li[5]')
ceramic_tale_title = (By.XPATH, '//*[@id="__layout"]/div/section/div[2]/div[1]/ul/li[3]')


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

    @property
    def ceramic_tale_left_menu_button(self):
        return self.find_element(ceramic_tale_left_menu)

    @property
    def ceramic_tale_by_icon_button(self):
        return self.find_element(ceramic_tale_by_icon_button)

    @property
    def ceramic_tale_by_bottom_menu(self):
        return self.find_element(ceramic_tale_by_bottom_menu)

    @property
    def ceramic_tale_title_check(self):
        return self.find_element(ceramic_tale_title)
