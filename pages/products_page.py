from selenium.webdriver.common.by import By

from utils.logger import get_logger

logger = get_logger(__name__)
class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    add_backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
    add_bike = (By.ID, "add-to-cart-sauce-labs-bike-light")
    cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
    cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    def add_products(self):
        logger.info("Adding products to the cart")
        self.driver.find_element(*self.add_backpack).click()
        self.driver.find_element(*self.add_bike).click()
        logger.info("Products added to the cart")

    def get_cart_count(self):
        logger.info("Getting the cart item count")
        return self.driver.find_element(*self.cart_badge).text

    def go_to_cart(self):
        logger.info("Navigating to the cart page")
        self.driver.find_element(*self.cart_icon).click()
        logger.info("Navigated to the cart page")
