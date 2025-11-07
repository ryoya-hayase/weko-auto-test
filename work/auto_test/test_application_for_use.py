import datetime
import inspect
import os
import shutil
import subprocess
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

import config
from methods_required_during_testing import (
    d,
    login,
    logout,
    search_and_display_target_item,
    click_detail_item_button,
    click_print_btn,
    click_quit_btn,
    enter_guest_email_for_get_usage_application,
    enter_guest_email_after_approval,
    click_approval_btn,
    click_reject_btn,
)

# pytest auto_test/test_application_for_use.py::TestScenario1
class TestScenario1:
    """Test Scenario 1
    
    Requirements for items to be used:
        - The Providing Method is terms_of_use_only
        - The Providing Role is General
        - The Terms and Conditions are voluntary
    """
    # pytest auto_test/test_application_for_use.py::TestScenario1::test_scenario_1_1
    def test_scenario_1_1(self, driver):
        """Test Scenario 1-1
        
        1. The Download button appears.
        2. Registered content is downloaded.
        3. No "Request for register Data Usage Report" email is sent to the applicant.
        
        User's role is Contributor and the item's owner

        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as Contributor
        login_as_target(driver, 'RegCon')

        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_1'])

        # 1. The Download button appears.
        assert check_item_button(driver, True)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. Registered content is downloaded.
        click_detail_item_button(driver)
        time.sleep(1)
        file_list = os.listdir(config.base_download_dir)
        assert 'test_scenario_1.txt' in file_list

        # 3. No "Request for register Data Usage Report" email is sent to the applicant.
        assert not check_request_for_register_mail(
            config.users['RegCon']['mail'],
            config.item_name_dic['scenario_1'])

        # move downloaded file to do other tests
        move_downloaded_files(['test_scenario_1.txt'], inspect.currentframe().f_code.co_name)

    # pytest auto_test/test_application_for_use.py::TestScenario1::test_scenario_1_2
    def test_scenario_1_2(self, driver):
        """Test Scenario 1-2
        
        1. The Apply button appears.
        2. The error message appears.
        
        User's role is Contributor and not the item's owner
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as Contributor
        login_as_target(driver, 'NoRegCon')

        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_1'])

        # 1. The Apply button appears.
        assert check_item_button(driver, False)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. The error message appears.
        click_detail_item_button(driver)
        time.sleep(1)
        assert check_error_page(driver)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '2')

    # pytest auto_test/test_application_for_use.py::TestScenario1::test_scenario_1_3
    def test_scenario_1_3(self, driver):
        """Test Scenario 1-3
        
        1. The Download button appears.
        2. Registered content is downloaded.
        3. No "Request for register Data Usage Report" email is sent to the applicant.
        
        User's role is Contributor and the item's contributor
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as Contributor
        login_as_target(driver, 'PrxRegCon')

        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_1'])

        # 1. The Download button appears.
        assert check_item_button(driver, True)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. Registered content is downloaded.
        click_detail_item_button(driver)
        time.sleep(1)
        file_list = os.listdir(config.base_download_dir)
        assert 'test_scenario_1.txt' in file_list

        # 3. No "Request for register Data Usage Report" email is sent to the applicant.
        assert not check_request_for_register_mail(
            config.users['PrxRegCon']['mail'],
            config.item_name_dic['scenario_1'])

        # move downloaded file to do other tests
        move_downloaded_files(['test_scenario_1.txt'], inspect.currentframe().f_code.co_name)

    # pytest auto_test/test_application_for_use.py::TestScenario1::test_scenario_1_4
    def test_scenario_1_4(self, driver):
        """Test Scenario 1-4
        
        1. The Apply button appears.
        2. The error message appears.
        
        User's role is Community Administrator
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as Community Administrator
        login_as_target(driver, 'Community')

        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_1'])

        # 1. The Apply button appears.
        assert check_item_button(driver, False)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. The error message appears.
        click_detail_item_button(driver)
        time.sleep(1)
        assert check_error_page(driver)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '2')

    # pytest auto_test/test_application_for_use.py::TestScenario1::test_scenario_1_5_1_to_3
    def test_scenario_1_5_1_to_3(self, driver):
        """Test Scenario 1-5-1, 1-5-2, 1-5-3
        
        1. The Apply button appears.
        2. The Terms and Conditions modal appears.
        3. The print dialog appears.

        User's role is General

        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as General
        login_as_target(driver, 'General')

        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_1'])

        # 1. The Apply button appears.
        assert check_item_button(driver, False)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. The Terms and Conditions modal appears.
        click_detail_item_button(driver)
        time.sleep(1)
        assert check_terms_and_conditions_modal(driver, '利用規約のみ\nGeneral')
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '2')

        # 3. The print dialog appears.
        click_print_btn(driver)
        time.sleep(1)
        window_handles = driver.window_handles
        # after print button clicked, window handles increase
        assert len(window_handles) == 2
        driver.switch_to.window(window_handles[1])
        time.sleep(3)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '3')
        driver.switch_to.window(window_handles[0])
        time.sleep(1)

    # pytest auto_test/test_application_for_use.py::TestScenario1::test_scenario_1_5_4
    def test_scenario_1_5_4(self, driver):
        """Test Scenario 1-5-4
        
        1. The Apply button appears.
        2. The Terms and Conditions modal appears.
        4. Not working before checking the box.
        
        User's role is General
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as General
        login_as_target(driver, 'General')

        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_1'])

        # 1. The Apply button appears.
        # 2. The Terms and Conditions modal appears.
        click_detail_item_button(driver)
        time.sleep(1)

        # 4. Not working before checking the box.
        modal = driver.find_element(By.CLASS_NAME, 'modal.fade.in')
        modal_id = modal.get_attribute('id')
        next_id = modal_id.replace('term_and_condtion_modal', 'term_next')
        next_btn = modal.find_element(By.XPATH, './/*[@id="' + next_id + '"]')
        next_btn.click()
        time.sleep(1)
        file_list = os.listdir(config.base_download_dir)
        assert not 'test_scenario_1.txt' in file_list

    # pytest auto_test/test_application_for_use.py::TestScenario1::test_scenario_1_5_5_and_6
    def test_scenario_1_5_5_and_6(self, driver):
        """Test Scenario 1-5-5, 1-5-6
        
        1. The Apply button appears.
        2. The Terms and Conditions modal appears.
        5. Registered content is downloaded.
        6. No "Request for register Data Usage Report" email is sent to the applicant.
        
        User's role is General
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as General
        login_as_target(driver, 'General')

        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_1'])

        # 1. The Apply button appears.
        # 2. The Terms and Conditions modal appears.
        click_detail_item_button(driver)
        time.sleep(1)

        # 5. Registered content is downloaded.
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
        file_list = os.listdir(config.base_download_dir)
        assert 'test_scenario_1.txt' in file_list

        # 6. No "Request for register Data Usage Report" email is sent to the applicant.
        assert not check_request_for_register_mail(
            config.users['General']['mail'],
            config.item_name_dic['scenario_1'])

        # move downloaded file to do other tests
        move_downloaded_files(['test_scenario_1.txt'], inspect.currentframe().f_code.co_name)

    # pytest auto_test/test_application_for_use.py::TestScenario1::test_scenario_1_6
    def test_scenario_1_6(self, driver):
        """Test Scenario 1-6
        
        1. The Apply button appears.
        2. The error message appears.
        
        User is not logged in
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_1'])

        # 1. The Apply button appears.
        assert check_item_button(driver, False)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. The error message appears.
        click_detail_item_button(driver)
        time.sleep(1)
        assert check_error_page(driver)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '2')

# pytest auto_test/test_application_for_use.py::TestScenario2
class TestScenario2:
    """Test Scenario 2
    
    Requirements for item to be used:
        - The Providing Method is terms_of_use_only
        - The Providing Role is Guest
        - The Terms and Conditions are voluntary
    """
    # pytest auto_test/test_application_for_use.py::TestScenario2::test_scenario_2_1
    def test_scenario_2_1(self, driver):
        """Test Scenario 2-1
        
        1. The Download button appears.
        2. Registered content is downloaded.
        3. No "Request for register Data Usage Report" email is sent to the applicant.
        
        User's role is Contributor and the item's owner
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as Contributor
        login_as_target(driver, 'RegCon')

        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_2'])

        # 1. The Download button appears.
        assert check_item_button(driver, True)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. Registered content is downloaded.
        click_detail_item_button(driver)
        time.sleep(1)
        file_list = os.listdir(config.base_download_dir)
        assert 'test_scenario_2.txt' in file_list

        # 3. No "Request for register Data Usage Report" email is sent to the applicant.
        assert not check_request_for_register_mail(
            config.users['RegCon']['mail'],
            config.item_name_dic['scenario_2'])

        # move downloaded file to do other tests
        move_downloaded_files(['test_scenario_2.txt'], inspect.currentframe().f_code.co_name)

    # pytest auto_test/test_application_for_use.py::TestScenario2::test_scenario_2_2
    def test_scenario_2_2(self, driver):
        """Test Scenario 2-2
        
        1. The Apply button appears.
        2. The error message appears.
        
        User's role is Contributor and not the item's owner
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as Contributor
        login_as_target(driver, 'NoRegCon')

        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_2'])

        # 1. The Apply button appears.
        assert check_item_button(driver, False)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. The error message appears.
        click_detail_item_button(driver)
        time.sleep(1)
        assert check_error_page(driver)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '2')

    # pytest auto_test/test_application_for_use.py::TestScenario2::test_scenario_2_3
    def test_scenario_2_3(self, driver):
        """Test Scenario 2-3
        
        1. The Download button appears.
        2. Registered content is downloaded.
        3. No "Request for register Data Usage Report" email is sent to the applicant.
        
        User's role is Contributor and the item's contributor
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as Contributor
        login_as_target(driver, 'PrxRegCon')

        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_2'])

        # 1. The Download button appears.
        assert check_item_button(driver, True)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. Registered content is downloaded.
        click_detail_item_button(driver)
        time.sleep(1)
        file_list = os.listdir(config.base_download_dir)
        assert 'test_scenario_2.txt' in file_list

        # 3. No "Request for register Data Usage Report" email is sent to the applicant.
        assert not check_request_for_register_mail(
            config.users['PrxRegCon']['mail'],
            config.item_name_dic['scenario_2'])

        # move downloaded file to do other tests
        move_downloaded_files(['test_scenario_2.txt'], inspect.currentframe().f_code.co_name)

    # pytest auto_test/test_application_for_use.py::TestScenario2::test_scenario_2_4
    def test_scenario_2_4(self, driver):
        """Test Scenario 2-4
        
        1. The Apply button appears.
        2. The error message appears.
        
        User's role is Community Administrator
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as Community Administrator
        login_as_target(driver, 'Community')

        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_2'])

        # 1. The Apply button appears.
        assert check_item_button(driver, False)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. The error message appears.
        click_detail_item_button(driver)
        time.sleep(1)
        assert check_error_page(driver)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '2')

    # pytest auto_test/test_application_for_use.py::TestScenario2::test_scenario_2_5
    def test_scenario_2_5(self, driver):
        """Test Scenario 2-5
        
        1. The Apply button appears.
        2. The error message appears.
        
        User's role is General
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as General
        login_as_target(driver, 'General')

        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_2'])

        # 1. The Apply button appears.
        assert check_item_button(driver, False)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. The error message appears.
        click_detail_item_button(driver)
        time.sleep(1)
        assert check_error_page(driver)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '2')

    # pytest auto_test/test_application_for_use.py::TestScenario2::test_scenario_2_6_1_to_3
    def test_scenario_2_6_1_to_3(self, driver):
        """Test Scenario 2-6-1, 2-6-2, 2-6-3
        
        1. The Apply button appears.
        2. The Terms and Conditions modal appears.
        3. The print dialog appears.
        
        User is not logged in
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_2'])

        # 1. The Apply button appears.
        assert check_item_button(driver, False)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. The Terms and Conditions modal appears.
        click_detail_item_button(driver)
        time.sleep(1)
        assert check_terms_and_conditions_modal(driver, '利用規約のみ\nGuest')
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '2')

        # 3. The print dialog appears.
        click_print_btn(driver)
        time.sleep(1)
        window_handles = driver.window_handles
        # after print button clicked, window handles increase
        assert len(window_handles) == 2
        driver.switch_to.window(window_handles[1])
        time.sleep(1)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '3')
        driver.switch_to.window(window_handles[0])
        time.sleep(1)

    # pytest auto_test/test_application_for_use.py::TestScenario2::test_scenario_2_6_4
    def test_scenario_2_6_4(self, driver):
        """Test Scenario 2-6-4
        
        1. The Apply button appears.
        2. The Terms and Conditions modal appears.
        4. Not working before checking the box.
        
        User is not logged in
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_2'])

        # 1. The Apply button appears.
        # 2. The Terms and Conditions modal appears.
        click_detail_item_button(driver)
        time.sleep(1)

        # 4. Not working before checking the box.
        modal = driver.find_element(By.CLASS_NAME, 'modal.fade.in')
        modal_id = modal.get_attribute('id')
        next_id = modal_id.replace('term_and_condtion_modal', 'term_next')
        next_btn = modal.find_element(By.XPATH, './/*[@id="' + next_id + '"]')
        next_btn.click()
        time.sleep(1)
        file_list = os.listdir(config.base_download_dir)
        assert not 'test_scenario_2.txt' in file_list

    # pytest auto_test/test_application_for_use.py::TestScenario2::test_scenario_2_6_5_to_7
    def test_scenario_2_6_5_to_7(self, driver):
        """Test Scenario 2-6-5, 2-6-6, 2-6-7
        
        1. The Apply button appears.
        2. The Terms and Conditions modal appears.
        5. Registered content is downloaded.
        6. No "Request for register Data Usage Report" email is sent to the applicant.
        7. The error message appears on 11th download.
        
        User is not logged in
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_2'])

        # 1. The Apply button appears.
        # 2. The Terms and Conditions modal appears.
        click_detail_item_button(driver)
        time.sleep(1)

        # 5. Registered content is downloaded.
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
        file_list = os.listdir(config.base_download_dir)
        assert 'test_scenario_2.txt' in file_list

        # 6. No "Request for register Data Usage Report" email is sent to the applicant.
        assert not check_request_for_register_mail(
            config.users['General']['mail'],
            config.item_name_dic['scenario_2'])

        # 7. The error message appears on 11th download.
        for i in range(10):
            click_detail_item_button(driver)
            time.sleep(1)
            modal = driver.find_element(By.CLASS_NAME, 'modal.fade.in')
            modal_id = modal.get_attribute('id')
            next_id = modal_id.replace('term_and_condtion_modal', 'term_next')
            next_btn = modal.find_element(By.XPATH, './/*[@id="' + next_id + '"]')
            check_id = modal_id.replace('term_and_condtion_modal', 'term_checked')
            check_box = modal.find_element(By.XPATH, './/*[@id="' + check_id + '"]')
            if not check_box.is_selected():
                check_box.click()
                time.sleep(1)
            next_btn.click()
            time.sleep(1)
            if i < 9:
                file_list = os.listdir(config.base_download_dir)
                assert 'test_scenario_2 (' + str(i + 1) + ').txt' in file_list
            else:
                file_list = os.listdir(config.base_download_dir)
                assert 'test_scenario_2 (' + str(i + 1) + ').txt' not in file_list

        # move downloaded files to do other tests
        move_target_files = [file for file in file_list if file.startswith('test_scenario_2')]
        move_downloaded_files(move_target_files, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_application_for_use.py::TestScenario3
class TestScenario3:
    """Test Scenario 3
    
    Requirements for item to be used
        - The Providing Method is Usage Registration
        - The Providing Role is General
        - The Terms and Conditions are voluntary
    """
    # pytest auto_test/test_application_for_use.py::TestScenario3::test_scenario_3_1
    def test_scenario_3_1(self, driver):
        """Test Scenario 3-1
        
        1. The Download button appears.
        2. Registered content is downloaded.
        3. No "Request for register Data Usage Report" email is sent to the applicant.
        
        User's role is Contributor and the item's owner
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as Contributor
        login_as_target(driver, 'RegCon')

        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_3'])

        # 1. The Download button appears.
        assert check_item_button(driver, True)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. Registered content is downloaded.
        click_detail_item_button(driver)
        time.sleep(1)
        file_list = os.listdir(config.base_download_dir)
        assert 'test_scenario_3.txt' in file_list

        # 3. No "Request for register Data Usage Report" email is sent to the applicant.
        assert not check_request_for_register_mail(
            config.users['RegCon']['mail'],
            config.item_name_dic['scenario_3'])

        # move downloaded file to do other tests
        move_downloaded_files(['test_scenario_3.txt'], inspect.currentframe().f_code.co_name)

    # pytest auto_test/test_application_for_use.py::TestScenario3::test_scenario_3_2
    def test_scenario_3_2(self, driver):
        """Test Scenario 3-2
        
        1. The Apply button appears.
        2. The error message appears.
        
        User's role is Contributor and not the item's owner
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as Contributor
        login_as_target(driver, 'NoRegCon')

        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_3'])

        # 1. The Apply button appears.
        assert check_item_button(driver, False)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. The error message appears.
        click_detail_item_button(driver)
        time.sleep(1)
        assert check_error_page(driver)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '2')

    # pytest auto_test/test_application_for_use.py::TestScenario3::test_scenario_3_3
    def test_scenario_3_3(self, driver):
        """Test Scenario 3-3
        
        1. The Download button appears.
        2. Registered content is downloaded.
        3. No "Request for register Data Usage Report" email is sent to the applicant.
        
        User's role is Contributor and the item's contributor
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as Contributor
        login_as_target(driver, 'PrxRegCon')

        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_3'])

        # 1. The Download button appears.
        assert check_item_button(driver, True)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. Registered content is downloaded.
        click_detail_item_button(driver)
        time.sleep(1)
        file_list = os.listdir(config.base_download_dir)
        assert 'test_scenario_3.txt' in file_list

        # 3. No "Request for register Data Usage Report" email is sent to the applicant.
        assert not check_request_for_register_mail(
            config.users['PrxRegCon']['mail'],
            config.item_name_dic['scenario_3'])

        # move downloaded file to do other tests
        move_downloaded_files(['test_scenario_3.txt'], inspect.currentframe().f_code.co_name)

    # pytest auto_test/test_application_for_use.py::TestScenario3::test_scenario_3_4
    def test_scenario_3_4(self, driver):
        """Test Scenario 3-4
        
        1. The Apply button appears.
        2. The error message appears.
        
        User's role is Community Administrator
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as Community Administrator
        login_as_target(driver, 'Community')

        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_3'])

        # 1. The Apply button appears.
        assert check_item_button(driver, False)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. The error message appears.
        click_detail_item_button(driver)
        time.sleep(1)
        assert check_error_page(driver)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '2')

    # pytest auto_test/test_application_for_use.py::TestScenario3::test_scenario_3_5_1_to_3
    def test_scenario_3_5_1_to_3(self, driver):
        """Test Scenario 3-5-1, 3-5-2, 3-5-3
        
        1. The Apply button appears.
        2. The Terms and Conditions modal appears.
        3. The print dialog appears.
        
        User's role is General
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as General
        login_as_target(driver, 'General')

        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_3'])

        # 1. The Apply button appears.
        assert check_item_button(driver, False)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. The Terms and Conditions modal appears.
        click_detail_item_button(driver)
        time.sleep(1)
        assert check_terms_and_conditions_modal(driver, '利用登録\nGeneral')
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '2')

        # 3. The print dialog appears.
        click_print_btn(driver)
        time.sleep(1)
        window_handles = driver.window_handles
        # after print button clicked, window handles increase
        assert len(window_handles) == 2
        driver.switch_to.window(window_handles[1])
        time.sleep(3)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '3')
        driver.switch_to.window(window_handles[0])
        time.sleep(1)

    # pytest auto_test/test_application_for_use.py::TestScenario3::test_scenario_3_5_4
    def test_scenario_3_5_4(self, driver):
        """Test Scenario 3-5-4
        
        1. The Apply button appears.
        2. The Terms and Conditions modal appears.
        4. Not working before checking the box.
        
        User's role is General
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as General
        login_as_target(driver, 'General')

        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_3'])

        # 1. The Apply button appears.
        # 2. The Terms and Conditions modal appears.
        click_detail_item_button(driver)
        time.sleep(1)

        # 4. Not working before checking the box.
        modal = driver.find_element(By.CLASS_NAME, 'modal.fade.in')
        modal_id = modal.get_attribute('id')
        next_id = modal_id.replace('term_and_condtion_modal', 'term_next')
        next_btn = modal.find_element(By.XPATH, './/*[@id="' + next_id + '"]')
        next_btn.click()
        time.sleep(1)
        assert not driver.current_url.startswith(config.base_url + '/workflow/activity/detail')

    # pytest auto_test/test_application_for_use.py::TestScenario3::test_scenario_3_5_5_and_6_and_10_to_12
    def test_scenario_3_5_5_and_6_and_10_to_12(self, driver):
        """Test Scenario 3-5-5, 3-5-6, 3-5-10, 3-5-11, 3-5-12
        
        1. The Apply button appears.
        2. The Terms and Conditions modal appears.
        5. Transition to the usage registration workflow.
        6. An email with the landing URL attached is sent to the applicant.
        10. The Download button appears and the registered content is downloaded.
        11. "Request for register Data Usage Report" email is sent to the applicant.
        12. "Your Application was Received" email is sent to the applicant.
        
        User's role is General
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as General
        login_as_target(driver, 'General')

        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_3'])

        # 1. The Apply button appears.
        # 2. The Terms and Conditions modal appears.
        click_detail_item_button(driver)
        time.sleep(1)

        # 5. Transition to the usage registration workflow.
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
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '5')

        # 6. An email with the landing URL attached is sent to the applicant.
        driver.find_element(By.CLASS_NAME, 'next-button').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="btn-finish"]').click()
        WebDriverWait(driver, 10).until(
            lambda d: len(d.find_elements(
                By.XPATH, '//*[@id="myTabContent"]/div[2]/div[2]/button[2]')) > 0
        )
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '6')
        activity_id = driver.find_element(By.XPATH, '//*[@id="activity_id"]').text
        assert check_approved_application_mail(
            config.users['General']['mail'],
            config.item_name_dic['scenario_3'],
            activity_id)

        # 10. The Download button appears and the registered content is downloaded.
        lines = get_latest_mail_body(config.users['General']['mail'].split('@', 1)[0])
        url = [line for line in lines if line.startswith('https://')][0]
        driver.get(url)
        time.sleep(3)
        assert check_item_button(driver, True)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '10')
        click_detail_item_button(driver)
        time.sleep(1)
        file_list = os.listdir(config.base_download_dir)
        assert 'test_scenario_3.txt' in file_list

        # 11. "Request for register Data Usage Report" email is not sent to the applicant.
        assert not check_request_for_register_mail(
            config.users['General']['mail'],
            config.item_name_dic['scenario_3'])

        # 12. "Your Application was Received" email is sent to the applicant.
        driver.get(config.base_url + '/workflow/')
        time.sleep(1)
        table = driver.find_element(By.XPATH, '//*[@id="myTabContent"]/div[4]/div/div[1]/table')
        headers_text = [header.text for header in table.find_elements(By.TAG_NAME, 'th')]
        activity_id_idx = headers_text.index('Activity')
        workflow_idx = headers_text.index('WorkFlow')
        user_idx = headers_text.index('User')
        rows = table.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
        for row in rows:
            # the tag of the first of row's cell is 'th', so idx - 1 is correct
            rds = row.find_elements(By.TAG_NAME, 'td')
            if rds[workflow_idx - 1].text.startswith('利用報告')\
                and rds[user_idx - 1].text == config.users['General']['mail']:
                rds[activity_id_idx - 1].find_element(By.TAG_NAME, 'a').click()
                time.sleep(3)
                break
        driver.find_element(By.CLASS_NAME, 'next-button').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="btn-finish"]').click()
        time.sleep(3)
        activity_id = driver.find_element(By.XPATH, '//*[@id="activity_id"]').text
        assert check_received_application_mail(
            config.users['General']['mail'],
            config.item_name_dic['scenario_3'],
            activity_id)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '12')

        # cancel the workflow to do other tests
        logout(driver)
        login_as_target(driver, 'Repository')
        driver.get(config.base_url + '/workflow/activity/detail/' + activity_id)
        time.sleep(3)
        click_quit_btn(driver)
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="btn_cancel"]').click()
        time.sleep(3)

        # download the file 9 times to do other tests
        logout(driver)
        login_as_target(driver, 'General')
        driver.get(url)
        time.sleep(3)
        for _ in range(9):
            click_detail_item_button(driver)
            time.sleep(1)

        # move downloaded files to do other tests
        move_downloaded_files(['test_scenario_3.txt'], inspect.currentframe().f_code.co_name)
        file_list = os.listdir(config.base_download_dir)
        delete_target_files = [file for file in file_list if file.startswith('test_scenario_3')]
        for file in delete_target_files:
            os.remove(config.base_download_dir + file)

    # pytest auto_test/test_application_for_use.py::TestScenario3::test_scenario_3_5_7
    def test_scenario_3_5_7(self, driver):
        """Test Scenario 3-5-7
        
        1. The Apply button appears.
        2. The Terms and Conditions modal appears.
        5. Transition to the usage registration workflow.
        7. An email with the landing URL attached is sent to the applicant.

        User's role is General

        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as General
        login_as_target(driver, 'General')

        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_3'])

        # 1. The Apply button appears.
        # 2. The Terms and Conditions modal appears.
        click_detail_item_button(driver)
        time.sleep(1)

        # 5. Transition to the usage registration workflow.
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

        # 7. An email with the landing URL attached is sent to the applicant.
        activity_id = driver.find_element(By.XPATH, '//*[@id="activity_id"]').text
        driver.find_element(By.CLASS_NAME, 'back-button').click()
        time.sleep(3)
        table = driver.find_element(By.XPATH, '//*[@id="myTabContent"]/div[4]/div/div[1]/table')
        headers_text = [header.text for header in table.find_elements(By.TAG_NAME, 'th')]
        activity_id_idx = headers_text.index('Activity')
        rows = table.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
        for row in rows:
            # the tag of the first of row's cell is 'th', so idx - 1 is correct
            rds = row.find_elements(By.TAG_NAME, 'td')
            if rds[activity_id_idx - 1].text == activity_id:
                rds[activity_id_idx - 1].find_element(By.TAG_NAME, 'a').click()
                time.sleep(3)
                break
        driver.find_element(By.CLASS_NAME, 'next-button').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="btn-finish"]').click()
        WebDriverWait(driver, 10).until(
            lambda d: len(d.find_elements(
                By.XPATH, '//*[@id="myTabContent"]/div[2]/div[2]/button[2]')) > 0
        )
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '7')
        assert check_approved_application_mail(
            config.users['General']['mail'],
            config.item_name_dic['scenario_3'],
            activity_id)
        
        # download the file to do other tests
        search_and_display_target_item(driver, config.item_name_dic['scenario_3'])
        for _ in range(10):
            click_detail_item_button(driver)
            time.sleep(1)
        
        # delete the file to do other tests
        file_list = os.listdir(config.base_download_dir)
        delete_target_files = [file for file in file_list if file.startswith('test_scenario_3')]
        for file in delete_target_files:
            os.remove(config.base_download_dir + file)

    # pytest auto_test/test_application_for_use.py::TestScenario3::test_scenario_3_5_8
    def test_scenario_3_5_8(self, driver):
        """Test Scenario 3-5-8
        
        1. The Apply button appears.
        2. The Terms and Conditions modal appears.
        5. Transition to the usage registration workflow.
        8. Transition to the workflow with input retained.
        
        User's role is General
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as General
        login_as_target(driver, 'General')

        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_3'])

        # 1. The Apply button appears.
        # 2. The Terms and Conditions modal appears.
        click_detail_item_button(driver)
        time.sleep(1)

        # 5. Transition to the usage registration workflow.
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

        # 8. Transition to the workflow with input retained.
        # edit target is Research Title
        before_activity_id = driver.find_element(By.XPATH, '//*[@id="activity_id"]').text
        panel_toggles = driver.find_elements(By.CLASS_NAME, 'panel-toggle')
        for pt in panel_toggles:
            if pt.text == 'Research Title':
                research_title_location = pt.location
                driver.execute_script(
                    'window.scrollTo(0, ' + str(research_title_location['y'] - 100) + ')')
                pt.click()
                time.sleep(1)
                break
        research_title = 'test research'
        driver.find_element(By.XPATH, '//*[@id="subitem_restricted_access_research_title"]')\
            .send_keys(research_title)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '8_before')
        driver.find_elements(By.CLASS_NAME, 'save-button')[1].click()
        time.sleep(3)
        # press the Apply button again to check the input is retained
        search_and_display_target_item(driver, config.item_name_dic['scenario_3'])
        click_detail_item_button(driver)
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
        after_activity_id = driver.find_element(By.XPATH, '//*[@id="activity_id"]').text
        assert before_activity_id == after_activity_id
        panel_toggles = driver.find_elements(By.CLASS_NAME, 'panel-toggle')
        for pt in panel_toggles:
            if pt.text == 'Research Title':
                research_title_location = pt.location
                driver.execute_script(
                    'window.scrollTo(0, ' + str(research_title_location['y'] - 100) + ')')
                pt.click()
                time.sleep(1)
                break
        target_element = driver.find_element(
            By.XPATH,
            '//*[@id="subitem_restricted_access_research_title"]')
        assert target_element.get_attribute('value') == research_title
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '8_after')

    # pytest auto_test/test_application_for_use.py::TestScenario3::test_scenario_3_5_9
    def test_scenario_3_5_9(self, driver):
        """Test Scenario 3-5-9
        
        1. The Apply button appears.
        2. The Terms and Conditions modal appears.
        5. Transition to the usage registration workflow.
        9. Transition to the new usage registration workflow.
        
        User's role is General
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as General
        login_as_target(driver, 'General')

        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_3'])

        # 1. The Apply button appears.
        # 2. The Terms and Conditions modal appears.
        click_detail_item_button(driver)
        time.sleep(1)

        # 5. Transition to the usage registration workflow.
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

        # 9. Transition to the new usage registration workflow.
        # edit target is Research Title
        before_activity_id = driver.find_element(By.XPATH, '//*[@id="activity_id"]').text
        panel_toggles = driver.find_elements(By.CLASS_NAME, 'panel-toggle')
        for pt in panel_toggles:
            if pt.text == 'Research Title':
                research_title_location = pt.location
                driver.execute_script(
                    'window.scrollTo(0, ' + str(research_title_location['y'] - 100) + ')')
                pt.click()
                time.sleep(1)
                break
        research_title = 'test research'
        driver.find_element(By.XPATH, '//*[@id="subitem_restricted_access_research_title"]')\
            .send_keys(research_title)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '9_before')
        click_quit_btn(driver)
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="btn_cancel"]').click()
        time.sleep(3)
        # press the Apply button again to check the input is retained
        search_and_display_target_item(driver, config.item_name_dic['scenario_3'])
        click_detail_item_button(driver)
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
        after_activity_id = driver.find_element(By.XPATH, '//*[@id="activity_id"]').text
        assert before_activity_id != after_activity_id
        panel_toggles = driver.find_elements(By.CLASS_NAME, 'panel-toggle')
        for pt in panel_toggles:
            if pt.text == 'Research Title':
                research_title_location = pt.location
                driver.execute_script(
                    'window.scrollTo(0, ' + str(research_title_location['y'] - 100) + ')')
                pt.click()
                time.sleep(1)
                break
        target_element = driver.find_element(
            By.XPATH,
            '//*[@id="subitem_restricted_access_research_title"]')
        assert target_element.get_attribute('value') != research_title
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '9_after')

    # pytest auto_test/test_application_for_use.py::TestScenario3::test_scenario_3_5_13
    def test_scenario_3_5_13(self, driver):
        """Test Scenario 3-5-13
        
        1. The Apply button appears.
        2. The Terms and Conditions modal appears.
        5. Transition to the usage registration workflow.
        6. An email with the landing URL attached is sent to the applicant.
        10. The Download button appears and the registered content is downloaded.
        11. "Request for register Data Usage Report" email is sent to the applicant.
        13. Transition to the workflow with input retained.
        
        User's role is General
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as General
        login_as_target(driver, 'General')

        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_3'])

        # 1. The Apply button appears.
        # 2. The Terms and Conditions modal appears.
        click_detail_item_button(driver)
        time.sleep(1)

        # 5. Transition to the usage registration workflow.
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

        # 6. An email with the landing URL attached is sent to the applicant.
        driver.find_element(By.CLASS_NAME, 'next-button').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="btn-finish"]').click()
        time.sleep(3)

        # 10. The Download button appears and the registered content is downloaded.
        lines = get_latest_mail_body(config.users['General']['mail'].split('@', 1)[0])
        url = [line for line in lines if line.startswith('https://')][0]
        driver.get(url)
        time.sleep(3)
        click_detail_item_button(driver)
        time.sleep(1)

        # 11. "Request for register Data Usage Report" email is sent to the applicant.

        # 13. Transition to the workflow with input retained.
        driver.get(config.base_url + '/workflow/')
        time.sleep(1)
        table = driver.find_element(By.XPATH, '//*[@id="myTabContent"]/div[4]/div/div[1]/table')
        headers_text = [header.text for header in table.find_elements(By.TAG_NAME, 'th')]
        activity_id_idx = headers_text.index('Activity')
        workflow_idx = headers_text.index('WorkFlow')
        user_idx = headers_text.index('User')
        rows = table.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
        for row in rows:
            # the tag of the first of row's cell is 'th', so idx - 1 is correct
            rds = row.find_elements(By.TAG_NAME, 'td')
            if rds[workflow_idx - 1].text.startswith('利用報告')\
                and rds[user_idx - 1].text == config.users['General']['mail']:
                rds[activity_id_idx - 1].find_element(By.TAG_NAME, 'a').click()
                time.sleep(3)
                break
        # edit target is Usage Report
        activity_id = driver.find_element(By.XPATH, '//*[@id="activity_id"]').text
        panel_toggles = driver.find_elements(By.CLASS_NAME, 'panel-toggle')
        for pt in panel_toggles:
            if pt.text == 'Usage Report':
                usage_report_location = pt.location
                driver.execute_script(
                    'window.scrollTo(0, ' + str(usage_report_location['y'] - 100) + ')')
                pt.click()
                time.sleep(1)
                break
        usage_report = 'test usage report'
        driver.find_element(By.XPATH, '//*[@id="subitem_restricted_access_usage_report"]')\
            .send_keys(usage_report)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '13_before')
        driver.find_elements(By.CLASS_NAME, 'save-button')[1].click()
        time.sleep(3)
        # search for edited workflow from the Workflow tab
        driver.get(config.base_url + '/workflow/')
        time.sleep(1)
        table = driver.find_element(By.XPATH, '//*[@id="myTabContent"]/div[4]/div/div[1]/table')
        headers_text = [header.text for header in table.find_elements(By.TAG_NAME, 'th')]
        activity_id_idx = headers_text.index('Activity')
        rows = table.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
        for row in rows:
            # the tag of the first of row's cell is 'th', so idx - 1 is correct
            rds = row.find_elements(By.TAG_NAME, 'td')
            if rds[activity_id_idx - 1].text == activity_id:
                rds[activity_id_idx - 1].find_element(By.TAG_NAME, 'a').click()
                time.sleep(3)
                break
        panel_toggles = driver.find_elements(By.CLASS_NAME, 'panel-toggle')
        for pt in panel_toggles:
            if pt.text == 'Usage Report':
                usage_report_location = pt.location
                driver.execute_script(
                    'window.scrollTo(0, ' + str(usage_report_location['y'] - 100) + ')')
                pt.click()
                time.sleep(1)
                break
        target_element = driver.find_element(
            By.XPATH,
            '//*[@id="subitem_restricted_access_usage_report"]')
        assert target_element.get_attribute('value') == usage_report
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '13_after')

        # cancel the workflow to do other tests
        driver.get(config.base_url + '/workflow/activity/detail/' + activity_id)
        time.sleep(3)
        click_quit_btn(driver)
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="btn_cancel"]').click()
        time.sleep(3)

        # download the file 9 times to do other tests
        search_and_display_target_item(driver, config.item_name_dic['scenario_3'])
        for _ in range(9):
            click_detail_item_button(driver)
            time.sleep(1)

        # move downloaded files to do other tests
        move_downloaded_files(['test_scenario_3.txt'], inspect.currentframe().f_code.co_name)
        file_list = os.listdir(config.base_download_dir)
        delete_target_files = [file for file in file_list if file.startswith('test_scenario_3')]
        for file in delete_target_files:
            os.remove(config.base_download_dir + file)

    # pytest auto_test/test_application_for_use.py::TestScenario3::test_scenario_3_5_14
    def test_scenario_3_5_14(self, driver):
        """Test Scenario 3-5-14
        
        1. The Apply button appears.
        2. The Terms and Conditions modal appears.
        5. Transition to the usage registration workflow.
        6. An email with the landing URL attached is sent to the applicant.
        10. The Download button appears and the registered content is downloaded.
        11. "Request for register Data Usage Report" email is sent to the applicant.
        14. Status is recorded in the workflow tab as aborted.
        
        User's role is General
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as General
        login_as_target(driver, 'General')

        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_3'])

        # 1. The Apply button appears.
        # 2. The Terms and Conditions modal appears.
        click_detail_item_button(driver)
        time.sleep(1)

        # 5. Transition to the usage registration workflow.
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

        # 6. An email with the landing URL attached is sent to the applicant.
        driver.find_element(By.CLASS_NAME, 'next-button').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="btn-finish"]').click()
        time.sleep(3)

        # 10. The Download button appears and the registered content is downloaded.
        lines = get_latest_mail_body(config.users['General']['mail'].split('@', 1)[0])
        url = [line for line in lines if line.startswith('https://')][0]
        driver.get(url)
        time.sleep(3)
        click_detail_item_button(driver)
        time.sleep(1)

        # 11. "Request for register Data Usage Report" email is sent to the applicant.

        # 14. Status is recorded in the workflow tab as aborted.
        driver.get(config.base_url + '/workflow/')
        time.sleep(1)
        table = driver.find_element(By.XPATH, '//*[@id="myTabContent"]/div[4]/div/div[1]/table')
        headers_text = [header.text for header in table.find_elements(By.TAG_NAME, 'th')]
        activity_id_idx = headers_text.index('Activity')
        workflow_idx = headers_text.index('WorkFlow')
        user_idx = headers_text.index('User')
        rows = table.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
        for row in rows:
            # the tag of the first of row's cell is 'th', so idx - 1 is correct
            rds = row.find_elements(By.TAG_NAME, 'td')
            if rds[workflow_idx - 1].text.startswith('利用報告')\
                and rds[user_idx - 1].text == config.users['General']['mail']:
                rds[activity_id_idx - 1].find_element(By.TAG_NAME, 'a').click()
                time.sleep(3)
                break
        activity_id = driver.find_element(By.XPATH, '//*[@id="activity_id"]').text
        click_quit_btn(driver)
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="btn_cancel"]').click()
        time.sleep(3)
        driver.get(config.base_url + '/workflow/?tab=all')
        time.sleep(1)
        table = driver.find_element(By.XPATH, '//*[@id="myTabContent"]/div[4]/div/div[1]/table')
        headers_text = [header.text for header in table.find_elements(By.TAG_NAME, 'th')]
        activity_id_idx = headers_text.index('Activity')
        status_idx = headers_text.index('Status')
        rows = table.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
        for row in rows:
            # the tag of the first of row's cell is 'th', so idx - 1 is correct
            rds = row.find_elements(By.TAG_NAME, 'td')
            if rds[activity_id_idx - 1].text == activity_id:
                assert rds[status_idx - 1].text == 'Canceled'
                break
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '14')

        # download the file 9 times to do other tests
        search_and_display_target_item(driver, config.item_name_dic['scenario_3'])
        for _ in range(9):
            click_detail_item_button(driver)
            time.sleep(1)

        # move downloaded files to do other tests
        move_downloaded_files(['test_scenario_3.txt'], inspect.currentframe().f_code.co_name)
        file_list = os.listdir(config.base_download_dir)
        delete_target_files = [file for file in file_list if file.startswith('test_scenario_3')]
        for file in delete_target_files:
            os.remove(config.base_download_dir + file)

    # pytest auto_test/test_application_for_use.py::TestScenario3::test_scenario_3_6
    def test_scenario_3_6(self, driver):
        """Test Scenario 3-6
        
        1. The Apply button appears.
        2. The error message appears.
        
        User is not logged in
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_3'])

        # 1. The Apply button appears.
        assert check_item_button(driver, False)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. The error message appears.
        click_detail_item_button(driver)
        time.sleep(1)
        assert check_error_page(driver)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '2')

# pytest auto_test/test_application_for_use.py::TestScenario4
class TestScenario4:
    """Test Scenario 4
    
    Requirements for item to be used
        - The Providing Method is Usage Registration
        - The Providing Role is Guest
        - The Terms and Conditions are voluntary
    """
    # pytest auto_test/test_application_for_use.py::TestScenario4::test_scenario_4_1
    def test_scenario_4_1(self, driver):
        """Test Scenario 4-1
        
        1. The Download button appears.
        2. Registered content is downloaded.
        3. No "Request for register Data Usage Report" email is sent to the applicant.
        
        User's role is Contributor and the item's owner
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as Contributor
        login_as_target(driver, 'RegCon')

        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_4'])

        # 1. The Download button appears.
        assert check_item_button(driver, True)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. Registered content is downloaded.
        click_detail_item_button(driver)
        time.sleep(1)
        file_list = os.listdir(config.base_download_dir)
        assert 'test_scenario_4.txt' in file_list

        # 3. No "Request for register Data Usage Report" email is sent to the applicant.
        assert not check_request_for_register_mail(
            config.users['RegCon']['mail'],
            config.item_name_dic['scenario_4'])

        # move downloaded file to do other tests
        move_downloaded_files(['test_scenario_4.txt'], inspect.currentframe().f_code.co_name)

    # pytest auto_test/test_application_for_use.py::TestScenario4::test_scenario_4_2
    def test_scenario_4_2(self, driver):
        """Test Scenario 4-2
        
        1. The Apply button appears.
        2. The error message appears.
        
        User's role is Contributor and not the item's owner
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as Contributor
        login_as_target(driver, 'NoRegCon')

        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_4'])

        # 1. The Apply button appears.
        assert check_item_button(driver, False)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. The error message appears.
        click_detail_item_button(driver)
        time.sleep(1)
        assert check_error_page(driver)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '2')

    # pytest auto_test/test_application_for_use.py::TestScenario4::test_scenario_4_3
    def test_scenario_4_3(self, driver):
        """Test Scenario 4-3
        
        1. The Download button appears.
        2. Registered content is downloaded.
        3. No "Request for register Data Usage Report" email is sent to the applicant.
        
        User's role is Contributor and the item's contributor
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as Contributor
        login_as_target(driver, 'PrxRegCon')

        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_4'])

        # 1. The Download button appears.
        assert check_item_button(driver, True)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. Registered content is downloaded.
        click_detail_item_button(driver)
        time.sleep(1)
        file_list = os.listdir(config.base_download_dir)
        assert 'test_scenario_4.txt' in file_list

        # 3. No "Request for register Data Usage Report" email is sent to the applicant.
        assert not check_request_for_register_mail(
            config.users['PrxRegCon']['mail'],
            config.item_name_dic['scenario_4'])

        # move downloaded file to do other tests
        move_downloaded_files(['test_scenario_4.txt'], inspect.currentframe().f_code.co_name)

    # pytest auto_test/test_application_for_use.py::TestScenario4::test_scenario_4_4
    def test_scenario_4_4(self, driver):
        """Test Scenario 4-4
        
        1. The Apply button appears.
        2. The error message appears.
        
        User's role is Community Administrator
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as Community Administrator
        login_as_target(driver, 'Community')

        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_4'])

        # 1. The Apply button appears.
        assert check_item_button(driver, False)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. The error message appears.
        click_detail_item_button(driver)
        time.sleep(1)
        assert check_error_page(driver)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '2')

    # pytest auto_test/test_application_for_use.py::TestScenario4::test_scenario_4_5
    def test_scenario_4_5(self, driver):
        """Test Scenario 4-5
        
        1. The Apply button appears.
        2. The error message appears.
        
        User's role is General
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as General
        login_as_target(driver, 'General')

        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_4'])

        # 1. The Apply button appears.
        assert check_item_button(driver, False)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. The error message appears.
        click_detail_item_button(driver)
        time.sleep(1)
        assert check_error_page(driver)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '2')

    # pytest auto_test/test_application_for_use.py::TestScenario4::test_scenario_4_6_1_to_3
    def test_scenario_4_6_1_to_3(self, driver):
        """Test Scenario 4-6-1, 4-6-2, 4-6-3
        
        1. The Apply button appears.
        2. The Terms and Conditions modal appears.
        3. The print dialog appears.
        
        User is not logged in
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_4'])

        # 1. The Apply button appears.
        assert check_item_button(driver, False)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. The Terms and Conditions modal appears.
        click_detail_item_button(driver)
        time.sleep(1)
        assert check_terms_and_conditions_modal(driver, '利用登録\nGuest')
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '2')

        # 3. The print dialog appears.
        click_print_btn(driver)
        time.sleep(1)
        window_handles = driver.window_handles
        # after print button clicked, window handles increase
        assert len(window_handles) == 2
        driver.switch_to.window(window_handles[1])
        time.sleep(3)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '3')
        driver.switch_to.window(window_handles[0])
        time.sleep(1)

    # pytest auto_test/test_application_for_use.py::TestScenario4::test_scenario_4_6_4
    def test_scenario_4_6_4(self, driver):
        """Test Scenario 4-6-4
        
        1. The Apply button appears.
        2. The Terms and Conditions modal appears.
        4. Not working before checking the box.
        
        User is not logged in
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_4'])

        # 1. The Apply button appears.
        # 2. The Terms and Conditions modal appears.
        click_detail_item_button(driver)
        time.sleep(1)

        # 4. Not working before checking the box.
        modal = driver.find_element(By.CLASS_NAME, 'modal.fade.in')
        modal_id = modal.get_attribute('id')
        next_id = modal_id.replace('term_and_condtion_modal', 'term_next')
        next_btn = modal.find_element(By.XPATH, './/*[@id="' + next_id + '"]')
        next_btn.click()
        time.sleep(1)
        email_modal = driver.find_element(By.XPATH, '//*[@id="email_modal"]')
        assert not email_modal.get_attribute('style')

    # pytest auto_test/test_application_for_use.py::TestScenario4::test_scenario_4_6_5_to_8_and_12_and_13_and_15_and_16
    def test_scenario_4_6_5_to_8_and_12_and_13_and_15_and_16(self, driver):
        """Test Scenario 4-6-5, 4-6-6, 4-6-7, 4-6-8, 4-6-12, 4-6-13, 4-6-15, 4-6-16
        
        1. The Apply button appears.
        2. The Terms and Conditions modal appears.
        5. The account entry dialog appears.
        6. "Register Application for Use" email is sent to the applicant.
        7. Transition to the usage registration workflow.
        8. An email with a one-time address attached is sent to the applicant.
        12. The error message appears.
        13. Registered content is downloaded.
        15. "Request for register Data Usage Report" email is sent to the applicant.
        16. "Your Application was Received" email is sent to the applicant.
        
        User is not logged in
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_4'])

        # 1. The Apply button appears.
        # 2. The Terms and Conditions modal appears.
        click_detail_item_button(driver)
        time.sleep(1)

        # 5. The account entry dialog appears.
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
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '5')

        # 6. "Register Application for Use" email is sent to the applicant.
        enter_guest_email_for_get_usage_application(driver, config.guest_mail)
        assert check_register_application_mail(
            config.guest_mail,
            'test_scenario_4.txt')

        # 7. Transition to the usage registration workflow.
        lines = get_latest_mail_body(config.guest_mail.split('@', 1)[0])
        url = [line for line in lines if line.startswith('https://')][0]
        driver.get(url)
        time.sleep(3)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '7')

        # 8. An email with a one-time address attached is sent to the applicant.
        driver.find_element(By.CLASS_NAME, 'next-button').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="btn-finish"]').click()
        time.sleep(3)
        activity_id = driver.find_element(By.XPATH, '//*[@id="activity_id"]').text
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '8')
        assert check_approved_application_mail_for_guest(
            config.guest_mail,
            config.item_name_dic['scenario_4'],
            activity_id)

        # 12. The error message appears.
        lines = get_latest_mail_body(config.guest_mail.split('@', 1)[0])
        url = [line for line in lines if line.startswith('https://')][0]
        driver.get(url)
        time.sleep(3)
        enter_guest_email_after_approval(driver, config.users['General']['mail'])
        time.sleep(1)
        alert = driver.switch_to.alert
        alert_msg = alert.text
        assert alert_msg == config.cannot_download_msg
        alert.accept()

        # 13. Registered content is downloaded.
        driver.get(url)
        time.sleep(3)
        enter_guest_email_after_approval(driver, config.guest_mail)
        time.sleep(3)
        file_list = os.listdir(config.base_download_dir)
        assert 'test_scenario_4.txt' in file_list

        # 15. "Request for register Data Usage Report" email is sent to the applicant.
        assert check_request_for_register_mail(
            config.guest_mail,
            config.item_name_dic['scenario_4'],
            activity_id)

        # 16. "Your Application was Received" email is sent to the applicant.
        lines = get_latest_mail_body(config.guest_mail.split('@', 1)[0])
        url = [line for line in lines if line.startswith('https://')][0]
        driver.get(url)
        time.sleep(3)
        driver.find_element(By.CLASS_NAME, 'next-button').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="btn-finish"]').click()
        time.sleep(3)
        activity_id = driver.find_element(By.XPATH, '//*[@id="activity_id"]').text
        assert check_received_application_mail(
            config.guest_mail,
            config.item_name_dic['scenario_4'],
            activity_id)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '16')

        # cancel the workflow to do other tests
        login_as_target(driver, 'Repository')
        driver.get(config.base_url + '/workflow/activity/detail/' + activity_id)
        time.sleep(3)
        click_quit_btn(driver)
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="btn_cancel"]').click()

        # move downloaded file to do other tests
        move_downloaded_files(['test_scenario_4.txt'], inspect.currentframe().f_code.co_name)

    # pytest auto_test/test_application_for_use.py::TestScenario4::test_scenario_4_6_9_and_14
    def test_scenario_4_6_9_and_14(self, driver):
        """Test Scenario 4-6-9, 4-6-14
        
        1. The Apply button appears.
        2. The Terms and Conditions modal appears.
        5. The account entry dialog appears.
        6. "Register Application for Use" email is sent to the applicant.
        7. Transition to the usage registration workflow.
        9. An email with a one-time address attached is sent to the applicant.
        14. Registered content is downloaded.
        
        User is not logged in
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_4'])

        # 1. The Apply button appears.
        # 2. The Terms and Conditions modal appears.
        click_detail_item_button(driver)
        time.sleep(1)

        # 5. The account entry dialog appears.
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

        # 6. "Register Application for Use" email is sent to the applicant.
        # 7. Transition to the usage registration workflow.
        enter_guest_email_for_get_usage_application(driver, config.guest_mail)
        lines = get_latest_mail_body(config.guest_mail.split('@', 1)[0])
        url = [line for line in lines if line.startswith('https://')][0]
        driver.get(url)
        time.sleep(3)

        # 9. An email with a one-time address attached is sent to the applicant.
        driver.find_element(By.CLASS_NAME, 'back-button').click()
        time.sleep(3)
        driver.get(url)
        time.sleep(3)
        driver.find_element(By.CLASS_NAME, 'next-button').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="btn-finish"]').click()
        time.sleep(3)
        activity_id = driver.find_element(By.XPATH, '//*[@id="activity_id"]').text
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '9')
        assert check_approved_application_mail_for_guest(
            config.guest_mail,
            config.item_name_dic['scenario_4'],
            activity_id)

        # 14. Registered content is downloaded.
        lines = get_latest_mail_body(config.guest_mail.split('@', 1)[0])
        url = [line for line in lines if line.startswith('https://')][0]
        driver.get(url)
        time.sleep(3)
        enter_guest_email_after_approval(driver, config.guest_mail)
        time.sleep(3)
        file_list = os.listdir(config.base_download_dir)
        assert 'test_scenario_4.txt' in file_list

        # cancel the workflow to do other tests
        lines = get_latest_mail_body(config.guest_mail.split('@', 1)[0])
        url = [line for line in lines if line.startswith('https://')][0]
        driver.get(url)
        time.sleep(3)
        click_quit_btn(driver)
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="btn_cancel"]').click()

        # move downloaded file to do other tests
        move_downloaded_files(['test_scenario_4.txt'], inspect.currentframe().f_code.co_name)

    # pytest auto_test/test_application_for_use.py::TestScenario4::test_scenario_4_6_10
    def test_scenario_4_6_10(self, driver):
        """Test Scenario 4-6-10
        
        1. The Apply button appears.
        2. The Terms and Conditions modal appears.
        5. The account entry dialog appears.
        6. "Register Application for Use" email is sent to the applicant.
        7. Transition to the usage registration workflow.
        10. Transition to the workflow with input retained.
        
        User is not logged in
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_4'])

        # 1. The Apply button appears.
        # 2. The Terms and Conditions modal appears.
        click_detail_item_button(driver)
        time.sleep(1)

        # 5. The account entry dialog appears.
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

        # 6. "Register Application for Use" email is sent to the applicant.
        # 7. Transition to the usage registration workflow.
        enter_guest_email_for_get_usage_application(driver, config.guest_mail)
        lines = get_latest_mail_body(config.guest_mail.split('@', 1)[0])
        url = [line for line in lines if line.startswith('https://')][0]
        driver.get(url)
        time.sleep(3)

        # 10. Transition to the workflow with input retained.
        # edit target is Research Title
        before_activity_id = driver.find_element(By.XPATH, '//*[@id="activity_id"]').text
        panel_toggles = driver.find_elements(By.CLASS_NAME, 'panel-toggle')
        for pt in panel_toggles:
            if pt.text == 'Research Title':
                research_title_location = pt.location
                driver.execute_script(
                    'window.scrollTo(0, ' + str(research_title_location['y'] - 100) + ')')
                pt.click()
                time.sleep(1)
                break
        research_title = 'test research'
        driver.find_element(By.XPATH, '//*[@id="subitem_restricted_access_research_title"]')\
            .send_keys(research_title)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '10_before')
        driver.find_elements(By.CLASS_NAME, 'save-button')[1].click()
        time.sleep(3)
        # execute 4-6-1, 4-6-2, 4-6-5, 4-6-6 and 4-6-7 again
        search_and_display_target_item(driver, config.item_name_dic['scenario_4'])
        click_detail_item_button(driver)
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
        time.sleep(3)
        after_activity_id = driver.find_element(By.XPATH, '//*[@id="activity_id"]').text
        assert before_activity_id == after_activity_id
        panel_toggles = driver.find_elements(By.CLASS_NAME, 'panel-toggle')
        for pt in panel_toggles:
            if pt.text == 'Research Title':
                research_title_location = pt.location
                driver.execute_script(
                    'window.scrollTo(0, ' + str(research_title_location['y'] - 100) + ')')
                pt.click()
                time.sleep(1)
                break
        target_element = driver.find_element(
            By.XPATH,
            '//*[@id="subitem_restricted_access_research_title"]')
        assert target_element.get_attribute('value') == research_title
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '10_after')

        # cancel the workflow to do other tests
        click_quit_btn(driver)
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="btn_cancel"]').click()

    # pytest auto_test/test_application_for_use.py::TestScenario4::test_scenario_4_6_11
    def test_scenario_4_6_11(self, driver):
        """Test Scenario 4-6-11
        
        1. The Apply button appears.
        2. The Terms and Conditions modal appears.
        5. The account entry dialog appears.
        6. "Register Application for Use" email is sent to the applicant.
        7. Transition to the usage registration workflow.
        11. Transition to the new usage registration workflow.
        
        User is not logged in
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_4'])

        # 1. The Apply button appears.
        # 2. The Terms and Conditions modal appears.
        click_detail_item_button(driver)
        time.sleep(1)

        # 5. The account entry dialog appears.
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

        # 6. "Register Application for Use" email is sent to the applicant.
        # 7. Transition to the usage registration workflow.
        enter_guest_email_for_get_usage_application(driver, config.guest_mail)
        lines = get_latest_mail_body(config.guest_mail.split('@', 1)[0])
        url = [line for line in lines if line.startswith('https://')][0]
        driver.get(url)
        time.sleep(3)

        # 11. Transition to the new usage registration workflow.
        # edit target is Research Title
        before_activity_id = driver.find_element(By.XPATH, '//*[@id="activity_id"]').text
        panel_toggles = driver.find_elements(By.CLASS_NAME, 'panel-toggle')
        for pt in panel_toggles:
            if pt.text == 'Research Title':
                research_title_location = pt.location
                driver.execute_script(
                    'window.scrollTo(0, ' + str(research_title_location['y'] - 100) + ')')
                pt.click()
                time.sleep(1)
                break
        research_title = 'test research'
        driver.find_element(By.XPATH, '//*[@id="subitem_restricted_access_research_title"]')\
            .send_keys(research_title)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '11_before')
        click_quit_btn(driver)
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="btn_cancel"]').click()
        time.sleep(3)
        # execute 4-6-1, 4-6-2, 4-6-5, 4-6-6 and 4-6-7 again
        search_and_display_target_item(driver, config.item_name_dic['scenario_4'])
        click_detail_item_button(driver)
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
        time.sleep(3)
        after_activity_id = driver.find_element(By.XPATH, '//*[@id="activity_id"]').text
        assert before_activity_id != after_activity_id
        panel_toggles = driver.find_elements(By.CLASS_NAME, 'panel-toggle')
        for pt in panel_toggles:
            if pt.text == 'Research Title':
                research_title_location = pt.location
                driver.execute_script(
                    'window.scrollTo(0, ' + str(research_title_location['y'] - 100) + ')')
                pt.click()
                time.sleep(1)
                break
        target_element = driver.find_element(
            By.XPATH,
            '//*[@id="subitem_restricted_access_research_title"]')
        assert target_element.get_attribute('value') != research_title
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '11_after')

        # cancel the workflow to do other tests
        click_quit_btn(driver)
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="btn_cancel"]').click()

    # pytest auto_test/test_application_for_use.py::TestScenario4::test_scenario_4_6_17
    def test_scenario_4_6_17(self, driver):
        """Test Scenario 4-6-17
        
        1. The Apply button appears.
        2. The Terms and Conditions modal appears.
        5. The account entry dialog appears.
        6. "Register Application for Use" email is sent to the applicant.
        7. Transition to the usage registration workflow.
        8. An email with a one-time address attached is sent to the applicant.
        13. Registered content is downloaded.
        17. Transition to the workflow with input retained.
        
        User is not logged in
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_4'])

        # 1. The Apply button appears.
        # 2. The Terms and Conditions modal appears.
        click_detail_item_button(driver)
        time.sleep(1)

        # 5. The account entry dialog appears.
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

        # 6. "Register Application for Use" email is sent to the applicant.
        # 7. Transition to the usage registration workflow.
        enter_guest_email_for_get_usage_application(driver, config.guest_mail)
        lines = get_latest_mail_body(config.guest_mail.split('@', 1)[0])
        url = [line for line in lines if line.startswith('https://')][0]
        driver.get(url)
        time.sleep(3)

        # 8. An email with a one-time address attached is sent to the applicant.
        driver.find_element(By.CLASS_NAME, 'next-button').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="btn-finish"]').click()
        time.sleep(3)

        # 13. Registered content is downloaded.
        lines = get_latest_mail_body(config.guest_mail.split('@', 1)[0])
        url = [line for line in lines if line.startswith('https://')][0]
        driver.get(url)
        time.sleep(3)
        enter_guest_email_after_approval(driver, config.guest_mail)
        time.sleep(3)

        # 17. Transition to the workflow with input retained.
        # edit target is Usage Report
        lines = get_latest_mail_body(config.guest_mail.split('@', 1)[0])
        url = [line for line in lines if line.startswith('https://')][0]
        driver.get(url)
        time.sleep(3)
        panel_toggles = driver.find_elements(By.CLASS_NAME, 'panel-toggle')
        for pt in panel_toggles:
            if pt.text == 'Usage Report':
                usage_report_location = pt.location
                driver.execute_script(
                    'window.scrollTo(0, ' + str(usage_report_location['y'] - 100) + ')')
                pt.click()
                time.sleep(1)
                break
        usage_report = 'test usage report'
        driver.find_element(By.XPATH, '//*[@id="subitem_restricted_access_usage_report"]')\
            .send_keys(usage_report)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '17_before')
        driver.find_elements(By.CLASS_NAME, 'save-button')[1].click()
        time.sleep(3)
        # reaccess to the workflow
        driver.get(url)
        time.sleep(3)
        panel_toggles = driver.find_elements(By.CLASS_NAME, 'panel-toggle')
        for pt in panel_toggles:
            if pt.text == 'Usage Report':
                usage_report_location = pt.location
                driver.execute_script(
                    'window.scrollTo(0, ' + str(usage_report_location['y'] - 100) + ')')
                pt.click()
                time.sleep(1)
                break
        target_element = driver.find_element(
            By.XPATH,
            '//*[@id="subitem_restricted_access_usage_report"]')
        assert target_element.get_attribute('value') == usage_report
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '17_after')

        # cancel the workflow to do other tests
        click_quit_btn(driver)
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="btn_cancel"]').click()

        # move downloaded file to do other tests
        move_downloaded_files(['test_scenario_4.txt'], inspect.currentframe().f_code.co_name)

    # pytest auto_test/test_application_for_use.py::TestScenario4::test_scenario_4_6_18
    def test_scenario_4_6_18(self, driver):
        """Test Scenario 4-6-18
        
        1. The Apply button appears.
        2. The Terms and Conditions modal appears.
        5. The account entry dialog appears.
        6. "Register Application for Use" email is sent to the applicant.
        7. Transition to the usage registration workflow.
        8. An email with a one-time address attached is sent to the applicant.
        13. Registered content is downloaded.
        18. The status of the target workflow is "Canceled"
        
        User is not logged in
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_4'])

        # 1. The Apply button appears.
        # 2. The Terms and Conditions modal appears.
        click_detail_item_button(driver)
        time.sleep(1)

        # 5. The account entry dialog appears.
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

        # 6. "Register Application for Use" email is sent to the applicant.
        # 7. Transition to the usage registration workflow.
        enter_guest_email_for_get_usage_application(driver, config.guest_mail)
        lines = get_latest_mail_body(config.guest_mail.split('@', 1)[0])
        url = [line for line in lines if line.startswith('https://')][0]
        driver.get(url)
        time.sleep(3)

        # 8. An email with a one-time address attached is sent to the applicant.
        driver.find_element(By.CLASS_NAME, 'next-button').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="btn-finish"]').click()
        time.sleep(3)

        # 13. Registered content is downloaded.
        lines = get_latest_mail_body(config.guest_mail.split('@', 1)[0])
        url = [line for line in lines if line.startswith('https://')][0]
        driver.get(url)
        time.sleep(3)
        enter_guest_email_after_approval(driver, config.guest_mail)
        time.sleep(3)

        # 18. The status of the target workflow is "Canceled"
        lines = get_latest_mail_body(config.guest_mail.split('@', 1)[0])
        url = [line for line in lines if line.startswith('https://')][0]
        driver.get(url)
        time.sleep(3)
        activity_id = driver.find_element(By.XPATH, '//*[@id="activity_id"]').text
        click_quit_btn(driver)
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="btn_cancel"]').click()
        time.sleep(3)
        login_as_target(driver, 'Repository')
        driver.get(config.base_url + '/workflow/?tab=all')
        time.sleep(1)
        table = driver.find_element(By.XPATH, '//*[@id="myTabContent"]/div[4]/div/div[1]/table')
        headers_text = [header.text for header in table.find_elements(By.TAG_NAME, 'th')]
        activity_id_idx = headers_text.index('Activity')
        status_idx = headers_text.index('Status')
        rows = table.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
        for row in rows:
            # the tag of the first of row's cell is 'th', so idx - 1 is correct
            rds = row.find_elements(By.TAG_NAME, 'td')
            if rds[activity_id_idx - 1].text == activity_id:
                assert rds[status_idx - 1].text == 'Canceled'
                break
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '18')

        # move downloaded file to do other tests
        move_downloaded_files(['test_scenario_4.txt'], inspect.currentframe().f_code.co_name)

# pytest auto_test/test_application_for_use.py::TestScenario5
class TestScenario5:
    """Test Scenario 5
    
    Requirements for item to be used
        - The Providing Method is Usage Application
        - The Providing Role is General
        - The Terms and Conditions are voluntary
    """
    # pytest auto_test/test_application_for_use.py::TestScenario5::test_scenario_5_1
    def test_scenario_5_1(self, driver):
        """Test Scenario 5-1
        
        1. The Download button appears.
        2. Registered content is downloaded.
        3. No "Request for register Data Usage Report" email is sent to the applicant.
        
        User's role is Contributor and the item's owner
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as Contributor
        login_as_target(driver, 'RegCon')

        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_5'])

        # 1. The Download button appears.
        assert check_item_button(driver, True)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. Registered content is downloaded.
        click_detail_item_button(driver)
        time.sleep(1)
        file_list = os.listdir(config.base_download_dir)
        assert 'test_scenario_5.txt' in file_list

        # 3. No "Request for register Data Usage Report" email is sent to the applicant.
        assert not check_request_for_register_mail(
            config.users['RegCon']['mail'],
            config.item_name_dic['scenario_5'])

        # move downloaded file to do other tests
        move_downloaded_files(['test_scenario_5.txt'], inspect.currentframe().f_code.co_name)

    # pytest auto_test/test_application_for_use.py::TestScenario5::test_scenario_5_2
    def test_scenario_5_2(self, driver):
        """Test Scenario 5-2
        
        1. The Apply button appears.
        2. The error message appears.
        
        User's role is Contributor and not the item's owner
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as Contributor
        login_as_target(driver, 'NoRegCon')

        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_5'])

        # 1. The Apply button appears.
        assert check_item_button(driver, False)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. The error message appears.
        click_detail_item_button(driver)
        time.sleep(1)
        assert check_error_page(driver)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '2')

    # pytest auto_test/test_application_for_use.py::TestScenario5::test_scenario_5_3
    def test_scenario_5_3(self, driver):
        """Test Scenario 5-3
        
        1. The Download button appears.
        2. Registered content is downloaded.
        3. No "Request for register Data Usage Report" email is sent to the applicant.
        
        User's role is Contributor and the item's contributor
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as Contributor
        login_as_target(driver, 'PrxRegCon')

        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_5'])

        # 1. The Download button appears.
        assert check_item_button(driver, True)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. Registered content is downloaded.
        click_detail_item_button(driver)
        time.sleep(1)
        file_list = os.listdir(config.base_download_dir)
        assert 'test_scenario_5.txt' in file_list

        # 3. No "Request for register Data Usage Report" email is sent to the applicant.
        assert not check_request_for_register_mail(
            config.users['PrxRegCon']['mail'],
            config.item_name_dic['scenario_5'])

        # move downloaded file to do other tests
        move_downloaded_files(['test_scenario_5.txt'], inspect.currentframe().f_code.co_name)

    # pytest auto_test/test_application_for_use.py::TestScenario5::test_scenario_5_4
    def test_scenario_5_4(self, driver):
        """Test Scenario 5-4
        
        1. The Apply button appears.
        2. The error message appears.
        
        User's role is Community Administrator
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as Community Administrator
        login_as_target(driver, 'Community')

        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_5'])

        # 1. The Apply button appears.
        assert check_item_button(driver, False)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. The error message appears.
        click_detail_item_button(driver)
        time.sleep(1)
        assert check_error_page(driver)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '2')

    # pytest auto_test/test_application_for_use.py::TestScenario5::test_scenario_5_5_1_to_3
    def test_scenario_5_5_1_to_3(self, driver):
        """Test Scenario 5-5-1, 5-5-2, 5-5-3
        
        1. The Apply button appears.
        2. The Terms and Conditions modal appears.
        3. The print dialog appears.
        
        User's role is General
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as General
        login_as_target(driver, 'General')

        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_5'])

        # 1. The Apply button appears.
        assert check_item_button(driver, False)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. The Terms and Conditions modal appears.
        click_detail_item_button(driver)
        time.sleep(1)
        assert check_terms_and_conditions_modal(driver, '利用申請\nGeneral')
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '2')

        # 3. The print dialog appears.
        click_print_btn(driver)
        time.sleep(1)
        window_handles = driver.window_handles
        # after print button clicked, window handles increase
        assert len(window_handles) == 2
        driver.switch_to.window(window_handles[1])
        time.sleep(3)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '3')
        driver.switch_to.window(window_handles[0])
        time.sleep(1)

    # pytest auto_test/test_application_for_use.py::TestScenario5::test_scenario_5_5_4
    def test_scenario_5_5_4(self, driver):
        """Test Scenario 5-5-4
        
        1. The Apply button appears.
        2. The Terms and Conditions modal appears.
        4. Not working before checking the box.
        
        User's role is General
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as General
        login_as_target(driver, 'General')

        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_5'])

        # 1. The Apply button appears.
        # 2. The Terms and Conditions modal appears.
        click_detail_item_button(driver)
        time.sleep(1)

        # 4. Not working before checking the box.
        modal = driver.find_element(By.CLASS_NAME, 'modal.fade.in')
        modal_id = modal.get_attribute('id')
        next_id = modal_id.replace('term_and_condtion_modal', 'term_next')
        next_btn = modal.find_element(By.XPATH, './/*[@id="' + next_id + '"]')
        next_btn.click()
        time.sleep(1)
        assert not driver.current_url.startswith(config.base_url + '/workflow/activity/detail')

    # pytest auto_test/test_application_for_use.py::TestScenario5::test_scenario_5_5_5_and_6_and_10_to_13
    def test_scenario_5_5_5_and_6_and_10_to_13(self, driver):
        """Test Scenario 5-5-5, 5-5-6, 5-5-10, 5-5-11, 5-5-12, 5-5-13
        
        1. The Apply button appears.
        2. The Terms and Conditions modal appears.
        5. Transition to the usage application workflow.
        6. A reminder email is sent to the applicant.
        10. The usage application workflow with the action status "Approval" is displayed.
        11. The Download button appears and the registered content is downloaded.
        12. "Request for register Data Usage Report" email is sent to the applicant.
        13. "Your Application was Received" email is sent to the applicant.

        User's role is General

        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as General
        login_as_target(driver, 'General')

        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_5'])

        # 1. The Apply button appears.
        # 2. The Terms and Conditions modal appears.
        click_detail_item_button(driver)
        time.sleep(1)

        # 5. Transition to the usage application workflow.
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
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '5')

        # 6. A reminder email is sent to the applicant.
        driver.find_element(By.CLASS_NAME, 'next-button').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="btn-finish"]').click()
        time.sleep(3)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '6')
        activity_id = driver.find_element(By.XPATH, '//*[@id="activity_id"]').text
        assert check_request_for_approval_mail(
            config.users['General']['mail'],
            config.item_name_dic['scenario_5'],
            activity_id)

        # 10. The usage application workflow with the action status "Approval" is displayed.
        logout(driver)
        login_as_target(driver, 'Repository')
        driver.get(config.base_url + '/workflow/')
        time.sleep(1)
        table = driver.find_element(By.XPATH, '//*[@id="myTabContent"]/div[4]/div/div[1]/table')
        headers_text = [header.text for header in table.find_elements(By.TAG_NAME, 'th')]
        activity_id_idx = headers_text.index('Activity')
        action_idx = headers_text.index('Action')
        rows = table.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
        target_element = None
        for row in rows:
            # the tag of the first of row's cell is 'th', so idx - 1 is correct
            rds = row.find_elements(By.TAG_NAME, 'td')
            if rds[activity_id_idx - 1].text == activity_id:
                assert rds[action_idx - 1].text == 'Approval'
                target_element = rds[activity_id_idx - 1]
                break
        assert target_element, 'Could not get target workflow'
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '10')

        # 11. The Download button appears and the registered content is downloaded.
        target_element.find_element(By.TAG_NAME, 'a').click()
        time.sleep(3)
        click_approval_btn(driver)
        time.sleep(3)
        logout(driver)
        login_as_target(driver, 'General')
        search_and_display_target_item(driver, config.item_name_dic['scenario_5'])
        assert check_item_button(driver, True)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '11')
        click_detail_item_button(driver)
        time.sleep(1)
        file_list = os.listdir(config.base_download_dir)
        assert 'test_scenario_5.txt' in file_list

        # 12. "Request for register Data Usage Report" email is sent to the applicant.
        assert not check_request_for_register_mail(
            config.users['General']['mail'],
            config.item_name_dic['scenario_5'])

        # 13. "Your Application was Received" email is sent to the applicant.
        driver.get(config.base_url + '/workflow/')
        time.sleep(1)
        table = driver.find_element(By.XPATH, '//*[@id="myTabContent"]/div[4]/div/div[1]/table')
        headers_text = [header.text for header in table.find_elements(By.TAG_NAME, 'th')]
        activity_id_idx = headers_text.index('Activity')
        workflow_idx = headers_text.index('Workflow')
        user_idx = headers_text.index('User')
        rows = table.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
        for row in rows:
            # the tag of the first of row's cell is 'th', so idx - 1 is correct
            rds = row.find_elements(By.TAG_NAME, 'td')
            if rds[workflow_idx - 1].text.startswith('利用報告')\
                and rds[user_idx - 1].text == config.users['General']['mail']:
                rds[activity_id_idx - 1].find_element(By.TAG_NAME, 'a').click()
                time.sleep(3)
                break
        driver.find_element(By.CLASS_NAME, 'next-button').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="btn-finish"]').click()
        time.sleep(3)
        activity_id = driver.find_element(By.XPATH, '//*[@id="activity_id"]').text
        assert check_received_application_mail(
            config.users['General']['mail'],
            config.item_name_dic['scenario_5'],
            activity_id)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '13')

        # cancel the workflow to do other tests
        logout(driver)
        login_as_target(driver, 'Repository')
        driver.get(config.base_url + '/workflow/activity/detail/' + activity_id)
        time.sleep(3)
        click_quit_btn(driver)
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="btn_cancel"]').click()
        time.sleep(3)

        # download the file 9 times to do other tests
        search_and_display_target_item(driver, config.item_name_dic['scenario_5'])
        for _ in range(9):
            click_detail_item_button(driver)
            time.sleep(1)

        # move downloaded files to do other tests
        move_downloaded_files(['test_scenario_5.txt'], inspect.currentframe().f_code.co_name)
        file_list = os.listdir(config.base_download_dir)
        delete_target_files = [file for file in file_list if file.startswith('test_scenario_5')]
        for file in delete_target_files:
            os.remove(config.base_download_dir + file)

    # pytest auto_test/test_application_for_use.py::TestScenario5::test_scenario_5_5_7
    def test_scenario_5_5_7(self, driver):
        """Test Scenario 5-5-7
        
        1. The Apply button appears.
        2. The Terms and Conditions modal appears.
        5. Transition to the usage application workflow.
        7. A reminder email is sent to the applicant.
        
        User's role is General
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as General
        login_as_target(driver, 'General')

        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_5'])

        # 1. The Apply button appears.
        # 2. The Terms and Conditions modal appears.
        click_detail_item_button(driver)
        time.sleep(1)

        # 5. Transition to the usage application workflow.
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

        # 7. A reminder email is sent to the applicant.
        activity_id = driver.find_element(By.XPATH, '//*[@id="activity_id"]').text
        driver.find_element(By.CLASS_NAME, 'back-button').click()
        time.sleep(3)
        table = driver.find_element(By.XPATH, '//*[@id="myTabContent"]/div[4]/div/div[1]/table')
        headers_text = [header.text for header in table.find_elements(By.TAG_NAME, 'th')]
        activity_id_idx = headers_text.index('Activity')
        rows = table.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
        for row in rows:
            # the tag of the first of row's cell is 'th', so idx - 1 is correct
            rds = row.find_elements(By.TAG_NAME, 'td')
            if rds[activity_id_idx - 1].text == activity_id:
                rds[activity_id_idx - 1].find_element(By.TAG_NAME, 'a').click()
                time.sleep(3)
                break
        driver.find_element(By.CLASS_NAME, 'next-button').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="btn-finish"]').click()
        time.sleep(3)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '7')
        assert check_request_for_approval_mail(
            config.users['General']['mail'],
            config.item_name_dic['scenario_5'],
            activity_id)

        # cancel the workflow to do other tests
        logout(driver)
        login_as_target(driver, 'Repository')
        driver.get(config.base_url + '/workflow/activity/detail/' + activity_id)
        time.sleep(3)
        click_quit_btn(driver)
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="btn_cancel"]').click()

    # pytest auto_test/test_application_for_use.py::TestScenario5::test_scenario_5_5_8
    def test_scenario_5_5_8(self, driver):
        """Test Scenario 5-5-8
        
        1. The Apply button appears.
        2. The Terms and Conditions modal appears.
        5. Transition to the usage application workflow.
        8. Transition to the workflow with input retained.
        
        User's role is General
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as General
        login_as_target(driver, 'General')

        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_5'])

        # 1. The Apply button appears.
        # 2. The Terms and Conditions modal appears.
        click_detail_item_button(driver)
        time.sleep(1)

        # 5. Transition to the usage application workflow.
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

        # 8. Transition to the workflow with input retained.
        # edit target is Research Title
        before_activity_id = driver.find_element(By.XPATH, '//*[@id="activity_id"]').text
        panel_toggles = driver.find_elements(By.CLASS_NAME, 'panel-toggle')
        for pt in panel_toggles:
            if pt.text == 'Research Title':
                research_title_location = pt.location
                driver.execute_script(
                    'window.scrollTo(0, ' + str(research_title_location['y'] - 100) + ')')
                pt.click()
                time.sleep(1)
                break
        research_title = 'test research'
        driver.find_element(By.XPATH, '//*[@id="subitem_restricted_access_research_title"]')\
            .send_keys(research_title)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '8_before')
        driver.find_elements(By.CLASS_NAME, 'save-button')[1].click()
        time.sleep(3)
        # press the Apply button again to check the input is retained
        search_and_display_target_item(driver, config.item_name_dic['scenario_5'])
        click_detail_item_button(driver)
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
        after_activity_id = driver.find_element(By.XPATH, '//*[@id="activity_id"]').text
        assert before_activity_id == after_activity_id
        panel_toggles = driver.find_elements(By.CLASS_NAME, 'panel-toggle')
        for pt in panel_toggles:
            if pt.text == 'Research Title':
                research_title_location = pt.location
                driver.execute_script(
                    'window.scrollTo(0, ' + str(research_title_location['y'] - 100) + ')')
                pt.click()
                time.sleep(1)
                break
        target_element = driver.find_element(
            By.XPATH,
            '//*[@id="subitem_restricted_access_research_title"]')
        assert target_element.get_attribute('value') == research_title
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '8_after')

    # pytest auto_test/test_application_for_use.py::TestScenario5::test_scenario_5_5_9
    def test_scenario_5_5_9(self, driver):
        """Test Scenario 5-5-9
        
        1. The Apply button appears.
        2. The Terms and Conditions modal appears.
        5. Transition to the usage application workflow.
        9. Transition to the new usage application workflow.

        User's role is General

        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as General
        login_as_target(driver, 'General')

        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_5'])

        # 1. The Apply button appears.
        # 2. The Terms and Conditions modal appears.
        click_detail_item_button(driver)
        time.sleep(1)

        # 5. Transition to the usage application workflow.
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

        # 9. Transition to the new usage application workflow.
        # edit target is Research Title
        before_activity_id = driver.find_element(By.XPATH, '//*[@id="activity_id"]').text
        panel_toggles = driver.find_elements(By.CLASS_NAME, 'panel-toggle')
        for pt in panel_toggles:
            if pt.text == 'Research Title':
                research_title_location = pt.location
                driver.execute_script(
                    'window.scrollTo(0, ' + str(research_title_location['y'] - 100) + ')')
                pt.click()
                time.sleep(1)
                break
        research_title = 'test research'
        driver.find_element(By.XPATH, '//*[@id="subitem_restricted_access_research_title"]')\
            .send_keys(research_title)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '9_before')
        click_quit_btn(driver)
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="btn_cancel"]').click()
        time.sleep(3)
        # press the Apply button again to check the input is retained
        search_and_display_target_item(driver, config.item_name_dic['scenario_5'])
        click_detail_item_button(driver)
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
        after_activity_id = driver.find_element(By.XPATH, '//*[@id="activity_id"]').text
        assert before_activity_id != after_activity_id
        panel_toggles = driver.find_elements(By.CLASS_NAME, 'panel-toggle')
        for pt in panel_toggles:
            if pt.text == 'Research Title':
                research_title_location = pt.location
                driver.execute_script(
                    'window.scrollTo(0, ' + str(research_title_location['y'] - 100) + ')')
                pt.click()
                time.sleep(1)
                break
        target_element = driver.find_element(
            By.XPATH,
            '//*[@id="subitem_restricted_access_research_title"]')
        assert target_element.get_attribute('value') != research_title
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '9_after')

    # pytest auto_test/test_application_for_use.py::TestScenario5::test_scenario_5_5_14
    def test_scenario_5_5_14(self, driver):
        """Test Scenario 5-5-14
        
        1. The Apply button appears.
        2. The Terms and Conditions modal appears.
        5. Transition to the usage application workflow.
        6. A reminder email is sent to the applicant.
        11. The Download button appears and the registered content is downloaded.
        14. Transition to the workflow with input retained.

        User's role is General

        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as General
        login_as_target(driver, 'General')

        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_5'])

        # 1. The Apply button appears.
        # 2. The Terms and Conditions modal appears.
        click_detail_item_button(driver)
        time.sleep(1)

        # 5. Transition to the usage application workflow.
        modal = driver.find_element(By.CLASS_NAME, 'modal.fade.in')
        modal_id = modal.get_attribute('id')
        next_id = modal_id.replace('term_and_condtion_modal', 'term_next')
        next_btn = modal.find_element(By.XPATH, './/*[@id="' + next_id + '"]')
        check_id = modal_id.replace('term_and_condtion_modal', 'term_checked')
        check_box = modal.find_element(By.XPATH, './/*[@id="' + check_id + '"]')
        check_box.click()
        time.sleep(1)
        next_btn.click()
        time.sleep(3)

        # 6. A reminder email is sent to the applicant.
        driver.find_element(By.CLASS_NAME, 'next-button').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="btn-finish"]').click()
        time.sleep(3)
        activity_id = driver.find_element(By.XPATH, '//*[@id="activity_id"]').text

        # 11. The Download button appears and the registered content is downloaded.
        logout(driver)
        login_as_target(driver, 'Repository')
        driver.get(config.base_url + '/workflow/')
        time.sleep(1)
        table = driver.find_element(By.XPATH, '//*[@id="myTabContent"]/div[4]/div/div[1]/table')
        headers_text = [header.text for header in table.find_elements(By.TAG_NAME, 'th')]
        activity_id_idx = headers_text.index('Activity')
        rows = table.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
        for row in rows:
            # the tag of the first of row's cell is 'th', so idx - 1 is correct
            rds = row.find_elements(By.TAG_NAME, 'td')
            if rds[activity_id_idx - 1].text == activity_id:
                rds[activity_id_idx - 1].find_element(By.TAG_NAME, 'a').click()
                time.sleep(3)
                break
        click_approval_btn(driver)
        time.sleep(3)
        logout(driver)
        login_as_target(driver, 'General')
        search_and_display_target_item(driver, config.item_name_dic['scenario_5'])
        click_detail_item_button(driver)
        time.sleep(1)

        # 14. Transition to the workflow with input retained.
        driver.get(config.base_url + '/workflow/')
        time.sleep(1)
        table = driver.find_element(By.XPATH, '//*[@id="myTabContent"]/div[4]/div/div[1]/table')
        headers_text = [header.text for header in table.find_elements(By.TAG_NAME, 'th')]
        activity_id_idx = headers_text.index('Activity')
        workflow_idx = headers_text.index('WorkFlow')
        user_idx = headers_text.index('User')
        rows = table.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
        for row in rows:
            # the tag of the first of row's cell is 'th', so idx - 1 is correct
            rds = row.find_elements(By.TAG_NAME, 'td')
            if rds[workflow_idx - 1].text.startswith('利用報告')\
                and rds[user_idx - 1].text == config.users['General']['mail']:
                rds[activity_id_idx - 1].find_element(By.TAG_NAME, 'a').click()
                time.sleep(3)
                break
        # edit target is Usage Report
        activity_id = driver.find_element(By.XPATH, '//*[@id="activity_id"]').text
        panel_toggles = driver.find_elements(By.CLASS_NAME, 'panel-toggle')
        for pt in panel_toggles:
            if pt.text == 'Usage Report':
                usage_report_location = pt.location
                driver.execute_script(
                    'window.scrollTo(0, ' + str(usage_report_location['y'] - 100) + ')')
                pt.click()
                time.sleep(1)
                break
        usage_report = 'test usage report'
        driver.find_element(By.XPATH, '//*[@id="subitem_restricted_access_usage_report"]')\
            .send_keys(usage_report)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '14_before')
        driver.find_elements(By.CLASS_NAME, 'save-button')[1].click()
        time.sleep(3)
        # search for edited workflow from the Workflow tab
        driver.get(config.base_url + '/workflow/')
        time.sleep(1)
        table = driver.find_element(By.XPATH, '//*[@id="myTabContent"]/div[4]/div/div[1]/table')
        headers_text = [header.text for header in table.find_elements(By.TAG_NAME, 'th')]
        activity_id_idx = headers_text.index('Activity')
        rows = table.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
        for row in rows:
            # the tag of the first of row's cell is 'th', so idx - 1 is correct
            rds = row.find_elements(By.TAG_NAME, 'td')
            if rds[activity_id_idx - 1].text == activity_id:
                rds[activity_id_idx - 1].find_element(By.TAG_NAME, 'a').click()
                time.sleep(3)
                break
        panel_toggles = driver.find_elements(By.CLASS_NAME, 'panel-toggle')
        for pt in panel_toggles:
            if pt.text == 'Usage Report':
                usage_report_location = pt.location
                driver.execute_script(
                    'window.scrollTo(0, ' + str(usage_report_location['y'] - 100) + ')')
                pt.click()
                time.sleep(1)
                break
        target_element = driver.find_element(
            By.XPATH,
            '//*[@id="subitem_restricted_access_usage_report"]')
        assert target_element.get_attribute('value') == usage_report
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '14_after')

        # cancel the workflow to do other tests
        driver.get(config.base_url + '/workflow/activity/detail/' + activity_id)
        time.sleep(3)
        click_quit_btn(driver)
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="btn_cancel"]').click()
        time.sleep(3)

        # download the file 9 times to do other tests
        search_and_display_target_item(driver, config.item_name_dic['scenario_5'])
        for _ in range(9):
            click_detail_item_button(driver)
            time.sleep(1)

        # move downloaded files to do other tests
        move_downloaded_files(['test_scenario_5.txt'], inspect.currentframe().f_code.co_name)
        file_list = os.listdir(config.base_download_dir)
        delete_target_files = [file for file in file_list if file.startswith('test_scenario_5')]
        for file in delete_target_files:
            os.remove(config.base_download_dir + '/' + file)

    # pytest auto_test/test_application_for_use.py::TestScenario5::test_scenario_5_5_15
    def test_scenario_5_5_15(self, driver):
        """Test Scenario 5-5-15
        
        1. The Apply button appears.
        2. The Terms and Conditions modal appears.
        5. Transition to the usage application workflow.
        6. A reminder email is sent to the applicant.
        11. The Download button appears and the registered content is downloaded.
        15. Status is recorded in the workflow tab as aborted.

        User's role is General

        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as General
        login_as_target(driver, 'General')

        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_5'])

        # 1. The Apply button appears.
        # 2. The Terms and Conditions modal appears.
        click_detail_item_button(driver)
        time.sleep(1)

        # 5. Transition to the usage application workflow.
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

        # 6. A reminder email is sent to the applicant.
        driver.find_element(By.CLASS_NAME, 'next-button').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="btn-finish"]').click()
        time.sleep(3)
        activity_id = driver.find_element(By.XPATH, '//*[@id="activity_id"]').text

        # 11. The Download button appears and the registered content is downloaded.
        logout(driver)
        login_as_target(driver, 'Repository')
        driver.get(config.base_url + '/workflow/')
        time.sleep(1)
        table = driver.find_element(By.XPATH, '//*[@id="myTabContent"]/div[4]/div/div[1]/table')
        headers_text = [header.text for header in table.find_elements(By.TAG_NAME, 'th')]
        activity_id_idx = headers_text.index('Activity')
        rows = table.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
        for row in rows:
            # the tag of the first of row's cell is 'th', so idx - 1 is correct
            rds = row.find_elements(By.TAG_NAME, 'td')
            if rds[activity_id_idx - 1].text == activity_id:
                rds[activity_id_idx - 1].find_element(By.TAG_NAME, 'a').click()
                time.sleep(3)
                break
        click_approval_btn(driver)
        time.sleep(3)
        logout(driver)
        login_as_target(driver, 'General')
        search_and_display_target_item(driver, config.item_name_dic['scenario_5'])
        click_detail_item_button(driver)
        time.sleep(1)

        # 15. Status is recorded in the workflow tab as aborted.
        driver.get(config.base_url + '/workflow/')
        time.sleep(1)
        table = driver.find_element(By.XPATH, '//*[@id="myTabContent"]/div[4]/div/div[1]/table')
        headers_text = [header.text for header in table.find_elements(By.TAG_NAME, 'th')]
        activity_id_idx = headers_text.index('Activity')
        workflow_idx = headers_text.index('WorkFlow')
        user_idx = headers_text.index('User')
        rows = table.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
        for row in rows:
            # the tag of the first of row's cell is 'th', so idx - 1 is correct
            rds = row.find_elements(By.TAG_NAME, 'td')
            if rds[workflow_idx - 1].text.startswith('利用報告')\
                and rds[user_idx - 1].text == config.users['General']['mail']:
                rds[activity_id_idx - 1].find_element(By.TAG_NAME, 'a').click()
                time.sleep(3)
                break
        activity_id = driver.find_element(By.XPATH, '//*[@id="activity_id"]').text
        click_quit_btn(driver)
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="btn_cancel"]').click()
        time.sleep(3)
        driver.get(config.base_url + '/workflow/?tab=all')
        time.sleep(1)
        table = driver.find_element(By.XPATH, '//*[@id="myTabContent"]/div[4]/div/div[1]/table')
        headers_text = [header.text for header in table.find_elements(By.TAG_NAME, 'th')]
        activity_id_idx = headers_text.index('Activity')
        status_idx = headers_text.index('Status')
        rows = table.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
        for row in rows:
            # the tag of the first of row's cell is 'th', so idx - 1 is correct
            rds = row.find_elements(By.TAG_NAME, 'td')
            if rds[activity_id_idx - 1].text == activity_id:
                assert rds[status_idx - 1].text == 'Canceled'
                break
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '15')

        # download the file 9 times to do other tests
        search_and_display_target_item(driver, config.item_name_dic['scenario_5'])
        for _ in range(9):
            click_detail_item_button(driver)
            time.sleep(1)

        # move downloaded files to do other tests
        move_downloaded_files(['test_scenario_5.txt'], inspect.currentframe().f_code.co_name)
        file_list = os.listdir(config.base_download_dir)
        delete_target_files = [file for file in file_list if file.startswith('test_scenario_5')]
        for file in delete_target_files:
            os.remove(config.base_download_dir + '/' + file)

    # pytest auto_test/test_application_for_use.py::TestScenario5::test_scenario_5_5_16
    def test_scenario_5_5_16(self, driver):
        """Test Scenario 5-5-16
        
        1. The Apply button appears.
        2. The Terms and Conditions modal appears.
        5. Transition to the usage application workflow.
        6. A reminder email is sent to the applicant.
        16. An approval rejection email is sent to the applicant.
            The status of the action of the usage application changed back to "Item Registration".

        User's role is General

        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as General
        login_as_target(driver, 'General')

        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_5'])

        # 1. The Apply button appears.
        # 2. The Terms and Conditions modal appears.
        click_detail_item_button(driver)
        time.sleep(1)

        # 5. Transition to the usage application workflow.
        modal = driver.find_element(By.CLASS_NAME, 'modal.fade.in')
        modal_id = modal.get_attribute('id')
        next_id = modal_id.replace('term_and_condtion_modal', 'term_next')
        next_btn = modal.find_element(By.XPATH, './/*[@id="' + next_id + '"]')
        check_id = modal_id.replace('term_and_condtion_modal', 'term_checked')
        check_box = modal.find_element(By.XPATH, './/*[@id="' + check_id + '"]')
        check_box.click()
        time.sleep(1)
        next_btn.click()
        time.sleep(3)

        # 6. A reminder email is sent to the applicant.
        driver.find_element(By.CLASS_NAME, 'next-button').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="btn-finish"]').click()
        time.sleep(3)
        activity_id = driver.find_element(By.XPATH, '//*[@id="activity_id"]').text

        # 16. An approval rejection email is sent to the applicant.
        #     The status of the action of the usage application changed back to "Item Registration".
        logout(driver)
        login_as_target(driver, 'Repository')
        driver.get(config.base_url + '/workflow/')
        time.sleep(1)
        table = driver.find_element(By.XPATH, '//*[@id="myTabContent"]/div[4]/div/div[1]/table')
        headers_text = [header.text for header in table.find_elements(By.TAG_NAME, 'th')]
        activity_id_idx = headers_text.index('Activity')
        rows = table.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
        for row in rows:
            # the tag of the first of row's cell is 'th', so idx - 1 is correct
            rds = row.find_elements(By.TAG_NAME, 'td')
            if rds[activity_id_idx - 1].text == activity_id:
                rds[activity_id_idx - 1].find_element(By.TAG_NAME, 'a').click()
                time.sleep(1)
                break
        click_reject_btn(driver)
        time.sleep(3)
        logout(driver)
        login_as_target(driver, 'General')
        driver.get(config.base_url + '/workflow/')
        time.sleep(1)
        table = driver.find_element(By.XPATH, '//*[@id="myTabContent"]/div[4]/div/div[1]/table')
        headers_text = [header.text for header in table.find_elements(By.TAG_NAME, 'th')]
        activity_id_idx = headers_text.index('Activity')
        action_idx = headers_text.index('Action')
        rows = table.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
        for row in rows:
            # the tag of the first of row's cell is 'th', so idx - 1 is correct
            rds = row.find_elements(By.TAG_NAME, 'td')
            if rds[activity_id_idx - 1].text == activity_id:
                assert rds[action_idx - 1].text == 'Item Registration'
                break
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '16')
        assert check_results_of_the_review_mail(
            config.users['General']['mail'],
            config.item_name_dic['scenario_5'],
            activity_id)

    # pytest auto_test/test_application_for_use.py::TestScenario5::test_scenario_5_6
    def test_scenario_5_6(self, driver):
        """Test Scenario 5-6
        
        1. The Apply button appears.
        2. The error message appears.
        
        User is not logged in
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_5'])

        # 1. The Apply button appears.
        assert check_item_button(driver, False)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. The error message appears.
        click_detail_item_button(driver)
        time.sleep(1)
        assert check_error_page(driver)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '2')

# pytest auto_test/test_application_for_use.py::TestScenario6
class TestScenario6:
    """Test Scenario 6
    
    Requirements for item to be used
        - The Providing Method is Usage Application
        - The Providing Role is Guest
        - The Terms and Conditions are voluntary
    """
    # pytest auto_test/test_application_for_use.py::TestScenario6::test_scenario_6_1
    def test_scenario_6_1(self, driver):
        """ Test Scenario 6-1
        
        1. The Download button appears.
        2. Registered content is downloaded.
        3. No "Request for register Data Usage Report" email is sent to the applicant.
        
        User's role is Contributor and the item's owner
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as Contributor
        login_as_target(driver, 'RegCon')

        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_6'])

        # 1. The Download button appears.
        assert check_item_button(driver, True)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. Registered content is downloaded.
        click_detail_item_button(driver)
        time.sleep(1)
        file_list = os.listdir(config.base_download_dir)
        assert 'test_scenario_6.txt' in file_list

        # 3. No "Request for register Data Usage Report" email is sent to the applicant.
        assert not check_request_for_register_mail(
            config.users['RegCon']['mail'],
            config.item_name_dic['scenario_6'])

        # move downloaded file to do other tests
        move_downloaded_files(['test_scenario_6.txt'], inspect.currentframe().f_code.co_name)

    # pytest auto_test/test_application_for_use.py::TestScenario6::test_scenario_6_2
    def test_scenario_6_2(self, driver):
        """ Test Scenario 6-2
        
        1. The Apply button appears.
        2. The error message appears.
        
        User's role is Contributor and not the item's owner
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as Contributor
        login_as_target(driver, 'NoRegCon')

        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_6'])

        # 1. The Apply button appears.
        assert check_item_button(driver, False)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. The error message appears.
        click_detail_item_button(driver)
        time.sleep(1)
        assert check_error_page(driver)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '2')

    # pytest auto_test/test_application_for_use.py::TestScenario6::test_scenario_6_3
    def test_scenario_6_3(self, driver):
        """Test Scenario 6-3
        
        1. The Download button appears.
        2. Registered content is downloaded.
        3. No "Request for register Data Usage Report" email is sent to the applicant.
        
        User's role is Contributor and the item's contributor
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as Contributor
        login_as_target(driver, 'PrxRegCon')

        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_6'])

        # 1. The Download button appears.
        assert check_item_button(driver, True)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. Registered content is downloaded.
        click_detail_item_button(driver)
        time.sleep(1)
        file_list = os.listdir(config.base_download_dir)
        assert 'test_scenario_6.txt' in file_list

        # 3. No "Request for register Data Usage Report" email is sent to the applicant.
        assert not check_request_for_register_mail(
            config.users['PrxRegCon']['mail'],
            config.item_name_dic['scenario_6'])

        # move downloaded file to do other tests
        move_downloaded_files(['test_scenario_6.txt'], inspect.currentframe().f_code.co_name)

    # pytest auto_test/test_application_for_use.py::TestScenario6::test_scenario_6_4
    def test_scenario_6_4(self, driver):
        """Test Scenario 6-4
        
        1. The Apply button appears.
        2. The error message appears.
        
        User's role is Community Administrator
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as Community Administrator
        login_as_target(driver, 'Community')

        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_6'])

        # 1. The Apply button appears.
        assert check_item_button(driver, False)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. The error message appears.
        click_detail_item_button(driver)
        time.sleep(1)
        assert check_error_page(driver)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '2')

    # pytest auto_test/test_application_for_use.py::TestScenario6::test_scenario_6_5
    def test_scenario_6_5(self, driver):
        """Test Scenario 6-5
        
        1. The Apply button appears.
        2. The error message appears.
        
        User's role is General
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as General
        login_as_target(driver, 'General')

        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_6'])

        # 1. The Apply button appears.
        assert check_item_button(driver, False)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. The error message appears.
        click_detail_item_button(driver)
        time.sleep(1)
        assert check_error_page(driver)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '2')

    # pytest auto_test/test_application_for_use.py::TestScenario6::test_scenario_6_6_1_to_3
    def test_scenario_6_6_1_to_3(self, driver):
        """Test Scenario 6-6-1, 6-6-2, 6-6-3
        
        1. The Apply button appears.
        2. The Terms and Conditions modal appears.
        3. The print dialog appears.
        
        User is not logged in
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_6'])

        # 1. The Apply button appears.
        assert check_item_button(driver, False)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. The Terms and Conditions modal appears.
        click_detail_item_button(driver)
        time.sleep(1)
        assert check_terms_and_conditions_modal(driver, '利用申請\nGuest')
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '2')

        # 3. The print dialog appears.
        click_print_btn(driver)
        time.sleep(1)
        window_handles = driver.window_handles
        # after print button clicked, window handles increase
        assert len(window_handles) == 2
        driver.switch_to.window(window_handles[1])
        time.sleep(3)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '3')
        driver.switch_to.window(window_handles[0])
        time.sleep(1)

    # pytest auto_test/test_application_for_use.py::TestScenario6::test_scenario_6_6_4
    def test_scenario_6_6_4(self, driver):
        """Test Scenario 6-6-4
        
        1. The Apply button appears.
        2. The Terms and Conditions modal appears.
        4. Not working before checking the box
        
        User is not logged in
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_6'])

        # 1. The Apply button appears.
        # 2. The Terms and Conditions modal appears.
        click_detail_item_button(driver)
        time.sleep(1)

        # 4. Not working before checking the box
        modal = driver.find_element(By.CLASS_NAME, 'modal.fade.in')
        modal_id = modal.get_attribute('id')
        next_id = modal_id.replace('term_and_condtion_modal', 'term_next')
        next_btn = modal.find_element(By.XPATH, './/*[@id="' + next_id + '"]')
        next_btn.click()
        time.sleep(1)
        email_modal = driver.find_element(By.XPATH, '//*[@id="email_modal"]')
        assert not email_modal.get_attribute('style')

    # pytest auto_test/test_application_for_use.py::TestScenario6::test_scenario_6_6_5_to_8_and_20
    def test_scenario_6_6_5_to_8_and_20(self, driver):
        """Test Scenario 6-6-5, 6-6-6, 6-6-7, 6-6-8, 6-6-20
        
        1. The Apply button appears.
        2. The Terms and Conditions modal appears.
        5. The account entry dialog appears.
        6. "Register Application for Use" email is sent to the applicant.
        7. Transition to the workflow page.
        8. A mail acknowledging receipt of the usage application is sent to the applicant.
        20. An approval rejection email is sent to the applicant.
            The status of the action of the usage application changed back to "Item Registration".
        
        User is not logged in
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_6'])

        # 1. The Apply button appears.
        # 2. The Terms and Conditions modal appears.
        click_detail_item_button(driver)
        time.sleep(1)

        # 5. The account entry dialog appears.
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
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '5')

        # 6. "Register Application for Use" email is sent to the applicant.
        enter_guest_email_for_get_usage_application(driver, config.guest_mail)
        assert check_register_application_mail(
            config.guest_mail,
            'test_scenario_6.txt')

        # 7. Transition to the workflow page.
        lines = get_latest_mail_body(config.guest_mail.split('@', 1)[0])
        url = [line for line in lines if line.startswith('https://')][0]
        driver.get(url)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '7')

        # 8. A mail acknowledging receipt of the usage application is sent to the applicant.
        driver.find_element(By.CLASS_NAME, 'next-button').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="btn-finish"]').click()
        time.sleep(3)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '8')
        activity_id = driver.find_element(By.XPATH, '//*[@id="activity_id"]').text
        assert check_request_for_approval_mail_for_guest(
            config.guest_mail,
            config.item_name_dic['scenario_6'],
            activity_id)

        # 20. An approval rejection email is sent to the applicant.
        #     The status of the action of the usage application changed back to "Item Registration".
        login_as_target(driver, 'Repository')
        driver.get(config.base_url + '/workflow/')
        time.sleep(1)
        table = driver.find_element(By.XPATH, '//*[@id="myTabContent"]/div[4]/div/div[1]/table')
        headers_text = [header.text for header in table.find_elements(By.TAG_NAME, 'th')]
        activity_id_idx = headers_text.index('Activity')
        rows = table.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
        for row in rows:
            # the tag of the first of row's cell is 'th', so idx - 1 is correct
            rds = row.find_elements(By.TAG_NAME, 'td')
            if rds[activity_id_idx - 1].text == activity_id:
                rds[activity_id_idx - 1].find_element(By.TAG_NAME, 'a').click()
                time.sleep(3)
                break
        click_reject_btn(driver)
        time.sleep(3)
        driver.get(config.base_url + '/workflow/')
        time.sleep(1)
        table = driver.find_element(By.XPATH, '//*[@id="myTabContent"]/div[4]/div/div[1]/table')
        headers_text = [header.text for header in table.find_elements(By.TAG_NAME, 'th')]
        activity_id_idx = headers_text.index('Activity')
        action_idx = headers_text.index('Action')
        rows = table.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
        for row in rows:
            # the tag of the first of row's cell is 'th', so idx - 1 is correct
            rds = row.find_elements(By.TAG_NAME, 'td')
            if rds[activity_id_idx - 1].text == activity_id:
                assert rds[action_idx - 1].text == 'Item Registration'
                break
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '20')
        assert check_results_of_the_review_mail_for_guest(
            config.guest_mail,
            config.item_name_dic['scenario_6'],
            activity_id)

        # cancel the workflow to do other tests
        logout(driver)
        driver.get(url)
        time.sleep(3)
        click_quit_btn(driver)
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="btn_cancel"]').click()

    # pytest auto_test/test_application_for_use.py::TestScenario6::test_scenario_6_6_9
    def test_scenario_6_6_9(self, driver):
        """Test Scenario 6-6-9
        
        1. The Apply button appears.
        2. The Terms and Conditions modal appears.
        5. The account entry dialog appears.
        6. "Register Application for Use" email is sent to the applicant.
        7. Transition to the workflow page.
        9. A mail acknowledging receipt of the usage application is sent to the applicant.
        
        User is not logged in
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_6'])

        # 1. The Apply button appears.
        # 2. The Terms and Conditions modal appears.
        click_detail_item_button(driver)
        time.sleep(1)

        # 5. The account entry dialog appears.
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

        # 6. "Register Application for Use" email is sent to the applicant.
        # 7. Transition to the workflow page.
        enter_guest_email_for_get_usage_application(driver, config.guest_mail)
        lines = get_latest_mail_body(config.guest_mail.split('@', 1)[0])
        url = [line for line in lines if line.startswith('https://')][0]
        driver.get(url)
        time.sleep(3)

        # 9. A mail acknowledging receipt of the usage application is sent to the applicant.
        driver.find_element(By.CLASS_NAME, 'back-button').click()
        time.sleep(3)
        driver.get(url)
        time.sleep(3)
        driver.find_element(By.CLASS_NAME, 'next-button').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="btn-finish"]').click()
        time.sleep(3)
        activity_id = driver.find_element(By.XPATH, '//*[@id="activity_id"]').text
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '9')
        assert check_request_for_approval_mail_for_guest(
            config.guest_mail,
            config.item_name_dic['scenario_6'],
            activity_id)

        # cancel the workflow to do other tests
        login_as_target(driver, 'Repository')
        driver.get(config.base_url + '/workflow/activity/detail/' + activity_id)
        time.sleep(3)
        click_quit_btn(driver)
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="btn_cancel"]').click()

    # pytest auto_test/test_application_for_use.py::TestScenario6::test_scenario_6_6_10
    def test_scenario_6_6_10(self, driver):
        """Test Scenario 6-6-10
        
        1. The Apply button appears.
        2. The Terms and Conditions modal appears.
        5. The account entry dialog appears.
        6. "Register Application for Use" email is sent to the applicant.
        7. Transition to the workflow page.
        10. Transition to the workflow with input retained.

        User is not logged in

        Args:
            driver(WebDriver): WebDriver object
        """
        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_6'])

        # 1. The Apply button appears.
        # 2. The Terms and Conditions modal appears.
        click_detail_item_button(driver)
        time.sleep(1)

        # 5. The account entry dialog appears.
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

        # 6. "Register Application for Use" email is sent to the applicant.
        # 7. Transition to the workflow page.
        enter_guest_email_for_get_usage_application(driver, config.guest_mail)
        lines = get_latest_mail_body(config.guest_mail.split('@', 1)[0])
        url = [line for line in lines if line.startswith('https://')][0]
        driver.get(url)
        time.sleep(3)

        # 10. Transition to the workflow with input retained.
        # edit target is Research Title
        before_activity_id = driver.find_element(By.XPATH, '//*[@id="activity_id"]').text
        panel_toggles = driver.find_elements(By.CLASS_NAME, 'panel-toggle')
        for pt in panel_toggles:
            if pt.text == 'Research Title':
                research_title_location = pt.location
                driver.execute_script(
                    'window.scrollTo(0, ' + str(research_title_location['y'] - 100) + ')')
                pt.click()
                time.sleep(1)
                break
        research_title = 'test research'
        driver.find_element(By.XPATH, '//*[@id="subitem_restricted_access_research_title"]')\
            .send_keys(research_title)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '10_before')
        driver.find_elements(By.CLASS_NAME, 'save-button')[1].click()
        time.sleep(3)
        # execute 6-6-1, 6-6-2, 6-6-5 and 6-6-6 again
        search_and_display_target_item(driver, config.item_name_dic['scenario_6'])
        click_detail_item_button(driver)
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
        time.sleep(3)
        after_activity_id = driver.find_element(By.XPATH, '//*[@id="activity_id"]').text
        assert before_activity_id == after_activity_id
        panel_toggles = driver.find_elements(By.CLASS_NAME, 'panel-toggle')
        for pt in panel_toggles:
            if pt.text == 'Research Title':
                research_title_location = pt.location
                driver.execute_script(
                    'window.scrollTo(0, ' + str(research_title_location['y'] - 100) + ')')
                pt.click()
                time.sleep(1)
                break
        target_element = driver.find_element(
            By.XPATH,
            '//*[@id="subitem_restricted_access_research_title"]')
        assert target_element.get_attribute('value') == research_title
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '10_after')

        # cancel the workflow to do other tests
        click_quit_btn(driver)
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="btn_cancel"]').click()

    # pytest auto_test/test_application_for_use.py::TestScenario6::test_scenario_6_6_11
    def test_scenario_6_6_11(self, driver):
        """Test Scenario 6-6-11
        
        1. The Apply button appears.
        2. The Terms and Conditions modal appears.
        5. The account entry dialog appears.
        6. "Register Application for Use" email is sent to the applicant.
        7. Transition to the workflow page.
        11. Transition to the new usage application workflow.
        
        User is not logged in
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_6'])

        # 1. The Apply button appears.
        # 2. The Terms and Conditions modal appears.
        click_detail_item_button(driver)
        time.sleep(1)

        # 5. The account entry dialog appears.
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

        # 6. "Register Application for Use" email is sent to the applicant.
        # 7. Transition to the workflow page.
        enter_guest_email_for_get_usage_application(driver, config.guest_mail)
        lines = get_latest_mail_body(config.guest_mail.split('@', 1)[0])
        url = [line for line in lines if line.startswith('https://')][0]
        driver.get(url)
        time.sleep(3)

        # 11. Transition to the new usage application workflow.
        # edit target is Research Title
        before_activity_id = driver.find_element(By.XPATH, '//*[@id="activity_id"]').text
        panel_toggles = driver.find_elements(By.CLASS_NAME, 'panel-toggle')
        for pt in panel_toggles:
            if pt.text == 'Research Title':
                research_title_location = pt.location
                driver.execute_script(
                    'window.scrollTo(0, ' + str(research_title_location['y'] - 100) + ')')
                pt.click()
                time.sleep(1)
                break
        research_title = 'test research'
        driver.find_element(By.XPATH, '//*[@id="subitem_restricted_access_research_title"]')\
            .send_keys(research_title)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '11_before')
        click_quit_btn(driver)
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="btn_cancel"]').click()
        time.sleep(3)
        # execute 6-6-1, 6-6-2, 6-6-5 and 6-6-6 again
        search_and_display_target_item(driver, config.item_name_dic['scenario_6'])
        click_detail_item_button(driver)
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
        time.sleep(3)
        after_activity_id = driver.find_element(By.XPATH, '//*[@id="activity_id"]').text
        assert before_activity_id != after_activity_id
        panel_toggles = driver.find_elements(By.CLASS_NAME, 'panel-toggle')
        for pt in panel_toggles:
            if pt.text == 'Research Title':
                research_title_location = pt.location
                driver.execute_script(
                    'window.scrollTo(0, ' + str(research_title_location['y'] - 100) + ')')
                pt.click()
                time.sleep(1)
                break
        target_element = driver.find_element(
            By.XPATH,
            '//*[@id="subitem_restricted_access_research_title"]')
        assert target_element.get_attribute('value') != research_title
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '11_after')

        # cancel the workflow to do other tests
        click_quit_btn(driver)
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="btn_cancel"]').click()

    # pytest auto_test/test_application_for_use.py::TestScenario6::test_scenario_6_6_12_to_17
    def test_scenario_6_6_12_to_17(self, driver):
        """Test Scenario 6-6-12, 6-6-13, 6-6-14, 6-6-15, 6-6-16, 6-6-17
        
        1. The Apply button appears.
        2. The Terms and Conditions modal appears.
        5. The account entry dialog appears.
        6. "Register Application for Use" email is sent to the applicant.
        7. Transition to the workflow page.
        8. A mail acknowledging receipt of the usage application is sent to the applicant.
        12. The usage application workflow with the action status "Approval" is displayed.
        13. An approval notification email is sent to the applicant.
        14. The error message appears.
        15. Registered content is downloaded.
        16. "Request for register Data Usage Report" email is sent to the applicant.
        17. "Your Application was Received" email is sent to the applicant.

        User is not logged in

        Args:
            driver(WebDriver): WebDriver object
        """
        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_6'])

        # 1. The Apply button appears.
        # 2. The Terms and Conditions modal appears.
        click_detail_item_button(driver)
        time.sleep(1)

        # 5. The account entry dialog appears.
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

        # 6. "Register Application for Use" email is sent to the applicant.
        # 7. Transition to the workflow page.
        enter_guest_email_for_get_usage_application(driver, config.guest_mail)
        lines = get_latest_mail_body(config.guest_mail.split('@', 1)[0])
        url = [line for line in lines if line.startswith('https://')][0]
        driver.get(url)
        time.sleep(3)

        # 8. A mail acknowledging receipt of the usage application is sent to the applicant.
        driver.find_element(By.CLASS_NAME, 'next-button').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="btn-finish"]').click()
        time.sleep(3)
        activity_id = driver.find_element(By.XPATH, '//*[@id="activity_id"]').text

        # 12. The usage application workflow with the action status "Approval" is displayed.
        login_as_target(driver, 'Repository')
        driver.get(config.base_url + '/workflow/')
        time.sleep(1)
        table = driver.find_element(By.XPATH, '//*[@id="myTabContent"]/div[4]/div/div[1]/table')
        headers_text = [header.text for header in table.find_elements(By.TAG_NAME, 'th')]
        activity_id_idx = headers_text.index('Activity')
        action_idx = headers_text.index('Action')
        rows = table.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
        target_element = None
        for row in rows:
            # the tag of the first of row's cell is 'th', so idx - 1 is correct
            rds = row.find_elements(By.TAG_NAME, 'td')
            if rds[activity_id_idx - 1].text == activity_id:
                assert rds[action_idx - 1].text == 'Approval'
                target_element = rds[activity_id_idx - 1]
                break
        assert target_element, 'Could not get target workflow'
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '12')

        # 13. An approval notification email is sent to the applicant.
        target_element.find_element(By.TAG_NAME, 'a').click()
        time.sleep(3)
        click_approval_btn(driver)
        WebDriverWait(driver, 10).until(
            lambda d: len(d.find_elements(
                By.XPATH, '//*[@id="myTabContent"]/div[2]/div[2]/button[2]')) > 0
        )
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '13')
        assert check_approved_application_mail_for_guest(
            config.guest_mail,
            config.item_name_dic['scenario_6'],
            activity_id)

        # 14. The error message appears.
        logout(driver)
        lines = get_latest_mail_body(config.guest_mail.split('@', 1)[0])
        url = [line for line in lines if line.startswith('https://')][0]
        driver.get(url)
        time.sleep(3)
        enter_guest_email_after_approval(driver, config.users['General']['mail'])
        time.sleep(1)
        alert = driver.switch_to.alert
        alert_msg = alert.text
        assert alert_msg == config.cannot_download_msg
        alert.accept()

        # 15. Registered content is downloaded.
        driver.get(url)
        time.sleep(3)
        enter_guest_email_after_approval(driver, config.guest_mail)
        time.sleep(3)
        file_list = os.listdir(config.base_download_dir)
        assert 'test_scenario_6.txt' in file_list

        # 16. "Request for register Data Usage Report" email is sent to the applicant.
        assert check_request_for_register_mail(
            config.guest_mail,
            config.item_name_dic['scenario_6'],
            activity_id)

        # 17. "Your Application was Received" email is sent to the applicant.
        lines = get_latest_mail_body(config.guest_mail.split('@', 1)[0])
        url = [line for line in lines if line.startswith('https://')][0]
        driver.get(url)
        time.sleep(3)
        driver.find_element(By.CLASS_NAME, 'next-button').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="btn-finish"]').click()
        time.sleep(3)
        activity_id = driver.find_element(By.XPATH, '//*[@id="activity_id"]').text
        assert check_received_application_mail(
            config.guest_mail,
            config.item_name_dic['scenario_6'],
            activity_id)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '17')

        # cancel the workflow to do other tests
        login_as_target(driver, 'Repository')
        driver.get(config.base_url + '/workflow/activity/detail/' + activity_id)
        time.sleep(3)
        click_quit_btn(driver)
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="btn_cancel"]').click()

        # move downloaded file to do other tests
        move_downloaded_files(['test_scenario_6.txt'], inspect.currentframe().f_code.co_name)

    # pytest auto_test/test_application_for_use.py::TestScenario6::test_scenario_6_6_18
    def test_scenario_6_6_18(self, driver):
        """Test Scenario 6-6-18
        
        1. The Apply button appears.
        2. The Terms and Conditions modal appears.
        5. The account entry dialog appears.
        6. "Register Application for Use" email is sent to the applicant.
        7. Transition to the workflow page.
        8. A mail acknowledging receipt of the usage application is sent to the applicant.
        12. The usage application workflow with the action status "Approval" is displayed.
        13. An approval notification email is sent to the applicant.
        15. Registered content is downloaded.
        18. Transition to the workflow with input retained.
        
        User is not logged in
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_6'])

        # 1. The Apply button appears.
        # 2. The Terms and Conditions modal appears.
        click_detail_item_button(driver)
        time.sleep(1)

        # 5. The account entry dialog appears.
        modal = driver.find_element(By.CLASS_NAME, 'modal.fade.in')
        modal_id = modal.get_attribute('id')
        next_id = modal_id.replace('term_and_condtion_modal', 'term_next')
        next_btn = modal.find_element(By.XPATH, './/*[@id="' + next_id + '"]')
        check_id = modal_id.replace('term_and_condtion_modal', 'term_checked')
        check_box = modal.find_element(By.XPATH, './/*[@id="' + check_id + '"]')
        check_box.click()
        time.sleep(1)
        next_btn.click()

        # 6. "Register Application for Use" email is sent to the applicant.
        # 7. Transition to the workflow page.
        enter_guest_email_for_get_usage_application(driver, config.guest_mail)
        lines = get_latest_mail_body(config.guest_mail.split('@', 1)[0])
        url = [line for line in lines if line.startswith('https://')][0]
        driver.get(url)
        time.sleep(3)

        # 8. A mail acknowledging receipt of the usage application is sent to the applicant.
        driver.find_element(By.CLASS_NAME, 'next-button').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="btn-finish"]').click()
        time.sleep(3)
        activity_id = driver.find_element(By.XPATH, '//*[@id="activity_id"]').text

        # 12. The usage application workflow with the action status "Approval" is displayed.
        login_as_target(driver, 'Repository')
        driver.get(config.base_url + '/workflow/')
        time.sleep(1)
        table = driver.find_element(By.XPATH, '//*[@id="myTabContent"]/div[4]/div/div[1]/table')
        headers_text = [header.text for header in table.find_elements(By.TAG_NAME, 'th')]
        activity_id_idx = headers_text.index('Activity')
        rows = table.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
        for row in rows:
            # the tag of the first of row's cell is 'th', so idx - 1 is correct
            rds = row.find_elements(By.TAG_NAME, 'td')
            if rds[activity_id_idx - 1].text == activity_id:
                rds[activity_id_idx - 1].find_element(By.TAG_NAME, 'a').click()
                time.sleep(3)
                break

        # 13. An approval notification email is sent to the applicant.
        click_approval_btn(driver)
        time.sleep(3)

        # 15. Registered content is downloaded.
        logout(driver)
        lines = get_latest_mail_body(config.guest_mail.split('@', 1)[0])
        url = [line for line in lines if line.startswith('https://')][0]
        driver.get(url)
        time.sleep(3)
        enter_guest_email_after_approval(driver, config.guest_mail)
        time.sleep(3)

        # 18. Transition to the workflow with input retained.
        # edit target is Usage Report
        lines = get_latest_mail_body(config.guest_mail.split('@', 1)[0])
        url = [line for line in lines if line.startswith('https://')][0]
        driver.get(url)
        time.sleep(3)
        panel_toggles = driver.find_elements(By.CLASS_NAME, 'panel-toggle')
        for pt in panel_toggles:
            if pt.text == 'Usage Report':
                usage_report_location = pt.location
                driver.execute_script(
                    'window.scrollTo(0, ' + str(usage_report_location['y'] - 100) + ')')
                pt.click()
                time.sleep(1)
                break
        usage_report = 'test usage report'
        driver.find_element(By.XPATH, '//*[@id="subitem_restricted_access_usage_report"]')\
            .send_keys(usage_report)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '18_before')
        driver.find_elements(By.CLASS_NAME, 'save-button')[1].click()
        time.sleep(3)
        # reaccess to the workflow
        driver.get(url)
        time.sleep(3)
        panel_toggles = driver.find_elements(By.CLASS_NAME, 'panel-toggle')
        for pt in panel_toggles:
            if pt.text == 'Usage Report':
                usage_report_location = pt.location
                driver.execute_script(
                    'window.scrollTo(0, ' + str(usage_report_location['y'] - 100) + ')')
                pt.click()
                time.sleep(1)
                break
        target_element = driver.find_element(
            By.XPATH,
            '//*[@id="subitem_restricted_access_usage_report"]')
        assert target_element.get_attribute('value') == usage_report
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '18_after')

        # cancel the workflow to do other tests
        click_quit_btn(driver)
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="btn_cancel"]').click()

        # move downloaded file to do other tests
        move_downloaded_files(['test_scenario_6.txt'], inspect.currentframe().f_code.co_name)

    # pytest auto_test/test_application_for_use.py::TestScenario6::test_scenario_6_6_19
    def test_scenario_6_6_19(self, driver):
        """Test Scenario 6-6-19
        
        1. The Apply button appears.
        2. The Terms and Conditions modal appears.
        5. The account entry dialog appears.
        6. "Register Application for Use" email is sent to the applicant.
        7. Transition to the workflow page.
        8. A mail acknowledging receipt of the usage application is sent to the applicant.
        12. The usage application workflow with the action status "Approval" is displayed.
        13. An approval notification email is sent to the applicant.
        15. Registered content is downloaded.
        19. The status of the target workflow is "Canceled"

        User is not logged in

        Args:
            driver(WebDriver): WebDriver object
        """
        # search target item
        search_and_display_target_item(driver, config.item_name_dic['scenario_6'])

        # 1. The Apply button appears.
        # 2. The Terms and Conditions modal appears.
        click_detail_item_button(driver)
        time.sleep(1)

        # 5. The account entry dialog appears.
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

        # 6. "Register Application for Use" email is sent to the applicant.
        # 7. Transition to the workflow page.
        enter_guest_email_for_get_usage_application(driver, config.guest_mail)
        lines = get_latest_mail_body(config.guest_mail.split('@', 1)[0])
        url = [line for line in lines if line.startswith('https://')][0]
        driver.get(url)
        time.sleep(3)

        # 8. A mail acknowledging receipt of the usage application is sent to the applicant.
        driver.find_element(By.CLASS_NAME, 'next-button').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="btn-finish"]').click()
        time.sleep(3)
        activity_id = driver.find_element(By.XPATH, '//*[@id="activity_id"]').text

        # 12. The usage application workflow with the action status "Approval" is displayed.
        login_as_target(driver, 'Repository')
        driver.get(config.base_url + '/workflow/')
        time.sleep(1)
        table = driver.find_element(By.XPATH, '//*[@id="myTabContent"]/div[4]/div/div[1]/table')
        headers_text = [header.text for header in table.find_elements(By.TAG_NAME, 'th')]
        activity_id_idx = headers_text.index('Activity')
        rows = table.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
        for row in rows:
            # the tag of the first of row's cell is 'th', so idx - 1 is correct
            rds = row.find_elements(By.TAG_NAME, 'td')
            if rds[activity_id_idx - 1].text == activity_id:
                rds[activity_id_idx - 1].find_element(By.TAG_NAME, 'a').click()
                time.sleep(3)
                break

        # 13. An approval notification email is sent to the applicant.
        click_approval_btn(driver)
        time.sleep(3)

        # 15. Registered content is downloaded.
        logout(driver)
        lines = get_latest_mail_body(config.guest_mail.split('@', 1)[0])
        url = [line for line in lines if line.startswith('https://')][0]
        driver.get(url)
        time.sleep(3)
        enter_guest_email_after_approval(driver, config.guest_mail)
        time.sleep(3)

        # 19. The status of the target workflow is "Canceled"
        lines = get_latest_mail_body(config.guest_mail.split('@', 1)[0])
        url = [line for line in lines if line.startswith('https://')][0]
        driver.get(url)
        time.sleep(3)
        activity_id = driver.find_element(By.XPATH, '//*[@id="activity_id"]').text
        click_quit_btn(driver)
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="btn_cancel"]').click()
        time.sleep(3)
        login_as_target(driver, 'Repository')
        driver.get(config.base_url + '/workflow/?tab=all')
        time.sleep(1)
        table = driver.find_element(By.XPATH, '//*[@id="myTabContent"]/div[4]/div/div[1]/table')
        headers_text = [header.text for header in table.find_elements(By.TAG_NAME, 'th')]
        activity_id_idx = headers_text.index('Activity')
        status_idx = headers_text.index('Status')
        rows = table.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
        for row in rows:
            # the tag of the first of row's cell is 'th', so idx - 1 is correct
            rds = row.find_elements(By.TAG_NAME, 'td')
            if rds[activity_id_idx - 1].text == activity_id:
                assert rds[status_idx - 1].text == 'Canceled'
                break
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '19')

        # move downloaded file to do other tests
        move_downloaded_files(['test_scenario_6.txt'], inspect.currentframe().f_code.co_name)

def login_as_target(driver, target_key: str):
    """Log in as target user
    
    Args:
        driver(WebDriver): WebDriver object
        target_key(str): target user's key in config
    """
    # set login_user from config
    login_user = config.users[target_key]
    # log in as target user
    login(driver, login_user['mail'], login_user['password'])

def check_item_button(driver, is_download: bool):
    """Check the button of the target item
    
    Args:
        driver(WebDriver): WebDriver object
        is_download(bool): True if the button is download, False if the button is apply
    """
    # set expected button text
    expected_button_text = 'Download' if is_download else 'Apply'

    # get button element
    button = driver.find_element(
        By.XPATH, '//*[@id="detail-item"]/table/tbody/tr/td[3]/a[1]')

    # check the button text
    return button.text == expected_button_text

def check_error_page(driver):
    """Check the error page
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # check modal and error message
    modals = driver.find_elements(By.XPATH, '//*[@id="allModal"]')
    modal_assert = len(modals) == 1
    err_msg = driver.find_element(By.XPATH, '//*[@id="inputModal"]')
    msg_assert = err_msg.text == config.application_for_use_error_msg
    return modal_assert and msg_assert

def check_terms_and_conditions_modal(driver, terms_text: str):
    """Check the Terms and Conditions modal
    
    Args:
        driver(WebDriver): WebDriver object
        terms_text(str): terms and conditions
    """
    # get modal elements
    modal = driver.find_element(By.CLASS_NAME, 'modal.fade.in')
    header = modal.find_element(By.XPATH, './/*[@id="exampleModalLongTitle"]')
    terms = modal.find_element(By.XPATH, './/*[@id="terms"]')
    header_assert = header.text == 'Terms and Conditions'
    terms_assert = terms.text == terms_text
    return header_assert and terms_assert

def check_request_for_register_mail(
        mail_address: str,
        target_item_name: str,
        activity_id: str = None):
    """Check the latest email

    for Request for register Data Usage Report
    
    Args:
        mail_address(str): recipient's email address
        target_item_name(str): target item's name
        activity_id(str): activity id
    """
    # get the latest email
    target_user_name = mail_address.split('@')[0]
    lines = get_latest_mail_body(target_user_name)

    # get the email title
    sub_list = get_mail_subject(lines)

    # decode and check the email title
    if decode_mail_subject(sub_list) == config.mail_subjects['request_for_register']:
        # check recipient's address
        recipient = [line for line in lines if line.startswith('To: ')][0]
        if recipient.split(' ')[1] == mail_address:
            # check the email body
            body_activity_id = [line for line in lines if line.startswith('申請番号：')]
            body_mail_address = [line for line in lines if line.startswith('メールアドレス：')]
            usage_data = [line for line in lines if line.startswith('申請データ：')]
            download_date = [line for line in lines if line.startswith('申請年月日：')]
            if compare_the_two_elements(mail_address, body_mail_address)\
                and compare_the_two_elements(target_item_name, usage_data)\
                and compare_the_two_elements(
                    datetime.datetime.today().strftime('%Y-%m-%d'),
                    download_date):
                if activity_id:
                    return compare_the_two_elements(activity_id, body_activity_id)
                return True
    return False

def check_request_for_approval_mail(mail_address: str, target_item_name: str, activity_id: str):
    """Check the latest email

    for Request for Approval of Application for Use
    
    Args:
        mail_address(str): recipient's email address
        target_item_name(str): target item's name
        activity_id(str): activity id
    """
    # get the latest mail
    target_user_name = config.users['Repository']['mail'].split('@', 1)[0]
    lines = get_latest_mail_body(target_user_name)

    # get the email title
    sub_list = get_mail_subject(lines)

    # decode and check the email title
    if decode_mail_subject(sub_list) == config.mail_subjects['request_for_approval']:
        # check recipient's address
        recipient = [line for line in lines if line.startswith('To: ')][0]
        if recipient.split(' ')[1] == config.users['Repository']['mail']:
            # check the email body
            body_activity_id = [line for line in lines if line.startswith('申請番号：')]
            body_mail_address = [line for line in lines if line.startswith('メールアドレス：')]
            request_data = [line for line in lines if line.startswith('申請データ：')]
            request_date = [line for line in lines if line.startswith('申請年月日：')]
            if compare_the_two_elements(activity_id, body_activity_id)\
                and compare_the_two_elements(mail_address, body_mail_address)\
                and compare_the_two_elements(target_item_name, request_data)\
                and compare_the_two_elements(
                    datetime.datetime.today().strftime('%Y-%m-%d'),
                    request_date):
                return True
    return False

def check_request_for_approval_mail_for_guest(
        mail_address: str,
        target_item_name: str,
        activity_id: str
    ):
    """Check the latest email
    
    for Request for Approval of Application for Use (for guest user)
    
    Args:
        mail_address(str): recipient's email address
        target_item_name(str): target item's name
        activity_id(str): activity id
    """
    # get the latest mail
    target_user_name = config.users['Repository']['mail'].split('@', 1)[0]
    lines = get_latest_mail_body(target_user_name)

    # get the email title
    sub_list = get_mail_subject(lines)

    # decode and check the email title
    if decode_mail_subject(sub_list) == config.mail_subjects['request_for_approval_for_guest']:
        # check recipient's address
        recipient = [line for line in lines if line.startswith('To: ')][0]
        if recipient.split(' ')[1] == config.users['Repository']['mail']:
            # check the email body
            body_activity_id = [line for line in lines if line.startswith('申請番号：')]
            body_mail_address = [line for line in lines if line.startswith('メールアドレス：')]
            request_data = [line for line in lines if line.startswith('申請データ：')]
            request_date = [line for line in lines if line.startswith('申請年月日：')]
            if compare_the_two_elements(activity_id, body_activity_id)\
                and compare_the_two_elements(mail_address, body_mail_address)\
                and compare_the_two_elements(target_item_name, request_data)\
                and compare_the_two_elements(
                    datetime.datetime.today().strftime('%Y-%m-%d'),
                    request_date):
                return True
    return False

def check_approved_application_mail(mail_address: str, target_item_name: str, activity_id: str):
    """Check the latest email
    
    for Your application was approved  （for logged in users）
    
    Args:
        mail_address(str): recipient's email address
        target_item_name(str): target item's name
        activity_id(str): activity id
    """
    # get the latest mail
    target_user_name = mail_address.split('@')[0]
    lines = get_latest_mail_body(target_user_name)

    # get the email title
    sub_list = get_mail_subject(lines)

    # decode and check the email title
    if decode_mail_subject(sub_list) == config.mail_subjects['approved_application']:
        # check recipient's address
        recipient = [line for line in lines if line.startswith('To: ')][0]
        if recipient.split(' ')[1] == mail_address:
            # check the email body
            body_activity_id = [line for line in lines if line.startswith('申請番号：')]
            body_mail_address = [line for line in lines if line.startswith('メールアドレス：')]
            request_data = [line for line in lines if line.startswith('申請データ：')]
            request_date = [line for line in lines if line.startswith('申請年月日：')]
            if compare_the_two_elements(activity_id, body_activity_id)\
                and compare_the_two_elements(mail_address, body_mail_address)\
                and compare_the_two_elements(target_item_name, request_data)\
                and compare_the_two_elements(
                    datetime.datetime.today().strftime('%Y-%m-%d'),
                    request_date):
                return True
    return False

def check_approved_application_mail_for_guest(
    mail_address: str,
    target_item_name: str,
    activity_id: str):
    """Check the latest email
    
    for Guest''s application was approved （for guest user）
    
    Args:
        mail_address(str): recipient's email address
        target_item_name(str): target item's name
        activity_id(str): activity id
    """
    # get the latest mail
    target_user_name = mail_address.split('@')[0]
    lines = get_latest_mail_body(target_user_name)

    # get the email title
    sub_list = get_mail_subject(lines)

    # decode and check the email title
    if decode_mail_subject(sub_list) == config.mail_subjects['approved_application_for_guest']:
        # check recipient's address
        recipient = [line for line in lines if line.startswith('To: ')][0]
        if recipient.split(' ')[1] == mail_address:
            # check the email body
            body_activity_id = [line for line in lines if line.startswith('申請番号：')]
            body_mail_address = [line for line in lines if line.startswith('メールアドレス：')]
            request_data = [line for line in lines if line.startswith('申請データ：')]
            request_date = [line for line in lines if line.startswith('申請年月日：')]
            if compare_the_two_elements(activity_id, body_activity_id)\
                and compare_the_two_elements(mail_address, body_mail_address)\
                and compare_the_two_elements(target_item_name, request_data)\
                and compare_the_two_elements(
                    datetime.datetime.today().strftime('%Y-%m-%d'),
                    request_date):
                return True
    return False

def check_results_of_the_review_mail(mail_address: str, target_item_name: str, activity_id: str):
    """Check the latest email
    
    for The results of the review of your application
    
    Args:
        mail_address(str): recipient's email address
        target_item_name(str): target item's name
        activity_id(str): activity id
    """
    # get the latest mail
    target_user_name = mail_address.split('@')[0]
    lines = get_latest_mail_body(target_user_name)

    # get the email title
    sub_list = get_mail_subject(lines)

    # decode and check the email title
    if decode_mail_subject(sub_list) == config.mail_subjects['results_of_the_review']:
        # check recipient's address
        recipient = [line for line in lines if line.startswith('To: ')][0]
        if recipient.split(' ')[1] == mail_address:
            # check the email body
            body_activity_id = [line for line in lines if line.startswith('申請番号：')]
            body_mail_address = [line for line in lines if line.startswith('メールアドレス：')]
            request_data = [line for line in lines if line.startswith('申請データ：')]
            request_date = [line for line in lines if line.startswith('申請年月日：')]
            if compare_the_two_elements(activity_id, body_activity_id)\
                and compare_the_two_elements(mail_address, body_mail_address)\
                and compare_the_two_elements(target_item_name, request_data)\
                and compare_the_two_elements(
                    datetime.datetime.today().strftime('%Y-%m-%d'),
                    request_date):
                return True
    return False

def check_results_of_the_review_mail_for_guest(
        mail_address: str,
        target_item_name: str,
        activity_id: str):
    """Check the latest email
    
    for The results of the review of your application (for guest user)

    Args:
        mail_address(str): recipient's email address
        target_item_name(str): target item's name
        activity_id(str): activity id
    """
    # get the latest mail
    target_user_name = mail_address.split('@')[0]
    lines = get_latest_mail_body(target_user_name)

    # get the email title
    sub_list = get_mail_subject(lines)

    # decode and check the email title
    if decode_mail_subject(sub_list) == config.mail_subjects['results_of_the_review_for_guest']:
        # check recipient's address
        recipient = [line for line in lines if line.startswith('To: ')][0]
        if recipient.split(' ')[1] == mail_address:
            # check the email body
            body_activity_id = [line for line in lines if line.startswith('申請番号：')]
            body_mail_address = [line for line in lines if line.startswith('メールアドレス：')]
            request_data = [line for line in lines if line.startswith('申請データ：')]
            request_date = [line for line in lines if line.startswith('申請年月日：')]
            if compare_the_two_elements(activity_id, body_activity_id)\
                and compare_the_two_elements(mail_address, body_mail_address)\
                and compare_the_two_elements(target_item_name, request_data)\
                and compare_the_two_elements(
                    datetime.datetime.today().strftime('%Y-%m-%d'),
                    request_date):
                return True
    return False

def check_received_application_mail(mail_address: str, target_item_name: str, activity_id: str):
    """Check the latest email
    
    for Your Application was Received
    
    Args:
        mail_address(str): recipient's email address
        target_item_name(str): target item's name
        activity_id(str): activity id
    """
    # get the latest mail
    target_user_name = mail_address.split('@')[0]
    lines = get_latest_mail_body(target_user_name)

    # get the email title
    sub_list = get_mail_subject(lines)

    # decode and check the email title
    if decode_mail_subject(sub_list) == config.mail_subjects['received_application']:
        # check recipient's address
        recipient = [line for line in lines if line.startswith('To: ')][0]
        if recipient.split(' ')[1] == mail_address:
            # check the email body
            body_activity_id = [line for line in lines if line.startswith('申請番号：')]
            body_mail_address = [line for line in lines if line.startswith('メールアドレス：')]
            request_data = [line for line in lines if line.startswith('申請データ：')]
            request_date = [line for line in lines if line.startswith('申請年月日：')]
            if compare_the_two_elements(activity_id, body_activity_id)\
                and compare_the_two_elements(mail_address, body_mail_address)\
                and compare_the_two_elements(target_item_name, request_data)\
                and compare_the_two_elements(
                    datetime.datetime.today().strftime('%Y-%m-%d'),
                    request_date):
                return True
    return False

def check_register_application_mail(mail_address: str, target_file_name: str):
    """Check the latest email
    
    for Register Application for Use
    
    Args:
        mail_address(str): recipient's email address
        target_file_name(str): target file name
    """
    # get the latest mail
    target_user_name = mail_address.split('@')[0]
    lines = get_latest_mail_body(target_user_name)

    # get the email title
    sub_list = get_mail_subject(lines)

    # decode and check the email title
    if decode_mail_subject(sub_list) == config.mail_subjects['register_application']:
        # check recipient's address
        recipient = [line for line in lines if line.startswith('To: ')][0]
        if recipient.split(' ')[1] == mail_address:
            # check the email body
            url = [line for line in lines if line.startswith('https://')][0]
            return url.find(target_file_name) != -1
    return False

def get_mail_subject(lines: list[str]):
    """Get the email subject
    
    Args:
        lines(list[str]): email lines
    """
    is_subject = False
    sub_list = []
    for line in lines:
        if line.startswith('Subject: '):
            sub_list.append(line)
            is_subject = True
            continue
        if is_subject:
            if line.startswith('From: '):
                is_subject = False
                break
            sub_list.append(line)
    return sub_list

def decode_mail_subject(param_list: list[str]):
    """Decode the email subject
    
    Args:
        param_list(list[str]): email subject"""
    plasticated_list = []
    for param in param_list:
        if param.startswith('Subject: '):
            plasticated_list.append(param.split(' ')[1])
        else:
            plasticated_list.append(param)

    echo_target = str.join('\n', plasticated_list)
    return subprocess.run(
        'echo "' + echo_target + '" | nkf -wd',
        capture_output=True,
        text=True,
        shell=True,
        check=True).stdout.replace('\n', '')

def get_latest_mail_body(user_name: str):
    """Get the latest mail body
    
    Args:
        user_name(str): user name
    """
    mail_list = os.listdir('mail/' + user_name + '/new')
    with open('mail/' + user_name + '/new/' + mail_list[-1], 'r', encoding='utf-8') as f:
        return f.read().splitlines()

def compare_the_two_elements(expected: str, actual: list[str]):
    """Compare the two elements
    
    Args:
        expected(str): expected element
        actual(list[str]): actual element
    """
    return len(actual) > 0 and expected == actual[0].split('：')[1].strip()

def save_screenshot(driver, co_name: str, scenario_number: str):
    """Save screenshot
    
    Args:
        driver(WebDriver): WebDriver object
        co_name(str): test case name
        scenario_number(str): scenario number
    """
    idx = -1
    for _ in range(4):
        idx = co_name.find('_', idx + 1)
    if idx != -1:
        co_name = co_name[:idx]
    co_name = co_name + "_" + scenario_number
    time.sleep(1)
    driver.save_screenshot(
        config.base_save_folder + 'application_for_use/' + d + "_" + co_name + ".png")

def move_downloaded_files(target_file_name_list, method_name):
    """Move downloaded files to the directory of each test case
    
    Args:
        target_file_name_list(list): target file name list
        method_name(str): target method name
    """
    directory_name = d + '_' + method_name
    os.makedirs(config.base_download_dir + 'application_for_use/' + directory_name, exist_ok=True)
    for target_file_name in target_file_name_list:
        shutil.move(
            config.base_download_dir + target_file_name,
            config.base_download_dir + 'application_for_use/' + directory_name
        )
