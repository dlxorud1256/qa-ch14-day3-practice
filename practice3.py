from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

options = Options()
options.add_argument("--guest")
options.add_argument("--disable-features=PasswordLeakDetection,AutofillServerCommunication,OptInRelaunch")

def mouse_actions_problems(driver, wait):
    print("\n--- Mouse Actions 문제 ---")
    actions = ActionChains(driver)

    # 1. section(class="long-text")로 이동(스크롤) >> 버튼(id="btn-form-submit")로 이동(스크롤) >> 해당 버튼 클릭
    locator_css = (By.CSS_SELECTOR, "")
    locator_btn = (By.ID, "")
    scroll_elem = wait.until(EC.presence_of_element_located(locator_css))
    submit_button = wait.until(EC.presence_of_element_located(locator_btn))
    actions.xxxx
    
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
    locator_hover = (By.ID, "")
    hover_elem = wait.until(EC.presence_of_element_located(locator_hover))
    actions.xxxx
    
    locator_button_menu = (By.ID, "")
    submenu_button = wait.until(EC.element_to_be_clickable(locator_button_menu))
    submenu_button.click()
    print("actions 문제 2(마우스 오버>버튼클릭) 완료")


print("!!STARTED!!")
with webdriver.Chrome(options=options) as driver:
    wait = WebDriverWait(driver, 10)
    driver.get("https://jinny-dev-anything.github.io/locator_ex_webpage")

    mouse_actions_problems(driver, wait)

    print("\n!!FINISHED!!")
    driver.quit()
