from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import *
import time

from utilities import *

HOST = "https://demoqa.com/automation-practice-form"

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
    hobbies_sp_xpath = '//input[@id="hobbies-checkbox-1"]/..'
    hobbies_reading_xpath = '//input[@id="hobbies-checkbox-2"]/..'
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
    driver.get(HOST)
    # let all ads load
    time.sleep(5)
    # after loading all ads this step will go through all of them and disable
    disable_google_ads(driver)

    print("Starting test with various properties and methods for WebElement class.")
    # driver.execute_script("document.body.style.zoom='0.9'")

    # enter first name , last name and email
    fn_box = driver.find_element(By.ID, fn_input)
    fn_box.send_keys('Delete me Please')
    time.sleep(5)
    fn_box.clear()
    fn_box.send_keys(first_name)
    time.sleep(5)
    driver.find_element(By.ID, ln_input).send_keys(last_name)
    driver.find_element(By.ID, email_input).send_keys(email)
    # mobile_number = 9876543210
    driver.find_element(By.ID, mobile_number_input).send_keys('9876543210')
    # select radio button Gender=Male
    driver.find_element(By.XPATH, gender_male_xpath).click()
    # (optional) enter date_of_birth = '27 Nov 2000'
    # (optional) enter subjects = 'selenium forms testing'
    # select checkboxes, select Sports, Reading
    driver.find_element(By.XPATH, hobbies_sp_xpath).click()
    driver.find_element(By.XPATH, hobbies_reading_xpath).click()
    # (optional) upload picture
    # enter message in text_area = '2906 Shell Road, 12224'
    driver.find_element(By.ID, address_textarea).send_keys('2906 Shell Road, 12224')
    # check is City list is enabled.
    print('is City list is enabled before selecting state?', driver.find_element(By.ID, city_list).is_selected())
    # select state=NCR
    print('is State list is enabled before selecting state?', driver.find_element(By.ID, state_list).is_selected())
    driver.find_element(By.ID, state_input).send_keys('NCR' + Keys.TAB)
    print("state is entered.")
    # check is City list is enabled.
    time.sleep(2)
    print('is City list enabled after selecting state?', driver.find_element(By.ID, city_list).is_enabled())
    # select city=Delhi
    driver.find_element(By.ID, city_input).send_keys('Delhi' + Keys.TAB)
    print('city is entered.')
    # check if Male gender is selected
    print('is Male gender radio button selected?', driver.find_element(By.XPATH, gender_male_xpath).is_enabled())
    # check if Sports Hobbies is selected
    print('is Sports selected from Hobbies?', driver.find_element(By.XPATH, hobbies_sp_xpath).is_selected())
    # click submit
    submit_button = driver.find_element(By.ID, submit_button)
    # below step is optional, it is to scroll to the element, but we dont have scroll bar on the website, it wont work
    # but this is good case to show that we can execute javascript with Selenium commands
    driver.execute_script("arguments[0].scrollIntoView();", submit_button)
    driver.execute_script("arguments[0].click();", submit_button)
    # submit_button.click()
    time.sleep(5)
    print("all information was entered and submitted...")

    # verify the message='Thanks for submitting the form'
    print("Is Confirmation message displayed?", driver.find_element(By.ID, confirmation_msg).is_displayed())
    # close the confirmation window
    close_btn = driver.find_element(By.ID, close_cm_button)
    close_btn.click()
    time.sleep(2)
    print("Test Successfully executed.")

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
