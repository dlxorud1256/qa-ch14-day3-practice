from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

options = Options()
options.add_argument("--guest")
options.add_argument("--disable-features=PasswordLeakDetection,AutofillServerCommunication,OptInRelaunch")

def xpath_axes_problems(driver, wait):
    print("\n--- XPath Axes 문제 ---")
    # 1. id='xpath-head' 인 h3 >> 다음에 오는 형제들 중, 첫번재 형제(ul) >> 의 자식 중, 두번재 자식(li) 선택
    locator_xpath_1 = (By.XPATH, "")
    second_li = wait.until(EC.presence_of_element_located(locator_xpath_1))
    print("xpath 문제 1 완료(html):", second_li.get_attribute("outerHTML"))

    # 2. text()='Item B'인  li >> 바로 이전 형제 li
    locator_xpath_2 = (By.XPATH, "")
    prev_li = wait.until(EC.presence_of_element_located(locator_xpath_2))
    print("xpath 문제 2 완료(text):", prev_li.text)

    # 3. text()='Item B'인  li >> 바로 이후 형제 li
    locator_xpath_3 = (By.XPATH, "")
    next_li = wait.until(EC.presence_of_element_located(locator_xpath_3))
    print("xpath 문제 3 완료(text):", next_li.text)

print("!!STARTED!!")
with webdriver.Chrome(options=options) as driver:
    wait = WebDriverWait(driver, 10)
    driver.get("https://jinny-dev-anything.github.io/locator_ex_webpage")

    xpath_axes_problems(driver, wait)

    print("\n!!FINISHED!!")
    driver.quit()
