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

move_up_button = (By.CLASS_NAME, 'toTop')
main_logo = (By.XPATH, '//*[@id="__layout"]/div/div[1]/header/div[2]/a/div[1]/img')

popular_arrow_prev = (By.XPATH, '//*[@id="__layout"]/div/div[2]/section[2]/div/div/div[1]/i')
popular_arrow_next = (By.XPATH, '//*[@id="__layout"]/div/div[2]/section[2]/div/div/div[3]/i')
popular_first_page_scroll_button = (By.XPATH, '//*[@id="__layout"]/div/div[2]/section[2]/div/div/ul/li[1]')
popular_second_page_scroll_button = (By.XPATH, '//*[@id="__layout"]/div/div[2]/section[2]/div/div/ul/li[2]')
popular_first_page_product = (By.XPATH, '//*[@id="__layout"]/div/div[2]/section[2]/div/div/div[2]/div/div[4]/div/a')
popular_second_page_product = (By.XPATH, '//*[@id="__layout"]/div/div[2]/section[2]/div/div/div[2]/div/div[6]/div/a')
popular_target = (By.XPATH, '//*[@id="__layout"]/div/div[2]/section[2]')

buyers_choice_arrow_prev = (By.XPATH, '//*[@id="__layout"]/div/div[2]/section[4]/div/div/div[1]/i')
buyers_choice_arrow_next = (By.XPATH, '//*[@id="__layout"]/div/div[2]/section[4]/div/div/div[3]/i')
buyers_choice_first_page_scroll_button = (By.XPATH, '//*[@id="__layout"]/div/div[2]/section[4]/div/div/ul/li[1]')
buyers_choice_second_page_scroll_button = (By.XPATH, '//*[@id="__layout"]/div/div[2]/section[4]/div/div/ul/li[2]')
buyers_choice_first_page_product = (By.XPATH, '//*[@id="__layout"]/div/div[2]/section[4]/div/div/div[2]/div/div['
                                              '5]/div/div/div[1]/a/div[1]')
buyers_choice_second_page_product = (By.XPATH, '//*[@id="__layout"]/div/div[2]/section[4]/div/div/div[2]/div/div['
                                               '7]/div/div/div[1]/a/div[1]')
buyers_choice_target = (By.XPATH, '//*[@id="__layout"]/div/div[2]/section[4]/div[1]/div/div[3]')


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

    @property
    def open_move_up(self):
        return self.find_element(move_up_button)

    @property
    def check_main_logo(self):
        return self.find_element(main_logo)

    @property
    def popular_arrow_prev(self):
        return self.find_element(popular_arrow_prev)

    @property
    def popular_arrow_next(self):
        return self.find_element(popular_arrow_next)

    @property
    def popular_first_page_scroll_button(self):
        return self.find_element(popular_first_page_scroll_button)

    @property
    def popular_second_page_scroll_button(self):
        return self.find_element(popular_second_page_scroll_button)

    @property
    def popular_first_page_product_title(self):
        return self.find_element(popular_first_page_product)

    @property
    def popular_second_page_product_title(self):
        return self.find_element(popular_second_page_product)

    @property
    def popular_target_field(self):
        return self.find_element(popular_target)

    @property
    def buyers_choice_arrow_prev(self):
        return self.find_element(buyers_choice_arrow_prev)

    @property
    def buyers_choice_arrow_next(self):
        return self.find_element(buyers_choice_arrow_next)

    @property
    def buyers_choice_first_page_scroll_button(self):
        return self.find_element(buyers_choice_first_page_scroll_button)

    @property
    def buyers_choice_second_page_scroll_button(self):
        return self.find_element(buyers_choice_second_page_scroll_button)

    @property
    def buyers_choice_first_page_product_title(self):
        return self.find_element(buyers_choice_first_page_product)

    @property
    def buyers_choice_second_page_product_title(self):
        return self.find_element(buyers_choice_second_page_product)

    @property
    def buyers_choice_target_field(self):
        return self.find_element(buyers_choice_target)
