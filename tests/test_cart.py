from selenium.webdriver.common.action_chains import ActionChains
from pages.catalog_ceramic_tale_page import CeramicTalePage
from pages.cart_page import CartPage
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


def test_add_product_to_cart(driver):
    catalog_ceramic_page = CeramicTalePage(driver)
    catalog_ceramic_page.open()
    catalog_ceramic_page.first_product_field.click()
    driver.switch_to.window(driver.window_handles[1])
    add_button = catalog_ceramic_page.add_first_product_field
    ActionChains(driver).move_to_element(add_button).perform()
    add_button.click()
    cart_page = CartPage(driver)
    cart_page.open()
    sleep(1)
    assert catalog_ceramic_page.check_first_product.is_displayed()


def test_plus_product_cost(driver):
    catalog_ceramic_page = CeramicTalePage(driver)
    catalog_ceramic_page.open()
    catalog_ceramic_page.first_product_field.click()
    driver.switch_to.window(driver.window_handles[1])
    add_button = catalog_ceramic_page.add_first_product_field
    ActionChains(driver).move_to_element(add_button).perform()
    add_button.click()
    cart_page = CartPage(driver)
    cart_page.open()
    sleep(1)
    catalog_ceramic_page.plus_first_product_button.click()
    sleep(2)
    cost = catalog_ceramic_page.cost_first_product_value
    assert '5 742 ₽' in cost.text


def test_minus_product_cost(driver):
    catalog_ceramic_page = CeramicTalePage(driver)
    catalog_ceramic_page.open()
    catalog_ceramic_page.first_product_field.click()
    driver.switch_to.window(driver.window_handles[1])
    add_button = catalog_ceramic_page.add_first_product_field
    ActionChains(driver).move_to_element(add_button).perform()
    add_button.click()
    cart_page = CartPage(driver)
    cart_page.open()
    sleep(1)
    catalog_ceramic_page.plus_first_product_button.click()
    sleep(1)
    catalog_ceramic_page.minus_first_product_button.click()
    sleep(2)
    cost = catalog_ceramic_page.cost_first_product_value
    assert '2 871 ₽' in cost.text


def test_adequate_amount_of_product(driver):
    catalog_ceramic_page = CeramicTalePage(driver)
    catalog_ceramic_page.open()
    catalog_ceramic_page.first_product_field.click()
    driver.switch_to.window(driver.window_handles[1])
    add_button = catalog_ceramic_page.add_first_product_field
    ActionChains(driver).move_to_element(add_button).perform()
    add_button.click()
    cart_page = CartPage(driver)
    cart_page.open()
    sleep(1)
    assert not EC.element_to_be_clickable(catalog_ceramic_page.minus_first_product_button)


def test_delete_product_from_cart(driver):
    catalog_ceramic_page = CeramicTalePage(driver)
    catalog_ceramic_page.open()
    catalog_ceramic_page.first_product_field.click()
    driver.switch_to.window(driver.window_handles[1])
    add_button = catalog_ceramic_page.add_first_product_field
    ActionChains(driver).move_to_element(add_button).perform()
    add_button.click()
    cart_page = CartPage(driver)
    cart_page.open()
    sleep(1)
    catalog_ceramic_page.delete_first_product_button.click()
    assert catalog_ceramic_page.check_first_product.is_enabled()
