from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.home_page import HomePage
from pages.catalog_ceramic_tale_page import CeramicTalePage
from pages.catalog_ceramic_granite_page import CeramicGranitePage
from pages.catalog_mosaic_page import MosaicPage
from pages.catalog_plumbing_and_furniture_page import PlumbingAndFurniturePage


def test_open_ceramic_tale_by_catalog(driver):
    home_page = HomePage(driver)
    home_page.open()
    ActionChains(driver).double_click(home_page.open_catalog_by_header).perform()
    catalog_ceramic_tale_page = CeramicTalePage(driver)
    catalog_ceramic_tale_page.ceramic_tale_button.click()
    assert 'Керамическая плитка' in catalog_ceramic_tale_page.ceramic_tale_title_check.text


def test_open_ceramic_granite_by_catalog(driver):
    home_page = HomePage(driver)
    home_page.open()
    ActionChains(driver).double_click(home_page.open_catalog_by_header).perform()
    catalog_ceramic_granite_page = CeramicGranitePage(driver)
    catalog_ceramic_granite_page.ceramic_granite_button.click()
    assert 'Керамический гранит' in catalog_ceramic_granite_page.ceramic_granite_title_check.text


def test_open_mosaic_by_catalog(driver):
    home_page = HomePage(driver)
    home_page.open()
    ActionChains(driver).double_click(home_page.open_catalog_by_header).perform()
    catalog_mosaic_page = MosaicPage(driver)
    catalog_mosaic_page.mosaic_button.click()
    assert 'Мозаика' in catalog_mosaic_page.mosaic_title_check.text


def test_open_plumbing_and_furniture_by_catalog(driver):
    home_page = HomePage(driver)
    home_page.open()
    ActionChains(driver).double_click(home_page.open_catalog_by_header).perform()
    catalog_plumbing_and_furniture_page = PlumbingAndFurniturePage(driver)
    catalog_plumbing_and_furniture_page.plumbing_and_furniture_button.click()
    assert 'Сантехника и мебель' in catalog_plumbing_and_furniture_page.plumbing_and_furniture_title_check.text
