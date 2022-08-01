import json
# dic = '''
# {
#     "age" : 20,
#     "name" : "hong",
#     "home" : "Daejeon"
# }
# '''
#dic['age']
#dic = json.loads(dic)

# dic1 = {"no" : 1, "name" : "hong"}
# dic2 = {"no" : 2, "name" : "lee"}

# dic_list = [dic1, dic2]

def save_to_json(file_path, data) :
    with open(file_path, "w", encoding='utf-8-sig') as f :
        json.dump(data, f, ensure_ascii=False)

def load_json(file_path) :
    with open(file_path, "r", encoding='utf-8-sig') as f :
        news_list = json.load(f)
        return news_list


