__author__ = 'Ricardo'

from Data.Data import Data
from Pages.TestingSoftwareHomePage import TestingSoftwareHomePage
from Pages.TestingSoftwareSearchResultPage import TestingSoftwareSearchResultPage
from General.EnvironmentSetUp import EnvironmentSetUp
from time import sleep
import unittest


class CheckTestingSoftwareSearchBarTest(EnvironmentSetUp):

    def test_search_bar(self):
        driver = self.driver
        self.driver.get(Data.TESTING_SOFTWARE_ADDRESS)
        self.driver.set_page_load_timeout(20)

        # calling Testing Software home page
        testing_software_home_page = TestingSoftwareHomePage(driver)
        self.assertTrue(testing_software_home_page.get_search_btn().is_displayed())
        print("TS home page is displayed")

        # clicking on search icon
        testing_software_home_page.click_search()

        # verifying search bar is shown
        self.assertTrue(testing_software_home_page.get_search_tbx().is_displayed())
        print("TS search text field is displayed")

        # entering text to search bar
        testing_software_home_page.set_search_tbx(Data.TS_SEARCH_TEXT)

        # capturing "enter" key event
        testing_software_home_page.set_enter_search_tbx()
        sleep(5)

        # verifying search result
        testing_software_search_result_page = TestingSoftwareSearchResultPage(driver)
        self.assertTrue(testing_software_search_result_page.get_search_result().is_displayed())
        print("TS search process completed successfully.")


if __name__ == '__main__':
    unittest.main()
