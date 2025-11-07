import os
import pytest
import time

import config
from methods_required_during_testing import login, logout, set_secret_url,\
    change_secret_url_expiration_date, change_secret_url_download_limit
from selenium.webdriver.common.by import By

@pytest.fixture()
def driver():
    """Setup driver
    
    Returns:
        WebDriver: The driver instance
    """
    setup_driver = config.SetupDriver()
    try:
        setup_driver.setup_driver()
        setup_driver.driver.execute_script('window.scroll(0, 0)')
        time.sleep(3)
        setup_driver.driver.find_element(
            By.XPATH,
            '//*[@id="klaro"]/div/div/div/div/div/button'
        ).click()
        yield setup_driver.driver
        logout(setup_driver.driver)
        setup_driver.teardown_method()
        time.sleep(1)
    except Exception as e:
        setup_driver.teardown_method()
        time.sleep(1)
        raise e
    finally:
        # Clean download folder
        file_paths = [
            os.path.join(config.base_download_dir, f)
            for f in os.listdir(config.base_download_dir)
            if os.path.isfile(os.path.join(config.base_download_dir, f))
        ]
        for file_path in file_paths:
            os.remove(file_path)

@pytest.fixture()
def enable_secret_url(driver):
    """Enable secret URL
    
    Args:
        driver (WebDriver): The driver instance

    Returns:
        WebDriver: The driver instance
    """
    login(driver, config.users['System']['mail'], config.users['System']['password'])
    set_secret_url(driver, True)
    change_secret_url_expiration_date(driver, 3)
    change_secret_url_download_limit(driver, 3)
    logout(driver)
    return driver

@pytest.fixture()
def disable_secret_url(driver):
    """Disable secret URL
    
    Args:
        driver (WebDriver): The driver instance

    Returns:
        WebDriver: The driver instance
    """
    login(driver, config.users['System']['mail'], config.users['System']['password'])
    set_secret_url(driver, False)
    change_secret_url_expiration_date(driver, 3)
    change_secret_url_download_limit(driver, 3)
    logout(driver)
    return driver
