from src.pages.base_page import BasePage
from src.utilities import *
from selenium.webdriver.common.keys import Keys

logfile = f'{ROOT_DIR}/logs/{get_str_day()}.log'
log = create_logger(logfile)


class FormsPage(BasePage):
    """Page Model of forms webpage that defines all locators as variables and actions as methods"""

    # All Locators (all values are ID locators):
    fn_input = 'firstName'
    ln_input = 'lastName'
    email_input = 'userEmail'
    gender_male_xpath = '//input[@id="gender-radio-1"]/..'
    gender_female_xpath = '//input[@id="gender-radio-2"]/..'
    gender_other_xpath = '//input[@id="gender-radio-3"]/..'
    hobbies_sp_xpath = '//input[@id="hobbies-checkbox-1"]/..'
    hobbies_reading_xpath = '//input[@id="hobbies-checkbox-2"]/..'
    hobbies_music_xpath = '//input[@id="hobbies-checkbox-3"]/..'
    mobile_number_input = 'userNumber'
    date_of_birth_input = 'dateOfBirthInput'
    upload_pic_input = 'uploadPicture'
    address_textarea = 'currentAddress'
    state_list = 'state'
    state_input = 'react-select-3-input'
    city_list = 'city'
    city_input = 'react-select-4-input'
    submit_button = 'submit'
    confirmation_msg = 'example-modal-sizes-title-lg'
    close_cm_button = 'closeLargeModal'

    # What action I can do on this page - Methods

    def enter_first_name(self, first_name):
        self.enter_text_by_id(self.fn_input, first_name)

    def enter_last_name(self, last_name):
        self.enter_text_by_id(self.ln_input, last_name)

    def enter_email(self, email):
        self.enter_text_by_id(self.email_input, email)

    def select_gender(self, gender: str):
        if gender.lower() == 'male':
            self.click_element_by_xpath(self.gender_male_xpath)
        elif gender.lower() == 'female':
            self.click_element_by_xpath(self.gender_female_xpath)
        elif gender.lower() == 'other':
            self.click_element_by_xpath(self.gender_other_xpath)
        else:
            log.error("Incorrect option was given!!. No gender selected")

    def enter_mobile_number(self, mobile_number):
        self.enter_text_by_id(self.mobile_number_input, mobile_number)

    def select_hobbies(self, hobbies: list):
        for hobby in hobbies:
            if hobby.lower() == 'sports':
                self.click_element_by_xpath(self.hobbies_sp_xpath)
            elif hobby.lower() == 'reading':
                self.click_element_by_xpath(self.hobbies_reading_xpath)
            elif hobby.lower() == 'music':
                self.click_element_by_xpath(self.hobbies_music_xpath)
            else:
                log.error("Incorrect option was given!!. No hobbies selected")

    def enter_current_address(self, address):
        self.enter_text_by_id(self.address_textarea, address)

    def select_state_city(self, state, city):
        # check is City list is enabled.
        log.info('is City list is enabled before selecting state?',
                 self.driver.find_element(By.ID, self.city_list).is_selected())
        log.info('is State list is enabled before selecting state?',
                 self.driver.find_element(By.ID, self.state_list).is_selected())
        # select state=NCR
        self.enter_text_by_id(self.state_input, (city + Keys.TAB))
        log.info("state is entered.")
        time.sleep(2)
        # check is City list is enabled.
        log.info('is City list enabled after selecting state?',
                 self.driver.find_element(By.ID, self.city_list).is_enabled())
        # select city=Delhi
        self.enter_text_by_id(self.city_input, ('Delhi' + Keys.TAB))
        log.info('city is entered.')

    def click_submit(self):
        self.click_element_by_id(self.submit_button)

    def close_confirmation_page(self):
        # verify the message='Thanks for submitting the form'
        log.info("Is Confirmation message displayed?",
                 self.driver.find_element(By.ID, self.confirmation_msg).is_displayed())
        # close the confirmation window
        self.click_element_by_id(self.close_cm_button)
