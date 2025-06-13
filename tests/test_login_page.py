import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def driver():
    print("Creating Chrome Driver")
    my_driver = webdriver.Chrome()
    yield my_driver
    print("Closing Chrome Driver")
    my_driver.quit()

class TestPositivesScenarios:

    @pytest.mark.login
    def test_positive_login(self, driver):

        driver.get("https://practicetestautomation.com/practice-test-login/")

        time.sleep(5)

        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("student")

        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys("Password123")

        submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        submit_button_locator.click()

        actual_url = driver.current_url
        assert actual_url == "https://practicetestautomation.com/logged-in-successfully/"

        text_locator = driver.find_element(By.TAG_NAME, "h1")
        actual_text = text_locator.text
        assert actual_text == "Logged In Successfully"

        log_out_button_locator = driver.find_element(By.LINK_TEXT, "Log out")
        assert log_out_button_locator.is_displayed()