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
# This sets a sticky timeout to implicitly wait for an element to be found, or a command to complete.
driver.implicitly_wait(20)

try:
    print("Starting test with various locator to use in find_element() method.")
    driver.get(HOST)
    # time.sleep(5)

    print("# WebDriver Properties:---------------------------")
    print("This is my current url:", driver.current_url)
    print("driver.name:", driver.name)
    # print("driver.orientation:", driver.orientation)
    print("driver.title:", driver.title)
    print("driver.current_window_handle:", driver.current_window_handle)
    print("driver.window_handles:", driver.window_handles)
    time.sleep(0.5)
    print("# WebDriver Methods:---------------------------")
    next_page = "https://www.google.com/"
    driver.get(next_page)
    driver.back()
    print("we are here now(qa tools):", driver.current_url)
    driver.forward()
    print("we are here now(google):", driver.current_url)
    driver.refresh()
    print("we are here now(google):", driver.current_url)
    time.sleep(0.5)
    print("# switching between browser windows(or tab).****************")
    # we are on /browser-windows page, get current window handle
    driver.get(HOST)
    # first_window_handle = "CDwindow-281C036C081C5E81AD2A374F5F1CA968"
    first_handle = driver.current_window_handle
    print("ID of the page opened:", first_handle)

    # click on new tab button, this opens new tab
    # driver.find_element(By.ID, "tabButton").click()
    driver.find_element(By.ID, "windowButton").click()
    # now we have 2 tabs, get window handles (list), tabs are in order handles=[idoffirsttab, idofsecondtab]
    handles = driver.window_handles
    print("number of handles found:", len(handles))
    print("IDs of all tabs/windows open:", handles)
    print("current browser window ID:", driver.current_window_handle)
    # switch to the second tab, switch to handles[1] or handles[-1]
    print("**** switching to a new window/tab ***********")
    driver.switch_to.window(handles[1])
    print("current url:", driver.current_url)
    print("Getting the text from new tab: ", driver.find_element(By.ID, 'sampleHeading').text)
    time.sleep(5)
    print("switching back to the first tab...")
    driver.switch_to.window(handles[0])
    print("current url:", driver.current_url)
    driver.find_element(By.ID, 'windowButton')

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
