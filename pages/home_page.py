from selenium.webdriver.common.by import By
from ssqatest.end_to_end.pages.base_page import BasePage


class HomePage(BasePage):

    # LOCATORS
    ADD_TO_CART_BTN = (By.XPATH, "//a[@data-product_id='23']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_first_add_to_cart_button(self):
        self.wait_and_click(self.ADD_TO_CART_BTN)




