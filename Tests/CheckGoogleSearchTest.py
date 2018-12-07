__author__ = 'Ricardo'

from Pages.GoogleHomePage import GoogleHomePage
from Pages.GoogleSearchResultPage import GoogleSearchResultPage
from Pages.TestingSoftwareHomePage import TestingSoftwareHomePage
from General.EnvironmentSetUp import EnvironmentSetUp
from Data.Data import Data
from time import sleep
import unittest


class CheckGoogleSearchTest(EnvironmentSetUp):

    def test_google_search(self):
        driver = self.driver
        self.driver.get(Data.GOOGLE_WEB_ADDRESS)
        self.driver.set_page_load_timeout(20)

        # calling Google home page
        google_home_page = GoogleHomePage(driver)
        self.assertTrue(google_home_page.get_search_tbx().is_displayed())
        print("Search page is displayed")

        # entering data to search bar
        google_home_page.set_search_tbx(Data.GOOGLE_SEARCH_TEXT)

        # clicking on search button
        google_home_page.submit_search()
        sleep(3)
        print("Search process successful")
        google_search_result_page = GoogleSearchResultPage(driver)

        # verifying Testing Software result is shown
        self.assertTrue(google_search_result_page.get_testing_software_result().is_displayed())
        print("Testing Software result is displayed")

        # clicking on Testing Software result
        google_search_result_page.click_testing_software_result()
        sleep(5)

        # verifying Testing Software web page is shown
        testing_software_home_page = TestingSoftwareHomePage(driver)
        self.assertTrue(testing_software_home_page.get_home_logo().is_displayed())
        print("Test completed")


if __name__ == '__main__':
    unittest.main()
