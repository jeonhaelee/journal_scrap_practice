import csv

# csv -> ,로 구분한 데이터

# 1. csv 쓰기1
with open("day2/file_exam/exam2_data/test.csv", "w", encoding='utf-8-sig') as f:
    csv_writer = csv.writer(f, delimiter=',')
    csv_writer.writerow([1,2,3,4])
    csv_writer.writerows([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
    
# 2. csv 쓰기2
with open("day2/file_exam/exam2_data/test2.csv", "w", encoding='utf-8-sig') as f:
    dict_writer = csv.DictWriter(f, fieldnames = ["name", "age", "home"])
    dict_writer.writeheader()
    dict_writer.writerow({"name" : "hong", "age" : 30, "home" : "daejeon"})
    dict_writer.writerow({"name" : "lee", "age" : 33, "home" : "seoul"})
    
# 3. csv 읽기1
with open("day2/file_exam/exam2_data/test.csv", "r", encoding='utf-8-sig') as f:
    csv_reader = csv.reader(f, delimiter = ',')
    csv_list = list(csv_reader)
    print(csv_list)
    
# 4. csv 읽기2
with open("day2/file_exam/exam2_data/test2.csv", "r", encoding='utf-8-sig') as f:
    csv_reader = csv.DictReader(f)
    for dic in csv_reader:
        print(dic)