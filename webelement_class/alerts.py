from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import *
import time


HOST = "https://demoqa.com/alerts"

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
    # Input DATA:
    alert_input = 'United States'

    # All Locators (all values are ID locators):
    alert_notify = 'alertButton'
    alert_confirm = 'confirmButton'
    confirm_result = 'confirmResult'
    alert_prompt = 'promtButton'
    prompt_result = 'promptResult'

    # Steps:
    driver.get(HOST)
    time.sleep(5)
    # click alert 1 button, click ok button to close the alert
    # click alert 2 button, confirm the alert, verify Ok button is clicked in the result test
    # click alert 2 button, dismiss the alert, verify Cancel button is clicked in the result text
    # click alert 3 button, enter the alert_input, confirm the alert,  verify alert_input message in result text
    # click alert 3 button, enter the alert_input, dismiss the alert,  verify no result message

    time.sleep(2)
    print("Alert Test Successfully executed.")

except Exception as err:
    time.sleep(10)
    print("Python Exception: test failed with following exception.")
    print(err)
except (NoSuchElementException, TimeoutException) as err:
    time.sleep(10)
    print("Selenium Exception: test failed with following exception.")
    print(err)
finally:
    # close all tabs:
    driver.quit()
    print("TEST Completed!!")
