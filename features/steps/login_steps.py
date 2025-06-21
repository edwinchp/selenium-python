from behave import given, when, then, step
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.login_page import LoginPage

from page_objects.logged_in_successfully_page import LoggedInSuccessfullyPage


@given('I am on the login page')
def step_given_on_login_page(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.open()


@when('I enter username "{username}" and password "{password}"')
def step_when_enter_credentials(context, username, password):
    context.login_page.execute_login("student", "Password123")
    context.logged_in_page = LoggedInSuccessfullyPage(context.driver)
    assert context.logged_in_page.expected_url == context.logged_in_page.current_url, "Actual URL is not the same as expected."
    assert context.logged_in_page.header == "Logged In Successfully", "Header is not expected"
    assert context.logged_in_page.is_logout_button_displayed(), "Logout button should be visible"

@when('I click the login button')
def step_when_click_login(context):
    context.login_page.click_login_button()

@then('I should be redirected to the dashboard')
def step_then_redirected_to_dashboard(context):
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.url_contains("/dashboard"))
    assert "/dashboard" in context.driver.current_url

@then('I should see a welcome message')
def step_then_see_welcome_message(context):
    welcome_element = context.driver.find_element(By.CLASS_NAME, "welcome-message")
    assert welcome_element.is_displayed()
    assert "Welcome" in welcome_element.text

@then('I should see an error message "{error_message}"')
def step_then_see_error_message(context, error_message):
    error_element = context.driver.find_element(By.CLASS_NAME, "error-message")
    assert error_element.is_displayed()
    assert error_message in error_element.text

@then('I should remain on the login page')
def step_then_remain_on_login_page(context):
    assert "/login" in context.driver.current_url

@then('I should see "{expected_result}"')
def step_then_see_expected_result(context, expected_result):
    page_text = context.driver.find_element(By.TAG_NAME, "body").text
    assert expected_result in page_text

# Generic step for reusable actions
@step('I wait for {seconds:d} seconds')
def step_wait_for_seconds(context, seconds):
    import time
    time.sleep(seconds)

@step('I take a screenshot')
def step_take_screenshot(context):
    context.driver.save_screenshot(f"screenshot_{context.scenario.name}.png")