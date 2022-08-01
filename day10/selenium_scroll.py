
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

dr = webdriver.Chrome('C:/Users/전해리/Downloads/chromedriver.exe')
dr.get("https://www.pexels.com/ko-kr/search/%EA%B3%A0%EC%96%91%EC%9D%B4/")


# 현재 스크롤 위치 저장
scroll_location = dr.execute_script("return document.body.scrollHeight")

while True:
	#현재 스크롤의 가장 아래로 내림
    dr.execute_script("window.scrollTo(0,document.body.scrollHeight)")
       
    #전체 스크롤이 늘어날 때까지 대기
    time.sleep(2)
    
    #늘어난 스크롤 높이
    scroll_height = dr.execute_script("return document.body.scrollHeight")

    #늘어난 스크롤 위치와 이동 전 위치 같으면(더 이상 스크롤이 늘어나지 않으면) 종료
    if scroll_location == scroll_height:
        break
    #같지 않으면 스크롤 위치 값을 수정하여 같아질 때까지 반복
    else:
    	scroll_location = dr.execute_script("return document.body.scrollHeight") #스크롤 위치값을 수정