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
try:
    # Input DATA:
    first_name = 'john'
    last_name = 'doe'
    email = 'jdoe@email.com'

    # All Locators (all values are ID locators):
    fn_input = 'firstName'
    ln_input = 'lastName'
    email_input = 'userEmail'
    gender_male_xpath = '//input[@id="gender-radio-1"]/..'
    mobile_number_input = 'userNumber'
    date_of_birth_input = 'dateOfBirthInput'
    hobbies_sp = 'hobbies-checkbox-1'
    hobbies_reading = 'hobbies-checkbox-2'
    upload_pic_input = 'uploadPicture'
    address_textarea = 'currentAddress'
    state_list = 'state'
    state_input = 'react-select-3-input'
    city_list = 'city'
    city_input = 'react-select-4-input'
    submit_button = 'submit'
    confirmation_msg = 'example-modal-sizes-title-lg'
    close_cm_button = 'closeLargeModal'

    # Steps:
    print("Starting test with various locator to use in find_element() method.")
    driver.get(HOST)
    # time.sleep(5)
    # enter first name , last name and email
    driver.find_element(By.ID, fn_input).send_keys(first_name)
    driver.find_element(By.ID, ln_input).send_keys(last_name)
    driver.find_element(By.ID, email_input).send_keys(email)
    # mobile_number = 9876543210
    driver.find_element(By.ID, mobile_number_input).send_keys('9876543210')
    # select radio button Gender=Male
    driver.find_element(By.XPATH, gender_male_xpath).click()
    # (optional) enter date_of_birth = '27 Nov 2000'
    # (optional) enter subjects = 'selenium forms testing'
    # select checkboxes, select Sports, Reading
    driver.find_element(By.ID, hobbies_sp).click()
    driver.find_element(By.ID, hobbies_reading).click()
    # (optional) upload picture
    # enter message in text_area = '2906 Shell Road, 12224'
    driver.find_element(By.ID, address_textarea).send_keys('2906 Shell Road, 12224')
    # check is City list is enabled.
    print('is City list is enabled before selecting state?', driver.find_element(By.ID, city_list).is_enabled())
    # select state=NCR
    print('is State list is enabled before selecting state?', driver.find_element(By.ID, state_list).is_enabled())
    driver.find_element(By.ID, state_input).send_keys('NCR')
    # check is City list is enabled.
    print('is City list enabled after selecting state?', driver.find_element(By.ID, city_list).is_enabled())
    # select city=Delhi
    driver.find_element(By.ID, city_input).send_keys('Delhi')
    # check if Male gender is selected
    print('is Male gender radio button selected?', driver.find_element(By.ID, gender_male_xpath).is_selected())
    # check if Sports Hobbies is selected
    print('is Sports selected from Hobbies?', driver.find_element(By.ID, hobbies_sp).is_selected())
    # click submit
    driver.find_element(By.ID, submit_button).click()
    # verify the message='Thanks for submitting the form'
    print("Is Confirmation message displayed?", driver.find_element(By.ID, confirmation_msg).is_displayed())
    # close the confirmation window
    driver.find_element(By.ID, close_cm_button).click()
    time.sleep(10)

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
driver.implicitly_wait(20)
