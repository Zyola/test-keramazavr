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
manufacturer_filter = (By.XPATH, '//*[@id="__layout"]/div/section/div[2]/div[2]/div[2]/div[3]/div')
manufacturer_filter_by_atlas_concorde = (By.XPATH, '//*[@id="__layout"]/div/section/div[2]/div[2]/div[2]/div[3]/div['
                                                   '2]/div/div/div[1]/label')
product_by_atlas_concorde = (By.XPATH, '//*[@id="__layout"]/div/section/div[3]/div[2]/div/div[1]/div[2]/div/ul/li['
                                       '5]/div')
surface_pattern_filter = (By.XPATH, '//*[@id="__layout"]/div/section/div[2]/div[2]/div[2]/div[4]/div')
surface_pattern_filter_wood = (By.XPATH, '//*[@id="__layout"]/div/section/div[2]/div[2]/div[2]/div[4]/div['
                                         '2]/div/div/div[1]/label')
product_wood_pattern = (By.XPATH, '//*[@id="__layout"]/div/section/div[3]/div[2]/div/div[1]/div[2]/div/ul/li[8]/div')
product_control_object_button_wood = (By.XPATH, '//*[@id="__layout"]/div/section/div[2]/div[4]/div[2]/div[1]/a/div[1]')
colour_filter = (By.XPATH, '//*[@id="__layout"]/div/section/div[2]/div[2]/div[2]/div[5]/div[1]')
colour_filter_white = (By.XPATH, '//*[@id="__layout"]/div/section/div[2]/div[2]/div[2]/div[5]/div[2]/div/div/div['
                                 '1]/label')
product_colour_white = (By.XPATH, '//*[@id="__layout"]/div/section/div[3]/div[2]/div/div[1]/div[2]/div/ul/li[9]/div')
form_filter = (By.XPATH, '//*[@id="__layout"]/div/section/div[2]/div[2]/div[2]/div[6]')
form_filter_wild_boar = (By.XPATH, '//*[@id="__layout"]/div/section/div[2]/div[2]/div[2]/div[6]/div[2]/div/div/div['
                                   '1]/label')
product_filter_wild_boar = (By.XPATH, '//*[@id="__layout"]/div/section/div[3]/div[2]/div/div[1]/div[2]/div/ul/li['
                                      '10]/div')
surface_filter = (By.XPATH, '//*[@id="__layout"]/div/section/div[2]/div[2]/div[2]/div[7]/div[1]')
surface_filter_matt = (By.XPATH, '//*[@id="__layout"]/div/section/div[2]/div[2]/div[2]/div[7]/div[2]/div/div/div['
                                 '1]/label')
product_filter_matt = (By.XPATH, '//*[@id="__layout"]/div/section/div[3]/div[2]/div/div[1]/div[2]/div/ul/li[9]/div')
size_filter = (By.XPATH, '//*[@id="__layout"]/div/section/div[2]/div[2]/div[2]/div[8]/div')
size_filter_100_100 = (By.XPATH, '//*[@id="__layout"]/div/section/div[2]/div[2]/div[2]/div[8]/div[2]/div/div/div['
                                 '1]/label')
product_filter_size = (By.XPATH, '//*[@id="__layout"]/div/section/div[3]/div[2]/div/div[1]/div[2]/div/ul/li[4]/div')
cost_filter = (By.XPATH, '//*[@id="__layout"]/div/section/div[2]/div[2]/div[2]/div[9]/div')
cost_filter_max = (By.XPATH, '//*[@id="__layout"]/div/section/div[2]/div[2]/div[2]/div[9]/div[2]/div/div['
                             '2]/div/div/div[4]/div')
cost_target = (By.XPATH, '//*[@id="__layout"]/div/section/div[2]/div[2]/div[2]/div[9]/div[2]/div/div[2]/div/div/div['
                         '2]/div[1]/div[2]')
product_filter_cost = (By.XPATH, '//*[@id="__layout"]/div/section/div[2]/div[4]/div[1]/div[1]/div[3]/div/span[1]')


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

    @property
    def manufacturer_filter_button(self):
        return self.find_element(manufacturer_filter)

    @property
    def manufacturer_filter_atlas_concorde(self):
        return self.find_element(manufacturer_filter_by_atlas_concorde)

    @property
    def product_by_atlas_concorde(self):
        return self.find_element(product_by_atlas_concorde)

    @property
    def surface_pattern_filter_button(self):
        return self.find_element(surface_pattern_filter)

    @property
    def surface_pattern_filter_wood(self):
        return self.find_element(surface_pattern_filter_wood)

    @property
    def product_wood_pattern_tittle(self):
        return self.find_element(product_wood_pattern)

    @property
    def product_control_object_button_wood(self):
        return self.find_element(product_control_object_button_wood)

    @property
    def colour_filter_button(self):
        return self.find_element(colour_filter)

    @property
    def colour_filter_white_button(self):
        return self.find_element(colour_filter_white)

    @property
    def product_colour_white_title(self):
        return self.find_element(product_colour_white)

    @property
    def form_filter_button(self):
        return self.find_element(form_filter)

    @property
    def form_filter_wild_boar_button(self):
        return self.find_element(form_filter_wild_boar)

    @property
    def product_form_wild_boar_title(self):
        return self.find_element(product_filter_wild_boar)

    @property
    def surface_filter_button(self):
        return self.find_element(surface_filter)

    @property
    def surface_filter_matt_button(self):
        return self.find_element(surface_filter_matt)

    @property
    def product_surface_matt_title(self):
        return self.find_element(product_filter_matt)

    @property
    def size_filter_button(self):
        return self.find_element(size_filter)

    @property
    def size_filter_100_100_button(self):
        return self.find_element(size_filter_100_100)

    @property
    def product_size_100_100_title(self):
        return self.find_element(product_filter_size)

    @property
    def cost_filter_button(self):
        return self.find_element(cost_filter)

    @property
    def cost_filter_max_button(self):
        return self.find_element(cost_filter_max)

    @property
    def cost_target_field(self):
        return self.find_element(cost_target)

    @property
    def product_cost_filter(self):
        return self.find_element(product_filter_cost)
