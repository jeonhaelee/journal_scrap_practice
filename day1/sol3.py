class Warrior:
    def __init__(self, name, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense
        print('전사가 생성됩니다.')
        
    def doAttack(self):
        print(f'{self.name}이 {self.attack}의 데미지를 입힙니다.')

    def assault(self):
        print(f'{self.name}이 돌진 스킬을 사용합니다. {self.attack*1.5}의 피해를 입힙니다.')
        
    def move(self):
        print('씩씩하게 걸어갑니다.')

class Magician:
    def __init__(self, name, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense
        print('마법사가 생성됩니다.')
        
    def doAttack(self):
        print(f'{self.name}이 {self.attack}의 데미지를 입힙니다.')

    def fire(self):
        print(f'{self.name}이 파이어 스킬을 사용합니다. {self.attack*2}의 피해를 입힙니다.')
        
    def move(self):
        print('텔레포트로 이동합니다.')
    
    
    	
c1 = Warrior("홍길동", 20, 10); # 전사가 생성됩니다.

c1.doAttack(); # 홍길동이 20의 데미지를 입힙니다.
c1.assault(); # 홍길동이 돌진 스킬을 사용합니다. (공격력의 1.5배)의 피해를 입힙니다.
c1.move(); # 씩씩하게 걸어갑니다.


c2 = Magician("홍길순", 15, 15); # 마법사가 생성됩니다.

c2.doAttack(); # 홍길순이 15의 데미지를 입힙니다.
c2.fire(); # 홍길순이 파이어 스킬을 사용합니다. (공격력의 2배)의 피해를 입힙니다.
c2.move(); # 텔레포트로 이동합니다.