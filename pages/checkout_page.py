from selenium.webdriver.common.by import By

from utils.logger import get_logger

logger = get_logger(__name__)

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    checkout_btn = (By.ID, "checkout")
    first_name = (By.ID, "first-name")
    last_name = (By.ID, "last-name")
    postal_code = (By.ID, "postal-code")
    continue_btn = (By.ID, "continue")
    finish_btn = (By.ID, "finish")
    success_msg = (By.CLASS_NAME, "complete-header")

    def start_checkout(self):
        logger.info("Starting the checkout process")
        self.driver.find_element(*self.checkout_btn).click()
        logger.info("Checkout process started")

    def enter_details(self, fname, lname, zip):
        logger.info("Entering checkout details")
        self.driver.find_element(*self.first_name).send_keys(fname)
        self.driver.find_element(*self.last_name).send_keys(lname)
        self.driver.find_element(*self.postal_code).send_keys(zip)
        self.driver.find_element(*self.continue_btn).click()
        logger.info("Checkout details entered")

    def finish_order(self):
        logger.info("Finishing the order")
        self.driver.find_element(*self.finish_btn).click()
        logger.info("Order finished")

    def get_success_message(self):
        logger.info("Retrieving success message")
        return self.driver.find_element(*self.success_msg).text
    logger.info("Success message retrieved")
