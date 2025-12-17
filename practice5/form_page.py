from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import helper

class FormPage:
    def __init__(self, driver):
        self.driver = driver
        # Locators
        self.text_input = (By.CSS_SELECTOR, "input[type='text']")
        self.email_input = (By.CSS_SELECTOR, "input[type='email']")
        self.pwd_input = (By.CSS_SELECTOR, "input[type='password']")
        self.submit_button = (By.ID, "btn-form-submit")

    # 입력 메서드
    def enter_text(self, text):
        elem = helper.wait_for_element(self.driver, self.text_input)
        elem.clear()
        elem.send_keys(text)

    def enter_email(self, email):
        elem = helper.wait_for_element(self.driver, self.email_input)
        elem.clear()
        elem.send_keys(email)

    def enter_password(self, pwd):
        elem = helper.wait_for_element(self.driver, self.pwd_input)
        elem.clear()
        elem.send_keys(pwd)

    # 제출 메서드
    def submit_form(self):
        btn = helper.wait_for_element(self.driver, self.submit_button)
        btn.click()
        try:
            alert = helper.wait_for_alert(self.driver)
            print("Alert text:", alert.text)
            alert.accept()
            print("Form 제출 완료")
        except:
            print("Alert 없음")
