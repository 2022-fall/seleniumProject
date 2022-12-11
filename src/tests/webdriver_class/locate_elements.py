from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time


HOST = "https://demoqa.com/text-box"

# created the object for chromedriver that talks to Chrome Browser
chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chr_options)
print('maximizing the browser window')
driver.maximize_window()

print("Starting test with various locator to use in find_element() method.")
driver.get(HOST)
time.sleep(5)

fullname = driver.find_element(By.ID, "userName")
fullname.send_keys('John')
# driver.find_element(By.NAME, 'q')
driver.find_element(By.TAG_NAME, 'textarea').send_keys("selenium found 'textarea on html, this is first element of this type")
element_list = driver.find_elements(By.CLASS_NAME, 'form-control')    # list
print(element_list)
print(f"Number of elements in primary_buttons list: {len(element_list)}")
time.sleep(5)

print("opening the google for link text locator..")
driver.get("https://www.google.com/")
driver.find_element(By.LINK_TEXT, 'Gmail')
driver.find_element(By.PARTIAL_LINK_TEXT, 'mail').click()


# driver.find_element(By.XPATH, '//form[0]/div[0]/input[0]')
# driver.find_element(By.CSS_SELECTOR, '#search')
time.sleep(5)
driver.quit()
print("Test is complete!!")


# [
# <selenium.webdriver.remote.webelement.WebElement (session="a0a87d1a4144f6f37f86eeebf228c320", element="44bdb432-4708-4bf7-bc06-c16271a143bc")>,
# <selenium.webdriver.remote.webelement.WebElement (session="a0a87d1a4144f6f37f86eeebf228c320", element="4d6f8410-adf5-4e44-835b-2de79ec8eb01")>,
# <selenium.webdriver.remote.webelement.WebElement (session="a0a87d1a4144f6f37f86eeebf228c320", element="e46f454f-7fb2-4e2e-8e96-fa26d9008c3e")>,
# <selenium.webdriver.remote.webelement.WebElement (session="a0a87d1a4144f6f37f86eeebf228c320", element="35e0bd9c-d11d-449c-9c77-53f4d95f7cbe")>
# ]