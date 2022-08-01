class Person:
    def __init__(self, age, name):
       self.age = age
       self.name = name
       
    def get_age(self):
        return self.age
    
    def introduce(self):
        print(f'{self.age} , {self.name}')
        
p1 = Person(22, '홍길동')
p2 = Person(32, '이순신')
p3 = Person(18, '정약용')
p4 = Person(54, '황진이')


people = [p1, p2, p3, p4]

for p in people :
  if p.get_age() > 20 :
    p.introduce()

# 출력 
# 22 , 홍길동
# 32 , 이순신
# 54 , 황진이