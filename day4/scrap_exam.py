from bs4 import BeautifulSoup   # html 형식으로 작성된 문자열을 html 구조로 파싱하기 위한 모듈
import requests   # 특정 서버에 웹요청 보내기위한 모듈

# 1. 특정 페이지로 요청 보내서 html 문서 받아오기.
url = "https://www.naver.com"

res = requests.get(url) # url에 요청 보내고 , 요청에 대한 응답이 리턴됨.

html = res.text # 응답 결과의 문서

soup = BeautifulSoup(html, 'html.parser')

print(soup.find('option'))
print(soup.find_all('option'))

