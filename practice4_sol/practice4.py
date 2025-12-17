from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from form_page import FormPage

options = Options()
options.add_argument("--guest")
options.add_argument("--disable-features=PasswordLeakDetection,AutofillServerCommunication,OptInRelaunch")

print("!!STARTED!!")

with webdriver.Chrome(options=options) as driver:
    driver.get("https://jinny-dev-anything.github.io/locator_ex_webpage")

    form_page = FormPage(driver)

    print("\n--- 문제 4: POM 적용 Form 입력 테스트 ---")
    form_page.enter_text("Hello World")
    form_page.enter_email("test@example.com")
    form_page.enter_password("pass1234")
    form_page.submit_form()

    print("\n!!FINISHED!!")
