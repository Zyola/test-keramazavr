from pages.home_page import HomePage
from pages.search_page import SearchPage


def test_search_by_header_open(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.open_search_by_header.click()
    search_title = home_page.open_search_by_header_check
    assert '' in search_title.text


def test_search_by_left_menu_open(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.open_catalog_by_header.click()
    search_page = SearchPage(driver)
    search_page.open_search_by_left_menu.click()
    search_title = home_page.open_search_by_header_check
    assert '' in search_title.text


def test_search_by_header_result_name(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.open_search_by_header.click()
    input_field = home_page.open_search_by_header_check
    input_field.send_keys('Wood Abba')
    search_page = SearchPage(driver)
    search_page.search_enter_header_button.click()
    assert 'Wood Abba' in search_page.product_name_title.text


def test_search_by_header_result_article(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.open_search_by_header.click()
    input_field = home_page.open_search_by_header_check
    input_field.send_keys('65216')
    search_page = SearchPage(driver)
    search_page.search_enter_header_button.click()
    assert '65216' in search_page.product_article_title.text


def test_search_by_header_result_collection_name(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.open_search_by_header.click()
    input_field = home_page.open_search_by_header_check
    input_field.send_keys('Abba')
    search_page = SearchPage(driver)
    search_page.search_enter_header_button.click()
    assert 'Abba' in search_page.product_collection_name_title.text


def test_search_by_header_result_not_found(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.open_search_by_header.click()
    input_field = home_page.open_search_by_header_check
    input_field.send_keys('   ')
    search_page = SearchPage(driver)
    search_page.search_enter_header_button.click()
    assert 'По Вашему запросу ничего не найдено!' in search_page.product_not_found_title.text
