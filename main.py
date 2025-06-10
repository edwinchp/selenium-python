import time

from selenium import webdriver

driver = webdriver.Chrome()
time.sleep(5)

driver.get("https://www.google.com")

time.sleep(5)

driver.close()