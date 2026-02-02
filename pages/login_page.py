from selenium.webdriver.common.by import By
from utils.logger import get_logger
from utils.wait_utils import wait_for_element

logger = get_logger(__name__)
class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    username = (By.ID, "user-name")
    password = (By.ID, "password")
    login_btn = (By.ID, "login-button")

    def login(self, user, pwd):
        logger.info("Logging into the application")
        wait_for_element(self.driver, self.username).send_keys(user)
        wait_for_element(self.driver, self.password).send_keys(pwd)
        wait_for_element(self.driver, self.login_btn).click()