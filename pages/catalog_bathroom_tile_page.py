from pages.catalog_page import CatalogPage
from selenium.webdriver.common.by import By


bathroom_tale = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div/div[2]/ul/li[1]/a')
bathroom_tale_title = (By.XPATH, '//*[@id="__layout"]/div/section/div[2]/div[1]/ul/li[3]')
bathroom_tale_by_bottom_menu = (By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/div[1]/div[2]/ul/li[2]')
bathroom_tale_by_icon = (By.XPATH, '//*[@id="__layout"]/div/div[2]/div[1]/div/a[1]')


class BathroomTalePage(CatalogPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        CatalogPage.open(self)
        self.bathroom_tale_button.click()

    @property
    def bathroom_tale_button(self):
        return self.find_element(bathroom_tale)

    @property
    def bathroom_tale_title_check(self):
        return self.find_element(bathroom_tale_title)

    @property
    def bathroom_tale_by_icon_button(self):
        return self.find_element(bathroom_tale_by_icon)

    @property
    def bathroom_tale_by_bottom_menu(self):
        return self.find_element(bathroom_tale_by_bottom_menu)
