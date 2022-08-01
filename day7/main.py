import journal_scrap as js
import news_scrap_sele as nss
import json
import file_manager as fm
import selenium_comment as sc

# 1. MBC, SBS, KBS 6월 25일자 랭킹뉴스 5개씩 -> selenium
# j1 = js.get_journal_by_name('MBC')
# # print(j1)
# j2 = js.get_journal_by_name('SBS')
# # print(j2)
# j3 = js.get_journal_by_name('KBS')
# print(j3)

# news1 = nss.get_new_list_by_journal(j1)
# news2 = nss.get_new_list_by_journal(j2)
# news3 = nss.get_new_list_by_journal(j3)

# 1.5 뉴스 데이터 파일 저장
# file_path1 = "C:/py_work/day7/data/" + j1['name'] + ".json"
# fm.save_news_to_json(file_path1, news1)

# file_path2 = "C:/py_work/day7/data/" + j2['name'] + ".json"
# fm.save_news_to_json(file_path2, news2)

# file_path3 = "C:/py_work/day7/data/" + j3['name'] + ".json"
# fm.save_news_to_json(file_path3, news3)


# 2. 위 뉴스 15개의 댓글 통계 정보 가져오기
news_list = fm.load_json("C:/work/python/scrap3/data/SBS.json")

comments = []
for news in news_list :
    comment_info = sc.get_comment_info(news)
    if comment_info :
        comments.append(comment_info)

file_path = "C:/work/python/scrap3/data/SBS_comment.json"
fm.save_to_json(file_path, comments)

# 3. 댓글 통계 결과 낼 때 해당 댓글의 원본 뉴스 아이디 생성해주세요.



# 4. 뉴스는 news.json, 댓글은 comment.json으로 파일 저장


