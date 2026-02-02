from utils.configReader import get_config
from utils.driver_factory import get_driver
from pages.login_page import LoginPage

def test_valid_login(driver):
    driver = get_driver()
    driver.get(get_config("base_url"))

    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    assert "inventory" in driver.current_url
    driver.quit()