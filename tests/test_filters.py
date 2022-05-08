from pages.catalog_ceramic_tale_page import CeramicTalePage
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
