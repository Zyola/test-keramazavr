from pages.catalog_page import CatalogPage
from selenium.webdriver.common.by import By


ceramic_tale = (By.XPATH, '//*[@id="__layout"]/div/section/div/div[2]/div[1]')
ceramic_tale_left_menu = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div/div[2]/ul/li[4]/a')
ceramic_tale_by_icon_button = (By.XPATH, '//*[@id="__layout"]/div/div[2]/div[1]/div/a[4]')
ceramic_tale_by_bottom_menu = (By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/div[1]/div[2]/ul/li[5]')
ceramic_tale_title = (By.XPATH, '//*[@id="__layout"]/div/section/div[2]/div[1]/ul/li[3]')
first_product = (By.XPATH, '//*[@id="__layout"]/div/section/div[2]/div[3]/div[1]')
add_first_product = (By.XPATH, '//*[@id="__layout"]/div/section/div[3]/div[4]/div[1]/div[2]/div[2]')
first_product_page = (By.XPATH, '//*[@id="__layout"]/div/section/div/span/div/div[1]/div/div[1]/a')
first_product_title = (By.XPATH, '//*[@id="__layout"]/div/section/div/span/div/div[1]/div/div[2]/a/div/div')
plus_first_product = (By.XPATH, '//*[@id="__layout"]/div/section/div/span/div/div[1]/div/div[2]/div[2]/div['
                                '3]/div/div/div[2]/span[2]/i')
minus_first_product = (By.XPATH, '//*[@id="__layout"]/div/section/div/span/div/div[1]/div/div[2]/div[2]/div['
                                 '3]/div/div/div[2]/span[1]/i')
cost_first_product = (By.XPATH, '//*[@id="__layout"]/div/section/div/span/div/div[2]/div[2]')
amount_of_product = (By.XPATH, '//*[@id="__layout"]/div/section/div/span/div/div[1]/div/div[2]/div[2]/div['
                               '3]/div/div/div[2]/input')
delete_first_product = (By.XPATH, '//*[@id="__layout"]/div/section/div/span/div/div[1]/div/div[1]/div')
add_second_product = (By.XPATH, '//*[@id="__layout"]/div/section/div[3]/div[4]/div[2]/div[2]/div[2]')
second_product = (By.XPATH, '//*[@id="__layout"]/div/section/div[2]/div[3]/div[2]')
add_to_cart = (By.XPATH, '//*[@id="__layout"]/div/section/div[2]/div[3]/div/div[4]/div')

sorting = (By.XPATH, '//*[@id="__layout"]/div/section/div[2]/div[2]/div[1]/div[2]')
sorting_cheapest = (By.XPATH, '//*[@id="__layout"]/div/section/div[2]/div[2]/div[1]/div[2]/div/div[2]/div[2]')
sorting_the_most_expensive = (By.XPATH, '//*[@id="__layout"]/div/section/div[2]/div[2]/div[1]/div[2]/div/div[2]/div[3]')
cost_first_product_after_sorting = (By.XPATH, '//*[@id="__layout"]/div/section/div[2]/div[3]/div[1]/a/div[3]/span')
cost_second_product_after_sorting = (By.XPATH, '//*[@id="__layout"]/div/section/div[2]/div[3]/div[3]/a/div[3]')

show_filters = (By.XPATH, '//*[@id="__layout"]/div/section/div[2]/div[2]/div[1]/div[1]')
appointment_filter = (By.XPATH, '//*[@id="__layout"]/div/section/div[2]/div[2]/div[2]/div[1]/div')
appointment_filter_for_walls = (By.XPATH, '//*[@id="__layout"]/div/section/div[2]/div[2]/div[2]/div[1]/div['
                                          '2]/div/div/div[1]/label')
product_for_walls_title = (By.XPATH, '//*[@id="__layout"]/div/section/div[3]/div[2]/div/div[1]/div[2]/div/ul/li[6]/div')
products_filtered = (By.XPATH, '//*[@id="__layout"]/div/section/div[2]/div[3]/span[3]')
product_control_object = (By.XPATH, '//*[@id="__layout"]/div/section/div[2]/div[4]/div[1]/div[1]/a')
application_filter = (By.XPATH, '//*[@id="__layout"]/div/section/div[2]/div[2]/div[2]/div[2]/div')
application_filter_for_kitchen = (By.XPATH, '//*[@id="__layout"]/div/section/div[2]/div[2]/div[2]/div[2]/div['
                                            '2]/div/div/div[1]/label')
product_for_kitchen_title = (By.XPATH, '//*[@id="__layout"]/div/section/div[3]/div[2]/div/div[1]/div[2]/div/ul/li['
                                       '7]/div')


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

    @property
    def first_product_field(self):
        return self.find_element(first_product)

    @property
    def second_product_field(self):
        return self.find_element(second_product)

    @property
    def add_first_product_field(self):
        return self.find_element(add_first_product)

    @property
    def add_second_product_field(self):
        return self.find_element(add_second_product)

    @property
    def check_first_product(self):
        return self.find_element(first_product_title)

    @property
    def add_to_cart_button(self):
        return self.find_element(add_to_cart)

    @property
    def first_product_page_button(self):
        return self.find_element(first_product_page)

    @property
    def plus_first_product_button(self):
        return self.find_element(plus_first_product)

    @property
    def minus_first_product_button(self):
        return self.find_element(minus_first_product)

    @property
    def cost_first_product_value(self):
        return self.find_element(cost_first_product)

    @property
    def delete_first_product_button(self):
        return self.find_element(delete_first_product)

    @property
    def amount_of_product_value(self):
        return self.find_element(amount_of_product)

    @property
    def sorting_button(self):
        return self.find_element(sorting)

    @property
    def sorting_cheapest_button(self):
        return self.find_element(sorting_cheapest)

    @property
    def sorting_the_most_expensive_button(self):
        return self.find_element(sorting_the_most_expensive)

    @property
    def cost_first_product_after_sorting_value(self):
        return self.find_element(cost_first_product_after_sorting)

    @property
    def cost_second_product_after_sorting_value(self):
        return self.find_element(cost_second_product_after_sorting)

    @property
    def show_filters_button(self):
        return self.find_element(show_filters)

    @property
    def appointment_filter_button(self):
        return self.find_element(appointment_filter)

    @property
    def appointment_filter_for_walls_button(self):
        return self.find_element(appointment_filter_for_walls)

    @property
    def products_filtered_button(self):
        return self.find_element(products_filtered)

    @property
    def product_control_object_button(self):
        return self.find_element(product_control_object)

    @property
    def product_for_walls(self):
        return self.find_element(product_for_walls_title)

    @property
    def application_filter_button(self):
        return self.find_element(application_filter)

    @property
    def application_filter_for_kitchen_button(self):
        return self.find_element(application_filter_for_kitchen)

    @property
    def product_for_kitchen(self):
        return self.find_element(product_for_kitchen_title)
