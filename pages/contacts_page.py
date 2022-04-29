from pages.base_page import BasePage
from selenium.webdriver.common.by import By


contacts_title = (By.CLASS_NAME, 'left-title')


class ContactsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        self.driver.get('https://keramazavr.ru/contacts')

    @property
    def check_contacts_title(self):
        return self.find_element(contacts_title)
