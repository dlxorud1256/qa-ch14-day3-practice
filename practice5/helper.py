import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_element(driver, by_locator, timeout=10):
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.presence_of_element_located(by_locator))

def wait_for_alert(driver, timeout=5):
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.alert_is_present())

def read_csv(file_path):

    data_list = []
    """
    문제5. CSV 파일을 읽어 딕셔너리 리스트로 반환 (csv.DictReader 사용)

    (추가문제) 파일의 유효성을 검사하여, 유효하지 않은 경우에는 목록에서 제외하고 로깅(콘솔 출력)
    """

    with open(file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        required_fields = ["text", "email", "pwd"]

        for line_num, row in enumerate(reader, start=2):  # 데이터는 2행부터 시작
            # 필수 필드가 모두 존재하는지 확인
            if not all(field in row for field in required_fields):
                print(f"[Invalid Row {line_num}] 필수 필드 누락: {row}")
                continue

            text = (row.get("text") or "").strip()
            email = (row.get("email") or "").strip()
            pwd = (row.get("pwd") or "").strip()

            # 값이 비어있거나 이메일 형식이 올바르지 않으면 스킵
            if not text or not email or not pwd:
                print(f"[Invalid Row {line_num}] 비어있는 값 발견: {row}")
                continue

            if email.count("@") != 1 or email.startswith("@") or email.endswith("@"):
                print(f"[Invalid Row {line_num}] 잘못된 이메일 형식: {email}")
                continue

            local_part, domain_part = email.split("@")
            if not local_part or "." not in domain_part:
                print(f"[Invalid Row {line_num}] 잘못된 이메일 도메인: {email}")
                continue

            data_list.append({"text": text, "email": email, "pwd": pwd})

    return data_list
