import time

import pytest
from selenium.webdriver.common.by import By

from page_objects.login_page import LoginPage


class TestPositivesScenarios:

    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, expected_error_message",
                             [("incorrectUser", "incorrectPassword", "Your username is invalid!"),
                              ("student", "incorrectPassword", "Your password is invalid!")])
    def test_negative_login(self, driver, username, password, expected_error_message):

        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login(username, password)

        assert login_page.current_url == "https://practicetestautomation.com/practice-test-login/", "Actual URL is not expected"
        assert login_page.error_message == expected_error_message,  "Error message is not expected"
