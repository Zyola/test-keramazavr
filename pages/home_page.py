from pages.base_page import BasePage
from selenium.webdriver.common.by import By


chapter_catalog_by_header = (By.XPATH, '//*[@id="__layout"]/div/div[1]/header/div[2]/ul/li[1]/a')
delivery_button_by_header = (By.XPATH, '//*[@id="__layout"]/div/div[1]/header/div[2]/ul/li[2]/a')
buy_info_button_by_header = (By.XPATH, '//*[@id="__layout"]/div/div[1]/header/div[2]/ul/li[3]/a')
pay_info_button_by_header = (By.XPATH, '//*[@id="__layout"]/div/div[1]/header/div[2]/ul/li[4]/a')
contacts_button_by_header = (By.XPATH, '//*[@id="__layout"]/div/div[1]/header/div[2]/ul/li[5]/a')
cart_button_by_header = (By.CLASS_NAME, 'cart')
search_button_by_header = (By.XPATH, '//*[@id="__layout"]/div/div[1]/header/div[3]/div[1]/li/a')


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        self.driver.get('https://keramazavr.ru/')

    @property
    def open_catalog_by_header(self):
        return self.find_element(chapter_catalog_by_header)

    @property
    def open_delivery_by_header(self):
        return self.find_element(delivery_button_by_header)

    @property
    def open_buy_info_by_header(self):
        return self.find_element(buy_info_button_by_header)

    @property
    def open_pay_info_by_header(self):
        return self.find_element(pay_info_button_by_header)

    @property
    def open_contacts_by_header(self):
        return self.find_element(contacts_button_by_header)

    @property
    def open_cart_by_header(self):
        return self.find_element(cart_button_by_header)

    @property
    def open_search_header(self):
        return self.find_element(search_button_by_header)

