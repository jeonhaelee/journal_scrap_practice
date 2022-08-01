from konlpy.tag import Okt
import file_manager as fm
from collections import Counter

# 형태소 분석기 (Okt) 생성
ok = Okt()

# 분석 대상 텍스트
string = "안녕하세요 저는 홍길동입니다. 만나서 반가워요 저는 떡볶이를 좋아합니다. 대전을 살기 좋아요."

# 형태로 단위로 쪼개기
rst = ok.morphs(string)

# 명사 단위로 쪼개기
rst2 = ok.nouns(string)
print(rst2)

# 형태소를 품사 태깅하여 쪼개기
rst3 = ok.pos(string)

for (word, tag) in rst3 :
    # 품사가 형용사, 명사, 동사인 것만
    if tag in ['Adjective', 'Noun', 'Verv'] :
        print(word, tag)
        
# 키워드 분석
# 2021년 가장 많이 언급된 키워드 
file_path = "C:/py_work/day9/data/KBS_new_bodies.json"
bodies = fm.load_json(file_path)

# 첫번째 뉴스의 본문
body = bodies[0]['body']

result_list = []

for target in bodies:
    
    word_list = []
    for word, tag in ok.pos(target['body']) :
        if tag in ['Adjective', 'Noun', 'Verv'] :
            word_list.append(word)   
            
    counts = Counter(word_list)     
    
    keyword_list = []
    for key, value in counts.items():
        keyword = {
            "nid" : target['nid'],
            "word" : key,
            "cnt" : value
        }
        keyword_list.append(keyword)
    
    result_list.extend(keyword_list)

file_path = "C:/py_work/day9/data/news_keyword2.json"
fm.save_to_json(file_path, result_list)



word_list = []
for word, tag in ok.pos(target['body']) :
    if tag in ['Adjective', 'Noun', 'Verv'] :
        word_list.append(word)   
        
counts = Counter(word_list)

tags = counts.most_common(50)

print(dict(tags))

from wordcloud import WordCloud
import matplotlib.pyplot as plt

wc = WordCloud(font_path="C:/Windows/Fonts/MALGUN.TTF", background_color='white', max_font_size=60)
cloud = wc.generate_from_frequencies(dict(tags))

plt.axis("off")
plt.imshow(cloud)
plt.show()