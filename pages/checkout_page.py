from selenium.webdriver.common.by import By
from ssqatest.end_to_end.utilities.utils import generate_random_email_and_password
from ssqatest.end_to_end.pages.base_page import BasePage


class CheckoutPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS
    BILLING_FIRST_NAME_FIELD = (By.ID, 'billing_first_name')
    BILLING_LAST_NAME_FIELD = (By.ID, 'billing_last_name')
    BILLING_STREET_ADDRESS_FIELD = (By.ID, 'billing_address_1')
    BILLING_TOWN_FIELD = (By.ID, 'billing_city')
    BILLING_ZIP_FIELD = (By.ID, 'billing_postcode')
    BILLING_PHONE_FIELD = (By.ID, 'billing_phone')
    BILLING_EMAIL_FIELD = (By.ID, 'billing_email')
    PLACE_ORDER_BTN = (By.ID, 'place_order')

    def input_billing_fname(self, first_name="TestFname"):
        self.wait_and_input_text(self.BILLING_FIRST_NAME_FIELD, first_name)

    def input_billing_lname(self, lname="TestLname"):
        self.wait_and_input_text(self.BILLING_LAST_NAME_FIELD, lname)

    def input_billing_street_address(self, address="123 Main St"):
        self.wait_and_input_text(self.BILLING_STREET_ADDRESS_FIELD, address)

    def input_billing_town(self, town="San Francisco"):
        self.wait_and_input_text(self.BILLING_TOWN_FIELD, town)

    def input_billing_zip(self, zip_code="94018"):
        self.wait_and_input_text(self.BILLING_ZIP_FIELD, zip_code)

    def input_billing_phone_num(self, phone_num="8051111111"):
        self.wait_and_input_text(self.BILLING_PHONE_FIELD, phone_num)

    def input_billing_email(self, email=None):
        if not email:
            rand_email = generate_random_email_and_password()
            email = rand_email['email']
        self.wait_and_input_text(self.BILLING_EMAIL_FIELD, email)

    def fill_in_billing_info(self):
        self.input_billing_fname()
        self.input_billing_lname()
        self.input_billing_street_address()
        self.input_billing_town()
        self.input_billing_zip()
        self.input_billing_phone_num()
        self.input_billing_email()

    def click_place_order_btn(self):
        self.wait_and_click(self.PLACE_ORDER_BTN)
