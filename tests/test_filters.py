from pages.catalog_ceramic_tale_page import CeramicTalePage
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


def test_appointment_filter(driver):
    catalog_ceramic_page = CeramicTalePage(driver)
    catalog_ceramic_page.open()
    catalog_ceramic_page.show_filters_button.click()
    catalog_ceramic_page.appointment_filter_button.click()
    catalog_ceramic_page.appointment_filter_for_walls_button.click()
    sleep(3)
    catalog_ceramic_page.products_filtered_button.click()
    sleep(4)
    catalog_ceramic_page.product_control_object_button.click()
    sleep(1)
    assert 'Для стен' in catalog_ceramic_page.product_for_walls.text


def test_application_filter(driver):
    catalog_ceramic_page = CeramicTalePage(driver)
    catalog_ceramic_page.open()
    catalog_ceramic_page.show_filters_button.click()
    catalog_ceramic_page.application_filter_button.click()
    catalog_ceramic_page.application_filter_for_kitchen_button.click()
    sleep(3)
    catalog_ceramic_page.products_filtered_button.click()
    sleep(4)
    catalog_ceramic_page.product_control_object_button.click()
    sleep(1)
    assert 'Для кухни' in catalog_ceramic_page.product_for_kitchen.text


def test_manufacturer_filter(driver):
    catalog_ceramic_page = CeramicTalePage(driver)
    catalog_ceramic_page.open()
    catalog_ceramic_page.show_filters_button.click()
    catalog_ceramic_page.manufacturer_filter_button.click()
    catalog_ceramic_page.manufacturer_filter_atlas_concorde.click()
    sleep(3)
    catalog_ceramic_page.products_filtered_button.click()
    sleep(5)
    catalog_ceramic_page.product_control_object_button.click()
    sleep(2)
    assert 'Atlas Concorde' in catalog_ceramic_page.product_by_atlas_concorde.text


def test_surface_pattern_filter(driver):
    catalog_ceramic_page = CeramicTalePage(driver)
    catalog_ceramic_page.open()
    catalog_ceramic_page.show_filters_button.click()
    catalog_ceramic_page.surface_pattern_filter_button.click()
    catalog_ceramic_page.surface_pattern_filter_wood.click()
    catalog_ceramic_page.surface_pattern_filter_button.click()
    sleep(3)
    catalog_ceramic_page.products_filtered_button.click()
    sleep(5)
    catalog_ceramic_page.product_control_object_button_wood.click()
    sleep(2)
    assert 'Дерево' in catalog_ceramic_page.product_wood_pattern_tittle.text


def test_colour_filter(driver):
    catalog_ceramic_page = CeramicTalePage(driver)
    catalog_ceramic_page.open()
    catalog_ceramic_page.show_filters_button.click()
    catalog_ceramic_page.colour_filter_button.click()
    catalog_ceramic_page.colour_filter_white_button.click()
    sleep(3)
    catalog_ceramic_page.products_filtered_button.click()
    sleep(5)
    catalog_ceramic_page.product_control_object_button.click()
    sleep(2)
    assert 'Белый' in catalog_ceramic_page.product_colour_white_title.text


def test_form_filter(driver):
    catalog_ceramic_page = CeramicTalePage(driver)
    catalog_ceramic_page.open()
    catalog_ceramic_page.show_filters_button.click()
    catalog_ceramic_page.form_filter_button.click()
    catalog_ceramic_page.form_filter_wild_boar_button.click()
    sleep(3)
    catalog_ceramic_page.products_filtered_button.click()
    sleep(5)
    catalog_ceramic_page.product_control_object_button.click()
    sleep(2)
    assert 'Кабанчик' in catalog_ceramic_page.product_form_wild_boar_title.text


def test_surface_filter(driver):
    catalog_ceramic_page = CeramicTalePage(driver)
    catalog_ceramic_page.open()
    catalog_ceramic_page.show_filters_button.click()
    catalog_ceramic_page.surface_filter_button.click()
    catalog_ceramic_page.surface_filter_matt_button.click()
    catalog_ceramic_page.surface_filter_button.click()
    sleep(3)
    catalog_ceramic_page.products_filtered_button.click()
    sleep(5)
    catalog_ceramic_page.product_control_object_button.click()
    sleep(2)
    assert 'Матовая' in catalog_ceramic_page.product_surface_matt_title.text


def test_size_filter(driver):
    catalog_ceramic_page = CeramicTalePage(driver)
    catalog_ceramic_page.open()
    catalog_ceramic_page.show_filters_button.click()
    catalog_ceramic_page.size_filter_button.click()
    catalog_ceramic_page.size_filter_100_100_button.click()
    catalog_ceramic_page.size_filter_button.click()
    sleep(3)
    catalog_ceramic_page.products_filtered_button.click()
    sleep(5)
    catalog_ceramic_page.product_control_object_button.click()
    sleep(2)
    assert '100x100' in catalog_ceramic_page.product_size_100_100_title.text


def test_cost_filter(driver):
    catalog_ceramic_page = CeramicTalePage(driver)
    catalog_ceramic_page.open()
    catalog_ceramic_page.show_filters_button.click()
    catalog_ceramic_page.cost_filter_button.click()
    drop = catalog_ceramic_page.cost_filter_max_button
    drop_here = catalog_ceramic_page.cost_target_field
    ActionChains(driver).drag_and_drop(drop, drop_here).perform()
    catalog_ceramic_page.cost_filter_button.click()
    catalog_ceramic_page.sorting_button.click()
    sleep(1)
    catalog_ceramic_page.sorting_the_most_expensive_button.click()
    sleep(3)
    catalog_ceramic_page.products_filtered_button.click()
    sleep(3)
    max_cost_of_product = catalog_ceramic_page.product_cost_filter.text
    cost = [int(cost) for cost in str.split(max_cost_of_product) if cost.isdigit()]
    max_cost = [int(max_cost) for max_cost in str.split('8000') if max_cost.isdigit()]
    assert cost < max_cost
