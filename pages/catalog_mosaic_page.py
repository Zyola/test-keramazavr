from pages.catalog_page import CatalogPage
from selenium.webdriver.common.by import By


mosaic = (By.XPATH, '//*[@id="__layout"]/div/section/div/div[2]/div[3]/a')
mosaic_left_menu = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div/div[2]/ul/li[6]/a')
mosaic_by_icon = (By.XPATH, '//*[@id="__layout"]/div/div[2]/div[1]/div/a[6]')
mosaic_by_bottom_menu = (By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/div[1]/div[2]/ul/li[7]/a')
mosaic_title = (By.XPATH, '//*[@id="__layout"]/div/section/div[2]/div[1]/ul/li[3]')


class MosaicPage(CatalogPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        CatalogPage.open(self)
        self.mosaic_button.click()

    @property
    def mosaic_button(self):
        return self.find_element(mosaic)

    @property
    def mosaic_left_menu_button(self):
        return self.find_element(mosaic_left_menu)

    @property
    def mosaic_by_icon_button(self):
        return self.find_element(mosaic_by_icon)

    @property
    def mosaic_by_bottom_menu_button(self):
        return self.find_element(mosaic_by_bottom_menu)

    @property
    def mosaic_title_check(self):
        return self.find_element(mosaic_title)
