from itertools import count

from selenium.webdriver.common.by import By

from utils.logger import get_logger
from utils.wait_utils import wait_for_element

logger = get_logger(__name__)
class CartPage:
    def __init__(self, driver):
        self.driver = driver

    remove_backpack = (By.ID, "remove-sauce-labs-backpack")
    cart_items = (By.CLASS_NAME, "cart_item")

    def remove_product(self):
        logger.info("Removing product from cart")
        wait_for_element(self.driver, self.remove_backpack).click()
        logger.info("Product removed from cart")

    def get_cart_items_count(self):
        logger.info("Getting number of items in the cart")
        return len(self.driver.find_elements(*self.cart_items))
    logger.info(f"Number of items in the cart: {count}")