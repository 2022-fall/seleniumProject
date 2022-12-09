import time

from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utilities import *

HOST = "https://jqueryui.com/resources/demos/droppable/default.html"

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
    draggable_id = 'draggable'
    droppable_id = 'droppable'

    # Steps:
    driver.get(HOST)
    time.sleep(1)
    # disable_google_ads(driver)

    # code for drag and drop is here
    # verify drop box text before dropping, expected: 'Drop here'
    # drag and drop the object into the box
    # verify drop box text after dropping, expected: 'Dropped!'

    time.sleep(5)
    print("Drag and Drop Test Successfully executed.")

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
