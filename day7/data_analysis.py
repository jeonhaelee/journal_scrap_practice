import file_manager as fm
import pandas as pd


kbs_news = fm.load_json("C:/py_work/day7/data/KBS.json")

for news in kbs_news:
    print(news)

df = pd.read_json("C:/py_work/day7/data/KBS.json", orient='records', encoding='utf-8-sig')

print(df)
