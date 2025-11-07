import inspect
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import config
from methods_required_during_testing import (
    d,
    login,
    logout,
    change_usage_report_workflow_access,
    click_quit_btn,
    search_and_display_target_item,
    enter_guest_email_for_get_usage_application,
    enter_guest_email_after_approval
)

# pytest shell_test/test_admin_usage_report.py::TestPreparation
class TestPreparation:
    """Prepare for tests(No.10, 11) and Execute test No.9"""
    # pytest shell_test/test_admin_usage_report.py::TestPreparation::test_no_10
    def test_no_10(self, driver):
        """Prepare for test No.10

        User's Role is System Administrator
        Expiration date is 5

        Args:
            driver(WebDriver): Webdriver object
        """
        # log in as System Administrator
        login_as_target(driver, 'System')

        # set expiration date to 5
        change_usage_report_workflow_access(driver, 5)

        # log out
        logout(driver)

        # access to test_scenario_4 and download a file to create a usage report
        create_usage_report(driver, 'scenario_4')

        # get access url from mail and create a file to store it
        lines = get_latest_mail_body(config.guest_mail.split('@', 1)[0])
        url = [line for line in lines if line.startswith('https://')][0]
        with open(config.base_secret_url_dir + 'admin_10.txt', 'w', encoding='utf-8') as f:
            f.write(url)

        # delete download file
        os.remove(config.base_download_dir + 'test_scenario_4.txt')

    # pytest shell_test/test_admin_usage_report.py::TestPreparation::test_no_9
    def test_no_9(self, driver):
        """No.9 The change of expilation date must be adapted

        Log in User's role is System Administrator

        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as System Administrator
        login_as_target(driver, 'System')

        # change expiration date
        change_usage_report_workflow_access(driver, 3)

        # refresh and check if the change is successful
        driver.refresh()
        time.sleep(1)

        target = driver.find_element(By.XPATH, '//*[@id="expiration_date_access"]')
        assert target.get_attribute('value') == '3'

        location = driver.find_element(By.XPATH, '//*[@id="download_limit"]').location
        driver.execute_script('window.scrollTo(0, ' + str(location['y']) + ')')

        save_screenshot(driver, inspect.currentframe().f_code.co_name)

    # pytest shell_test/test_admin_usage_report.py::TestPreparation::test_no_11
    def test_no_11(self, driver):
        """Prepare for test No.11

        User's Role is System Administrator
        Expiration date is 3
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # access to test_scenario_6 and download a file to create a usage report
        create_usage_report(driver, 'scenario_6')

        # get access url from mail and create a file to store it
        lines = get_latest_mail_body(config.guest_mail.split('@', 1)[0])
        url = [line for line in lines if line.startswith('https://')][0]
        with open(config.base_secret_url_dir + 'admin_11.txt', 'w', encoding='utf-8') as f:
            f.write(url)

        # delete download file
        os.remove(config.base_download_dir + 'test_scenario_6.txt')

# pytest shell_test/test_admin_usage_report.py::TestExecution
class TestExecution:
    """Execute tests(No.10, 11)"""
    # pytest shell_test/test_admin_usage_report.py::TestExecution::test_no_10
    def test_no_10(self, driver):
        """Execute test No.10
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # get access url from file
        with open(config.base_secret_url_dir + 'admin_10.txt', 'r', encoding='utf-8') as f:
            url = f.read()

        # access usage report
        driver.get(url)
        time.sleep(3)

        # check that not displaying the error page
        check_error_page(driver, False)

        save_screenshot(driver, inspect.currentframe().f_code.co_name)

        os.remove(config.base_secret_url_dir + 'admin_10.txt')

        driver.get(url)
        time.sleep(3)
        click_quit_btn(driver)
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="btn_cancel"]').click()
        time.sleep(3)

    # pytest shell_test/test_admin_usage_report.py::TestExecution::test_no_11
    def test_no_11(self, driver):
        """Execute test No.11
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # get access url from file
        with open(config.base_secret_url_dir + 'admin_11.txt', 'r', encoding='utf-8') as f:
            url = f.read()

        # access usage report
        driver.get(url)
        time.sleep(3)

        # check that displaying the error page
        check_error_page(driver, True)

        save_screenshot(driver, inspect.currentframe().f_code.co_name)

        os.remove(config.base_secret_url_dir + 'admin_11.txt')

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

def create_usage_report(driver, target_key):
    """Create a usage report
    
    Args:
        driver(WebDriver): WebDriver object
        target_key(str): target user's key in config
    """
    # access to test_scenario_4's item
    search_and_display_target_item(driver, config.item_name_dic[target_key])

    # create and transiton to the usage registration workflow
    driver.find_element(By.XPATH, '//*[@id="detail-item"]/table/tbody/tr/td[3]/a[1]/button').click()
    time.sleep(1)
    modal = driver.find_element(By.CLASS_NAME, 'modal.fade.in')
    modal_id = modal.get_attribute('id')
    next_id = modal_id.replace('term_and_condtion_modal', 'term_next')
    next_btn = modal.find_element(By.XPATH, './/*[@id="' + next_id + '"]')
    check_id = modal_id.replace('term_and_condtion_modal', 'term_checked')
    check_box = modal.find_element(By.XPATH, './/*[@id="' + check_id + '"]')
    check_box.click()
    time.sleep(1)
    next_btn.click()
    time.sleep(1)
    enter_guest_email_for_get_usage_application(driver, config.guest_mail)
    lines = get_latest_mail_body(config.guest_mail.split('@', 1)[0])
    url = [line for line in lines if line.startswith('https://')][0]
    driver.get(url)
    WebDriverWait(driver, 10).until(
        lambda d: len(d.find_elements(By.CLASS_NAME, 'next-button')) > 0,
        'Usage report workflow page loading timeout'
    )

    # complete the workflow and download the file to create a usage report
    driver.find_element(By.CLASS_NAME, 'next-button').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="btn-finish"]').click()
    time.sleep(3)
    # scenario_6 is the item for usage application, so it is necessary to approve it
    if target_key == 'scenario_6':
        activity_id = driver.find_element(By.XPATH, '//*[@id="activity_id"]').text
        login_as_target(driver, 'Repository')
        driver.get(config.base_url + '/workflow/activity/detail/' + activity_id)
        time.sleep(5)
        driver.find_element(By.XPATH, '//*[@id="btn-approval"]').click()
        time.sleep(3)
        logout(driver)
    lines = get_latest_mail_body(config.guest_mail.split('@', 1)[0])
    url = [line for line in lines if line.startswith('https://')][0]
    driver.get(url)
    time.sleep(3)
    enter_guest_email_after_approval(driver, config.guest_mail)
    time.sleep(3)

def get_latest_mail_body(user_name: str):
    """Get the latest mail body
    
    Args:
        user_name(str): user name
    """
    mail_list = os.listdir('mail/' + user_name + '/new')
    with open('mail/' + user_name + '/new/' + mail_list[-1], 'r', encoding='utf-8') as f:
        return f.read().splitlines()

def check_error_page(driver, is_displayed):
    """Check if the error page is displayed
    
    Args:
        driver(WebDriver): WebDriver object
        is_displayed(bool): whether the error page is displayed
    """
    error_page = driver.find_elements(By.CLASS_NAME, 'error-page')
    if is_displayed:
        # check error page has the class what name is error-page
        assert len(error_page) > 0, 'This page is not error page'

        # check error message
        error_message = error_page[0].find_element(By.XPATH, './/div/div/h1')
        assert error_message.text == 'The specified link has expired.',\
            'Error message is not "The specified link has expired."'
    else:
        # check error page has not the class what name is error-page
        assert len(error_page) == 0, 'This page is error page'

def save_screenshot(driver, co_name):
    """Save screenshot
    
    Args:
        driver(WebDriver): WebDriver object
        co_name(str): test case name
    """
    time.sleep(1)
    driver.save_screenshot(
        config.base_save_folder + 'admin/' + d + "_" + co_name + ".png")
