import time

from selenium.webdriver.common.by import By

import logging


def disable_google_ads(driver):
    google_ads_iframe_xpath = "//iframe[contains(@id, 'google_ads_iframe_')]"

    all_iframes = driver.find_elements(By.XPATH, google_ads_iframe_xpath)
    if len(all_iframes) > 0:
        print("Ad Found\n")
        driver.execute_script("""
            var elems = document.getElementsByTagName("iframe"); 
            for(var i = 0, max = elems.length; i < max; i++)
                 {
                     elems[i].hidden=true;
                 }
                              """)
        print('Total Ads: ' + str(len(all_iframes)))
    else:
        print('No frames found')


def create_logger(file):
    logging.basicConfig(filename=file,
                        level=logging.INFO,
                        format='%(asctime)-15s [%(levelname)s]: %(message)s',
                        filemode='a')
    return logging.getLogger()


def get_str_day():
    return time.strftime("%Y%m%d")


def get_str_day_min_sec():
    return time.strftime("%Y%m%d %H%M%S")
