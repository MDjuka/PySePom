import pytest
from ssqatest.end_to_end.pages.home_page import HomePage
from ssqatest.end_to_end.pages.header import Header
from ssqatest.end_to_end.pages.cart_page import CartPage
from ssqatest.end_to_end.configs.generic_configs import GenericConfigs
from ssqatest.end_to_end.pages.order_received_page import OrderReceivedPage
from ssqatest.end_to_end.pages.checkout_page import CheckoutPage


@pytest.mark.usefixtures("setup")
class TestEndToEndCheckoutGuestUser:


    def test_end_to_end_checkout_guest_user(self):
        home_pg = HomePage(self.driver)
        header = Header(self.driver)
        cart_pg = CartPage(self.driver)
        checkout_pg = CheckoutPage(self.driver)
        order_receive_pg = OrderReceivedPage(self.driver)

        # add an item to basket
        home_pg.click_first_add_to_cart_button()

        # make sure cart is updated before clicking on it
        header.wait_until_cart_item_count(1)

        # go to cart
        header.click_on_cart_on_right_header()

        # verify cart contains selected product
        product_names = cart_pg.get_all_product_names()
        assert len(product_names) == 1, f"Expected 1 item in cart but found {len(product_names)}"

        # apply coupon
        coupon_code = GenericConfigs.FREE_COUPON
        cart_pg.apply_coupon(coupon_code)

        # click on checkout
        cart_pg.click_proceed_to_checkout_btn()

        # fill in form details
        checkout_pg.fill_in_billing_info()

        # click on place order
        checkout_pg.click_place_order_btn()

        # verify order confirmation
        order_receive_pg.verify_order_received_confirmation_loaded()

        # verify order is recorder in database (via SQL or vie API)
        order_num = order_receive_pg.get_order_number()
        print(order_num)