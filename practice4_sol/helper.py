from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_element(driver, by_locator, timeout=10):
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.presence_of_element_located(by_locator))

def wait_for_alert(driver, timeout=5):
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.alert_is_present())
