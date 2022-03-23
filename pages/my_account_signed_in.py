from selenium.webdriver.common.by import By
from ssqatest.end_to_end.pages.base_page import BasePage


class MyAccountSignedIn(BasePage):

    # LOCATORS
    LOGOUT_BTN = (By.LINK_TEXT, 'Logout')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def verify_user_is_signed_in(self):
        self.wait_until_element_is_visible(self.LOGOUT_BTN)