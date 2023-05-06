from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()


# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://www.amazon.com/')

# Find and click login link
driver.find_element(By.ID, "nav-link-accountList").click()

# Find Amazon Logo
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")

# Find Continue button
driver.find_element(By.XPATH, "//input[@aria-labelledby='continue-announce']")

# Find and click "need help" dropdown
driver.find_element(By.XPATH, "//span[contains(text(), 'Need help?') and @class='a-expander-prompt']").click()

# Find "Forgot your password" link
driver.find_element(By.ID, "auth-fpp-link-bottom")

# Find "Other issues with signin" link
driver.find_element(By.ID, "ap-other-signin-issues-link")

# Find "Conditions of use" link
driver.find_element(By.XPATH, "//div[@id='legalTextRow']//a[contains(text(), 'Conditions of Use')]")

# Find "Privacy notice" link
driver.find_element(By.XPATH, "//div[@id='legalTextRow']//a[contains(text(), 'Privacy Notice')]")

# sleep(5)
