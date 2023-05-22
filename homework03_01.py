from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# incognito mode setup
chrome_args = webdriver.ChromeOptions()
chrome_args.add_argument("--incognito")

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_args)
driver.maximize_window()

# Navigate to website
driver.get('https://www.amazon.com/')

# Mouse Actions
mouse_actions = ActionChains(driver)

# Find Sign In link
signin = driver.find_element(By.CSS_SELECTOR, "a#nav-link-accountList")

# Navigate to Sign In link
mouse_actions.move_to_element(signin).perform()

# Click Start Here link
driver.find_element(By.CSS_SELECTOR, 'a.nav-a[href*="https://www.amazon.com/ap/register"]').click()

# Find Amazon logo
driver.find_element(By.CSS_SELECTOR, 'i.a-icon-logo')

# Find page header
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')

# Find name input
driver.find_element(By.CSS_SELECTOR, 'input#ap_customer_name')

# Find email input
driver.find_element(By.CSS_SELECTOR, 'input#ap_email')

# Find password input
driver.find_element(By.CSS_SELECTOR, 'input#ap_password')

# Find password confirm input
driver.find_element(By.CSS_SELECTOR, 'input#ap_password_check')

# Find Create Account Button
driver.find_element(By.CSS_SELECTOR, 'input#continue')

# Find Conditions of Use Link
driver.find_element(By.CSS_SELECTOR, 'div#legalTextRow a[href*="/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use"]')

# Find Privacy Notice
driver.find_element(By.CSS_SELECTOR, 'div#legalTextRow a[href*="/gp/help/customer/display.html/ref=ap_register_notification_privacy_notice"]')

# Find Sign In button
driver.find_element(By.CSS_SELECTOR, 'a.a-link-emphasis[href*="/ap/signin"]')

sleep(5)
