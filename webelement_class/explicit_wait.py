import time

from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utilities import *

HOST = "https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver"

# created the object for chromedriver that talks to Chrome Browser
chr_options = Options()
chr_options.add_experimental_option("detach", True)
# chr_options.add_experimental_option('excludeSwitches',["disable-popup-blocking"])
driver = webdriver.Chrome(options=chr_options)
print('maximizing the browser window')
driver.maximize_window()
# This sets a sticky timeout to implicitly wait for an element to be found, or a command to complete.
driver.implicitly_wait(20)
time.sleep(0)

try:
    # All Locators (all values are ID locators):
    alert_button_id = 'alert'
    populate_text_id = 'populate-text'
    target_text_id = 'h2'
    display_other_button_id = 'display-other-button'
    hidden_button_id = 'hidden'
    button_id = 'enable-button'
    disabled_button_id = 'disable'
    check_button_id = 'checkbox'
    checkbox_id = 'ch'

    # Steps:
    driver.get(HOST)
    time.sleep(1)
    # disable_google_ads(driver)

    # code for explicit waits will be here
    print("# 1. click alert button, explicitly wait until alert appears (condition)")
    print("# click ok on alert to close")
    driver.find_element(By.ID, alert_button_id).click()
    print("applying explicit wait ...")
    wdwait = WebDriverWait(driver, 7)
    wdwait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    time.sleep(2)
    alert.accept()
    print('alert opened and ok button is clicked')

    print("# 2. get current text, click on ChangeText.. button, wait until text changes, get new text displayed")
    print('Text Displayed, before:', driver.find_element(By.ID, target_text_id).text)
    driver.find_element(By.ID, populate_text_id).click()
    print("applying explicit wait ...")
    wdwait = WebDriverWait(driver, 15)
    wdwait.until(EC.text_to_be_present_in_element((By.ID, target_text_id), 'Selenium'))
    print('Text Displayed, after:', driver.find_element(By.ID, target_text_id).text)

    print("# 3. check if button is displayed, click on 'Display button after ...' button, wait until hidden button is displayed, verify button is enabled")
    print('Is button displayed, before:', driver.find_element(By.ID, hidden_button_id).is_displayed())
    driver.find_element(By.ID, display_other_button_id).click()
    print("applying explicit wait ...")
    wdwait.until(EC.visibility_of_element_located((By.ID, hidden_button_id)))
    print('Is button displayed, after:', driver.find_element(By.ID, hidden_button_id).is_displayed())

    print("# 4. check if button is enabled, Click on 'Enable button after..' button, wait until 'Button' is enabled, click enabled Button")
    print('Is button enabled, before:', driver.find_element(By.ID, disabled_button_id).is_enabled())
    driver.find_element(By.ID, button_id).click()
    print("applying explicit wait ...")
    wdwait.until(EC.element_to_be_clickable((By.ID, disabled_button_id)))
    print('Is button enabled, after:', driver.find_element(By.ID, disabled_button_id).is_enabled())
    driver.find_element(By.ID, disabled_button_id).click()

    print("# 5. check if 'Checkbox' is checked, click 'Check Checkbox ...' button, wait until Checkbox is checked, verify 'Checkbox' is checked.")
    print('Is Checkbox checked, before:', driver.find_element(By.ID, checkbox_id).is_selected())
    # driver.find_element(By.ID, check_button_id).click()
    wdwait.until(EC.presence_of_element_located((By.ID, check_button_id))).click()
    print("applying explicit wait ...")
    wdwait.until(EC.element_to_be_selected(driver.find_element(By.ID, checkbox_id)))
    print('Is Checkbox checked, after:', driver.find_element(By.ID, checkbox_id).is_selected())

    time.sleep(5)
    print("Explicit wait Test Successfully executed.")

except Exception as err:
    time.sleep(2)
    print("Python Exception: test failed with following exception.")
    print(err)
except (NoSuchElementException, TimeoutException) as err:
    time.sleep(2)
    print("Selenium Exception: test failed with following exception.")
    print(err)
finally:
    # close all tabs:
    driver.quit()
    print("TEST Completed!!")
