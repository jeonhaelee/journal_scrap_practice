from bs4 import BeautifulSoup 
import requests 
import journal_scrap as js

url = "https://media.naver.com/press/662/ranking?type=comment" 

def set_url(url_param) :
    global url
    url = url_param

def get_soup() :    

    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }

    res = requests.get(url, headers=headers); 

    html = res.text
    soup = BeautifulSoup(html, 'html.parser')

    return soup

def get_news_id(link) :
    idx = link.rfind('/')   
    nid = link[idx + 1: idx + 11]  
    return nid

def get_new_list_by_journal(journal) :
    set_url(journal['link'])
    soup = get_soup()
    ranking_list = soup.find(attrs={'class' : 'press_ranking_list'})
    ranking_news_list = ranking_list.find_all(attrs={'class' : 'as_thumb'})    
    
    my_news_list = []
    for news in ranking_news_list :        
        # 해당 뉴스가 어떤 언론사의 뉴스인지. 언론사번호
        global url
        jid = js.get_journal_id(url)
        
        # 해당 뉴스의 링크
        a = news.find('a')
        link = a['href']
        
        # 해당 뉴스의 식별번호
        nid = get_news_id(link)
        
        # 해당 뉴스의 제목
        title = news.find(attrs={'class' : 'list_title'}).text
        
        my_news = {
            'jid' : jid,
            'nid' : nid,
            'title' : title,
            'link' : link
        }
        
        my_news_list.append(my_news)
        
    return my_news_list