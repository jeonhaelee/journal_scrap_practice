class Car :
    def __init__(self, velo, model):
        self.velo = velo
        self.model = model
        
    def run(self) :
        print(f'{self.model}이/가 {self.velo}km로 달립니다.')


c1 = Car(120, '소나타') 
c1.run() # 소나타이/가 120km로 달립니다.

c2 = Car(140, '싼타페') 
c2.run() # 싼타페이/가 140km로 달립니다.