import time

from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.chrome.options import Options

from utilities import *

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
    disable_google_ads(driver)
    print("# click alert 1 button, click ok button to close the alert")
    driver.find_element(By.ID, alert_notify).click()
    alert = driver.switch_to.alert
    time.sleep(2)
    print(f"Text on the alert: '{alert.text}'")
    alert.accept()
    print(".......................................")
    time.sleep(5)

    print("# click alert 2 button, confirm the alert, verify Ok button is clicked in the result test")
    driver.find_element(By.ID, alert_confirm).click()
    alert = driver.switch_to.alert
    time.sleep(2)
    print(f"Text on the alert: '{alert.text}'")
    alert.accept()
    result_msg = driver.find_element(By.ID, confirm_result).text
    print(f"Result message : '{result_msg}'")
    print(".......................................")
    time.sleep(5)

    print("# click alert 2 button, dismiss the alert, verify Cancel button is clicked in the result text")
    driver.find_element(By.ID, alert_confirm).click()
    alert = driver.switch_to.alert
    time.sleep(2)
    print(f"Text on the alert: '{alert.text}'")
    alert.dismiss()
    result_msg = driver.find_element(By.ID, confirm_result).text
    print(f"Result message : '{result_msg}'")
    print(".......................................")
    time.sleep(5)

    print("# click alert 3 button, enter the alert_input, confirm the alert,  verify alert_input message in result text")
    driver.find_element(By.ID, alert_prompt).click()
    alert = driver.switch_to.alert
    time.sleep(2)
    print(f"Text on the alert: '{alert.text}'")
    alert.send_keys(alert_input)
    alert.accept()
    result_msg = driver.find_element(By.ID, prompt_result).text
    print(f"Result message : '{result_msg}'")
    print(".......................................")
    time.sleep(5)

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
