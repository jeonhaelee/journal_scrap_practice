from bs4 import BeautifulSoup   # html 형식으로 작성된 문자열을 html 구조로 파싱하기 위한 모듈
import requests   # 특정 서버에 웹요청 보내기위한 모듈

# 1. 특정 페이지로 요청 보내서 html 문서 받아오기.
url = "https://news.naver.com/main/ranking/popularDay.naver"

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}

res = requests.get(url, headers=headers) # url에 요청 보내고 , 요청에 대한 응답이 리턴됨.

html = res.text # 응답 결과의 문서

soup = BeautifulSoup(html, 'html.parser')

# print(soup.prettify())

tag = soup.find(attrs={'class' : '_officeCard _officeCard0'})

# print(tag.prettify())

alist = tag.find_all(attrs={'class' : 'rankingnews_box'})

journal_list = []

for tag in alist:
    
    a = tag.find('a')

    strong = a.find('strong')
    name = strong.text
    link = a['href']

    # 문자열 다루기 - 문자열 자르기, 특정문자 위치 찾기
    # find() - 특정 문자를 앞에서부터 찾음.
    # rfind() - 특정 문자를 뒤에서부터 찾음.

    idx = link.rfind('/')

    # 문자열 슬라이싱 [시작:끝:단계]
    jid = link[idx-3:idx:1]
    print(jid)

    my_journal = {
        'id' : jid,
        'name' : name,
        'link' : link
    }
    
    journal_list.append(my_journal)


for j in journal_list:
    print(f"번호 : {j['id']}")
    print(f"이름 : {j['name']}")
    print(f"링크 : {j['link']}")
    print("=============================================================")









