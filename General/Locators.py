__author__ = 'Ricardo Acosta'


class Locators(object):

    # ------------------- XPATHS ----------------------------

    # Google Home page locator
    google_search_tbx = "//input[@name='q' and @type='text']"
    google_search_btn = "//input[@name='btnK' and @type='submit']"

    # Google Search page locator
    testing_software_result = "//div[@class='r']/a[@href='http://www.testingsoft.com/']"

    # Testing Software Home page locator
    ts_search_btn = "//div[@id='et_top_search']"
    ts_search_tbx = "//input[@type='search']"
    ts_what_is_ts_dropdown = "//nav//a[contains(string(), 'What is TS')]"
    ts_services_dropdown = "//nav//a[contains(string(), 'Services')]"
    ts_home_logo = "//img[@id='logo']"

    # Testing Software Search page locator
    ts_search_result = "//a[contains(string(), 'Automation')]"

    # Testing Software Services page locator
    ts_services = "//span[@id='Services']"

    # -------------------- CSS SELECTORS --------------------------

    # Google Drive page locator
    google_go_to_drive_btn = ".maia-button.button-download.mobile-is-hidden.get-started.go-to-drive"
    google_main_text = "//h1[contains(string(), 'Todos tus archivos')]"

    # Google Accounts page
    google_access_text = "//h1[contains(string(), 'Acceder')]"
    google_account_email = "#identifierId"
    google_next_btn = "//span[contains(string(), 'Siguiente')]"
    google_account_password = "//input[@type='password']"
    google_account_show_password_btn = "//span[@class='nK6IJ iStiSd']"
    # google_account_password = "input[type='password']"

    # Online Convert Page
    online_convert_input_file = "#fileUploadInput"
    online_convert_logo = "img[alt='Online-Convert.com']"
    online_convert_submit_btn = "#multifile-submit-button-main"
    online_convert_success_txt = "//h2[contains(string(), 'finalizada')]"

