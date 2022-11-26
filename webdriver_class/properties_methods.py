# Chapter 4:

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import *
import time

HOST = "https://demoqa.com/browser-windows"

# created the object for chromedriver that talks to Chrome Browser
chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chr_options)
print('maximizing the browser window')
driver.maximize_window()
try:
    print("Starting test with various locator to use in find_element() method.")
    driver.get(HOST)
    time.sleep(5)

    print("# WebDriver Properties:---------------------------")
    print("This is my current url:", driver.current_url)
    print("driver.name:", driver.name)
    # print("driver.orientation:", driver.orientation)
    print("driver.title:", driver.title)
    print("driver.current_window_handle:", driver.current_window_handle)
    print("driver.window_handles:", driver.window_handles)
    time.sleep(5)
    print("# WebDriver Methods:---------------------------")
    next_page = "https://www.google.com/"
    driver.get(next_page)
    driver.back()
    print("we are here now(qa tools):", driver.current_url)
    driver.forward()
    print("we are here now(google):", driver.current_url)
    driver.refresh()
    print("we are here now(google):", driver.current_url)
    time.sleep(5)


except Exception as err:
    print("Python Exception: test failed with following exception.")
    print(err)
except (NoSuchElementException, TimeoutException) as err:
    print("Selenium Exception: test failed with following exception.")
    print(err)
finally:
    # close all tabs:
    driver.quit()
    # pass
