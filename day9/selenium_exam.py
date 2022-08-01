from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome('C:/Users/taeji/Downloads/chrome-driver/chromedriver.exe')
driver.get("http://www.python.org")


assert "Python" in driver.title

# find_element(soup의 find와 동일)  단일 태그 찾기
# find_elements(soup의 find_all과 동일) 여러개 태그 찾기

# By.ID -> id 속성으로 찾기 => id속성값은 무조건 결과가 1개 아니면 0개
# By.CLASS_NAME -> class 속성으로 찾기
# By.TAG_NAME -> 태그 이름으로 찾기
# By.Name -> name 속성으로 찾기
elem = driver.find_element(By.NAME, "q")

elem2 = driver.find_element(By.CLASS_NAME, "donate-button")

# 텍스트 가져오기 - tag.text
print(elem2.text)

# 속성값 가져오기 - .get_attribute('속성명')
print(elem2.get_attribute('href'))
elem3 = None
try:
    elem3 = driver.find_element(By.CLASS_NAME, "aaa")
except:
    pass

print(elem3)