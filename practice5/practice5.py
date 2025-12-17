from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import helper as helper
from form_page import FormPage
import os

options = Options()
options.add_argument("--guest")
options.add_argument("--disable-features=PasswordLeakDetection,AutofillServerCommunication,OptInRelaunch")

# CSV 파일 경로
# 현재 파일 기준 CSV 경로
current_dir = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(current_dir, "user_data.csv")
test_data = helper.read_csv(csv_file)

print("!!DDT STARTED (CSV 기반)!!")

with webdriver.Chrome(options=options) as driver:
    driver.get("https://jinny-dev-anything.github.io/locator_ex_webpage")
    form_page = FormPage(driver)

    for i, data in enumerate(test_data, start=1):
        print(f"\n--- DDT Test {i}: {data} ---")
        form_page.enter_text(data["text"])
        form_page.enter_email(data["email"])
        form_page.enter_password(data["pwd"])
        form_page.submit_form()

print("\n!!DDT FINISHED!!")
