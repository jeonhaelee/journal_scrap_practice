# 절대경로 -> 루트 디렉터리 기준
# 상대경로 -> 현재 파일 기준

# 모듈에서 다른 모듈을 임포트 할 때는 무조건 절대경로를 써야 함.



def print_str(str1):
    print(str1)

# if __name__ == "__main__":
#     # import pkg1.mod1 as m1
#     # m1.print_num(10)