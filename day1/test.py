class Person:
    
    # 생성자
    def __init__(self, age, name):
        self.age = age
        self.name = name
    
    def intro(self):
        print(f'{self.age}살 {self.name}입니다.')
        
    def add_age(self):
        self.age += 1
        
    def change_name(self, new_name):
        self.name = new_name
        
p1 = Person(21, '홍길동')
p2 = Person(22, '홍길순')
p3 = Person(23, '황진이')

p1.intro()
p1.add_age()
p1.intro()

