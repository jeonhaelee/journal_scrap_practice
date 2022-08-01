# JSON

import json

# 프로그램 오브젝트 > 파일 : 직렬화,
# 파일 > 오브젝트 : 역직렬화

# 파이썬 - 딕셔너리, 다른데서는 JSON

txt = '{ "이름" : "홍길동", "나이" : 20, "거주지" : "대전" }'

dic2 = { "이름" : "홍길동", "나이" : 20, "거주지" : "대전" }


with open("day2/file_exam/exam3_data/test.json", "w", encoding='utf-8-sig') as f:
    json.dump(txt, f, ensure_ascii=False)   # json 텍스트를 파일에 저장해주는 함수.
    json_str = json.dumps(dic2) # 딕셔너리를 json 문자열로 변환해주는 함수.
    
with open("day2/file_exam/exam3_data/test.json", "r", encoding='utf-8-sig') as f:
    rst = json.load(f)  # load는 json 텍스트를 파일에서 읽어오는 함수.
    
    # print(rst) # 딕셔너리처럼 생겼지만 문자열임. json형식임.
    # 그런데 json 형식은 아래의 코드로 바로 딕셔너리 형태로 바꿀 수 있음!
    
    dic = json.loads(rst)   # loads는 json 텍스트를 딕셔너리로 변환해주는 함수.
    print(dic["이름"])
    
    