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
    locator_1 = "//h3[@id='xpath-head']/following-sibling::ul[1]/li[2]"
    second_li = wait.until(EC.presence_of_element_located((By.XPATH, locator_1)))
    print("xpath 문제 1 완료(html):", second_li.get_attribute("outerHTML"))

    # 2. text()='Item B'인  li >> 바로 이전 형제 li
    prev_li = wait.until(
        EC.presence_of_element_located((By.XPATH, "//li[text()='Item B']/preceding-sibling::li"))
    )
    print("xpath 문제 2 완료(text):", prev_li.text)

    # 3. text()='Item B'인  li >> 바로 이후 형제 li
    next_li = wait.until(
        EC.presence_of_element_located((By.XPATH, "//li[text()='Item B']/following-sibling::li"))
    )
    print("xpath 문제 3 완료(text):", next_li.text)


def iframe_problems(driver, wait):
    print("\n--- Iframe 문제 ---")

    # details section 열기
    details_elem = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "section details")))
    details_elem.click()

    # 1. 대상 iframe 으로 이동
    iframe = wait.until(EC.presence_of_element_located((By.ID, "test-iframe")))
    driver.switch_to.frame(iframe)

    # 2. iframe 내부 input(id="iframe-input") 확인
    iframe_input = wait.until(EC.presence_of_element_located((By.ID, "iframe-input")))
    print("ifram 문제2(내부 input placeholder):", iframe_input.get_attribute("placeholder"))

    
    # 3. 원래 창(default content)으로 복귀 후, h1 확인
    driver.switch_to.default_content()
    header = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    print("ifram 문제3(원래창 헤더 text):", header.text)


def mouse_actions_problems(driver, wait):
    print("\n--- Mouse Actions 문제 ---")
    actions = ActionChains(driver)

    # 1. section(class="long-text")로 이동(스크롤) >> 버튼(id="btn-form-submit")로 이동(스크롤) >> 해당 버튼 클릭
    scroll_elem = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "section.long-text")))
    submit_button = wait.until(EC.presence_of_element_located((By.ID, "btn-form-submit")))
    actions.move_to_element(scroll_elem).move_to_element(submit_button).click().perform()
    
    # 정상적으로 버튼이 클릭 되었을 경우, alert 처리
    try:
        alert = wait.until(EC.alert_is_present())
        print("Alert text:", alert.text)
        alert.accept()
        print("actions 문제 1(스크롤) 완료")
    except Exception:
        print("No alert appeared")
        print("actions 문제 1(스크롤) 실패")

    # 2. div(id="hover-menu")에 마우스 오버(Hover) >> 버튼(id="hover-submenu-button") 클릭가능한지 확인 후 클릭
    hover_elem = wait.until(EC.presence_of_element_located((By.ID, "hover-menu")))
    actions.move_to_element(hover_elem).perform()
    submenu_button = wait.until(EC.element_to_be_clickable((By.ID, "hover-submenu-button")))
    submenu_button.click()
    print("actions 문제 2(마우스 오버>버튼클릭) 완료")


print("!!STARTED!!")
with webdriver.Chrome(options=options) as driver:
    wait = WebDriverWait(driver, 10)
    driver.get("https://jinny-dev-anything.github.io/locator_ex_webpage")

    xpath_axes_problems(driver, wait)
    iframe_problems(driver, wait)
    mouse_actions_problems(driver, wait)

    print("\n!!FINISHED!!")
    driver.quit()
