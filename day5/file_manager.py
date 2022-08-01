import json

# dic1 = {"no" : 1, "name" : "hong"}
# dic2 = {"no" : 1, "name" : "hong"}

# dic_list = [dic1, dic2]

file_path = "C:/py_work/day5/data/"

def save_news_to_json(file_path, news):
    with open(file_path, "w", encoding="utf-8-sig") as f :
        json.dump(news, f, ensure_ascii=False)

def load_json_to_news(file_path):
    with open(file_path, "r", encoding="utf-8-sig") as f :
        news_list = json.load(f)
        return news_list











