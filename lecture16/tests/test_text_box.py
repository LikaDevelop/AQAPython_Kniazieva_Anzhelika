import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from lecture16.pages.page_text_box import PageTextBox


user_data = {'fullname': 'Vasya Pupkin',
             'email_сorrect': 'vasya@gmail.com',
             'email_incorrect': 'mcdefmce',
             'curr_addr': 'My current address',
             'perm_addr': 'My permanent address'}


@pytest.mark.usefixtures('chrome')
class TestTextBox:

    def test_full_name(self):
        page = PageTextBox(self.driver)
        page.open().set_full_name(user_data.get('fullname'))
        page.submit()
        name = page.get_full_name()
        assert name == user_data['fullname']

    def test_email_positive(self):
        page = PageTextBox(self.driver)
        page.open().set_email_name(user_data.get('email_correct'))
        page.submit()
        email = page.get_email()
        assert email == user_data['email_сorrect']

    def test_email_negative(self):
        # page = PageTextBox(self.driver)
        # page.open().set_email_name(user_data.get('email_incorrect'))
        # page.submit()
        # # is_error_present = page.is_error_in_email_present()
        # with pytest.raises(NoSuchElementException):
        #     page.get_email()
        # assert is_error_present


        # is_condition_one = True
        # is_condition_two = True
        # assert all([is_condition_one, is_condition_two])

        pass

    def test_curr_addr(self):
        pass

    def test_perm_addr(self):
        pass

    def test_full_form_positive(self):
        pass

    def test_full_form_negative(self):
        pass
