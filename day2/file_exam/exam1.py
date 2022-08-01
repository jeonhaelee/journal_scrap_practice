# plain text

txt = "안녕하세요 저는 전해리입니다. 잘 부탁드립니다.\n"

# 인코딩 -> 문자처리방식
# 127개 문자로 문자 처리 -> 127개의 문자를 모아놓은 것 (문자표, 캐릭터셋) -> ascii // 1바이트
# 중국이나 한국 같은 경우 2바이트 이용해서 처리
# 네트워크 발전 -> 웹 : 전세계 데이터가 공유.
# 유니코드로 문자표 통합. 유니코드를 처리하는 방식(utf-8)


# 1. 파일 저장
f = open('day2/file_exam/exam1_data/test.txt', 'w', encoding='utf-8-sig')

f.write(txt)

f.writelines(['aaa\n', 'bbb\n', 'cccc\n'])
f.close() # 사용 후엔 항상 close()로 메모리에서 제거해줘야 함. 안 그럼 자원 낭비됨.

f2 = open('day2/file_exam/exam1_data/test.txt', 'a', encoding='utf-8-sig')
f2.write('새로운 내용')
f2.close()

# 2. 파일 읽기

f3 = open('day2/file_exam/exam1_data/test.txt', 'r', encoding='utf-8-sig')

txt1 = f3.read() # 전체 읽어오기
print(txt1)

f3.seek(0)   # 커서 초기화

txt2 = f3.readline() # 한줄 읽어오기
print(txt2)

f3.seek(0)

txt3 = f3.readlines() # 한줄씩 리스트로 반환해줌
print(txt3)

f3.close()

with open('day2/file_exam/exam1_data/test.txt', 'r', encoding='utf-8-sig') as f4:
    print(f4.read())

# 문제
# 1. 고양이, 강아지, 오리, 원숭이, 악어 줄바꿈해서 파일에 저장.
# 2. 오리와 원숭이 사이에 말 저장

animal_list = ['고양이\n', '강아지\n', '오리\n', '원숭이\n', '악어\n']

with open('day2/file_exam/exam1_data/anim.txt', 'w', encoding='utf-8-sig') as f:
    f.writelines(animal_list)

with open('day2/file_exam/exam1_data/anim.txt', 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()
    idx = lines.index('오리\n')
    lines.insert(idx+1, '말\n')
    
    with open('day2/file_exam/exam1_data/anim.txt', 'w', encoding='utf-8-sig') as f2:
        f2.writelines(lines)