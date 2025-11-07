import inspect
import os
import re
import time
from selenium.webdriver.common.by import By

import config
from methods_required_during_testing import (
    d,
    login,
    set_secret_url_with_login,
    change_secret_url_expiration_date,
    change_secret_url_expiration_date_with_login,
    search_and_display_target_item,
    click_file_information_button,
    click_secret_url_btn
)

# pytest shell_test/test_secret_url_changing_deadline.py::TestPreparation
class TestPreparation:
    """Prepare for tests(No.99, 100, 101, 102)"""
    # pytest shell_test/test_secret_url_changing_deadline.py::TestPreparation::test_no_99
    def test_no_99(self, driver):
        """Prepare for test No.99
        
        Secret URL is enabled
        Expiration Date is 3 and switch to 5 after email is sent
        Download Limit is 3
        Access Setting is Open Date and publish date is after today
        User's Role is Repository Administrator
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # enable secret url and set expiration date to 3
        set_secret_url_with_login(driver, True)
        change_secret_url_expiration_date_with_login(driver, 3)

        # log in as Repository Administrator
        login_as_target(driver, 'Repository')

        # search target item
        search_and_display_target_item(driver, config.item_name_dic['before_publish'])

        # display content's info
        click_file_information_button(driver)

        # click secret url button
        click_secret_url_btn(driver)

        # get secret url from email and create a file to store it
        url = get_secret_url(config.users['Repository']['mail'].split('@', 1)[0])
        with open(config.base_secret_url_dir + 'secret_url_99.txt', 'w', encoding='utf-8') as f:
            f.write(url)

    # pytest shell_test/test_secret_url_changing_deadline.py::TestPreparation::test_no_100
    def test_no_100(self, driver):
        """Prepare for test No.100

        Secret URL is enabled
        Expiration Date is 3 and switch to 5 after email is sent
        Download Limit is 3
        Access Setting is Open Date and publish date is after today
        User's Role is Contributor and the item's owner

        Args:
            driver(WebDriver): WebDriver object
        """
        # enable secret url and set expiration date to 3
        set_secret_url_with_login(driver, True)
        change_secret_url_expiration_date_with_login(driver, 3)

        # log in as Contributor
        login_as_target(driver, 'RegCon')

        # search target item
        search_and_display_target_item(driver, config.item_name_dic['before_publish'])

        # display content's info
        click_file_information_button(driver)

        # click secret url button
        click_secret_url_btn(driver)

        # get secret url from email and create a file to store it
        url = get_secret_url(config.users['RegCon']['mail'].split('@', 1)[0])
        with open(config.base_secret_url_dir + 'secret_url_100.txt', 'w', encoding='utf-8') as f:
            f.write(url)

    # pytest shell_test/test_secret_url_changing_deadline.py::TestPreparation::test_no_101
    def test_no_101(self, driver):
        """Prepare for test No.101

        Secret URL is enabled
        Expiration Date is 3 and switch to 5 after email is sent
        Download Limit is 3
        Access Setting is Private
        User's Role is Repository Administrator

        Args:
            driver(WebDriver): WebDriver object
        """
        # enable secret url and set expiration date to 3
        set_secret_url_with_login(driver, True)
        change_secret_url_expiration_date_with_login(driver, 3)

        # log in as Repository Administrator
        login_as_target(driver, 'Repository')

        # search target item
        search_and_display_target_item(driver, config.item_name_dic['private'])

        # display content's info
        click_file_information_button(driver)

        # click secret url button
        click_secret_url_btn(driver)

        # get secret url from email and create a file to store it
        url = get_secret_url(config.users['Repository']['mail'].split('@', 1)[0])
        with open(config.base_secret_url_dir + 'secret_url_101.txt', 'w', encoding='utf-8') as f:
            f.write(url)

    # pytest shell_test/test_secret_url_changing_deadline.py::TestPreparation::test_no_102
    def test_no_102(self, driver):
        """Prepare for test No.102

        Secret URL is enabled
        Expiration Date is 3 and switch to 5 after email is sent
        Download Limit is 3
        Access Setting is Private
        User's Role is Contributor and the item's owner

        Args:
            driver(WebDriver): WebDriver object
        """
        # enable secret url and set expiration date to 3
        set_secret_url_with_login(driver, True)
        change_secret_url_expiration_date_with_login(driver, 3)

        # log in as Contributor
        login_as_target(driver, 'RegCon')

        # search target item
        search_and_display_target_item(driver, config.item_name_dic['private'])

        # display content's info
        click_file_information_button(driver)

        # click secret url button
        click_secret_url_btn(driver)

        # get secret url from email and create a file to store it
        url = get_secret_url(config.users['RegCon']['mail'].split('@', 1)[0])
        with open(config.base_secret_url_dir + 'secret_url_102.txt', 'w', encoding='utf-8') as f:
            f.write(url)

# pytest shell_test/test_secret_url_changing_deadline.py::test_change_expiration_date
def test_change_expiration_date(driver):
    """Change expiration date from 3 to 5 and check if the deadline is changed
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as System Administrator
    login_as_target(driver, 'System')

    # change expiration date from 3 to 5
    change_secret_url_expiration_date(driver, 5)

    # reload the page
    driver.refresh()

    # check if the deadline is changed
    assert driver.find_element(By.XPATH, '//*[@id="secret_expiration_date"]').get_attribute('value') == '5'

# pytest shell_test/test_secret_url_changing_deadline.py::TestExecution
class TestExecution:
    """Execute tests(No.99, 100, 101, 102)"""
    # pytest shell_test/test_secret_url_changing_deadline.py::TestExecution::test_no_99
    def test_no_99(self, driver):
        """Execute test No.99
        
        User's Role is Repository Administrator

        Args:
            driver(WebDriver): WebDriver object
        """
        # get secret url from file
        with open(config.base_secret_url_dir + 'secret_url_99.txt', 'r', encoding='utf-8') as f:
            url = f.read()

        # log in as Repository Administrator
        login_as_target(driver, 'Repository')

        # access secret url
        driver.get(url)
        time.sleep(1)

        # check download deadline passed error message
        check_download_deadline_passed_error_message(driver)

        # check if the file is downloaded
        file_list = os.listdir(config.base_download_dir)
        assert 'before_publish.txt' in file_list

        save_screenshot(driver, inspect.currentframe().f_code.co_name)

        os.remove(config.base_secret_url_dir + 'secret_url_99.txt')

    # pytest shell_test/test_secret_url_changing_deadline.py::TestExecution::test_no_100
    def test_no_100(self, driver):
        """Execute test No.100

        User's Role is Contributor and the item's owner

        Args:
            driver(WebDriver): WebDriver object
        """
        # get secret url from file
        with open(config.base_secret_url_dir + 'secret_url_100.txt', 'r', encoding='utf-8') as f:
            url = f.read()

        # log in as Contributor
        login_as_target(driver, 'RegCon')

        # access secret url
        driver.get(url)
        time.sleep(1)

        # check download deadline passed error message
        check_download_deadline_passed_error_message(driver)

        # check if the file is downloaded
        file_list = os.listdir(config.base_download_dir)
        assert 'before_publish.txt' in file_list

        save_screenshot(driver, inspect.currentframe().f_code.co_name)

        os.remove(config.base_secret_url_dir + 'secret_url_100.txt')

    # pytest shell_test/test_secret_url_changing_deadline.py::TestExecution::test_no_101
    def test_no_101(self, driver):
        """Execute test No.101
    
        User's Role is Repository Administrator

        Args:
            driver(WebDriver): WebDriver object
        """
        # get secret url from file
        with open(config.base_secret_url_dir + 'secret_url_101.txt', 'r', encoding='utf-8') as f:
            url = f.read()

        # log in as Repository Administrator
        login_as_target(driver, 'Repository')

        # access secret url
        driver.get(url)
        time.sleep(1)

        # check download deadline passed error message
        check_download_deadline_passed_error_message(driver)

        # check if the file is downloaded
        file_list = os.listdir(config.base_download_dir)
        assert 'private.txt' in file_list

        save_screenshot(driver, inspect.currentframe().f_code.co_name)

        os.remove(config.base_secret_url_dir + 'secret_url_101.txt')

    # pytest shell_test/test_secret_url_changing_deadline.py::TestExecution::test_no_102
    def test_no_102(self, driver):
        """Execute test No.102

        User's Role is Contributor and the item's owner

        Args:
            driver(WebDriver): WebDriver object
        """
        # get secret url from file
        with open(config.base_secret_url_dir + 'secret_url_102.txt', 'r', encoding='utf-8') as f:
            url = f.read()

        # log in as Contributor
        login_as_target(driver, 'RegCon')

        # access secret url
        driver.get(url)
        time.sleep(1)

        # check download deadline passed error message
        check_download_deadline_passed_error_message(driver)

        # check if the file is downloaded
        file_list = os.listdir(config.base_download_dir)
        assert 'private.txt' in file_list

        save_screenshot(driver, inspect.currentframe().f_code.co_name)

        os.remove(config.base_secret_url_dir + 'secret_url_102.txt')

def login_as_target(driver, target_key):
    """Log in as target user
    
    Args:
        driver(WebDriver): WebDriver object
        target_key(str): target user's key in config
    """
    # set login_user from config
    login_user = config.users[target_key]
    # log in as target user
    login(driver, login_user['mail'], login_user['password'])

def get_secret_url(user: str):
    """Get secret URL
    
    Args:
        user(str): user's role
        
    Returns:
        str: secret URL
    """
    mail_list = os.listdir('mail/' + user + '/new')

    with open('mail/' + user + '/new/' + mail_list[-1], 'r', encoding='utf-8') as f:
        text = f.read()
        url = re.search('https://.*', text).group()
        return url

def check_download_deadline_passed_error_message(driver):
    """Check if the error message for download deadline passed is displayed
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # check error page has the class what name is error-page
    error_page = driver.find_elements(By.CLASS_NAME, 'error-page')
    assert len(error_page) == 0, 'This page is error page'

def save_screenshot(driver, co_name):
    """Save screenshot
    
    Args:
        driver(WebDriver): WebDriver object
        co_name(str): test case name
    """
    time.sleep(1)
    driver.save_screenshot(
        config.base_save_folder + 'secret_url/' + d + "_" + co_name + ".png")
