from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when('Click on Returns and Orders')
def click_returns_link(context):
    context.driver.find_element(By.CSS_SELECTOR, 'a#nav-orders').click()

@then('Verify {expected_result} title exists')
def find_sign_in_title(context, expected_result):
    title = context.driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small').text
    assert title == expected_result, f'Error! Expected Sign in but got {title}'

@then('Verify email input is present')
def find_email_input(context):
    context.driver.find_element(By.CSS_SELECTOR, '#ap_email')
