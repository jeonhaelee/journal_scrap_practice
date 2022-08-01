from bs4 import BeautifulSoup   
import requests   

url = "https://news.naver.com/main/ranking/popularDay.naver"

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}

res = requests.get(url, headers=headers) 

html = res.text 

soup = BeautifulSoup(html, 'html.parser')

def get_my_journal(tag):
    
    a = tag.find('a')
    
    link = a['href']
    
    strong = a.find('strong')
    name = strong.text
    
    idx = link.rfind('/')
    jid = link[idx-3:idx:1]

    my_journal = {
        'id' : jid,
        'name' : name,
        'link' : link
    }
    
    return my_journal
    
def get_journal_list_by_group(group_id):
    
    tag = soup.find(attrs={'class' : group_id})
    alist = tag.find_all(attrs={'class' : 'rankingnews_box'})

    journal_list = []

    for tag in alist:
        
        my_journal = get_my_journal(tag)
        journal_list.append(my_journal)
        
    return journal_list

def print_journal_list(journal_list) :
    
    for j in journal_list:
        print(f"번호 : {j['id']}")
        print(f"이름 : {j['name']}")
        print(f"링크 : {j['link']}")
        print("=============================================================")

def get_group_id_list():

    group_id_list = []

    for tag in tags:
        group_id = ""
        group_id += tag['class'][0] 
        group_id += " " 
        group_id += tag['class'][1]
        group_id_list.append(group_id)
        
    return group_id_list



tags = soup.find_all(attrs={'class' : '_officeCard'})
glist = get_group_id_list()

for gid in glist:
    journal_list = get_journal_list_by_group(gid)
    print_journal_list(journal_list)



# 다음 수업 시간
# 각 언론사별 기사(댓글정보) => 파일 저장 => 판다스로 읽어옴 => 간단한 분석





