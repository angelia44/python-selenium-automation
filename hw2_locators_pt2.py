from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
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

# Go to Amazon page
driver.get('https://www.amazon.com/')

# Find and click on "orders" button
driver.find_element(By.ID, "nav-orders").click()

# Verify Sign In header is present in new page
driver.find_element(By.XPATH, "//h1[contains(text(), 'Sign in')]")

# Verify email field is present in new page
driver.find_element(By.ID, "ap_email")
