from pages.home_page import HomePage
from pages.catalog_page import CatalogPage


def test_open_catalog(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.open_catalog()
    catalog_page = CatalogPage(driver)
    assert catalog_page.chapter_catalog.is_displayed()
