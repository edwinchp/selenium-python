import time

import pytest
from selenium.webdriver.common.by import By


class TestPositivesScenarios:

    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, expected_error_message",
                             [("incorrectUser", "incorrectPassword", "Your username is invalid!"),
                              ("student", "incorrectPassword", "Your password is invalid!")])
    def test_negative_login(self, driver, username, password, expected_error_message):

        driver.get("https://practicetestautomation.com/practice-test-login/")

        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys(username)

        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys(password)

        submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        submit_button_locator.click()

        actual_url = driver.current_url
        assert actual_url == "https://practicetestautomation.com/practice-test-login/"

        error_text_locator = driver.find_element(By.ID, "error")
        actual_text = error_text_locator.text
        assert actual_text == expected_error_message
