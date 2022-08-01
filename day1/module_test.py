# 점점 더 구조화 하고 일반화하는 과정


# 클래스가 많아짐. 변수, 함수도 많아짐 
# 파일 하나에 코드가 너무 많아지면 힘들다. 코드 분리 필요
# 싹 정리해서 비슷한 역할, 분야에서 사용되는 것들끼리 따로 관리

# 파일 분리

# import pack1.mod1 as m

# c1 = m.Cat()
# c1.meow()

# print(m.data1)

# m.func1()

from pack1.mod1 import Cat

c1 = Cat()
c1.meow()