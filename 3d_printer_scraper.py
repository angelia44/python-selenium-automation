from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome()

products = []

# Navigate to the main product page
driver.get('https://www.amazon.com/')

driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('3D Printers')
driver.find_element(By.ID, "nav-search-submit-button").click()

# Find all the product links on the page
product_links = driver.find_elements(By.XPATH, "//span[@class = 'a-size-medium a-color-base a-text-normal']")

i = 0

# Iterate over each product link
for i, _ in enumerate(product_links):

    # Click on the product link to go to the product page
    product_links[i].click()

    driver.implicitly_wait(10)

    # Go back to the main product page
    driver.back()

    product_links = driver.find_elements(By.XPATH, "//span[@class = 'a-size-medium a-color-base a-text-normal']")

    # Wait for the page to load before finding the next link
    driver.implicitly_wait(10)

    # Find the title, description, and price elements on the product page
    #title = driver.find_element_by_xpath("//span[@id='productTitle']")
    #price_dollar = driver.find_element_by_xpath("//span[@class='a-price-whole']")
    #price_cents = driver.find_element_by_xpath("//span[@class='a-price-fraction']")
    #description_element = driver.find_element_by_xpath("//div[@id='productDescription']//p")
    #price_element = driver.find_element_by_xpath("//span[@id='priceblock_ourprice']")

    #product = {
   #     'title': title.text.strip(),
   #     'price': {'dollar': price_dollar.text.strip(), 'cents': price_cents.text.strip()}
    #}

    #products.append(product)

    # Get the text values of the title, description, and price elements
    #title = title_element.text
    #description = description_element.text
    #price = price_element.text

    # Print the values to the console
    #print('Title:', title)
    #print('Description:', description)
    #print('Price:', price)

    # Save the values to a data structure or file



# Close the browser window
#print(products)

driver.quit()
