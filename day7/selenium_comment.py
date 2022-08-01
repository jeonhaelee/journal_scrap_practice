from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import news_scrap_sele as nss

import time

url = ""

def set_url(url_param) :
    global url
    url = url_param

def get_driver() :    

    global url

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome('C:/Users/taeji/Downloads/chrome-driver/chromedriver.exe', options=options)
    driver.get(url)

    return driver
#time.sleep(5)

# 댓글수, 성별정보, 나이대정보

# 이 댓글의 뉴스 번호
def get_comment_info(news) :
    
    domain = "https://n.news.naver.com/article/comment/"
    link = news['jid'] + "/" + news['nid']
    
    link = domain + link 
           
    set_url(link)
    driver = get_driver()
    
    element = driver.find_element(By.ID, "cbox_module")
    time.sleep(1)
    try:
        slider = driver.find_element(By.CLASS_NAME, "u_cbox_slider")
    except:
        return None

    comment_info = {}
    nid = nss.get_news_id(news['link'])
    cnt = get_comment_count(element)    
    chart_sex = get_chart_sex(element)
    chart_age = get_chart_age(element)
    
    comment_info["번호"] = nid
    comment_info["댓글수"] = cnt
    comment_info.update(chart_sex)
    comment_info.update(chart_age)
    
    return comment_info

def get_chart_age(element) :
    chart_age = WebDriverWait(element, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "u_cbox_chart_age"))
    )
    
    childs = chart_age.find_elements(By.CLASS_NAME, "u_cbox_chart_progress")
    
    result = {}
    
    for child in childs :
        key = child.find_element(By.CLASS_NAME, "u_cbox_chart_cnt").text
        value = child.find_element(By.CLASS_NAME, "u_cbox_chart_per").text # 값
        result[key] = value
        
    return result
    

def get_chart_sex(element) :
    chart_sex = WebDriverWait(element, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "u_cbox_chart_sex"))
    )
    
    chart_progresses = chart_sex.find_elements(By.CLASS_NAME, 'u_cbox_chart_progress')
    
    result = {}
    for progress in chart_progresses :            
        value = progress.find_element(By.CLASS_NAME, 'u_cbox_chart_per').text
        key = progress.find_element(By.CLASS_NAME, 'u_cbox_chart_cnt').text
        result[key] = value
       
    return result
    
    

def get_comment_count(element) :
    span = WebDriverWait(element, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "u_cbox_count"))
    )
    
    if span != None :
        return span.text
    return "태그가 존재하지 않습니다."

# comment_info = get_comment_info()

# print(comment_info)



