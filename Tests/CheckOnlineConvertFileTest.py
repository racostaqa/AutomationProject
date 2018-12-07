__author__ = 'Ricardo'

from Pages.OnlineConvertPage import OnlineConvertPage
from General.EnvironmentSetUp import EnvironmentSetUp
from General.Locators import Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Data.Data import Data
from time import sleep
import unittest


class CheckOnlineConvertFileTest(EnvironmentSetUp):

    def test_convert_file(self):
        driver = self.driver
        self.driver.get(Data.ONLINE_CONVERT_WEB_PAGE)
        self.driver.set_page_load_timeout(20)
        # calling OnlineConvert page
        online_convert_page = OnlineConvertPage(driver)
        self.assertTrue(online_convert_page.get_logo().is_displayed())
        print("Online Convert page is displayed")

        # entering data to search bar
        online_convert_page.send_keys_file_input_btn(Data.MP3_FILE_LOCATION)
        sleep(8)

        # clicking on Convert button
        online_convert_page.submit_convert_btn()
        sleep(15)
        print("Convert process started")

        # waiting for Success element to be present
        success_web_element = WebDriverWait(driver, 20).until(
            ec.presence_of_element_located((By.XPATH, Locators.online_convert_success_txt)))
        online_convert_page.set_success_message(success_web_element)
        sleep(15)

        # verifying Conversion Successful
        self.assertTrue(online_convert_page.get_success_message().is_displayed())
        print("Conversion process successful")


if __name__ == '__main__':
    unittest.main()
