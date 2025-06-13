import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    print("Creating Chrome Driver")
    my_driver = webdriver.Chrome()
    yield my_driver
    print("Closing Chrome Driver")
    my_driver.quit()