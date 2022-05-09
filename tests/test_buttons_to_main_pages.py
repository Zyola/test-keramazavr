from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.home_page import HomePage
from pages.catalog_page import CatalogPage
from pages.delivery_page import DeliveryPage
from pages.buy_info_page import BuyInfoPage
from pages.pay_info_page import PayInfoPage
from pages.contacts_page import ContactsPage
from pages.cart_page import CartPage
import allure


 """
 Запуск тестов:
 pytest --alluredir=/home/zyola/test-keramazavr/tests/allure-reports
 """


@allure.feature('Buttons to main pages')
@allure.story('Open catalog by header')
def test_open_catalog_by_header(driver):
    home_page = HomePage(driver)
    home_page.open()
    ActionChains(driver).double_click(home_page.open_catalog_by_header).perform()
    catalog_page = CatalogPage(driver)
    assert 'Каталог' in catalog_page.check_catalog_title.text


@allure.feature('Buttons to main pages')
@allure.story('Open delivery by header')
def test_open_delivery_by_header(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.open_delivery_by_header.click()
    delivery_page = DeliveryPage(driver)
    assert 'Доставка' in delivery_page.check_delivery_title.text


@allure.feature('Buttons to main pages')
@allure.story('Open buy info by header')
def test_open_buy_info_by_header(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.open_buy_info_by_header.click()
    buy_info_page = BuyInfoPage(driver)
    assert 'Как сделать покупку' in buy_info_page.check_buy_info_title.text


@allure.feature('Buttons to main pages')
@allure.story('Open pay info by header')
def test_open_pay_info_by_header(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.open_pay_info_by_header.click()
    pay_info_page = PayInfoPage(driver)
    assert 'Способы оплаты' in pay_info_page.check_pay_info_title.text


@allure.feature('Buttons to main pages')
@allure.story('Open catalog by header')
def test_open_contacts_by_header(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.open_contacts_by_header.click()
    contacts_page = ContactsPage(driver)
    assert 'Контактная информация' in contacts_page.check_contacts_title.text


@allure.feature('Buttons to main pages')
@allure.story('Open cart by header')
def test_open_cart_by_header(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.open_cart_by_header.click()
    cart_page = CartPage(driver)
    assert 'Оформление заказа' in cart_page.check_cart_title.text


@allure.feature('Buttons to main pages')
@allure.story('Use reverting logo by header')
def test_reverting_logo_by_header(driver):
    home_page = HomePage(driver)
    home_page.open()
    ActionChains(driver).double_click(home_page.open_catalog_by_header).perform()
    home_page.reverting_logo_by_header.click()
    unico_image_home_page = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/section['
                                                          '1]/div/div/div/div/div/div/a/div/picture/img')
    assert unico_image_home_page.is_displayed()


@allure.feature('Buttons to main pages')
@allure.story('Open catalog by column menu')
def test_open_catalog_by_column_menu(driver):  # БАГ. Кнопка "Каталог" в столбцовом меню не открывает страницу каталога.
    home_page = HomePage(driver)
    home_page.open()
    home_page.open_catalog_by_header.click()
    home_page.open_catalog_by_column_menu.click()
    catalog_page = CatalogPage(driver)
    assert 'Каталог' in catalog_page.check_catalog_title.text


@allure.feature('Buttons to main pages')
@allure.story('Open delivery by column menu')
def test_open_delivery_by_column_menu(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.open_catalog_by_header.click()
    home_page.open_delivery_by_column_menu.click()
    delivery_page = DeliveryPage(driver)
    assert 'Доставка' in delivery_page.check_delivery_title.text


@allure.feature('Buttons to main pages')
@allure.story('Open buy info by column menu')
def test_open_buy_info_by_column_menu(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.open_catalog_by_header.click()
    home_page.open_buy_info_by_column_menu.click()
    buy_info_page = BuyInfoPage(driver)
    assert 'Как сделать покупку' in buy_info_page.check_buy_info_title.text


@allure.feature('Buttons to main pages')
@allure.story('Open articles by column menu')
def test_open_articles_by_column_menu(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.open_catalog_by_header.click()
    home_page.open_articles_by_column_menu.click()
    articles_title = driver.find_element(By.CLASS_NAME, 'left-title')
    assert 'Полезные статьи' in articles_title.text


@allure.feature('Buttons to main pages')
@allure.story('Open contacts by column menu')
def test_open_contacts_by_column_menu(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.open_catalog_by_header.click()
    home_page.open_contacts_by_column_menu.click()
    contacts_page = ContactsPage(driver)
    assert 'Контактная информация' in contacts_page.check_contacts_title.text


@allure.feature('Buttons to main pages')
@allure.story('Open catalog by bottom menu')
def test_open_catalog_by_bottom_menu(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.open_catalog_by_bottom_menu.click()
    catalog_page = CatalogPage(driver)
    assert 'Каталог' in catalog_page.check_catalog_title.text


@allure.feature('Buttons to main pages')
@allure.story('Open information by bottom menu')
def test_open_information_by_bottom_menu(driver):  # БАГ. Страницы "Информация" не существует. А эта кнопка
    # направляет на страницу "Доставка".
    home_page = HomePage(driver)
    home_page.open()
    home_page.open_information_by_bottom_menu.click()
    unico_image_home_page = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/section['
                                                          '1]/div/div/div/div/div/div/a/div/picture/img')
    assert unico_image_home_page.is_displayed()


@allure.feature('Buttons to main pages')
@allure.story('Open contacts by bottom menu')
def test_open_contacts_by_bottom_menu(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.open_contacts_by_bottom_menu.click()
    contacts_page = ContactsPage(driver)
    assert 'Контактная информация' in contacts_page.check_contacts_title.text


@allure.feature('Buttons to main pages')
@allure.story('Open delivery by bottom menu')
def test_open_delivery_by_bottom_menu(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.open_delivery_by_bottom_menu.click()
    delivery_page = DeliveryPage(driver)
    assert 'Доставка' in delivery_page.check_delivery_title.text


@allure.feature('Buttons to main pages')
@allure.story('Open pay info by bottom menu')
def test_open_pay_info_by_bottom_menu(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.open_pay_info_by_bottom_menu.click()
    pay_info_page = PayInfoPage(driver)
    assert 'Способы оплаты' in pay_info_page.check_pay_info_title.text


@allure.feature('Buttons to main pages')
@allure.story('Open articles by bottom menu')
def test_open_articles_by_bottom_menu(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.open_articles_by_bottom_menu.click()
    articles_title = driver.find_element(By.CLASS_NAME, 'left-title')
    assert 'Полезные статьи' in articles_title.text


@allure.feature('Buttons to main pages')
@allure.story('Open privacy policy by bottom menu')
def test_open_privacy_policy_by_bottom_menu(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.open_privacy_policy_by_bottom_menu.click()
    privacy_policy_title = driver.find_element(By.CLASS_NAME, 'left-title')
    assert 'Политика конфиденциальности' in privacy_policy_title.text
