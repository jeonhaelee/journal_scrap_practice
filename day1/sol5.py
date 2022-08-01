class my_math:
    
    PI = 3.141592
    
    def square(self, x):
        return x * x
    
    def get_circle_area(self, radius):
        return radius * radius * self.PI
    
math = my_math()

print(math.get_circle_area(3))