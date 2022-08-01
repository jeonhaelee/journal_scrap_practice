import file_manager as fm
import pandas as pd

news_file_path = 'C:/work/python/scrap3/data/KBS.json'
comment_file_path = 'C:/work/python/scrap3/data/KBS_comment.json'

news = fm.load_json(news_file_path)
df = pd.read_json('C:/work/python/scrap3/data/KBS.json', orient='records', encoding='utf-8-sig')