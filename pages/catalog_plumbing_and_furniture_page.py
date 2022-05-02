from pages.catalog_page import CatalogPage
from selenium.webdriver.common.by import By


plumbing_and_furniture = (By.XPATH, '//*[@id="__layout"]/div/section/div/div[2]/div[4]/a')
plumbing_and_furniture_left_menu = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div/div[2]/ul/li[7]/a')
plumbing_and_furniture_by_icon = (By.XPATH, '//*[@id="__layout"]/div/div[2]/div[1]/div/a[7]')
plumbing_and_furniture_by_bottom_menu = (By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/div[1]/div[2]/ul/li[8]')
plumbing_and_furniture_title = (By.XPATH, '//*[@id="__layout"]/div/section/div[2]/div[1]/ul/li[3]')


class PlumbingAndFurniturePage(CatalogPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        CatalogPage.open(self)
        self.plumbing_and_furniture_button.click()

    @property
    def plumbing_and_furniture_button(self):
        return self.find_element(plumbing_and_furniture)

    @property
    def plumbing_and_furniture_left_menu_button(self):
        return self.find_element(plumbing_and_furniture_left_menu)

    @property
    def plumbing_and_furniture_by_icon_button(self):
        return self.find_element(plumbing_and_furniture_by_icon)

    @property
    def plumbing_and_furniture_by_bottom_menu_button(self):
        return self.find_element(plumbing_and_furniture_by_bottom_menu)

    @property
    def plumbing_and_furniture_title_check(self):
        return self.find_element(plumbing_and_furniture_title)
