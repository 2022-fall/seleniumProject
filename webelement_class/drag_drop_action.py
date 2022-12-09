import time

from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

from utilities import *

HOST = "https://jqueryui.com/resources/demos/droppable/default.html"
scrshot_dir = '../screenshots/'

# created the object for chromedriver that talks to Chrome Browser
chr_options = Options()
chr_options.add_experimental_option("detach", True)
# chr_options.add_experimental_option('excludeSwitches',["disable-popup-blocking"])
driver = webdriver.Chrome(options=chr_options)
print('maximizing the browser window')
# driver.maximize_window()
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
    driver.save_screenshot(scrshot_dir+'dragdrop1.png')
    # disable_google_ads(driver)

    # code for drag and drop is here
    print("# verify drop box text before dropping, expected: 'Drop here'")
    drag_obj = driver.find_element(By.ID, draggable_id)
    drop_obj = driver.find_element(By.ID, droppable_id)
    print(f"text in drop box, before: '{drop_obj.text}'")
    assert drop_obj.text == 'Drop here', "Drop box text verification, before drop action, failed."
    driver.save_screenshot(scrshot_dir+'dragdrop2-before.png')

    print("# drag and drop the object into the box")
    actions = ActionChains(driver)
    actions.drag_and_drop(drag_obj, drop_obj).perform()
    # actions.click_and_hold(drag_obj).release(drop_obj).perform()
    # actions.click_and_hold(drag_obj).pause(2).release(drop_obj).perform()
    print("# verify drop box text after dropping, expected: 'Dropped!'")
    print(f"text in drop box, after: '{drop_obj.text}'")
    assert drop_obj.text == 'Dropped!', "Drop box text verification, after drop action, failed."
    driver.save_screenshot(scrshot_dir+'dragdrop3-after.png')

    time.sleep(5)
    print("Drag and Drop Test Successfully executed.")

except (FileNotFoundError, ZeroDivisionError) as err:
    time.sleep(2)
    print("Python Exception: test failed with following exception.")
    print(err)
    driver.save_screenshot(scrshot_dir+'PythonException.png')

except (NoSuchElementException, TimeoutException) as err:
    time.sleep(2)
    print("Selenium Exception: test failed with following exception.")
    print(err)
    driver.save_screenshot(scrshot_dir+'SeleniumException.png')

finally:
    # close all tabs:
    driver.quit()
    print("TEST Completed!!")
