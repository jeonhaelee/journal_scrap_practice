import json

person_list = []

# 사람 데이터를 json 파일로 저장해주세요.
no = 1

while True:
    menu = input("메뉴 선택(1. 사람 추가 2. 목록 조회 3. 종료) : ")
    
    if menu == "1":
        name = input("이름 : ")
        age = int(input("나이 : "))
        home = input("거주지 : ")
        
        person = {
            "name" : name,
            "age" : age,
            "home" : home
        }
        
        # person_list.append(person)
        json_str = json.dumps(person, ensure_ascii=False)
        filename = "person" + str(no)
        with open(f"day2/file_exam/exam3_person/{filename}.json", "w", encoding='utf-8-sig') as f:
            f.write(json_str)
            
        no += 1
    
    elif menu == "2":
        for person in person_list:
            print(f'이름 : {person["name"]}, 나이 : {person["age"]}, 거주지 : {person["home"]}')
            
            
    elif menu == "3":
        break
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
