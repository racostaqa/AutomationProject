__author__ = 'Ricardo'

from Data.Data import Data
from Pages.TestingSoftwareHomePage import TestingSoftwareHomePage
from Pages.TestingSoftwareServicesPage import TestingSoftwareServicesPage
from General.EnvironmentSetUp import EnvironmentSetUp
from time import sleep
import unittest


class CheckTestingSoftwareServicesDropdownTest(EnvironmentSetUp):

    def test_dropdown(self):
        driver = self.driver
        self.driver.get(Data.TESTING_SOFTWARE_ADDRESS)
        self.driver.set_page_load_timeout(20)

        # calling Testing Software home page
        testing_software_home_page = TestingSoftwareHomePage(driver)
        self.assertTrue(testing_software_home_page.get_what_is_it_dropdown().is_displayed())
        print("Testing Software home page is displayed")

        # clicking on "What is it" dropdown
        testing_software_home_page.click_what_is_it_dropdown()

        # verifying "Services" option is shown
        self.assertTrue(testing_software_home_page.get_services_dropdown().is_displayed())
        print("Services option is displayed.")

        # clicking on "Services" option
        testing_software_home_page.click_services_dropdown()
        sleep(4)

        # verifying "Services" page is shown
        testing_software_services_page = TestingSoftwareServicesPage(driver)
        self.assertTrue(testing_software_services_page.get_services().is_displayed())
        print("Check dropdown test completed successfully.")


if __name__ == '__main__':
    unittest.main()
