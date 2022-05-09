from selenium.webdriver.common.action_chains import ActionChains
from pages.home_page import HomePage
from pages.catalog_ceramic_tale_page import CeramicTalePage
from pages.catalog_ceramic_granite_page import CeramicGranitePage
from pages.catalog_mosaic_page import MosaicPage
from pages.catalog_plumbing_and_furniture_page import PlumbingAndFurniturePage
from pages.catalog_bathroom_tile_page import BathroomTalePage
from pages.catalog_wall_tile_page import WallTalePage
from pages.catalog_floor_tile_page import FloorTalePage
import allure


@allure.feature('Buttons to product categories pages')
@allure.story('Open ceramic tale by catalog')
def test_open_ceramic_tale_by_catalog(driver):
    home_page = HomePage(driver)
    home_page.open()
    ActionChains(driver).double_click(home_page.open_catalog_by_header).perform()
    catalog_ceramic_tale_page = CeramicTalePage(driver)
    catalog_ceramic_tale_page.ceramic_tale_button.click()
    assert 'Керамическая плитка' in catalog_ceramic_tale_page.ceramic_tale_title_check.text


@allure.feature('Buttons to product categories pages')
@allure.story('Open ceramic granite by catalog')
def test_open_ceramic_granite_by_catalog(driver):
    home_page = HomePage(driver)
    home_page.open()
    ActionChains(driver).double_click(home_page.open_catalog_by_header).perform()
    catalog_ceramic_granite_page = CeramicGranitePage(driver)
    catalog_ceramic_granite_page.ceramic_granite_button.click()
    assert 'Керамический гранит' in catalog_ceramic_granite_page.ceramic_granite_title_check.text


@allure.feature('Buttons to product categories pages')
@allure.story('Open mosaic by catalog')
def test_open_mosaic_by_catalog(driver):
    home_page = HomePage(driver)
    home_page.open()
    ActionChains(driver).double_click(home_page.open_catalog_by_header).perform()
    catalog_mosaic_page = MosaicPage(driver)
    catalog_mosaic_page.mosaic_button.click()
    assert 'Мозаика' in catalog_mosaic_page.mosaic_title_check.text


@allure.feature('Buttons to product categories pages')
@allure.story('Open plumbing and furniture by catalog')
def test_open_plumbing_and_furniture_by_catalog(driver):
    home_page = HomePage(driver)
    home_page.open()
    ActionChains(driver).double_click(home_page.open_catalog_by_header).perform()
    catalog_plumbing_and_furniture_page = PlumbingAndFurniturePage(driver)
    catalog_plumbing_and_furniture_page.plumbing_and_furniture_button.click()
    assert 'Сантехника и мебель' in catalog_plumbing_and_furniture_page.plumbing_and_furniture_title_check.text


@allure.feature('Buttons to product categories pages')
@allure.story('Open tale for bathroom by left menu')
def test_open_bathroom_tile_by_left_menu(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.open_catalog_by_header.click()
    catalog_bathroom_tile_page = BathroomTalePage(driver)
    catalog_bathroom_tile_page.bathroom_tale_button.click()
    assert 'Плитка для ванной' in catalog_bathroom_tile_page.bathroom_tale_title_check.text


@allure.feature('Buttons to product categories pages')
@allure.story('Open tale for wall by left menu')
def test_open_wall_tile_by_left_menu(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.open_catalog_by_header.click()
    catalog_wall_tile_page = WallTalePage(driver)
    catalog_wall_tile_page.wall_tale_button.click()
    assert 'Плитка для стен' in catalog_wall_tile_page.wall_tale_title_check.text


@allure.feature('Buttons to product categories pages')
@allure.story('Open tale for floor by left menu')
def test_open_floor_tile_by_left_menu(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.open_catalog_by_header.click()
    catalog_floor_tile_page = FloorTalePage(driver)
    catalog_floor_tile_page.floor_tale_button.click()
    assert 'Плитка для пола' in catalog_floor_tile_page.floor_tale_title_check.text


@allure.feature('Buttons to product categories pages')
@allure.story('Open ceramic tale by left menu')
def test_open_ceramic_tale_by_left_menu(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.open_catalog_by_header.click()
    ceramic_tale_page = CeramicTalePage(driver)
    ceramic_tale_page.ceramic_tale_left_menu_button.click()
    assert 'Керамическая плитка' in ceramic_tale_page.ceramic_tale_title_check.text


@allure.feature('Buttons to product categories pages')
@allure.story('Open ceramic granite by left menu')
def test_open_ceramic_granite_by_left_menu(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.open_catalog_by_header.click()
    ceramic_granite_page_by = CeramicGranitePage(driver)
    ceramic_granite_page_by.ceramic_granite_left_menu_button.click()
    assert 'Керамический гранит' in ceramic_granite_page_by.ceramic_granite_title_check.text


@allure.feature('Buttons to product categories pages')
@allure.story('Open mosaic by left menu')
def test_open_mosaic_by_left_menu(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.open_catalog_by_header.click()
    mosaic_page_by = MosaicPage(driver)
    mosaic_page_by.mosaic_left_menu_button.click()
    assert 'Мозаика' in mosaic_page_by.mosaic_title_check.text


@allure.feature('Buttons to product categories pages')
@allure.story('Open plumbing and furniture by left menu')
def test_open_plumbing_and_furniture_by_left_menu(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.open_catalog_by_header.click()
    plumbing_and_furniture_page_by = PlumbingAndFurniturePage(driver)
    plumbing_and_furniture_page_by.plumbing_and_furniture_left_menu_button.click()
    assert 'Сантехника и мебель' in plumbing_and_furniture_page_by.plumbing_and_furniture_title_check.text


@allure.feature('Buttons to product categories pages')
@allure.story('Open tale for bathroom by icon')
def test_open_bathroom_tile_by_icon(driver):
    home_page = HomePage(driver)
    home_page.open()
    catalog_bathroom_tile_page = BathroomTalePage(driver)
    catalog_bathroom_tile_page.bathroom_tale_by_icon_button.click()
    assert 'Плитка для ванной' in catalog_bathroom_tile_page.bathroom_tale_title_check.text


@allure.feature('Buttons to product categories pages')
@allure.story('Open tale for wall by icon')
def test_open_wall_tile_by_icon(driver):
    home_page = HomePage(driver)
    home_page.open()
    catalog_wall_tile_page = WallTalePage(driver)
    catalog_wall_tile_page.wall_tale_button_by_icon.click()
    assert 'Плитка для стен' in catalog_wall_tile_page.wall_tale_title_check.text


@allure.feature('Buttons to product categories pages')
@allure.story('Open tale for floor by icon')
def test_open_floor_tile_by_icon(driver):
    home_page = HomePage(driver)
    home_page.open()
    catalog_floor_tile_page = FloorTalePage(driver)
    catalog_floor_tile_page.floor_tale_by_icon.click()
    assert 'Плитка для пола' in catalog_floor_tile_page.floor_tale_title_check.text


@allure.feature('Buttons to product categories pages')
@allure.story('Open ceramic tale by icon')
def test_open_ceramic_tale_by_icon(driver):
    home_page = HomePage(driver)
    home_page.open()
    ceramic_tale_page = CeramicTalePage(driver)
    ceramic_tale_page.ceramic_tale_by_icon_button.click()
    assert 'Керамическая плитка' in ceramic_tale_page.ceramic_tale_title_check.text


@allure.feature('Buttons to product categories pages')
@allure.story('Open ceramic granite by icon')
def test_open_ceramic_granite_by_icon(driver):
    home_page = HomePage(driver)
    home_page.open()
    ceramic_granite_page_by = CeramicGranitePage(driver)
    ceramic_granite_page_by.ceramic_granite_by_icon_button.click()
    assert 'Керамический гранит' in ceramic_granite_page_by.ceramic_granite_title_check.text


@allure.feature('Buttons to product categories pages')
@allure.story('Open mosaic by icon')
def test_open_mosaic_by_icon(driver):
    home_page = HomePage(driver)
    home_page.open()
    mosaic_page_by = MosaicPage(driver)
    mosaic_page_by.mosaic_by_icon_button.click()
    assert 'Мозаика' in mosaic_page_by.mosaic_title_check.text


@allure.feature('Buttons to product categories pages')
@allure.story('Open plumbing and furniture by icon')
def test_open_plumbing_and_furniture_by_icon(driver):
    home_page = HomePage(driver)
    home_page.open()
    plumbing_and_furniture_page_by = PlumbingAndFurniturePage(driver)
    plumbing_and_furniture_page_by.plumbing_and_furniture_by_icon_button.click()
    assert 'Сантехника и мебель' in plumbing_and_furniture_page_by.plumbing_and_furniture_title_check.text


@allure.feature('Buttons to product categories pages')
@allure.story('Open tale for bathroom by bottom menu')
def test_open_bathroom_tile_by_bottom_menu(driver):
    home_page = HomePage(driver)
    home_page.open()
    catalog_bathroom_tile_page = BathroomTalePage(driver)
    catalog_bathroom_tile_page.bathroom_tale_by_bottom_menu.click()
    assert 'Плитка для ванной' in catalog_bathroom_tile_page.bathroom_tale_title_check.text


@allure.feature('Buttons to product categories pages')
@allure.story('Open tale for wall by bottom menu')
def test_open_wall_tile_by_bottom_menu(driver):
    home_page = HomePage(driver)
    home_page.open()
    catalog_wall_tile_page = WallTalePage(driver)
    catalog_wall_tile_page.wall_tale_button_by_bottom_menu.click()
    assert 'Плитка для стен' in catalog_wall_tile_page.wall_tale_title_check.text


@allure.feature('Buttons to product categories pages')
@allure.story('Open tale for floor by bottom menu')
def test_open_floor_tile_by_bottom_menu(driver):
    home_page = HomePage(driver)
    home_page.open()
    catalog_floor_tile_page = FloorTalePage(driver)
    catalog_floor_tile_page.floor_tale_by_bottom_menu.click()
    assert 'Плитка для пола' in catalog_floor_tile_page.floor_tale_title_check.text


@allure.feature('Buttons to product categories pages')
@allure.story('Open ceramic tale by bottom menu')
def test_open_ceramic_tale_by_bottom_menu(driver):
    home_page = HomePage(driver)
    home_page.open()
    ceramic_tale_page = CeramicTalePage(driver)
    ceramic_tale_page.ceramic_tale_by_bottom_menu.click()
    assert 'Керамическая плитка' in ceramic_tale_page.ceramic_tale_title_check.text


@allure.feature('Buttons to product categories pages')
@allure.story('Open ceramic granite by bottom menu')
def test_open_ceramic_granite_by_bottom_menu(driver):
    home_page = HomePage(driver)
    home_page.open()
    ceramic_granite_page_by = CeramicGranitePage(driver)
    ceramic_granite_page_by.ceramic_granite_by_bottom_menu.click()
    assert 'Керамический гранит' in ceramic_granite_page_by.ceramic_granite_title_check.text


@allure.feature('Buttons to product categories pages')
@allure.story('Open mosaic by bottom menu')
def test_open_mosaic_by_bottom_menu(driver):
    home_page = HomePage(driver)
    home_page.open()
    mosaic_page_by = MosaicPage(driver)
    mosaic_page_by.mosaic_by_bottom_menu_button.click()
    assert 'Мозаика' in mosaic_page_by.mosaic_title_check.text


@allure.feature('Buttons to product categories pages')
@allure.story('Open plumbing and furniture by bottom menu')
def test_open_plumbing_and_furniture_by_bottom_menu(driver):
    home_page = HomePage(driver)
    home_page.open()
    plumbing_and_furniture_page_by = PlumbingAndFurniturePage(driver)
    plumbing_and_furniture_page_by.plumbing_and_furniture_by_bottom_menu_button.click()
    assert 'Сантехника и мебель' in plumbing_and_furniture_page_by.plumbing_and_furniture_title_check.text
