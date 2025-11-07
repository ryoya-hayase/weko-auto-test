from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import datetime
import os
import re
import config

d = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

def is_integer(n):
    """Check if n is integer
    
    Args:
        n(str): number"""
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()

def logout(driver):
    """Logout from WEKO
    
    Args:
        driver(WebDriver): WebDriver object
    """
    driver.get(config.base_url + "/logout/")
    time.sleep(1)

def until_complete_download(time_limit):
    """Wait until download is complete
    
    Args:
        time_limit(int): time limit
    """
    for x in range(time_limit):
        file_list = os.listdir(config.base_download_dir)
        for filename in file_list:
            if re.search(r".*\.com\.google\.Chrome.*", filename) != None or re.search(r".*\.crdownload", filename) != None:
                # print(re.search(r"\.com\.google\.Chrome.*", filename), re.search(r"\.crdownload", filename))
                time.sleep(1)
                if x == time_limit - 1:
                    raise Exception(f"Download did not complete within {time_limit} seconds")
                break

# SecretURL
def login(driver, account_mail, account_password):
    """Login to WEKO
    
    Args:
        driver(WebDriver): WebDriver object
        account_mail(str): account mail address
        account_password(str): account password
    """
    # access to WEKO's TOP page
    driver.get(config.base_url)
    driver.implicitly_wait(10)

    # show Login page with press login button
    driver.find_element(By.XPATH, '//*[@id="fixed_header"]/form/a[1]').click()
    driver.implicitly_wait(10)

    # enter mail-address and password and click login button
    driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(account_mail)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(account_password)
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div/div[1]/form/button').click()
    time.sleep(1)

    # check if login is successful
    url = driver.current_url
    retry_count = 0
    err_msg = ''
    while url == config.base_url + '/login/' and retry_count < 10:
        time.sleep(5)
        driver.find_element(By.XPATH, '//*[@id="email"]').clear()
        driver.find_element(By.XPATH, '//*[@id="password"]').clear()
        driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(account_mail)
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(account_password)
        driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div/div[1]/form/button').click()
        time.sleep(1)
        url = driver.current_url
        retry_count += 1
        if retry_count == 10:
            err_msg = "Login failed"
    assert not err_msg, err_msg

def change_secret_url_expiration_date(driver, expiration_date):
    """Change SecretURL Expiration Date
    
    Args:
        driver(WebDriver): WebDriver object
        expiration_date(int): expiration date
    """
    # access to Administration/restricted access page
    driver.get(config.base_url + "/admin/restricted_access/")
    driver.implicitly_wait(10)

    # check if SecretURL is enabled
    check_box = driver.find_element(By.XPATH, '//*[@id="secret_enable"]')
    if check_box.get_attribute("checked") == "true":
        if is_integer(expiration_date):
            # change expiration_date
            driver.find_element(By.XPATH, '//*[@id="secret_expiration_date"]').clear()
            driver.find_element(By.XPATH, '//*[@id="secret_expiration_date"]').send_keys(expiration_date)
            driver.find_element(By.XPATH, '//*[@id="save-btn"]').click()
        else:
            print("Expiration Date must be an integer")
    else:
        print("Secret URL is not enable")

    time.sleep(1)

def change_secret_url_expiration_date_with_login(driver, days):
    """Change secret url expiration date with login as System Administrator

    Args:
        driver(WebDriver): WebDriver object
        days(int): expiration date
    """
    # log in as System Administrator
    login(driver, config.users['System']['mail'], config.users['System']['password'])

    # change secret url expiration date
    change_secret_url_expiration_date(driver, days)

    # log out
    logout(driver)

def change_secret_url_download_limit(driver, download_limit):
    """Change SecretURL Download Limit
    
    Args:
        driver(WebDriver): WebDriver object
        download_limit(int): download limit count
    """
    # access to Administration/restricted access page
    driver.get(config.base_url + "/admin/restricted_access/")
    driver.implicitly_wait(10)

    # check if SecretURL is enabled
    check_box = driver.find_element(By.XPATH, '//*[@id="secret_enable"]')
    if check_box.get_attribute("checked") == "true":
        if is_integer(download_limit):
            driver.find_element(By.XPATH, '//*[@id="secret_download_limit"]').clear()
            driver.find_element(By.XPATH, '//*[@id="secret_download_limit"]').send_keys(download_limit)
            driver.find_element(By.XPATH, '//*[@id="save-btn"]').click()
        else:
            print("Download Limit must be an integer")
    else:
        print("Secret URL is not enable")

    time.sleep(1)

def change_secret_url_download_limit_with_login(driver, limit):
    """Change secret url download limit with login as System Administrator

    Args:
        driver(WebDriver): WebDriver object
        limit(int): download limit
    """
    # log in as System Administrator
    login(driver, config.users['System']['mail'], config.users['System']['password'])

    # change secret url download limit
    change_secret_url_download_limit(driver, limit)

    # log out
    logout(driver)

def click_secret_url_btn(driver):
    """Click SecretURL button
    
    Args:
        driver(WebDriver): WebDriver object
    """
    driver.find_element(By.XPATH, '//*[@id="secret_url"]').click()

    # set timestamp to link name
    timestamp = int(time.time())
    driver.find_element(By.XPATH, '//*[@id="link_name"]').clear()
    driver.find_element(By.XPATH, '//*[@id="link_name"]').send_keys(str(timestamp))

    # Check the mail notification checkbox
    mail_checkbox = driver.find_element(By.XPATH, '//*[@id="send_email"]')
    if not mail_checkbox.is_selected():
        mail_checkbox.click()

    # click create_secret_url button
    driver.find_element(By.XPATH, '//*[@id="create_secret_url"]').click()

    wait = WebDriverWait(driver, timeout=10)
    wait.until(expected_conditions.alert_is_present())

    driver.switch_to.alert.accept()

    time.sleep(1)

def click_mail_link(driver, user):
    """Click mail link
    
    Args:
        driver(WebDriver): WebDriver object
        user(str): user name
    """
    mail_list = os.listdir("mail/" + user + "/new")

    with open("mail/" + user + "/new/" + mail_list[-1], "r", encoding='utf-8') as f:
        text = f.read()
        url = re.search("https://.*", text).group()
        driver.get(url)

    try:
        until_complete_download(10)
    except Exception as e:
        print(e)
    time.sleep(1)

# ダウンロードボタンまたは利用申請ボタン押下
def click_detail_item_button(driver):
    """Click Download button or Apply button
    
    Args:
        driver(WebDriver): WebDriver object
    """
    driver.find_element(By.XPATH, '//*[@id="detail-item"]/table/tbody/tr/td[3]/a[1]/button').click()

# プリントボタン押下
def click_print_btn(driver):
    """Click Print button
    
    Args:
        driver(WebDriver): WebDriver object
    """
    driver.find_element(By.XPATH, '//*[@id="print-btn"]').click()

# 利用申請メール入力・送信
def enter_guest_email_for_get_usage_application(driver, guest_mail):
    """Enter guest email address for get usage application
    
    Args:
        driver(WebDriver): WebDriver object
        guest_mail(str): guest email address
    """
    driver.find_element(By.XPATH, '//*[@id="user_mail"]').send_keys(guest_mail)
    driver.find_element(By.XPATH, '//*[@id="user_mail_confirm"]').send_keys(guest_mail)
    if driver.find_elements(By.XPATH, '//*[@id="password_for_download"]'):
        driver.find_element(By.XPATH, '//*[@id="password_for_download"]')\
            .send_keys(config.guest_password)
        driver.find_element(By.XPATH, '//*[@id="password_for_download_confirm"]')\
            .send_keys(config.guest_password)
    driver.find_element(By.XPATH, '//*[@id="confirm_email_btn"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="modalSendEmailSuccess"]/div/div/div[3]/div/button')\
        .click()

# WF承認
def click_approval_btn(driver):
    """Click Approval button
    
    Args:
        driver(WebDriver): WebDriver object
    """
    driver.find_element(By.XPATH, '//*[@id="btn-approval"]').click()

# WF却下
def click_reject_btn(driver):
    """Click Reject button
    
    Args:
        driver(WebDriver): WebDriver object
    """
    driver.find_element(By.XPATH, '//*[@id="btn-reject"]').click()

# 利用申請承認後のゲストでのDL（メールアドレス入力）
def enter_guest_email_after_approval(driver, guest_mail):
    """Enter guest email address after approval
    
    Args:
        driver(WebDriver): WebDriver object
        guest_mail(str): guest email address
    """
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, '//*[@id="mail_form"]').send_keys(guest_mail)
    if driver.find_elements(By.XPATH, '//*[@id="input_password"]'):
        driver.find_element(By.XPATH, '//*[@id="input_password"]')\
            .send_keys(config.guest_password)
    driver.find_element(By.XPATH, '//*[@id="mailaddress_confirm_download"]').click()

# WF強制終了ボタン押下
def click_quit_btn(driver):
    """Click Quit button
    
    Args:
        driver(WebDriver): WebDriver object
    """
    driver.find_element(By.XPATH, '//*[@id="btn_quit"]').click()

def transition_to_mail_template(driver):
    """Transition to Mail Template page
    
    Args:
        driver(WebDriver): WebDriver object
    """
    driver.get(config.base_url + "/admin/mailtemplates/")
    time.sleep(1)

def set_secret_url(driver, param):
    """Set SecretURL Status.

    Args:
        driver(WebDriver): WebDriver object
        param(bool): On(True) or OFF(False)
    """
    # access to Administration/restricted access page
    driver.get(config.base_url + "/admin/restricted_access/")
    WebDriverWait(driver, 10).until(
        lambda d: len(d.find_elements(By.XPATH, '//*[@id="secret_enable"]')) > 0,
        'Restricted Access page loading timeout'
    )

    # click 'SecretURL enable button' if its checked is not equal to param
    check_box = driver.find_element(By.XPATH, '//*[@id="secret_enable"]')
    if bool(check_box.get_attribute("checked")) != param:
        check_box.click()
        driver.find_element(By.XPATH, '//*[@id="save-btn"]').click()

    time.sleep(1)

def set_secret_url_with_login(driver, enable):
    """Set secret url with login as System Administrator
    
    Args:
        driver(WebDriver): WebDriver object
        enable(bool): whether to enable secret url or not
    """
    # log in as System Administrator
    login(driver, config.users['System']['mail'], config.users['System']['password'])

    # set secret url
    set_secret_url(driver, enable)

    # log out
    logout(driver)

def transition_to_restricted_access(driver):
    """Transition to Restricted Access page
    
    Args:
        driver(WebDriver): WebDriver object
    """
    driver.get(config.base_url + "/admin/restricted_access/")
    time.sleep(1)

def search_and_display_target_item(driver, param):
    """Search and display target item
    
    Args:
        driver(WebDriver): WebDriver object
        param(str): target item's title
    """
    # access to WEKO's TOP page
    driver.get(config.base_url)
    WebDriverWait(driver, 10).until(
        lambda d: len(d.find_elements(By.XPATH, '//*[@id="loading-bar"]')) == 0,
        'Top page loading timeout'
    )

    # search target item
    search_box = driver.find_element(By.XPATH, '//*[@id="q"]')
    search_box.send_keys(param)
    driver.find_element(By.XPATH, '//*[@id="top-search-btn"]').click()
    WebDriverWait(driver, 10).until(
        lambda d: len(d.find_elements(By.XPATH, '//*[@id="loading-bar"]')) == 0,
        'Search results loading timeout'
    )

    options = driver.find_element(By.XPATH, '//*[@id="sortType"]')\
        .find_elements(By.TAG_NAME, 'option')
    for option in options:
        if option.text == 'asc':
            option.click()
            time.sleep(3)
            break

    # display target item
    search_result = driver.find_element(
        By.XPATH, '//*[@id="index_item_list"]/div[2]/div/div/invenio-search-results')
    search_result_list = search_result.find_elements(By.CLASS_NAME, 'panel')
    for result in search_result_list:
        header = result.find_element(By.XPATH, './/div/div/a')
        if header.text == param:
            header.click()
            break

    time.sleep(3)

def click_file_information_button(driver):
    """Click File Information button
    
    Args:
        driver(WebDriver): WebDriver object
    """
    button_list = driver.find_element(
        By.XPATH, '//*[@id="detail-item"]/table/tbody/tr/td[3]').find_elements(By.TAG_NAME, 'a')
    for button in button_list:
        if button.text == 'Information':
            button.click()
            break
    time.sleep(1)

def change_usage_report_workflow_access(driver, expiration_date, expiration_date_unlimited=False):
    """Change Usage Report Workflow Access
    
    Args:
        driver(WebDriver): WebDriver object
        expiration_date(int): expiration date
        expiration_date_unlimited(bool): expiration date unlimited
    """
    # access to Administration/restricted access page
    transition_to_restricted_access(driver)

    location = driver.find_element(By.XPATH, '//*[@id="download_limit"]').location
    driver.execute_script('window.scrollTo(0, ' + str(location['y']) + ')')

    expiration_date_unlimited_check = \
        driver.find_element(By.XPATH, '//*[@id="expiration_date_access_unlimited_chk"]')
    # set expiration_date_unlimited_checkbox
    if (expiration_date_unlimited_check.get_attribute('checked') is not None) !=\
        expiration_date_unlimited:
        expiration_date_unlimited_check.click()
        driver.find_element(By.XPATH, '//*[@id="save-btn"]').click()
    if not expiration_date_unlimited:
        if is_integer(expiration_date):
            # change expiration_date
            target_element = driver.find_element(By.XPATH, '//*[@id="expiration_date_access"]')
            target_element.clear()
            target_element.send_keys(expiration_date)
            driver.find_element(By.XPATH, '//*[@id="save-btn"]').click()
        else:
            print('Expiration Date must be an integer')

    time.sleep(1)

def get_mail_template_body_element(driver):
    """Get Mail Template Body Element

    Args:
        driver(WebDriver): WebDriver object

    Returns:
        WebElement: Mail Template Body Element
    """
    mail_template_elements = driver.find_elements(By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div/div')
    for element in mail_template_elements:
        if element.tag_name == 'div':
            textareas = element.find_elements(By.TAG_NAME, 'textarea')
            if textareas:
                return textareas[0]
