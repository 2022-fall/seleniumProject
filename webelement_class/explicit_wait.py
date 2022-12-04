import time

from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
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
    time.sleep(5)
    disable_google_ads(driver)

    # code for explicit waits will be here
    print("# 1. click alert button, explicitly wait until alert appears (condition)")
    print("# click ok on alert to close")
    alert = driver.switch_to.alert
    alert.accept()

    print("# 2. click on ChangeText.. button, wait until text changes, get text and print")
    print("# 3. click on 'Display button ...' button, wait until hidden button is displayed, verify button is enabled")
    print("# 4. Click on 'Enable button after..' button, wait until 'Button' is enabled, click enabled Button")
    print("# 5. click 'Check Checkbox ...' button, wait until Checkbox is checked, verify 'Checkbox' is checked.")
    time.sleep(2)
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
