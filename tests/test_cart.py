from utils.driver_factory import get_driver
from pages.login_page import LoginPage
from pages.products_page import ProductPage
from pages.cart_page import CartPage

def test_add_and_remove_cart():
    driver = get_driver()
    driver.get("https://www.saucedemo.com")

    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    product = ProductPage(driver)
    product.add_products()

    assert product.get_cart_count() == "2"

    product.go_to_cart()

    cart = CartPage(driver)
    cart.remove_product()

    assert cart.get_cart_items_count() == 1

    driver.quit()