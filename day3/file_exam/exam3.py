import os

path = 'C:/py_work/day3/file_exam/person'
path2 = 'C:/py_work/day3/file_exam/person/person_list.csv'

print(os.path.isfile(path)) # False가 나옴 -> file이 아니라는 뜻.
print(os.path.isdir(path)) # True가 나옴 -> path라는 뜻.

print(os.path.isfile(path2)) # 이를 이용해 file인지 아닌지 등을 알 수 있겠지.
# 아예 존재하지 않는 파일일 때도 False가 나옴.

print(os.listdir(path)) # 어떤 경로에 있는 파일들을 리스트로 가져옴.