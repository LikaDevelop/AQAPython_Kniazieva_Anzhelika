from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class PageTextBox:
    page_url = 'https://demoqa.com/text-box'

    def __init__(self, driver):
        self.__driver: WebDriver = driver
        self.__submit_btn_loc: tuple = (By.XPATH, './/button[@id = "submit"]')
        self.__full_name_field_loc: tuple = (By.CSS_SELECTOR, 'input#userName')
        self.__email_field_loc: tuple = (By.CSS_SELECTOR, 'input#userEmail')
        self.__curr_addr_text_area_loc: tuple = (By.CSS_SELECTOR, 'textarea#currentAddress')
        self.__perm_addr_text_area_loc: tuple = (By.CSS_SELECTOR, 'textarea#permanentAddress')
        self.__output_fullname_loc: tuple = (By.CSS_SELECTOR, 'p#name')
        self.__output_email_loc: tuple = (By.CSS_SELECTOR, 'p#email')
        self.__output_curr_addr_loc: tuple = (By.CSS_SELECTOR, 'p#currentAddress')
        self.__output_perm_addr_loc: tuple = (By.CSS_SELECTOR, 'p#permanentAddress')

    def open(self) -> 'PageTextBox':
        self.__driver.get(self.page_url)
        element = self.__driver.find_element(By.CSS_SELECTOR, 'div.main-header')
        assert element.is_displayed()
        return self

    def fill_full_name(self, full_name: str) -> 'PageTextBox':
        field = self.__driver.find_element(*self.__full_name_field_loc)
        field.send_keys(full_name)
        return self

    def set_full_name(self, full_name: str) -> 'PageTextBox':
        field = self.__driver.find_element(*self.__full_name_field_loc)
        field.clear()
        field.send_keys(full_name)
        return self

    def set_email_name(self, email: str) -> 'PageTextBox':
        field = self.__driver.find_element(*self.__email_field_loc)
        field.clear()
        field.send_keys(email)
        return self

    def set_perm_addr(self, perm_addr: str) -> 'PageTextBox':
        field = self.__driver.find_element(*self.__perm_addr_text_area_loc)
        field.clear()
        field.send_keys(perm_addr)
        return self

    def set_curr_addr(self, curr_addr: str) -> 'PageTextBox':
        field = self.__driver.find_element(*self.__curr_addr_text_area_loc)
        field.clear()
        field.send_keys(curr_addr)
        return self


    def get_email_field_attribute(self, attr):
        field = self.__driver.find_element(*self.__email_field_loc)
        attribute = field.get_attribute(attr)
        return attribute

    def get_full_name(self):
        field = self.__driver.find_element(*self.__output_fullname_loc)
        return field.text.split(':')[1].strip()

    def get_email(self):
        field = self.__driver.find_element(*self.__output_email_loc)
        return field.text.split(':')[1].strip()

    def get_curr_addr(self):
        field = self.__driver.find_element(*self.__output_curr_addr_loc)
        return field.text.split(':')[1].strip()

    def get_perm_addr(self):
        field = self.__driver.find_element(*self.__output_perm_addr_loc)
        return field.text.split(':')[1].strip()

    def submit(self):
        button = self.__driver.find_element(*self.__submit_btn_loc)
        button.click()


