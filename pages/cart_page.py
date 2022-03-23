from selenium.webdriver.common.by import By
from ssqatest.end_to_end.pages.base_page import BasePage


class CartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS
    PRODUCT_NAMES_IN_CART = (By.CSS_SELECTOR, "tr.cart_item td.product-name")
    COUPON_FIELD = (By.ID, 'coupon_code')
    APPLY_COUPON_BTN = (By.XPATH, "//button[@class='button']")
    CONFIRMATION_CODE_MSG = (By.CLASS_NAME, "woocommerce-message")
    PROCEED_TO_CHECKOUT_BTN = (By.CSS_SELECTOR, "a.checkout-button")

    def get_all_product_names(self):
        product_name_elements = self.wait_and_get_elements(self.PRODUCT_NAMES_IN_CART)
        product_names = [i for i in product_name_elements]
        # import pdb; pdb.set_trace()
        return product_names

    def input_coupon_code(self, code):
        self.wait_and_input_text(self.COUPON_FIELD, code)

    def click_on_apply_coupon_btn(self):
        self.wait_and_click(self.APPLY_COUPON_BTN)

    def apply_coupon(self, code):
        self.input_coupon_code(code)
        self.click_on_apply_coupon_btn()
        success_msg = self.get_displayed_message()
        assert success_msg == "Coupon code applied successfully."

    def get_displayed_message(self):
        text = self.wait_and_get_element_text(self.CONFIRMATION_CODE_MSG)
        return text

    def click_proceed_to_checkout_btn(self):
        self.wait_and_click(self.PROCEED_TO_CHECKOUT_BTN)




    
