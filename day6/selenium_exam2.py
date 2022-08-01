from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome('C:/Users/Administrator/Downloads/google-driver/chromedriver.exe')
driver.get("https://www.naver.com")

# query = driver.find_element(By.ID, 'query')

# 인터랙션 - 특정 액션(키입력, 클릭 등)으로 브라우저와 상호작용 하는 것.

# 입력 - tag.send_keys(입력값)
# query.send_keys("장마")
# query.send_keys(Keys.RETURN)
# time.sleep(10)

# 클릭 - tag.click()
navs = driver.find_elements(By.CLASS_NAME, 'nav_item')

target = None
for nav in navs :
    if nav.text == "카페" :
        target = nav
        
if target != None :
    target.click()

# 주의할 점 => 문서가 도착할 때까지 시간이 걸릴 수 있기 때문에 대기를 해줘야 함.
driver.implicitly_wait(10) # 문서가 다 로드 되기까지 대기, 최대 10초까지 대기.

input_text =driver.find_element(By.CLASS_NAME, 'input_text')
input_text.send_keys("고양이")

time.sleep(10) 

# 절대 시간으로 대기 -> 시간만큼
# time.sleep(10)

# 문서로 로드될 때까지 최대 시간으로 대기 -> 문서로드 완료시 대기 종료. (최대시간까지만 기다림)
# driver.implicitly_wait(10)

# 특정 데이터가 나타날 때까지 최대 시간으로 대기 -> 특정 데이터 로드 완료시 대기 종료. (최대시간까지만 기다림)
# element = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.ID, "cbox_module"))
# )