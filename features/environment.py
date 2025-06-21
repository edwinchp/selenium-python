from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


def before_all(context):
    """Setup before all tests"""
    context.config.setup_logging()


def before_scenario(context, scenario):
    """Setup before each scenario"""
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    # Uncomment for headless mode
    # chrome_options.add_argument("--headless")

    #service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)


def after_scenario(context, scenario):
    """Cleanup after each scenario"""
    if hasattr(context, 'driver'):
        context.driver.quit()


def after_all(context):
    """Cleanup after all tests"""
    pass