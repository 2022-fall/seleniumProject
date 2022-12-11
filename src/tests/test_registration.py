import pytest
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *

from src.pages.forms_page import FormsPage
from src.utilities import *

filepath1 = ROOT_DIR + '/data/forms.yml'
data = load_yaml_file(filepath1)


@pytest.mark.forms1
def test_forms_case1(driver):
    # Input DATA:
    first_name = data['case1']['first_name']
    last_name = data['case1']['last_name']
    email = data['case1']['email']
    HOST = data['case1']['host']

    # Page objects:
    form_page = FormsPage(driver)

    # Steps:
    driver.get(HOST)
    # let all ads load
    time.sleep(5)
    # after loading all ads this step will go through all of them and disable
    disable_google_ads(driver)

    print("Starting test with various properties and methods for WebElement class.")
    # driver.execute_script("document.body.style.zoom='0.9'")

    form_page.enter_first_name('Delete me Please')
    time.sleep(5)
    form_page.enter_first_name(first_name)
    time.sleep(5)
    form_page.enter_last_name(last_name)
    form_page.enter_email(email)
    form_page.enter_mobile_number('9876543210')
    form_page.select_gender('male')
    # (optional) enter date_of_birth = '27 Nov 2000'
    # (optional) enter subjects = 'selenium forms testing'

    # select checkboxes, select Sports, Reading
    form_page.select_hobbies(['sports', 'reading'])
    # (optional) upload picture
    # enter message in text_area = '2906 Shell Road, 12224'
    form_page.enter_current_address('2906 Shell Road, 12224')
    form_page.select_state_city('NCR', 'Delhi')

    # # check if Male gender is selected
    # print('is Male gender radio button selected?', driver.find_element(By.XPATH, gender_male_xpath).is_enabled())
    # # check if Sports Hobbies is selected
    # print('is Sports selected from Hobbies?', driver.find_element(By.XPATH, hobbies_sp_xpath).is_selected())

    print("all information was entered and submitted...")
    time.sleep(2)
    form_page.click_submit()
    time.sleep(5)
    print("Test Successfully executed.")
