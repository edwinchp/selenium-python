import os

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from dotenv import load_dotenv


@pytest.fixture()
def driver(request):
    load_dotenv(dotenv_path='.env')
    browser = request.config.getoption("--browser").lower()
    print(f"Creating {browser} Driver")
    if browser == "chrome":
        my_driver = webdriver.Chrome()

    elif browser == "firefox":
        my_driver =  webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    elif browser == 'grid':
        selenium_grid_hub = os.getenv('SELENIUM_GRID_HUB')
        options = FirefoxOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')

        my_driver = webdriver.Remote(command_executor=selenium_grid_hub, options=options)
    else:
        raise TypeError(f"Browser not supported: {browser}")
    my_driver.implicitly_wait(30)
    yield my_driver
    print(f"Closing {browser} Driver")
    my_driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Browser to execute tests (chrome or firefox)"
    )