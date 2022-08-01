# pexels에서 고양이 사진 100개 다운로드 해서 img 폴더에 저장.


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

dr = webdriver.Chrome('C:/Users/전해리/Downloads/chromedriver.exe')
dr.get("https://www.pexels.com/ko-kr/search/%EA%B3%A0%EC%96%91%EC%9D%B4/")

dr.implicitly_wait(10)

tags = dr.find_elements(By.CLASS_NAME, 'BreakpointGrid_item__erUQQ')


# # 현재 스크롤 위치 저장
# scroll_location = dr.execute_script("return document.body.scrollHeight")

# target_list = []

# while True:
#     tags = dr.find_elements(By.CLASS_NAME, 'BreakpointGrid_item__erUQQ')
#     target_list = tags
    
# 	#현재 스크롤의 가장 아래로 내림
#     dr.execute_script("window.scrollTo(0,document.body.scrollHeight)")
       
#     #전체 스크롤이 늘어날 때까지 대기
#     time.sleep(2)
    
#     #늘어난 스크롤 높이
#     scroll_height = dr.execute_script("return document.body.scrollHeight")

#     #늘어난 스크롤 위치와 이동 전 위치 같으면(더 이상 스크롤이 늘어나지 않으면) 종료
#     if scroll_location == scroll_height:
#         break
#     elif len(target_list) >= 300:
#         break
#     #같지 않으면 스크롤 위치 값을 수정하여 같아질 때까지 반복
#     else:
#     	scroll_location = dr.execute_script("return document.body.scrollHeight") #스크롤 위치값을 수정

src_list = []

for tag in tags:
    img = tag.find_element(By.TAG_NAME, 'img')
    src = img.get_attribute('src')
    src_list.append(src)

import requests as req

# enumerate 하면 인덱스랑 리스트 값이랑 같이 나옴
for i, src in enumerate(src_list):

    res = req.get(src)
    bin_data = res.content
    
    file_name = "cat_" + str(i) + ".jpeg"
    
    with open(file_name, 'wb') as f:
        f.write(bin_data)