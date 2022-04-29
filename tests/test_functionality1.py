from selenium.webdriver.common.by import By
from pages.home_page import HomePage
from pages.catalog_page import CatalogPage
from pages.delivery_page import DeliveryPage
from pages.buy_info_page import BuyInfoPage
from pages.pay_info_page import PayInfoPage
from pages.contacts_page import ContactsPage
from pages.cart_page import CartPage
from time import sleep


def test_open_catalog_by_header(driver):
    home_page = HomePage(driver)
    home_page.open()
    sleep(0.5)
    home_page.open_catalog_by_header.click()
    home_page.open_catalog_by_header.click()
    sleep(0.5)
    catalog_page = CatalogPage(driver)
    assert 'Каталог' in catalog_page.check_catalog_title.text


def test_open_delivery_by_header(driver):
    home_page = HomePage(driver)
    home_page.open()
    sleep(0.5)
    home_page.open_delivery_by_header.click()
    sleep(0.5)
    delivery_page = DeliveryPage(driver)
    assert 'Доставка' in delivery_page.check_delivery_title.text


def test_open_buy_info_by_header(driver):
    home_page = HomePage(driver)
    home_page.open()
    sleep(0.5)
    home_page.open_buy_info_by_header.click()
    sleep(0.5)
    buy_info_page = BuyInfoPage(driver)
    assert 'Как сделать покупку' in buy_info_page.check_buy_info_title.text


def test_open_pay_info_by_header(driver):
    home_page = HomePage(driver)
    home_page.open()
    sleep(0.5)
    home_page.open_pay_info_by_header.click()
    sleep(0.5)
    pay_info_page = PayInfoPage(driver)
    assert 'Способы оплаты' in pay_info_page.check_pay_info_title.text


def test_open_contacts_by_header(driver):
    home_page = HomePage(driver)
    home_page.open()
    sleep(0.5)
    home_page.open_contacts_by_header.click()
    sleep(0.5)
    contacts_page = ContactsPage(driver)
    assert 'Контактная информация' in contacts_page.check_contacts_title.text


def test_open_cart_by_header(driver):
    home_page = HomePage(driver)
    home_page.open()
    sleep(0.5)
    home_page.open_cart_by_header.click()
    sleep(0.5)
    cart_page = CartPage(driver)
    assert 'Оформление заказа' in cart_page.check_cart_title.text


def test_search_by_header(driver):
    home_page = HomePage(driver)
    home_page.open()
    sleep(0.5)
    home_page.open_search_header.click()
    sleep(0.5)
    search_title = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[1]/header/div[4]/div/input')
    assert '' in search_title.text
