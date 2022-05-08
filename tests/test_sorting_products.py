from pages.catalog_ceramic_tale_page import CeramicTalePage
from time import sleep


def test_sorting_products_by_cheapest(driver):
    catalog_ceramic_page = CeramicTalePage(driver)
    catalog_ceramic_page.open()
    catalog_ceramic_page.sorting_button.click()
    sleep(1)
    catalog_ceramic_page.sorting_cheapest_button.click()
    sleep(5)
    cost_first_product = catalog_ceramic_page.cost_first_product_after_sorting_value.text
    f = [int(f) for f in str.split(cost_first_product) if f.isdigit()]
    cost_second_product = catalog_ceramic_page.cost_second_product_after_sorting_value.text
    s = [int(s) for s in str.split(cost_second_product) if s.isdigit()]
    assert f < s


def test_sorting_products_by_most_expensive(driver):
    catalog_ceramic_page = CeramicTalePage(driver)
    catalog_ceramic_page.open()
    catalog_ceramic_page.sorting_button.click()
    sleep(1)
    catalog_ceramic_page.sorting_the_most_expensive_button.click()
    sleep(4)
    cost_first_product = catalog_ceramic_page.cost_first_product_after_sorting_value.text
    f = [int(f) for f in str.split(cost_first_product) if f.isdigit()]
    cost_second_product = catalog_ceramic_page.cost_second_product_after_sorting_value.text
    s = [int(s) for s in str.split(cost_second_product) if s.isdigit()]
    assert f > s
