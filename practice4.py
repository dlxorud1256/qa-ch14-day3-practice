from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

options = Options()
options.add_argument("--guest")
options.add_argument("--disable-features=PasswordLeakDetection,AutofillServerCommunication,OptInRelaunch")

"""
주어진 practice4.py를 POM + Helper + Test 구조로 분리해 보세요
- POM (form_page.py): Locator 정의, 입력 및 제출 기능 포함
- Helper (selenium_helper.py): EC 관련 유틸 함수 (예: wait_for_element, wait_for_alert)
- Test (day2_practice.py): POM과 Helper만 사용해서 테스트 수행
"""

def basic_locators_problems(driver, wait):
    print("\n--- 문제 4: POM 적용 Form 입력 테스트 ---")
    
    # 1. 요소 찾기
    text_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='text']")))
    email_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='email']")))
    pwd_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='password']")))
    submit_button = wait.until(EC.presence_of_element_located((By.ID, "btn-form-submit")))

    print("텍스트 입력 필드:", text_input.get_attribute("outerHTML"))
    print("이메일 입력 필드:", email_input.get_attribute("outerHTML"))
    print("비밀번호 입력 필드:", pwd_input.get_attribute("outerHTML"))
    print("Submit 버튼:", submit_button.get_attribute("outerHTML"))

    # 2. 값 입력 / 선택
    text_input.send_keys("Hello World")
    email_input.send_keys("test@example.com")
    pwd_input.send_keys("pass1234")

    # 3. 버튼 클릭 → alert 확인
    submit_button.click()

    try:
        alert = wait.until(EC.alert_is_present())
        print("alert text:", alert.text)
        alert.accept()
        print("완료")
    except:
        print("실패: alert 없음")

print("!!STARTED!!")

with webdriver.Chrome(options=options) as driver:
    wait = WebDriverWait(driver, 10)
    driver.get("https://jinny-dev-anything.github.io/locator_ex_webpage")

    basic_locators_problems(driver, wait)

    print("\n!!FINISHED!!")
    driver.quit()
