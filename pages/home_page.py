from pages.base_page import BasePage
from selenium.webdriver.common.by import By


catalog_button_by_header = (By.XPATH, '//*[@id="__layout"]/div/div[1]/header/div[2]/ul/li[1]/a')
delivery_button_by_header = (By.XPATH, '//*[@id="__layout"]/div/div[1]/header/div[2]/ul/li[2]/a')
buy_info_button_by_header = (By.XPATH, '//*[@id="__layout"]/div/div[1]/header/div[2]/ul/li[3]/a')
pay_info_button_by_header = (By.XPATH, '//*[@id="__layout"]/div/div[1]/header/div[2]/ul/li[4]/a')
contacts_button_by_header = (By.XPATH, '//*[@id="__layout"]/div/div[1]/header/div[2]/ul/li[5]/a')
cart_button_by_header = (By.CLASS_NAME, 'cart')
search_button_by_header = (By.XPATH, '//*[@id="__layout"]/div/div[1]/header/div[3]/div[1]/li/a')
search_title = (By.XPATH, '//*[@id="__layout"]/div/div[1]/header/div[4]/div/input')
reverting_logo_button_by_header = (By.XPATH, '//*[@id="__layout"]/div/div[1]/header/div[2]/a/div[1]/img')

catalog_button_by_column_menu = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div/div[3]/ul/li[1]/a')
delivery_button_by_column_menu = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div/div[3]/ul/li[2]/a')
buy_info_button_by_column_menu = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div/div[3]/ul/li[3]/a')
articles_button_by_column_menu = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div/div[3]/ul/li[4]/a')
contacts_button_by_column_menu = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div/div[3]/ul/li[5]/a')

catalog_button_by_bottom_menu = (By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/div[1]/div[2]/ul/li[1]/a')
information_button_by_bottom_menu = (By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/div[1]/div[3]/ul/li[2]/a')
contacts_button_by_bottom_menu = (By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/div[1]/div[3]/ul/li[2]/a')
delivery_button_by_bottom_menu = (By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/div[1]/div[3]/ul/li[3]/a')
pay_info_button_by_bottom_menu = (By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/div[1]/div[3]/ul/li[4]/a')
articles_button_by_bottom_menu = (By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/div[1]/div[3]/ul/li[5]/a')
privacy_policy_by_bottom_menu = (By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/div[1]/div[3]/ul/li[6]/a')


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        self.driver.get('https://keramazavr.ru/')

    @property
    def open_catalog_by_header(self):
        return self.find_element(catalog_button_by_header)

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
    def open_search_by_header(self):
        return self.find_element(search_button_by_header)

    @property
    def open_search_by_header_check(self):
        return self.find_element(search_title)

    @property
    def reverting_logo_by_header(self):
        return self.find_element(reverting_logo_button_by_header)

    @property
    def open_catalog_by_column_menu(self):
        return self.find_element(catalog_button_by_column_menu)

    @property
    def open_delivery_by_column_menu(self):
        return self.find_element(delivery_button_by_column_menu)

    @property
    def open_buy_info_by_column_menu(self):
        return self.find_element(buy_info_button_by_column_menu)

    @property
    def open_articles_by_column_menu(self):
        return self.find_element(articles_button_by_column_menu)

    @property
    def open_contacts_by_column_menu(self):
        return self.find_element(contacts_button_by_column_menu)

    @property
    def open_catalog_by_bottom_menu(self):
        return self.find_element(catalog_button_by_bottom_menu)

    @property
    def open_information_by_bottom_menu(self):
        return self.find_element(information_button_by_bottom_menu)

    @property
    def open_contacts_by_bottom_menu(self):
        return self.find_element(contacts_button_by_bottom_menu)

    @property
    def open_delivery_by_bottom_menu(self):
        return self.find_element(delivery_button_by_bottom_menu)

    @property
    def open_pay_info_by_bottom_menu(self):
        return self.find_element(pay_info_button_by_bottom_menu)

    @property
    def open_articles_by_bottom_menu(self):
        return self.find_element(articles_button_by_bottom_menu)

    @property
    def open_privacy_policy_by_bottom_menu(self):
        return self.find_element(privacy_policy_by_bottom_menu)
