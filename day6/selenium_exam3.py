from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome('C:/Users/Administrator/Downloads/google-driver/chromedriver.exe')
driver.get("https://media.naver.com/press/469/ranking?type=popular")

button = driver.find_element(By.CLASS_NAME, 'button_date_prev')
button.click()
time.sleep(1)
button.click()
time.sleep(1)
button.click()
time.sleep(1)
button.click()

time.sleep(10)

# 언론사 별로 랭킹 뉴스 가져오기

## ================================ 셀레니움 이용해서 ===================================

# 언론사 별로 랭킹 뉴스를 10일치(현재 날짜 기준) 가져오기

# 특정 뉴스의 댓글 통계 정보 가져오기