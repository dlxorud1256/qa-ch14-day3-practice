from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

options = Options()
options.add_argument("--guest")
options.add_argument("--disable-features=PasswordLeakDetection,AutofillServerCommunication,OptInRelaunch")

def iframe_problems(driver, wait):
    print("\n--- Iframe 문제 ---")

    # details section 열기
    details_elem = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "section details")))
    details_elem.click()

    # 1. 대상 iframe 으로 이동(switch_to)
    iframe = wait.until(EC.presence_of_element_located((By.ID, "test-iframe")))
    driver.xxxx

    # 2. iframe 내부 input(id="iframe-input") 확인
    locator_input = (By.ID, "")
    iframe_input = wait.until(EC.presence_of_element_located(locator_input))
    print("ifram 문제2(내부 input placeholder):", iframe_input.get_attribute("placeholder"))

    
    # 3. 원래 창(default content)으로 복귀 후, h1 확인
    driver.xxx
    header = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    print("ifram 문제3(원래창 헤더 text):", header.text)



print("!!STARTED!!")
with webdriver.Chrome(options=options) as driver:
    wait = WebDriverWait(driver, 10)
    driver.get("https://jinny-dev-anything.github.io/locator_ex_webpage")

    iframe_problems(driver, wait)

    print("\n!!FINISHED!!")
    driver.quit()
