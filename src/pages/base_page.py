from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.utilities import *

logfile = f'{ROOT_DIR}/logs/{get_str_day()}.log'
log = create_logger(logfile)


class BasePage:
    """
    - abstract model (python class that includes common functions for selenium, )
    - 'page': python class that represents the attributes and methods that can be defined from the certain web page
    - other pages will inherit base_page, hence they will share the common webdriver (browser), base page shares the browser
    - in base page will contain a lof of wrapper functions
    """

    def __init__(self, driver):
        self.driver = driver
        self.wdwait = WebDriverWait(self.driver, 10)

    # METHOD: create common selenium functions
    # enter_text_by_id(id, text)
    # click_element_by_id(id)
    # click_element_by_xpath(id)
    # select_from_drop_down_by_id()
    # get_text_by_id() -> returns string text
    # and many more, but create whenever you need them in few places

    def enter_text_by_id(self, id, text):
        """Geneal function to enter any text to any element found by id."""
        try:
            log.info("entering the text by id ..")
            # element = self.driver.find_element(By.ID, id)
            element = self.wdwait.until(EC.presence_of_element_located((By.ID, id)))
            element.clear()
            element.send_keys(text)
            log.info(f"{text} is entered.")
        except (NoSuchElementException, TimeoutException) as err:
            time.sleep(1)
            log.error(f"Selenium Exception: test failed with following exception.\n{err}")

    def click_element_by_id(self, id):
        """Geneal function to click on any element found by id."""
        try:
            log.info("clicking the text by id ..")

            # element = self.driver.find_element(By.ID, id)
            element = self.wdwait.until(EC.element_to_be_clickable((By.ID, id)))

            # below step is optional, it is to scroll to the element, but we dont have scroll bar on the website, it wont work
            # but this is good case to show that we can execute javascript with Selenium commands
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            # self.driver.execute_script("arguments[0].click();", element)
            element.click()
            log.info(f"element is clicked.", id)
        except (NoSuchElementException, TimeoutException) as err:
            time.sleep(1)
            log.error(f"Selenium Exception: test failed with following exception.\n{err}")

    def click_element_by_xpath(self, xpath):
        """Geneal function to click on any element found by xpath."""
        try:
            log.info("clicking the text by id ..")
            # element = self.driver.find_element(By.ID, id)
            element = self.wdwait.until(EC.presence_of_element_located((By.XPATH, xpath)))
            element.click()
            log.info(f"element is clicked.", xpath)
        except (NoSuchElementException, TimeoutException) as err:
            time.sleep(1)
            log.error(f"Selenium Exception: test failed with following exception.\n{err}")

    def get_text_by_id(self, id):
        """Geneal function to get text from any element found by id."""
        try:
            log.info("getting the text by id ..")
            # element = self.driver.find_element(By.ID, id)
            element = self.wdwait.until(EC.presence_of_element_located((By.ID, id)))
            result = element.text
            log.info(f"returning the text.{result}")
            return result
        except (NoSuchElementException, TimeoutException) as err:
            time.sleep(1)
            log.error(f"Selenium Exception: test failed with following exception.\n{err}")
