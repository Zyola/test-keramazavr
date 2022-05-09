from pages.home_page import HomePage
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import allure


@allure.feature('Dynamic buttons')
@allure.story('Scroll up button')
def test_scroll_up_button(driver):
    home_page = HomePage(driver)
    home_page.open()
    bottom_target = home_page.open_catalog_by_bottom_menu
    ActionChains(driver).move_to_element(bottom_target).perform()
    home_page.open_move_up.click()
    sleep(2)
    assert home_page.check_main_logo.is_displayed()


@allure.feature('Dynamic buttons')
@allure.story('Popular arrow next')
def test_popular_arrow_next(driver):
    home_page = HomePage(driver)
    home_page.open()
    next_arrow_target = home_page.popular_target_field
    ActionChains(driver).move_to_element(next_arrow_target).perform()
    home_page.popular_first_page_scroll_button.click()
    home_page.popular_arrow_next.click()
    second_title = home_page.popular_second_page_product_title
    assert second_title.is_displayed()


@allure.feature('Dynamic buttons')
@allure.story('Popular arrow prev')
def test_popular_arrow_prev(driver):
    home_page = HomePage(driver)
    home_page.open()
    next_arrow_target = home_page.popular_target_field
    ActionChains(driver).move_to_element(next_arrow_target).perform()
    home_page.popular_second_page_scroll_button.click()
    home_page.popular_second_page_scroll_button.click()
    home_page.popular_arrow_prev.click()
    sleep(1)
    first_title = home_page.popular_first_page_product_title
    assert first_title.is_displayed()


@allure.feature('Dynamic buttons')
@allure.story('Popular second page scroll button')
def test_second_page_scroll_button(driver):
    home_page = HomePage(driver)
    home_page.open()
    next_arrow_target = home_page.popular_target_field
    ActionChains(driver).move_to_element(next_arrow_target).perform()
    home_page.popular_first_page_scroll_button.click()
    home_page.popular_second_page_scroll_button.click()
    sleep(1)
    second_title = home_page.popular_second_page_product_title
    assert second_title.is_displayed()


@allure.feature('Dynamic buttons')
@allure.story('Popular first page scroll button')
def test_first_page_scroll_button(driver):
    home_page = HomePage(driver)
    home_page.open()
    next_arrow_target = home_page.popular_target_field
    ActionChains(driver).move_to_element(next_arrow_target).perform()
    sleep(1)
    home_page.popular_second_page_scroll_button.click()
    sleep(1)
    home_page.popular_first_page_scroll_button.click()
    sleep(1)
    first_title = home_page.popular_first_page_product_title
    assert first_title.is_displayed()


@allure.feature('Dynamic buttons')
@allure.story('Buyers choice arrow next')
def test_buyers_choice_arrow_next(driver):
    home_page = HomePage(driver)
    home_page.open()
    next_arrow_target = home_page.buyers_choice_target_field
    ActionChains(driver).move_to_element(next_arrow_target).perform()
    home_page.buyers_choice_first_page_scroll_button.click()
    home_page.buyers_choice_arrow_next.click()
    second_title = home_page.buyers_choice_second_page_product_title
    assert second_title.is_displayed()


@allure.feature('Dynamic buttons')
@allure.story('Buyers choice arrow prev')
def test_buyers_choice_arrow_prev(driver):
    home_page = HomePage(driver)
    home_page.open()
    next_arrow_target = home_page.buyers_choice_target_field
    ActionChains(driver).move_to_element(next_arrow_target).perform()
    home_page.buyers_choice_second_page_scroll_button.click()
    sleep(1)
    home_page.buyers_choice_arrow_prev.click()
    sleep(1)
    first_title = home_page.buyers_choice_first_page_product_title
    assert first_title.is_displayed()


@allure.feature('Dynamic buttons')
@allure.story('Buyers choice second page scroll button')
def test_buyers_choice_second_page_scroll_button(driver):
    home_page = HomePage(driver)
    home_page.open()
    next_arrow_target = home_page.buyers_choice_target_field
    ActionChains(driver).move_to_element(next_arrow_target).perform()
    sleep(1)
    home_page.buyers_choice_first_page_scroll_button.click()
    home_page.buyers_choice_second_page_scroll_button.click()
    second_title = home_page.buyers_choice_second_page_product_title
    assert second_title.is_displayed()


@allure.feature('Dynamic buttons')
@allure.story('Buyers choice first page scroll button')
def test_buyers_choice_first_page_scroll_button(driver):
    home_page = HomePage(driver)
    home_page.open()
    next_arrow_target = home_page.buyers_choice_target_field
    ActionChains(driver).move_to_element(next_arrow_target).perform()
    home_page.buyers_choice_second_page_scroll_button.click()
    sleep(1)
    home_page.buyers_choice_first_page_scroll_button.click()
    sleep(1)
    first_title = home_page.buyers_choice_first_page_product_title
    assert first_title.is_displayed()
