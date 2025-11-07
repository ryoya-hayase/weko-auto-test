import datetime
import inspect
import os
import re
import shutil
import time
from selenium.webdriver.common.by import By

import config
from methods_required_during_testing import(
    d,
    login,
    logout,
    search_and_display_target_item,
    click_file_information_button,
    click_secret_url_btn,
    click_mail_link,
    set_secret_url_with_login,
    change_secret_url_download_limit_with_login
)

# pytest auto_test/test_secret_url.py::test_no_1
def test_no_1(enable_secret_url):
    """No.1 Secret URL button is hidden

    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Access
    User's Role is Repository Administrator

    Args:
        enable_secret_url(WebDriver): WebDriver object
    """
    # log in as Repository Administrator
    login_as_target(enable_secret_url, 'Repository')

    # search target item
    search_and_display_target_item(enable_secret_url, config.item_name_dic['open_access'])

    # display content's info
    click_file_information_button(enable_secret_url)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(enable_secret_url, True)

    save_screenshot(enable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_2
def test_no_2(enable_secret_url):
    """No.2 Secret URL button is hidden
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Access
    User's Role is Contributor and the item's owner
    
    Args:
        enable_secret_url(WebDriver): WebDriver object
    """
    # log in as Contributor
    login_as_target(enable_secret_url, 'RegCon')

    # search target item
    search_and_display_target_item(enable_secret_url, config.item_name_dic['open_access'])

    # display content's info
    click_file_information_button(enable_secret_url)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(enable_secret_url, True)

    save_screenshot(enable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_3
def test_no_3(enable_secret_url):
    """No.3 Secret URL button is hidden
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Access
    User's Role is Contributor and not the item's owner
    
    Args:
        enable_secret_url(WebDriver): WebDriver object
    """
    # log in as Contributor
    login_as_target(enable_secret_url, 'NoRegCon')

    # search target item
    search_and_display_target_item(enable_secret_url, config.item_name_dic['open_access'])

    # display content's info
    click_file_information_button(enable_secret_url)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(enable_secret_url, True)

    save_screenshot(enable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_4
def test_no_4(enable_secret_url):
    """No.4 Secret URL button is hidden
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Access
    User's Role is Contributor and the item's contributor
    
    Args:
        enable_secret_url(WebDriver): WebDriver object
    """
    # log in as Contributor
    login_as_target(enable_secret_url, 'PrxRegCon')

    # search target item
    search_and_display_target_item(enable_secret_url, config.item_name_dic['open_access'])

    # display content's info
    click_file_information_button(enable_secret_url)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(enable_secret_url, True)

    save_screenshot(enable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_5
def test_no_5(enable_secret_url):
    """No.5 Secret URL button is hidden
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Access
    User's Role is Community Administrator
    
    Args:
        enable_secret_url(WebDriver): WebDriver object
    """
    # log in as Community Administrator
    login_as_target(enable_secret_url, 'Community')

    # search target item
    search_and_display_target_item(enable_secret_url, config.item_name_dic['open_access'])

    # display content's info
    click_file_information_button(enable_secret_url)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(enable_secret_url, True)

    save_screenshot(enable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_6
def test_no_6(enable_secret_url):
    """No.6 Secret URL button is hidden
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Access
    User's Role is General
    
    Args:
        enable_secret_url(WebDriver): WebDriver object
    """
    # log in as General
    login_as_target(enable_secret_url, 'General')

    # search target item
    search_and_display_target_item(enable_secret_url, config.item_name_dic['open_access'])

    # display content's info
    click_file_information_button(enable_secret_url)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(enable_secret_url, True)

    save_screenshot(enable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_7
def test_no_7(enable_secret_url):
    """No.7 Secret URL button is hidden
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Access
    User is not logged in

    Args:
        enable_secret_url(WebDriver): WebDriver object
    """

    # search target item
    search_and_display_target_item(enable_secret_url, config.item_name_dic['open_access'])

    # display content's info
    click_file_information_button(enable_secret_url)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(enable_secret_url, True)

    save_screenshot(enable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_8
def test_no_8(enable_secret_url):
    """No.8 Secret URL button is hidden
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Restricted Access
    User's Role is Repository Administrator
    
    Args:
        enable_secret_url(WebDriver): WebDriver object
    """
    # log in as Repository Administrator
    login_as_target(enable_secret_url, 'Repository')

    # search target item
    search_and_display_target_item(enable_secret_url, config.item_name_dic['restricted_access'])

    # display content's info
    click_file_information_button(enable_secret_url)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(enable_secret_url, True)

    save_screenshot(enable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_9
def test_no_9(enable_secret_url):
    """No.9 Secret URL button is hidden
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Restricted Access
    User's Role is Contributor and the item's owner
    
    Args:
        enable_secret_url(WebDriver): WebDriver object
    """
    # log in as Contributor
    login_as_target(enable_secret_url, 'RegCon')

    # search target item
    search_and_display_target_item(enable_secret_url, config.item_name_dic['restricted_access'])

    # display content's info
    click_file_information_button(enable_secret_url)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(enable_secret_url, True)

    save_screenshot(enable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_10
def test_no_10(enable_secret_url):
    """No.10 Display error message
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Restricted Access
    User's Role is Contributor and not the item's owner
    
    Args:
        enable_secret_url(WebDriver): WebDriver object
    """
    # log in as Contributor
    login_as_target(enable_secret_url, 'NoRegCon')

    # search target item
    search_and_display_target_item(enable_secret_url, config.item_name_dic['restricted_access'])

    # display content's info
    click_file_information_button(enable_secret_url)

    # check permission error page
    check_permission_error_page(enable_secret_url)

    save_screenshot(enable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_11
def test_no_11(enable_secret_url):
    """No.11 Secret URL button is hidden
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Restricted Access
    User's Role is Contributor and the item's contributor

    Args:
        enable_secret_url(WebDriver): WebDriver object
    """
    # log in as Contributor
    login_as_target(enable_secret_url, 'PrxRegCon')

    # search target item
    search_and_display_target_item(enable_secret_url, config.item_name_dic['restricted_access'])

    # display content's info
    click_file_information_button(enable_secret_url)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(enable_secret_url, True)

    save_screenshot(enable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_12
def test_no_12(enable_secret_url):
    """No.12 Secret URL button is hidden
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Restricted Access
    User's Role is Community Administrator
    
    Args:
        enable_secret_url(WebDriver): WebDriver object
    """
    # log in as Community Administrator
    login_as_target(enable_secret_url, 'Community')

    # search target item
    search_and_display_target_item(enable_secret_url, config.item_name_dic['restricted_access'])

    # display content's info
    click_file_information_button(enable_secret_url)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(enable_secret_url, True)

    save_screenshot(enable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_13
def test_no_13(enable_secret_url):
    """No.13 Display error message
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Restricted Access
    User's Role is General

    Args:
        enable_secret_url(WebDriver): WebDriver object
    """
    # log in as General
    login_as_target(enable_secret_url, 'General')

    # search target item
    search_and_display_target_item(enable_secret_url, config.item_name_dic['restricted_access'])

    # display content's info
    click_file_information_button(enable_secret_url)

    # check permission error page
    check_permission_error_page(enable_secret_url)

    save_screenshot(enable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_14
def test_no_14(enable_secret_url):
    """No.14 Transition to the login page
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Restricted Access
    User is not logged in
    
    Args:
        enable_secret_url(WebDriver): WebDriver object
    """
    # search target item
    search_and_display_target_item(enable_secret_url, config.item_name_dic['restricted_access'])

    # display content's info
    click_file_information_button(enable_secret_url)

    # check transition destination is login page
    check_login_page(enable_secret_url)

    save_screenshot(enable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_15
def test_no_15(enable_secret_url):
    """No.15 Secret URL button is not hidden
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Date and publish date is after today
    User's Role is Repository Administrator
    
    Args:
        enable_secret_url(WebDriver): WebDriver object
    """
    # log in as Repository Administrator
    login_as_target(enable_secret_url, 'Repository')

    # search target item
    search_and_display_target_item(enable_secret_url, config.item_name_dic['before_publish'])

    # display content's info
    click_file_information_button(enable_secret_url)

    # check secret url button is not hidden
    check_secret_url_button_is_hidden(enable_secret_url, False)

    save_screenshot(enable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_16_to_18
def test_no_16_to_18(enable_secret_url):
    """Target Tests are No.16, No.17 and No.18
    
    No.16 Send email containing secret URL
    No.17 Download the target content
    No.18 Try to download the target content over the download limit

    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Date and publish date is after today
    User's Role is Repository Administrator
    
    Args:
        enable_secret_url(WebDriver): WebDriver object
    """
    # No.16 Send email containing secret URL
    # log in as Repository Administrator
    login_as_target(enable_secret_url, 'Repository')

    # search target item
    search_and_display_target_item(enable_secret_url, config.item_name_dic['before_publish'])

    # display content's info
    click_file_information_button(enable_secret_url)

    # click secret url button
    click_secret_url_btn(enable_secret_url)

    # check mail
    check_secret_url_mail(
        enable_secret_url,
        config.users['Repository']['mail'],
        config.item_name_dic['before_publish'],
        3,
        3)

    # No.17 Download the target content
    # download the target content
    click_mail_link(enable_secret_url, config.users['Repository']['mail'].split('@', 1)[0])

    # check download file
    file_list = os.listdir(config.base_download_dir)
    assert 'before_publish.txt' in file_list

    # No.18 Try to download the target content over the download limit
    # download the target content several times
    # In No.17, download the content once, so the number of remaining downloads is 2
    for i in range(3):
        click_mail_link(enable_secret_url, config.users['Repository']['mail'].split('@', 1)[0])
        if i < 2:
            # check download file
            file_list = os.listdir(config.base_download_dir)
            assert 'before_publish (' + str(i + 1) + ').txt' in file_list
        else:
            # check over download limit error message
            check_over_download_limit_error_message(enable_secret_url)

    save_screenshot(enable_secret_url, inspect.currentframe().f_code.co_name)

    # move downloaded files to do other tests
    move_target_files = [file for file in file_list if file.startswith('before_publish')]
    move_downloaded_files(move_target_files, inspect.currentframe().f_code.co_name)

# The test No.19 is in shell_test/test_secret_url_three_days.py

# pytest auto_test/test_secret_url.py::test_no_20
def test_no_20(enable_secret_url):
    """No.20 Secret URL different from No.16's secret URL
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Date and publish date is after today
    User's Role is Repository Administrator
    
    Args:
        enable_secret_url(WebDriver): WebDriver object
    """
    # log in as Repository Administrator
    login_as_target(enable_secret_url, 'Repository')

    # search target item
    search_and_display_target_item(enable_secret_url, config.item_name_dic['before_publish'])

    # display content's info
    click_file_information_button(enable_secret_url)

    # click secret url button
    click_secret_url_btn(enable_secret_url)

    # check secret url
    check_secret_url_is_difference(config.users['Repository']['mail'].split('@', 1)[0])

# pytest auto_test/test_secret_url.py::test_no_21
def test_no_21(enable_secret_url):
    """No.21 Secret URL button is not hidden
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Date and publish date is after today
    User's Role is Contributor and the item's owner
    
    Args:
        enable_secret_url(WebDriver): WebDriver object
    """
    # log in as Contributor
    login_as_target(enable_secret_url, 'RegCon')

    # search target item
    search_and_display_target_item(enable_secret_url, config.item_name_dic['before_publish'])

    # display content's info
    click_file_information_button(enable_secret_url)

    # check secret url button is not hidden
    check_secret_url_button_is_hidden(enable_secret_url, False)

    save_screenshot(enable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_22_to_24
def test_no_22_to_24(enable_secret_url):
    """Target Tests are No.22, No.23 and No.24
    
    No.22 Send email containing secret URL
    No.23 Download the target content
    No.24 Try to download the target content over the download limit
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Date and publish date is after today
    User's Role is Contributor and the item's owner
    
    Args:
        enable_secret_url(WebDriver): WebDriver object
    """
    # No.22 Send email containing secret URL
    # log in as Contributor
    login_as_target(enable_secret_url, 'RegCon')

    # search target item
    search_and_display_target_item(enable_secret_url, config.item_name_dic['before_publish'])

    # display content's info
    click_file_information_button(enable_secret_url)

    # click secret url button
    click_secret_url_btn(enable_secret_url)

    # check mail
    check_secret_url_mail(
        enable_secret_url,
        config.users['RegCon']['mail'],
        config.item_name_dic['before_publish'],
        3,
        3)

    # No.23 Download the target content
    # download the target content
    click_mail_link(enable_secret_url, config.users['RegCon']['mail'].split('@', 1)[0])

    # check download file
    file_list = os.listdir(config.base_download_dir)
    assert 'before_publish.txt' in file_list

    # No.24 Try to download the target content over the download limit
    # download the target content several times
    # In No.23, download the content once, so the number of remaining downloads is 2
    for i in range(3):
        click_mail_link(enable_secret_url, config.users['RegCon']['mail'].split('@', 1)[0])
        if i < 2:
            # check download file
            file_list = os.listdir(config.base_download_dir)
            assert 'before_publish (' + str(i + 1) + ').txt' in file_list
        else:
            # check over download limit error message
            check_over_download_limit_error_message(enable_secret_url)

    save_screenshot(enable_secret_url, inspect.currentframe().f_code.co_name)

    # move downloaded files to do other tests
    move_target_files = [file for file in file_list if file.startswith('before_publish')]
    move_downloaded_files(move_target_files, inspect.currentframe().f_code.co_name)

# The test No.25 is in shell_test/test_secret_url_three_days.py

# pytest auto_test/test_secret_url.py::test_no_26
def test_no_26(enable_secret_url):
    """No.26 Secret URL different from No.22's secret URL
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Date and publish date is after today
    User's Role is Contributor and the item's owner
    
    Args:
        enable_secret_url(WebDriver): WebDriver object
    """
    # log in as Contributor
    login_as_target(enable_secret_url, 'RegCon')

    # search target item
    search_and_display_target_item(enable_secret_url, config.item_name_dic['before_publish'])

    # display content's info
    click_file_information_button(enable_secret_url)

    # click secret url button
    click_secret_url_btn(enable_secret_url)

    # check secret url
    check_secret_url_is_difference(config.users['RegCon']['mail'].split('@', 1)[0])

# pytest auto_test/test_secret_url.py::test_no_27
def test_no_27(enable_secret_url):
    """No.27 Display error message
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Date and publish date is after today
    User's Role is Contributor and not the item's owner
    
    Args:
        enable_secret_url(WebDriver): WebDriver object
    """
    # log in as Contributor
    login_as_target(enable_secret_url, 'NoRegCon')

    # search target item
    search_and_display_target_item(enable_secret_url, config.item_name_dic['before_publish'])

    # display content's info
    click_file_information_button(enable_secret_url)

    # check permission error page
    check_permission_error_page(enable_secret_url)

    save_screenshot(enable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_28
def test_no_28(enable_secret_url):
    """No.28 Secret URL issuance and download are possible.

    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Date and publish date is after today
    User's Role is Contributor and the item's contributor
    
    Args:
        enable_secret_url(WebDriver): WebDriver object
    """
    # log in as Contributor
    login_as_target(enable_secret_url, 'PrxRegCon')

    # search target item
    search_and_display_target_item(enable_secret_url, config.item_name_dic['before_publish'])

    # display content's info
    click_file_information_button(enable_secret_url)

    # click secret url button
    click_secret_url_btn(enable_secret_url)

    # check mail
    check_secret_url_mail(
        enable_secret_url,
        config.users['PrxRegCon']['mail'],
        config.item_name_dic['before_publish'],
        3,
        3)

    # download the target content
    click_mail_link(enable_secret_url, config.users['PrxRegCon']['mail'].split('@', 1)[0])

    # check download file
    file_list = os.listdir(config.base_download_dir)
    assert 'before_publish.txt' in file_list

    # download the target content several times
    for i in range(3):
        click_mail_link(enable_secret_url, config.users['PrxRegCon']['mail'].split('@', 1)[0])
        if i < 2:
            # check download file
            file_list = os.listdir(config.base_download_dir)
            assert 'before_publish (' + str(i + 1) + ').txt' in file_list
        else:
            # check over download limit error message
            check_over_download_limit_error_message(enable_secret_url)

    save_screenshot(enable_secret_url, inspect.currentframe().f_code.co_name)

    # move downloaded files to do other tests
    move_target_files = [file for file in file_list if file.startswith('before_publish')]
    move_downloaded_files(move_target_files, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_29
def test_no_29(enable_secret_url):
    """No.29 Secret URL button is hidden
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Date and publish date is after today
    User's Role is Community Administrator
    
    Args:
        enable_secret_url(WebDriver): WebDriver object
    """
    # log in as Community Administrator
    login_as_target(enable_secret_url, 'Community')

    # search target item
    search_and_display_target_item(enable_secret_url, config.item_name_dic['before_publish'])

    # display content's info
    click_file_information_button(enable_secret_url)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(enable_secret_url, True)

    save_screenshot(enable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_30
def test_no_30(enable_secret_url):
    """No.30 Display error message
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Date and publish date is after today
    User's Role is General
    
    Args:
        enable_secret_url(WebDriver): WebDriver object
    """
    # log in as General
    login_as_target(enable_secret_url, 'General')

    # search target item
    search_and_display_target_item(enable_secret_url, config.item_name_dic['before_publish'])

    # display content's info
    click_file_information_button(enable_secret_url)

    # check permission error page
    check_permission_error_page(enable_secret_url)

    save_screenshot(enable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_31
def test_no_31(enable_secret_url):
    """No.31 Transition to the login page
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Date and publish date is after today
    User is not logged in
    
    Args:
        enable_secret_url(WebDriver): WebDriver object
    """
    # search target item
    search_and_display_target_item(enable_secret_url, config.item_name_dic['before_publish'])

    # display content's info
    click_file_information_button(enable_secret_url)

    # check transition destination is login page
    check_login_page(enable_secret_url)

    save_screenshot(enable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_32
def test_no_32(enable_secret_url):
    """No.32 Secret URL button is hidden
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Date and publish date is before today
    User's Role is Repository Administrator
    
    Args:
        enable_secret_url(WebDriver): WebDriver object
    """
    # log in as Repository Administrator
    login_as_target(enable_secret_url, 'Repository')

    # search target item
    search_and_display_target_item(enable_secret_url, config.item_name_dic['after_publish'])

    # display content's info
    click_file_information_button(enable_secret_url)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(enable_secret_url, True)

    save_screenshot(enable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_33
def test_no_33(enable_secret_url):
    """No.33 Secret URL button is hidden
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Date and publish date is before today
    User's Role is Contributor and the item's owner
    
    Args:
        enable_secret_url(WebDriver): WebDriver object
    """
    # log in as Contributor
    login_as_target(enable_secret_url, 'RegCon')

    # search target item
    search_and_display_target_item(enable_secret_url, config.item_name_dic['after_publish'])

    # display content's info
    click_file_information_button(enable_secret_url)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(enable_secret_url, True)

    save_screenshot(enable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_34
def test_no_34(enable_secret_url):
    """No.34 Secret URL button is hidden
    
    Secret URL is enabled
    Expliration Date is 3
    Download Limit is 3
    Access Setting is Open Date and publish date is before today
    User's Role is Contributor and not the item's owner
    
    Args:
        enable_secret_url(WebDriver): WebDriver object
    """
    # log in as Contributor
    login_as_target(enable_secret_url, 'NoRegCon')

    # search target item
    search_and_display_target_item(enable_secret_url, config.item_name_dic['after_publish'])

    # display content's info
    click_file_information_button(enable_secret_url)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(enable_secret_url, True)

    save_screenshot(enable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_35
def test_no_35(enable_secret_url):
    """No.35 Secret URL button is hidden
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Date and publish date is before today
    User's Role is Contributor and the item's contributor
    
    Args:
        enable_secret_url(WebDriver): WebDriver object
    """
    # log in as Contributor
    login_as_target(enable_secret_url, 'PrxRegCon')

    # search target item
    search_and_display_target_item(enable_secret_url, config.item_name_dic['after_publish'])

    # display content's info
    click_file_information_button(enable_secret_url)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(enable_secret_url, True)

    save_screenshot(enable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_36
def test_no_36(enable_secret_url):
    """No.36 Secret URL button is hidden
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Date and publish date is before today
    User's Role is Community Administrator
    
    Args:
        enable_secret_url(WebDriver): WebDriver object
    """
    # log in as Community Administrator
    login_as_target(enable_secret_url, 'Community')

    # search target item
    search_and_display_target_item(enable_secret_url, config.item_name_dic['after_publish'])

    # display content's info
    click_file_information_button(enable_secret_url)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(enable_secret_url, True)

    save_screenshot(enable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_37
def test_no_37(enable_secret_url):
    """No.37 Secret URL button is hidden
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Date and publish date is before today
    User's Role is General
    
    Args:
        enable_secret_url(WebDriver): WebDriver object
    """
    # log in as General
    login_as_target(enable_secret_url, 'General')

    # search target item
    search_and_display_target_item(enable_secret_url, config.item_name_dic['after_publish'])

    # display content's info
    click_file_information_button(enable_secret_url)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(enable_secret_url, True)

    save_screenshot(enable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_38
def test_no_38(enable_secret_url):
    """No.38 Secret URL button is hidden
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Date and publish date is before today
    User is not logged in
    
    Args:
        enable_secret_url(WebDriver): WebDriver object
    """
    # search target item
    search_and_display_target_item(enable_secret_url, config.item_name_dic['after_publish'])

    # display content's info
    click_file_information_button(enable_secret_url)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(enable_secret_url, True)

    save_screenshot(enable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_39
def test_no_39(enable_secret_url):
    """No.39 Secret URL button is not hidden
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Private
    User's Role is Repository Administrator
    
    Args:
        enable_secret_url(WebDriver): WebDriver object
    """
    # log in as Repository Administrator
    login_as_target(enable_secret_url, 'Repository')

    # search target item
    search_and_display_target_item(enable_secret_url, config.item_name_dic['private'])

    # display content's info
    click_file_information_button(enable_secret_url)

    # check secret url button is not hidden
    check_secret_url_button_is_hidden(enable_secret_url, False)

    save_screenshot(enable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_40_to_42
def test_no_40_to_42(enable_secret_url):
    """Target Tests are No.40, No.41 and No.42
    
    No.40 Send email containing secret URL
    No.41 Download the target content
    No.42 Try to download the target content over the download limit
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Private
    User's Role is Repository Administrator
    
    Args:
        enable_secret_url(WebDriver): WebDriver object
    """
    # No.40 Send email containing secret URL
    # log in as Repository Administrator
    login_as_target(enable_secret_url, 'Repository')

    # search target item
    search_and_display_target_item(enable_secret_url, config.item_name_dic['private'])

    # display content's info
    click_file_information_button(enable_secret_url)

    # click secret url button
    click_secret_url_btn(enable_secret_url)

    # check mail
    check_secret_url_mail(
        enable_secret_url,
        config.users['Repository']['mail'],
        config.item_name_dic['private'],
        3,
        3)

    # No.41 Download the target content
    # download the target content
    click_mail_link(enable_secret_url, config.users['Repository']['mail'].split('@', 1)[0])

    # check download file
    file_list = os.listdir(config.base_download_dir)
    assert 'private.txt' in file_list

    # No.42 Try to download the target content over the download limit
    # download the target content several times
    # In No.41, download the content once, so the number of remaining downloads is 2
    for i in range(3):
        click_mail_link(enable_secret_url, config.users['Repository']['mail'].split('@', 1)[0])
        if i < 2:
            # check download file
            file_list = os.listdir(config.base_download_dir)
            assert 'private (' + str(i + 1) + ').txt' in file_list
        else:
            # check over download limit error message
            check_over_download_limit_error_message(enable_secret_url)

    save_screenshot(enable_secret_url, inspect.currentframe().f_code.co_name)

    # move downloaded files to do other tests
    move_target_files = [file for file in file_list if file.startswith('private')]
    move_downloaded_files(move_target_files, inspect.currentframe().f_code.co_name)

# The test No.43 is in shell_test/test_secret_url_three_days.py

# pytest auto_test/test_secret_url.py::test_no_44
def test_no_44(enable_secret_url):
    """No.44 Secret URL different from No.40's secret URL
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Private
    User's Role is Repository Administrator
    
    Args:
        enable_secret_url(WebDriver): WebDriver object
    """
    # log in as Repository Administrator
    login_as_target(enable_secret_url, 'Repository')

    # search target item
    search_and_display_target_item(enable_secret_url, config.item_name_dic['private'])

    # display content's info
    click_file_information_button(enable_secret_url)

    # click secret url button
    click_secret_url_btn(enable_secret_url)

    # check secret url
    check_secret_url_is_difference(config.users['Repository']['mail'].split('@', 1)[0])

# pytest auto_test/test_secret_url.py::test_no_45
def test_no_45(enable_secret_url):
    """No.45 Secret URL button is not hidden
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Private
    User's Role is Contributor and the item's owner
    
    Args:
        enable_secret_url(WebDriver): WebDriver object
    """
    # log in as Contributor
    login_as_target(enable_secret_url, 'RegCon')

    # search target item
    search_and_display_target_item(enable_secret_url, config.item_name_dic['private'])

    # display content's info
    click_file_information_button(enable_secret_url)

    # check secret url button is not hidden
    check_secret_url_button_is_hidden(enable_secret_url, False)

    save_screenshot(enable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_46_to_48
def test_no_46_to_48(enable_secret_url):
    """Target Tests are No.46, No.47 and No.48
    
    No.46 Send email containing secret URL
    No.47 Download the target content
    No.48 Try to download the target content over the download limit
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Private
    User's Role is Contributor and the item's owner
    
    Args:
        enable_secret_url(WebDriver): WebDriver object
    """
    # No.46 Send email containing secret URL
    # log in as Contributor
    login_as_target(enable_secret_url, 'RegCon')

    # search target item
    search_and_display_target_item(enable_secret_url, config.item_name_dic['private'])

    # display content's info
    click_file_information_button(enable_secret_url)

    # click secret url button
    click_secret_url_btn(enable_secret_url)

    # check mail
    check_secret_url_mail(
        enable_secret_url,
        config.users['RegCon']['mail'],
        config.item_name_dic['private'],
        3,
        3)

    # No.47 Download the target content
    # download the target content
    click_mail_link(enable_secret_url, config.users['RegCon']['mail'].split('@', 1)[0])

    # check download file
    file_list = os.listdir(config.base_download_dir)
    assert 'private.txt' in file_list

    # No.48 Try to download the target content over the download limit
    # download the target content several times
    # In No.47, download the content once, so the number of remaining downloads is 2
    for i in range(3):
        click_mail_link(enable_secret_url, config.users['RegCon']['mail'].split('@', 1)[0])
        if i < 2:
            # check download file
            file_list = os.listdir(config.base_download_dir)
            assert 'private (' + str(i + 1) + ').txt' in file_list
        else:
            # check over download limit error message
            check_over_download_limit_error_message(enable_secret_url)

    save_screenshot(enable_secret_url, inspect.currentframe().f_code.co_name)

    # move downloaded files to do other tests
    move_target_files = [file for file in file_list if file.startswith('private')]
    move_downloaded_files(move_target_files, inspect.currentframe().f_code.co_name)

# The test No.49 is in shell_test/test_secret_url_three_days.py

# pytest auto_test/test_secret_url.py::test_no_50
def test_no_50(enable_secret_url):
    """No.50 Secret URL different from No.46's secret URL
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Private
    User's Role is Contributor and the item's owner
    
    Args:
        enable_secret_url(WebDriver): WebDriver object
    """
    # log in as Contributor
    login_as_target(enable_secret_url, 'RegCon')

    # search target item
    search_and_display_target_item(enable_secret_url, config.item_name_dic['private'])

    # display content's info
    click_file_information_button(enable_secret_url)

    # click secret url button
    click_secret_url_btn(enable_secret_url)

    # check secret url
    check_secret_url_is_difference(config.users['RegCon']['mail'].split('@', 1)[0])

# pytest auto_test/test_secret_url.py::test_no_51
def test_no_51(enable_secret_url):
    """No.51 Content's info is hidden
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Private
    User's Role is Contributor and not the item's owner
    
    Args:
        enable_secret_url(WebDriver): WebDriver object
    """
    # log in as Contributor
    login_as_target(enable_secret_url, 'NoRegCon')

    # search target item
    search_and_display_target_item(enable_secret_url, config.item_name_dic['private'])

    # check content's info is hidden
    el = enable_secret_url.find_elements(By.XPATH, '//*[@id="detail-item"]/table')
    assert len(el) == 0

    save_screenshot(enable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_52
def test_no_52(enable_secret_url):
    """No.52 Secret URL issuance and download are possible.
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Private
    User's Role is Contributor and the item's contributor
    
    Args:
        enable_secret_url(WebDriver): WebDriver object
    """
    # log in as Contributor
    login_as_target(enable_secret_url, 'PrxRegCon')

    # search target item
    search_and_display_target_item(enable_secret_url, config.item_name_dic['private'])

    # display content's info
    click_file_information_button(enable_secret_url)

    # click secret url button
    click_secret_url_btn(enable_secret_url)

    # check mail
    check_secret_url_mail(
        enable_secret_url,
        config.users['PrxRegCon']['mail'],
        config.item_name_dic['private'],
        3,
        3)

    # download the target content
    click_mail_link(enable_secret_url, config.users['PrxRegCon']['mail'].split('@', 1)[0])

    # check download file
    file_list = os.listdir(config.base_download_dir)
    assert 'private.txt' in file_list

    # download the target content several times
    for i in range(3):
        click_mail_link(enable_secret_url, config.users['PrxRegCon']['mail'].split('@', 1)[0])
        if i < 2:
            # check download file
            file_list = os.listdir(config.base_download_dir)
            assert 'private (' + str(i + 1) + ').txt' in file_list
        else:
            # check over download limit error message
            check_over_download_limit_error_message(enable_secret_url)

    save_screenshot(enable_secret_url, inspect.currentframe().f_code.co_name)

    # move downloaded files to do other tests
    move_target_files = [file for file in file_list if file.startswith('private')]
    move_downloaded_files(move_target_files, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_53
def test_no_53(enable_secret_url):
    """No.53 Secret URL button is hidden
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Private
    User's Role is Community Administrator
    
    Args:
        enable_secret_url(WebDriver): WebDriver object
    """
    # log in as Community Administrator
    login_as_target(enable_secret_url, 'Community')

    # search target item
    search_and_display_target_item(enable_secret_url, config.item_name_dic['private'])

    # display content's info
    click_file_information_button(enable_secret_url)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(enable_secret_url, True)

    save_screenshot(enable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_54
def test_no_54(enable_secret_url):
    """No.54 Content's info is hidden
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Private
    User's Role is General
    
    Args:
        enable_secret_url(WebDriver): WebDriver object
    """
    # log in as General
    login_as_target(enable_secret_url, 'General')

    # search target item
    search_and_display_target_item(enable_secret_url, config.item_name_dic['private'])

    # check content's info is hidden
    el = enable_secret_url.find_elements(By.XPATH, '//*[@id="detail-item"]/table')
    assert len(el) == 0

    save_screenshot(enable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_55
def test_no_55(enable_secret_url):
    """No.55 Content's info is hidden
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Private
    User is not logged in
    
    Args:
        enable_secret_url(WebDriver): WebDriver object
    """
    # search target item
    search_and_display_target_item(enable_secret_url, config.item_name_dic['private'])

    # check content's info is hidden
    el = enable_secret_url.find_elements(By.XPATH, '//*[@id="detail-item"]/table')
    assert len(el) == 0

    save_screenshot(enable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_56
def test_no_56(disable_secret_url):
    """No.56 Secret URL button is hidden
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Access
    User's Role is Repository Administrator
    
    Args:
        disable_secret_url(WebDriver): WebDriver object
    """
    # log in as Repository Administrator
    login_as_target(disable_secret_url, 'Repository')

    # search target item
    search_and_display_target_item(disable_secret_url, config.item_name_dic['open_access'])

    # display content's info
    click_file_information_button(disable_secret_url)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(disable_secret_url, True)

    save_screenshot(disable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_57
def test_no_57(disable_secret_url):
    """No.57 Secret URL button is hidden
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Access
    User's Role is Contributor and the item's owner
    
    Args:
        disable_secret_url(WebDriver): WebDriver object
    """
    # log in as Contributor
    login_as_target(disable_secret_url, 'RegCon')

    # search target item
    search_and_display_target_item(disable_secret_url, config.item_name_dic['open_access'])

    # display content's info
    click_file_information_button(disable_secret_url)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(disable_secret_url, True)

    save_screenshot(disable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_58
def test_no_58(disable_secret_url):
    """No.58 Secret URL button is hidden
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Access
    User's Role is Contributor and not the item's owner
    
    Args:
        disable_secret_url(WebDriver): WebDriver object
    """
    # log in as Contributor
    login_as_target(disable_secret_url, 'NoRegCon')

    # search target item
    search_and_display_target_item(disable_secret_url, config.item_name_dic['open_access'])

    # display content's info
    click_file_information_button(disable_secret_url)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(disable_secret_url, True)

    save_screenshot(disable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_59
def test_no_59(disable_secret_url):
    """No.59 Secret URL button is hidden
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Access
    User's Role is Contributor and the item's contributor
    
    Args:
        disable_secret_url(WebDriver): WebDriver object
    """
    # log in as Contributor
    login_as_target(disable_secret_url, 'PrxRegCon')

    # search target item
    search_and_display_target_item(disable_secret_url, config.item_name_dic['open_access'])

    # display content's info
    click_file_information_button(disable_secret_url)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(disable_secret_url, True)

    save_screenshot(disable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_60
def test_no_60(disable_secret_url):
    """No.60 Secret URL button is hidden
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Access
    User's Role is Community Administrator
    
    Args:
        disable_secret_url(WebDriver): WebDriver object
    """
    # log in as Community Administrator
    login_as_target(disable_secret_url, 'Community')

    # search target item
    search_and_display_target_item(disable_secret_url, config.item_name_dic['open_access'])

    # display content's info
    click_file_information_button(disable_secret_url)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(disable_secret_url, True)

    save_screenshot(disable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_61
def test_no_61(disable_secret_url):
    """No.61 Secret URL button is hidden
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Access
    User's Role is General
    
    Args:
        disable_secret_url(WebDriver): WebDriver object
    """
    # log in as General
    login_as_target(disable_secret_url, 'General')

    # search target item
    search_and_display_target_item(disable_secret_url, config.item_name_dic['open_access'])

    # display content's info
    click_file_information_button(disable_secret_url)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(disable_secret_url, True)

    save_screenshot(disable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_62
def test_no_62(disable_secret_url):
    """No.62 Secret URL button is hidden
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Access
    User is not logged in
    
    Args:
        disable_secret_url(WebDriver): WebDriver object
    """
    # search target item
    search_and_display_target_item(disable_secret_url, config.item_name_dic['open_access'])

    # display content's info
    click_file_information_button(disable_secret_url)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(disable_secret_url, True)

    save_screenshot(disable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_63
def test_no_63(disable_secret_url):
    """No.63 Secret URL button is hidden
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Restricted Access
    User's Role is Repository Administrator
    
    Args:
        disable_secret_url(WebDriver): WebDriver object
    """
    # log in as Repository Administrator
    login_as_target(disable_secret_url, 'Repository')

    # search target item
    search_and_display_target_item(disable_secret_url, config.item_name_dic['restricted_access'])

    # display content's info
    click_file_information_button(disable_secret_url)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(disable_secret_url, True)

    save_screenshot(disable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_64
def test_no_64(disable_secret_url):
    """No.64 Secret URL button is hidden
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Restricted Access
    User's Role is Contributor and the item's owner
    
    Args:
        disable_secret_url(WebDriver): WebDriver object
    """
    # log in as Contributor
    login_as_target(disable_secret_url, 'RegCon')

    # search target item
    search_and_display_target_item(disable_secret_url, config.item_name_dic['restricted_access'])

    # display content's info
    click_file_information_button(disable_secret_url)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(disable_secret_url, True)

    save_screenshot(disable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_65
def test_no_65(disable_secret_url):
    """No.65 Display error message
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Restricted Access
    User's Role is Contributor and not the item's owner
    
    Args:
        disable_secret_url(WebDriver): WebDriver object
    """
    # log in as Contributor
    login_as_target(disable_secret_url, 'NoRegCon')

    # search target item
    search_and_display_target_item(disable_secret_url, config.item_name_dic['restricted_access'])

    # display content's info
    click_file_information_button(disable_secret_url)

    # check permission error page
    check_permission_error_page(disable_secret_url)

    save_screenshot(disable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_66
def test_no_66(disable_secret_url):
    """No.66 Secret URL button is hidden
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Restricted Access
    User's Role is Contributor and the item's contributor
    
    Args:
        disable_secret_url(WebDriver): WebDriver object
    """
    # log in as Contributor
    login_as_target(disable_secret_url, 'PrxRegCon')

    # search target item
    search_and_display_target_item(disable_secret_url, config.item_name_dic['restricted_access'])

    # display content's info
    click_file_information_button(disable_secret_url)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(disable_secret_url, True)

    save_screenshot(disable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_67
def test_no_67(disable_secret_url):
    """No.67 Secret URL button is hidden
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Restricted Access
    User's Role is Community Administrator
    
    Args:
        disable_secret_url(WebDriver): WebDriver object
    """
    # log in as Community Administrator
    login_as_target(disable_secret_url, 'Community')

    # search target item
    search_and_display_target_item(disable_secret_url, config.item_name_dic['restricted_access'])

    # display content's info
    click_file_information_button(disable_secret_url)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(disable_secret_url, True)

    save_screenshot(disable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_68
def test_no_68(disable_secret_url):
    """No.68 Display error message
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Restricted Access
    User's Role is General
    
    Args:
        disable_secret_url(WebDriver): WebDriver object
    """
    # log in as General
    login_as_target(disable_secret_url, 'General')

    # search target item
    search_and_display_target_item(disable_secret_url, config.item_name_dic['restricted_access'])

    # display content's info
    click_file_information_button(disable_secret_url)

    # check permission error page
    check_permission_error_page(disable_secret_url)

    save_screenshot(disable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_69
def test_no_69(disable_secret_url):
    """No.69 Transition to the login page
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Restricted Access
    User is not logged in
    
    Args:
        disable_secret_url(WebDriver): WebDriver object
    """
    # search target item
    search_and_display_target_item(disable_secret_url, config.item_name_dic['restricted_access'])

    # display content's info
    click_file_information_button(disable_secret_url)

    # check transition destination is login page
    check_login_page(disable_secret_url)

    save_screenshot(disable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_70
def test_no_70(disable_secret_url):
    """No.70 Secret URL button is hidden
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Date and publish date is after today
    User's Role is Repository Administrator
    
    Args:
        disable_secret_url(WebDriver): WebDriver object
    """
    # log in as Repository Administrator
    login_as_target(disable_secret_url, 'Repository')

    # search target item
    search_and_display_target_item(disable_secret_url, config.item_name_dic['before_publish'])

    # display content's info
    click_file_information_button(disable_secret_url)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(disable_secret_url, True)

    save_screenshot(disable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_71
def test_no_71(disable_secret_url):
    """No.71 Secret URL button is hidden
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Date and publish date is after today
    User's Role is Contributor and the item's owner
    
    Args:
        disable_secret_url(WebDriver): WebDriver object
    """
    # log in as Contributor
    login_as_target(disable_secret_url, 'RegCon')

    # search target item
    search_and_display_target_item(disable_secret_url, config.item_name_dic['before_publish'])

    # display content's info
    click_file_information_button(disable_secret_url)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(disable_secret_url, True)

    save_screenshot(disable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_72
def test_no_72(disable_secret_url):
    """No.72 Display error message
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Date and publish date is after today
    User's Role is Contributor and not the item's owner
    
    Args:
        disable_secret_url(WebDriver): WebDriver object
    """
    # log in as Contributor
    login_as_target(disable_secret_url, 'NoRegCon')

    # search target item
    search_and_display_target_item(disable_secret_url, config.item_name_dic['before_publish'])

    # display content's info
    click_file_information_button(disable_secret_url)

    # check permission error page
    check_permission_error_page(disable_secret_url)

    save_screenshot(disable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_73
def test_no_73(disable_secret_url):
    """No.73 Secret URL button is hidden
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Date and publish date is after today
    User's Role is Contributor and the item's contributor
    
    Args:
        disable_secret_url(WebDriver): WebDriver object
    """
    # log in as Contributor
    login_as_target(disable_secret_url, 'PrxRegCon')

    # search target item
    search_and_display_target_item(disable_secret_url, config.item_name_dic['before_publish'])

    # display content's info
    click_file_information_button(disable_secret_url)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(disable_secret_url, True)

    save_screenshot(disable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_74
def test_no_74(disable_secret_url):
    """No.74 Secret URL button is hidden
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Date and publish date is after today
    User's Role is Community Administrator
    
    Args:
        disable_secret_url(WebDriver): WebDriver object
    """
    # log in as Community Administrator
    login_as_target(disable_secret_url, 'Community')

    # search target item
    search_and_display_target_item(disable_secret_url, config.item_name_dic['before_publish'])

    # display content's info
    click_file_information_button(disable_secret_url)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(disable_secret_url, True)

    save_screenshot(disable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_75
def test_no_75(disable_secret_url):
    """No.75 Display error message
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Date and publish date is after today
    User's Role is General
    
    Args:
        disable_secret_url(WebDriver): WebDriver object
    """
    # log in as General
    login_as_target(disable_secret_url, 'General')

    # search target item
    search_and_display_target_item(disable_secret_url, config.item_name_dic['before_publish'])

    # display content's info
    click_file_information_button(disable_secret_url)

    # check permission error page
    check_permission_error_page(disable_secret_url)

    save_screenshot(disable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_76
def test_no_76(disable_secret_url):
    """No.76 Transition to the login page
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Date and publish date is after today
    User is not logged in
    
    Args:
        disable_secret_url(WebDriver): WebDriver object
    """
    # search target item
    search_and_display_target_item(disable_secret_url, config.item_name_dic['before_publish'])

    # display content's info
    click_file_information_button(disable_secret_url)

    # check transition destination is login page
    check_login_page(disable_secret_url)

    save_screenshot(disable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_77
def test_no_77(disable_secret_url):
    """No.77 Secret URL button is hidden
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Date and publish date is before today
    User's Role is Repository Administrator
    
    Args:
        disable_secret_url(WebDriver): WebDriver object
    """
    # log in as Repository Administrator
    login_as_target(disable_secret_url, 'Repository')

    # search target item
    search_and_display_target_item(disable_secret_url, config.item_name_dic['after_publish'])

    # display content's info
    click_file_information_button(disable_secret_url)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(disable_secret_url, True)

    save_screenshot(disable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_78
def test_no_78(disable_secret_url):
    """No.78 Secret URL button is hidden
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Date and publish date is before today
    User's Role is Contributor and the item's owner
    
    Args:
        disable_secret_url(WebDriver): WebDriver object
    """
    # log in as Contributor
    login_as_target(disable_secret_url, 'RegCon')

    # search target item
    search_and_display_target_item(disable_secret_url, config.item_name_dic['after_publish'])

    # display content's info
    click_file_information_button(disable_secret_url)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(disable_secret_url, True)

    save_screenshot(disable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_79
def test_no_79(disable_secret_url):
    """No.79 Secret URL button is hidden
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Date and publish date is before today
    User's Role is Contributor and not the item's owner
    
    Args:
        disable_secret_url(WebDriver): WebDriver object
    """
    # log in as Contributor
    login_as_target(disable_secret_url, 'NoRegCon')

    # search target item
    search_and_display_target_item(disable_secret_url, config.item_name_dic['after_publish'])

    # display content's info
    click_file_information_button(disable_secret_url)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(disable_secret_url, True)

    save_screenshot(disable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_80
def test_no_80(disable_secret_url):
    """No.80 Secret URL button is hidden
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Date and publish date is before today
    User's Role is Contributor and the item's contributor
    
    Args:
        disable_secret_url(WebDriver): WebDriver object
    """
    # log in as Contributor
    login_as_target(disable_secret_url, 'PrxRegCon')

    # search target item
    search_and_display_target_item(disable_secret_url, config.item_name_dic['after_publish'])

    # display content's info
    click_file_information_button(disable_secret_url)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(disable_secret_url, True)

    save_screenshot(disable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_81
def test_no_81(disable_secret_url):
    """No.81 Secret URL button is hidden
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Date and publish date is before today
    User's Role is Community Administrator
    
    Args:
        disable_secret_url(WebDriver): WebDriver object
    """
    # log in as Community Administrator
    login_as_target(disable_secret_url, 'Community')

    # search target item
    search_and_display_target_item(disable_secret_url, config.item_name_dic['after_publish'])

    # display content's info
    click_file_information_button(disable_secret_url)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(disable_secret_url, True)

    save_screenshot(disable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_82
def test_no_82(disable_secret_url):
    """No.82 Secret URL button is hidden
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Date and publish date is before today
    User's Role is General
    
    Args:
        disable_secret_url(WebDriver): WebDriver object
    """
    # log in as General
    login_as_target(disable_secret_url, 'General')

    # search target item
    search_and_display_target_item(disable_secret_url, config.item_name_dic['after_publish'])

    # display content's info
    click_file_information_button(disable_secret_url)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(disable_secret_url, True)

    save_screenshot(disable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_83
def test_no_83(disable_secret_url):
    """No.83 Secret URL button is hidden
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Date and publish date is before today
    User is not logged in
    
    Args:
        disable_secret_url(WebDriver): WebDriver object
    """
    # search target item
    search_and_display_target_item(disable_secret_url, config.item_name_dic['after_publish'])

    # display content's info
    click_file_information_button(disable_secret_url)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(disable_secret_url, True)

    save_screenshot(disable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_84
def test_no_84(disable_secret_url):
    """No.84 Secret URL button is hidden
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Private
    User's Role is Repository Administrator
    
    Args:
        disable_secret_url(WebDriver): WebDriver object
    """
    # log in as Repository Administrator
    login_as_target(disable_secret_url, 'Repository')

    # search target item
    search_and_display_target_item(disable_secret_url, config.item_name_dic['private'])

    # display content's info
    click_file_information_button(disable_secret_url)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(disable_secret_url, True)

    save_screenshot(disable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_85
def test_no_85(disable_secret_url):
    """No.85 Secret URL button is hidden
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Private
    User's Role is Contributor and the item's owner
    
    Args:
        disable_secret_url(WebDriver): WebDriver object
    """
    # log in as Contributor
    login_as_target(disable_secret_url, 'RegCon')

    # search target item
    search_and_display_target_item(disable_secret_url, config.item_name_dic['private'])

    # display content's info
    click_file_information_button(disable_secret_url)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(disable_secret_url, True)

    save_screenshot(disable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_86
def test_no_86(disable_secret_url):
    """No.86 Content's info is hidden
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Private
    User's Role is Contributor and not the item's owner
    
    Args:
        disable_secret_url(WebDriver): WebDriver object
    """
    # log in as Contributor
    login_as_target(disable_secret_url, 'NoRegCon')

    # search target item
    search_and_display_target_item(disable_secret_url, config.item_name_dic['private'])

    # check content's info is hidden
    el = disable_secret_url.find_elements(By.XPATH, '//*[@id="detail-item"]/table')
    assert len(el) == 0

    save_screenshot(disable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_87
def test_no_87(disable_secret_url):
    """No.87 Secret URL button is hidden
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Private
    User's Role is Contributor and the item's contributor
    
    Args:
        disable_secret_url(WebDriver): WebDriver object
    """
    # log in as Contributor
    login_as_target(disable_secret_url, 'PrxRegCon')

    # search target item
    search_and_display_target_item(disable_secret_url, config.item_name_dic['private'])

    # display content's info
    click_file_information_button(disable_secret_url)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(disable_secret_url, True)

    save_screenshot(disable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_88
def test_no_88(disable_secret_url):
    """No.88 Secret URL button is hidden
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Private
    User's Role is Community Administrator
    
    Args:
        disable_secret_url(WebDriver): WebDriver object
    """
    # log in as Community Administrator
    login_as_target(disable_secret_url, 'Community')

    # search target item
    search_and_display_target_item(disable_secret_url, config.item_name_dic['private'])

    # display content's info
    click_file_information_button(disable_secret_url)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(disable_secret_url, True)

    save_screenshot(disable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_89
def test_no_89(disable_secret_url):
    """No.89 Content's info is hidden
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Private
    User's Role is General
    
    Args:
        disable_secret_url(WebDriver): WebDriver object
    """
    # log in as General
    login_as_target(disable_secret_url, 'General')

    # search target item
    search_and_display_target_item(disable_secret_url, config.item_name_dic['private'])

    # check content's info is hidden
    el = disable_secret_url.find_elements(By.XPATH, '//*[@id="detail-item"]/table')
    assert len(el) == 0

    save_screenshot(disable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_90
def test_no_90(disable_secret_url):
    """No.90 Content's info is hidden
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Private
    User is not logged in
    
    Args:
        disable_secret_url(WebDriver): WebDriver object
    """
    # search target item
    search_and_display_target_item(disable_secret_url, config.item_name_dic['private'])

    # check content's info is hidden
    el = disable_secret_url.find_elements(By.XPATH, '//*[@id="detail-item"]/table')
    assert len(el) == 0

    save_screenshot(disable_secret_url, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_91
def test_no_91(driver):
    """No.91 Download file with secret URL is failed
    
    Secret URL is enabled and switch to disabled after email is sent
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Date and publish date is after today
    User's Role is Repository Administrator
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # enable secret url
    set_secret_url_with_login(driver, True)

    # log in as Repository Administrator
    login_as_target(driver, 'Repository')

    # search target item
    search_and_display_target_item(driver, config.item_name_dic['before_publish'])

    # display content's info
    click_file_information_button(driver)

    # click secret url button
    click_secret_url_btn(driver)

    # log out
    logout(driver)

    # disable secret url
    set_secret_url_with_login(driver, False)

    # log in as Repository Administrator
    login_as_target(driver, 'Repository')

    # download the target file
    click_mail_link(driver, config.users['Repository']['mail'].split('@', 1)[0])

    # check error page has the class what name is error-page
    error_page = driver.find_elements(By.CLASS_NAME, 'error-page')
    assert len(error_page) > 0, 'This page is not error page'

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_92
def test_no_92(driver):
    """No.92 Download file with secret URL is failed
    
    Secret URL is enabled and switch to disabled after email is sent
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Date and publish date is after today
    User's Role is Contributor and the item's owner
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # enable secret url
    set_secret_url_with_login(driver, True)

    # log in as Contributor
    login_as_target(driver, 'RegCon')

    # search target item
    search_and_display_target_item(driver, config.item_name_dic['before_publish'])

    # display content's info
    click_file_information_button(driver)

    # click secret url button
    click_secret_url_btn(driver)

    # log out
    logout(driver)

    # disable secret url
    set_secret_url_with_login(driver, False)

    # log in as Contributor
    login_as_target(driver, 'RegCon')

    # download the target file
    click_mail_link(driver, config.users['RegCon']['mail'].split('@', 1)[0])

    # check error page has the class what name is error-page
    error_page = driver.find_elements(By.CLASS_NAME, 'error-page')
    assert len(error_page) > 0, 'This page is not error page'

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_93
def test_no_93(driver):
    """No.93 Download file with secret URL is failed
    
    Secret URL is enabled and switch to disabled after email is sent
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Private
    User's Role is Repository Administrator
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # enable secret url
    set_secret_url_with_login(driver, True)

    # log in as Repository Administrator
    login_as_target(driver, 'Repository')

    # search target item
    search_and_display_target_item(driver, config.item_name_dic['private'])

    # display content's info
    click_file_information_button(driver)

    # click secret url button
    click_secret_url_btn(driver)

    # log out
    logout(driver)

    # disable secret url
    set_secret_url_with_login(driver, False)

    # log in as Repository Administrator
    login_as_target(driver, 'Repository')

    # download the target file
    click_mail_link(driver, config.users['Repository']['mail'].split('@', 1)[0])

    # check error page has the class what name is error-page
    error_page = driver.find_elements(By.CLASS_NAME, 'error-page')
    assert len(error_page) > 0, 'This page is not error page'

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_94
def test_no_94(driver):
    """No.94 Download file with secret URL is failed
    
    Secret URL is enabled and switch to disabled after email is sent
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Private
    User's Role is Contributor and the item's owner
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # enable secret url
    set_secret_url_with_login(driver, True)

    # log in as Contributor
    login_as_target(driver, 'RegCon')

    # search target item
    search_and_display_target_item(driver, config.item_name_dic['private'])

    # display content's info
    click_file_information_button(driver)

    # click secret url button
    click_secret_url_btn(driver)

    # log out
    logout(driver)

    # disable secret url
    set_secret_url_with_login(driver, False)

    # log in as Contributor
    login_as_target(driver, 'RegCon')

    # download the target file
    click_mail_link(driver, config.users['RegCon']['mail'].split('@', 1)[0])

    # check error page has the class what name is error-page
    error_page = driver.find_elements(By.CLASS_NAME, 'error-page')
    assert len(error_page) > 0, 'This page is not error page'

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_95
def test_no_95(driver):
    """No.95 The number of possible downloads does not change by changing Download Limit
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3 and switch to 5 after email is sent
    Access Setting is Open Date and publish date is after today
    User's Role is Repository Administrator
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # enable secret url and set download limit to 3
    set_secret_url_with_login(driver, True)
    change_secret_url_download_limit_with_login(driver, 3)

    # log in as Repository Administrator
    login_as_target(driver, 'Repository')

    # search target item
    search_and_display_target_item(driver, config.item_name_dic['before_publish'])

    # display content's info
    click_file_information_button(driver)

    # click secret url button
    click_secret_url_btn(driver)

    # log out
    logout(driver)

    # set download limit to 5
    change_secret_url_download_limit_with_login(driver, 5)

    # log in as Repository Administrator
    login_as_target(driver, 'Repository')

    # download the target content several times
    for i in range(6):
        click_mail_link(driver, config.users['Repository']['mail'].split('@', 1)[0])
        if i < 5:
            # check download file
            parentheses = ' (' + str(i) + ')' if i > 0 else ''
            file_list = os.listdir(config.base_download_dir)
            assert 'before_publish' + parentheses + '.txt' in file_list
        else:
            # check over download limit error message
            check_over_download_limit_error_message(driver)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

    # move download files to do other tests
    move_target_files = [file for file in file_list if file.startswith('before_publish')]
    move_downloaded_files(move_target_files, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_96
def test_no_96(driver):
    """No.96 The number of possible downloads does not change by changing Download Limit
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3 and switch to 5 after email is sent
    Access Setting is Open Date and publish date is after today
    User's Role is Contributor and the item's owner
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # enable secret url and set download limit to 3
    set_secret_url_with_login(driver, True)
    change_secret_url_download_limit_with_login(driver, 3)

    # log in as Contributor
    login_as_target(driver, 'RegCon')

    # search target item
    search_and_display_target_item(driver, config.item_name_dic['before_publish'])

    # display content's info
    click_file_information_button(driver)

    # click secret url button
    click_secret_url_btn(driver)

    # log out
    logout(driver)

    # set download limit to 5
    change_secret_url_download_limit_with_login(driver, 5)

    # log in as Contributor
    login_as_target(driver, 'RegCon')

    # download the target content several times
    for i in range(6):
        click_mail_link(driver, config.users['RegCon']['mail'].split('@', 1)[0])
        if i < 5:
            # check download file
            parentheses = ' (' + str(i) + ')' if i > 0 else ''
            file_list = os.listdir(config.base_download_dir)
            assert 'before_publish' + parentheses + '.txt' in file_list
        else:
            # check over download limit error message
            check_over_download_limit_error_message(driver)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

    # move download files to do other tests
    move_target_files = [file for file in file_list if file.startswith('before_publish')]
    move_downloaded_files(move_target_files, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_97
def test_no_97(driver):
    """No.97 The number of possible downloads does not change by changing Download Limit
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3 and switch to 5 after email is sent
    Access Setting is Private
    User's Role is Repository Administrator
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # enable secret url and set download limit to 3
    set_secret_url_with_login(driver, True)
    change_secret_url_download_limit_with_login(driver, 3)

    # log in as Repository Administrator
    login_as_target(driver, 'Repository')

    # search target item
    search_and_display_target_item(driver, config.item_name_dic['private'])

    # display content's info
    click_file_information_button(driver)

    # click secret url button
    click_secret_url_btn(driver)

    # log out
    logout(driver)

    # set download limit to 5
    change_secret_url_download_limit_with_login(driver, 5)

    # log in as Repository Administrator
    login_as_target(driver, 'Repository')

    # download the target content several times
    for i in range(6):
        click_mail_link(driver, config.users['Repository']['mail'].split('@', 1)[0])
        if i < 5:
            # check download file
            parentheses = ' (' + str(i) + ')' if i > 0 else ''
            file_list = os.listdir(config.base_download_dir)
            assert 'private' + parentheses + '.txt' in file_list
        else:
            # check over download limit error message
            check_over_download_limit_error_message(driver)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

    # move download files to do other tests
    move_target_files = [file for file in file_list if file.startswith('private')]
    move_downloaded_files(move_target_files, inspect.currentframe().f_code.co_name)

# pytest auto_test/test_secret_url.py::test_no_98
def test_no_98(driver):
    """No.98 The number of possible downloads does not change by changing Download Limit
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3 and switch to 5 after email is sent
    Access Setting is Private
    User's Role is Contributor and the item's owner
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # enable secret url and set download limit to 3
    set_secret_url_with_login(driver, True)
    change_secret_url_download_limit_with_login(driver, 3)

    # log in as Contributor
    login_as_target(driver, 'RegCon')

    # search target item
    search_and_display_target_item(driver, config.item_name_dic['private'])

    # display content's info
    click_file_information_button(driver)

    # click secret url button
    click_secret_url_btn(driver)

    # log out
    logout(driver)

    # set download limit to 5
    change_secret_url_download_limit_with_login(driver, 5)

    # log in as Contributor
    login_as_target(driver, 'RegCon')

    # download the target content several times
    for i in range(6):
        click_mail_link(driver, config.users['RegCon']['mail'].split('@', 1)[0])
        if i < 5:
            # check download file
            parentheses = ' (' + str(i) + ')' if i > 0 else ''
            file_list = os.listdir(config.base_download_dir)
            assert 'private' + parentheses + '.txt' in file_list
        else:
            # check over download limit error message
            check_over_download_limit_error_message(driver)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

    # move download files to do other tests
    move_target_files = [file for file in file_list if file.startswith('private')]
    move_downloaded_files(move_target_files, inspect.currentframe().f_code.co_name)

# The tests No.99-102 are in shell_test/test_secret_url_changing_deadline.py

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

def check_secret_url_button_is_hidden(driver, is_hidden):
    """Check secret url button is hidden or not
    
    Args:
        driver(WebDriver): WebDriver object
        is_hidden(bool): whether secret url button is hidden or not
    """
    # check secret url button is hidden or not
    table = driver.find_element(
        By.XPATH,
        '//*[@id="detail-item"]/div[3]/div/div[2]/div/div/div[1]/table'
    )
    bodys = table.find_elements(By.XPATH, './/tbody/tr/td')
    is_exist = False
    for b in bodys:
        a_tag = b.find_elements(By.XPATH, './/a')
        for a in a_tag:
            if a.text == 'Secret URL':
                is_exist = True
                break
        if is_exist:
            break

    # is_hidden is True and is_exist is True -> assert False
    if is_hidden and is_exist:
        assert False, 'Secret URL button is not hidden'
    # is_hidden is False and is_exist is False -> assert False
    if not is_hidden and not is_exist:
        assert False, 'Secret URL button is hidden'
    assert True

def check_permission_error_page(driver):
    """Check permission error page
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # check error page does't have weko's panel component
    components = driver.find_elements(By.XPATH, '//*[@id="panel-main-content"]')
    assert len(components) == 0, 'This page is not error page'

    # check error page has the class what name is error-page
    error_page = driver.find_elements(By.CLASS_NAME, 'error-page')
    assert len(error_page) > 0, 'This page is not error page'

    # check error message
    error_message = error_page[0].find_element(By.XPATH, './/div/div/h1')
    assert error_message.text == 'Permission required', 'Error message is not "Permission required"'

def check_over_download_limit_error_message(driver):
    """Check over download limit error message
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # check error page has the class what name is error-page
    error_page = driver.find_elements(By.CLASS_NAME, 'error-page')
    assert len(error_page) > 0, 'This page is not error page'

    # check error message
    error_message = error_page[0].find_element(By.XPATH, './/div/div/h1')
    assert error_message.text == 'The download limit has been exceeded.',\
        'Error message is not "The download limit has been exceeded."'

def check_login_page(driver):
    """Check transition destination is login page
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # check transition destination is login page
    url = driver.current_url
    assert url.startswith(config.base_url + '/login'), 'Transition destination is not login page'

    # check next page is file detail page
    url_next = url.split('?next=')[1]
    assert url_next.find('file_details') != -1, 'Next page is not file detail page'

def check_secret_url_mail(driver, mail_address, item_name, expiration_date_num, download_limit):
    """Check secret url mail
    
    Args:
        driver(WebDriver): WebDriver object
        mail_address(str): mail address
        item_name(str): item name
        expiration_date_num(int): expiration date
        download_limit(int): download limit
    """
    # get target file name
    file_name = driver.find_element(
        By.XPATH,
        '//*[@id="detail-item"]/div[3]/div/div[2]/div/div/div[1]/table/tbody/tr/td[1]/span/a'
    ).text.split(' ')[0]

    # find target mail
    xs = []
    target_user = mail_address.split('@')[0]
    for root, _, files in os.walk('mail/' + target_user + '/new'):
        for file in files:
            path = os.path.join(root, file)
            xs.append((os.path.getmtime(path), path))
    target_mail = sorted(xs, reverse=True)[0][1]

    # check mail recipient
    with open(target_mail, 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()
    recipient = [line for line in lines if line.startswith('To: ')]
    assert recipient[0].split(' ')[1] == mail_address

    # check mail body
    secret_url_info_jp = [line for line in lines if line.endswith('シークレットURLを作成しました。')]
    secret_url_info_en = [line for line in lines if line.startswith('Secret URL for')]
    limit_sentence_jp = [line for line in lines if line.startswith('このURLは')]
    limit_sentence_en = [line for line in lines if line.startswith('This URL is')]
    download_limit_sentence_jp = [line for line in lines if line.startswith('ダウンロードは')]
    download_limit_sentence_en = [line for line in lines if line.startswith('You can download')]
    expiration_date = datetime.datetime.today() + datetime.timedelta(days=expiration_date_num+1)
    assert secret_url_info_jp[0].find(item_name) != -1\
        and secret_url_info_jp[0].find(file_name) != -1
    assert secret_url_info_en[0].find(item_name) != -1\
        and secret_url_info_en[0].find(file_name) != -1
    assert limit_sentence_jp[0].find(expiration_date.strftime('%Y-%m-%d')) != -1
    assert limit_sentence_en[0].find(expiration_date.strftime('%Y-%m-%d')) != -1
    assert download_limit_sentence_jp[0].find(str(download_limit) + '回') != -1
    assert download_limit_sentence_en[0].find(str(download_limit) + ' times') != -1

def check_secret_url_is_difference(user_name):
    """Check secret url is difference between the latest mail and the second latest mail
    
    Args:
        user_name(str): user name
    """
    # create path where mail is saved
    path = 'mail/' + user_name + '/new'

    # get all mail
    mail_list = os.listdir(path)

    # get the latest mail
    with open(path + '/' + mail_list[-1], 'r', encoding='utf-8') as f:
        text = f.read()
        latest_url = re.search('https://.*', text).group()

    # get the second latest mail
    with open(path + '/' + mail_list[-2], 'r', encoding='utf-8') as f:
        text = f.read()
        second_latest_url = re.search('https://.*', text).group()

    # compare the latest mail and the second latest mail
    assert latest_url != second_latest_url

def save_screenshot(driver, co_name):
    """Save screenshot
    
    Args:
        driver(WebDriver): WebDriver object
        co_name(str): test case name
    """
    time.sleep(1)
    driver.save_screenshot(
        config.base_save_folder + 'secret_url/' + d + "_" + co_name + ".png")

def move_downloaded_files(target_file_name_list, method_name):
    """Move downloaded files to the directory of each test case
    
    Args:
        target_file_name_list(list): target file name list
        method_name(str): target method name
    """
    directory_name = d + '_' + method_name
    os.makedirs(config.base_download_dir + 'secret_url/' + directory_name, exist_ok=True)
    for target_file_name in target_file_name_list:
        shutil.move(
            config.base_download_dir + target_file_name,
            config.base_download_dir + 'secret_url/' + directory_name
        )
