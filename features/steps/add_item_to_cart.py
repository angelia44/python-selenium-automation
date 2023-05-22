from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when('Click third result')
def click_third_link(context):
    search_results = context.driver.find_elements(By.XPATH, "//span[@class = 'a-size-medium a-color-base a-text-normal']")
    search_results[2].click()

@when('Add item to Cart')
def add_item_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, 'input#add-to-cart-button').click()
    sleep(5)

@when('Navigate to Cart Page')
def navigate_to_cart_page(context):
    context.driver.get('https://www.amazon.com/gp/cart/view.html?ref_=nav_cart')

@then('Verify item is in cart')
def verify_item_in_cart(context):
    items = context.driver.find_elements(By.CSS_SELECTOR, 'form#activeCartViewForm div.sc-list-item')
    assert len(items) > 0, f'Error! Expected item to exist but got {len(items)}'
