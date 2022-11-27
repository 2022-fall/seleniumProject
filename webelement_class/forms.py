from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import *
import time

HOST = "https://demoqa.com/automation-practice-form"

# created the object for chromedriver that talks to Chrome Browser
chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chr_options)
print('maximizing the browser window')
driver.maximize_window()
# This sets a sticky timeout to implicitly wait for an element to be found, or a command to complete.
driver.implicitly_wait(20)

try:
    # All Locators (all values are ID locators):
    fn_input = 'firstName'
    ln_input = 'lastName'
    email_input = 'userEmail'
    gender_male = 'gender-radio-1'
    mobile_number_input = 'userNumber'
    date_of_birth_input = 'dateOfBirthInput'
    hobbies_sp = 'hobbies-checkbox-1'
    hobbies_reading = 'hobbies-checkbox-2'
    upload_pic_input = 'uploadPicture'
    address_textarea = 'currentAddress'
    state_list = 'react-select-3-input'
    city_list = 'react-select-4-input'
    submit_button = 'submit'
    confirmation_msg = 'example-modal-sizes-title-lg'
    close_cm_button = 'closeLargeModal'

    # Steps:
    print("Starting test with various locator to use in find_element() method.")
    driver.get(HOST)
    # time.sleep(5)
    # enter first_name = 'john', enter last_name='doe', enter email='jdoe@email.com'
    # select radio button Gender=Male
    # mobile_number = 9876543210
    # (optional) enter date_of_birth = '27 Nov 2000'
    # (optional) enter subjects = 'selenium forms testing'
    # select checkboxes, select Sports, Reading
    # (optional) upload picture
    # enter message in text_area = '2906 Shell Road, 12224'
    # check is City list is enabled.
    # select state=NCR
    # check is City list is enabled.
    # select city=Delhi
    # check if Male gender is selected
    # check if Sports Hobbies is selected
    # click submit
    # verify the message='Thanks for submitting the form'


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
