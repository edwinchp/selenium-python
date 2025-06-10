import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
time.sleep(5)

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



driver.close()