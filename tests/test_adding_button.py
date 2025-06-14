import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestAddingButton:

    def test_adding_button(self, driver):
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        wait = WebDriverWait(driver, 30)
        is_hidden = wait.until(expected_conditions.invisibility_of_element_located((By.ID, "add_btn")))

        assert is_hidden