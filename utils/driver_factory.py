import tempfile

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from utils.configReader import get_config
from utils.logger import get_logger

logger = get_logger()

def get_driver():
    browser = get_config("browser")
    logger.info(f"Launching browser: {browser}")

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        temp_profile = tempfile.mkdtemp()
        options.add_argument("--disable-features=PasswordLeakDetection")
        options.add_argument("--disable-features=AutofillServerCommunication")
        options.add_argument("--disable-sync")
        options.add_argument("--disable-background-networking")
        options.add_argument("--disable-component-update")
        options.add_argument("--disable-default-apps")
        options.add_argument("--no-first-run")
        options.add_argument("--no-default-browser-check")
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-info-bars")
        options.add_argument(f"--user-data-dir={temp_profile}")
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        }
        options.add_experimental_option("prefs", prefs)

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
    else:
        raise Exception("Only Chrome supported currently")

    return driver
