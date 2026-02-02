from pages.login_page import LoginPage
from pages.products_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_complete_order(driver):
    driver.get("https://www.saucedemo.com")

    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    product = ProductPage(driver)
    product.add_products()
    product.go_to_cart()

    cart = CartPage(driver)
    cart.remove_product()   # leave 1 item

    checkout = CheckoutPage(driver)
    checkout.start_checkout()
    checkout.enter_details("John", "Doe", "560001")
    checkout.finish_order()

    assert checkout.get_success_message() == "Thank you for your order!"