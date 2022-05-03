from pages.base_page import BasePage
from selenium.webdriver.common.by import By


search_title = (By.CLASS_NAME, 'left-title')
search_title_button = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div/div[2]/ul/li[8]/a')
search_enter = (By.XPATH, '//*[@id="__layout"]/div/div[1]/header/div[4]/div/div')
product_name = (By.XPATH, '//*[@id="__layout"]/div/section/div/div[3]/div[1]/div[1]/a/div[2]/p[2]')
product_article = (By.XPATH, '//*[@id="__layout"]/div/section/div/div[3]/div/div[1]/div[2]/p[1]')
product_collection_name = (By.XPATH, '//*[@id="__layout"]/div/section/div/div[3]/div[1]/div[1]/div[2]/p[2]/span/a')
not_found = (By.XPATH, '//*[@id="__layout"]/div/section/div/div[3]')


class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        self.driver.get('https://keramazavr.ru/search')

    @property
    def check_search_title(self):
        return self.find_element(search_title)

    @property
    def open_search_by_left_menu(self):
        return self.find_element(search_title_button)

    @property
    def search_enter_header_button(self):
        return self.find_element(search_enter)

    @property
    def product_name_title(self):
        return self.find_element(product_name)

    @property
    def product_article_title(self):
        return self.find_element(product_article)

    @property
    def product_collection_name_title(self):
        return self.find_element(product_collection_name)

    @property
    def product_not_found_title(self):
        return self.find_element(not_found)
