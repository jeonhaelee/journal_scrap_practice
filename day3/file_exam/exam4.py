# XML

# XML을 알아야 하는 이유
# 1. 공공데이터가 XML로 많이 되어 있음.
# 2. 웹문서가 XML로 작성되어 있음. -> html

# 데이터를 저장하고 관리하는데 있어서는 xml 별로..
# 읽어서 분석하는 것 위주로..


html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup

f = open('day3/file_exam/person_xml/person.xml', 'r', encoding='utf-8-sig')

content = f.read()
soup = BeautifulSoup(content, 'html.parser')

tag = soup.find('name')
tags = soup.find_all('name')

# tag = soup.find('a') # 태그 이름으로 데이터 검색하기
# tags = soup.find_all('a') # 태그 이름 데이터 다 가져와서 리스트에 담아줌
# print(tags)

# tag = soup.find('p')
# print(tag)

total = soup.find_all('datas')
print(total)

persons = soup.find_all('persons')
print(persons)

names = soup.find_all('name')
print(names)

# 체이닝
dogs = soup.find('dogs')

dog_names = dogs.find_all('name')
print(dog_names)

founded_name = soup.find('datas').find('persons').find('person').find('name')
print(founded_name)

# 텍스트
print(founded_name.text)

# 특정 사람을 검색
person_tags = soup.find_all('person')
print(person_tags[1])
        
# 속성(attribute)
# 속성으로 가져오기

# 홍길동네
hongs = soup.find_all(attrs={'class' : 'hong'})
print(hongs)

# 이순신네
lees = soup.find_all(attrs={'class' : 'lee'})
print(lees)

result = soup.find(attrs={"id" : 3}) # id가 3인 태그를 찾아온다.
print(result['id'])

print(result)
print(result.text)