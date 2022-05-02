from pages.catalog_page import CatalogPage
from selenium.webdriver.common.by import By


wall_tale = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div/div[2]/ul/li[2]/a')
wall_tale_title = (By.XPATH, '//*[@id="__layout"]/div/section/div[2]/div[1]/ul/li[3]')
wall_tale_by_bottom_menu = (By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/div[1]/div[2]/ul/li[3]')
wall_tale_by_icon_button = (By.XPATH, '//*[@id="__layout"]/div/div[2]/div[1]/div/a[2]/div')


class WallTalePage(CatalogPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        CatalogPage.open(self)
        self.wall_tale_button.click()

    @property
    def wall_tale_button(self):
        return self.find_element(wall_tale)

    @property
    def wall_tale_button_by_icon(self):
        return self.find_element(wall_tale_by_icon_button)

    @property
    def wall_tale_button_by_bottom_menu(self):
        return self.find_element(wall_tale_by_bottom_menu)

    @property
    def wall_tale_title_check(self):
        return self.find_element(wall_tale_title)
