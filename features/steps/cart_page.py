from selenium.webdriver.common.by import By
from behave import given, when, then

@when('Click on Cart')
def click_on_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, 'a#nav-cart').click()

@then('Verify cart is empty')
def verify_cart_empty(context):
    context.driver.find_element(By.CSS_SELECTOR, 'div.sc-your-amazon-cart-is-empty')
