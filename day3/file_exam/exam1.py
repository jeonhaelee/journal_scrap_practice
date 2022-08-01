import csv
import os

file_name = "day3/file_exam/person/person_list.csv"

is_first = True
print(os.path.isfile(file_name))
if os.path.isfile(file_name) :
    is_first = False

while True :
    menu = input("메뉴 선택(1. 사람 추가 2. 목록 조회 3. 종료) :" )
    
    if menu == "1" :
        name = input("이름 : ")
        age = int(input("나이 : "))
        home = input("거주지 : ")
        
        person = {
            "name" : name,
            "age" : age,
            "home" : home
        }

        # 1. csv 파일에 누적 저장
        # with open('day2/file_exam/exam3_person/person_list.json', 'a', encoding='utf-8-sig') as f :
        with open(file_name, 'a', encoding='utf-8-sig') as f :
            dict_writer = csv.DictWriter(f, fieldnames=person.keys())
            if is_first :
                dict_writer.writeheader()
                is_first = False
            dict_writer.writerow(person)
            
    elif menu == "2" :
        if os.path.isfile(file_name) :
            with open(file_name, 'r', encoding='utf-8-sig') as f:
                dict_reader = csv.DictReader(f)
                for person in dict_reader :
                    print(f'이름 : {person["name"]}, 나이 : {person["age"]}, 거주지 : {person["home"]}')
        else :
            print("데이터가 없습니다.")    
    elif menu == "3" :
        break