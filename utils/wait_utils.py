from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.configReader import get_config

def wait_for_element(driver, locator):
    timeout = int(get_config("timeout"))
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )