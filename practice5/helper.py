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

    return data_list
