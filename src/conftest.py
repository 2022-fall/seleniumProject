# This is a shared fixture between modules
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='session')
def driver():
    print("\n----------------- SetUp ----------------")
    print('Initializing a webdriver for the browser...')
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

    yield driver
    print("\n------------------ TearDown ------------")
    print("# close all tabs:")
    driver.quit()
    print("TEST Completed!!")
    print("fixture steps are completed here.")

