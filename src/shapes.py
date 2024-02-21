import math

class Square:
    def __init__(self,side):
        self.side=side
        self._developer="Samuel Lunghe"
    def __repr__(self):
        return f"Square: {self.side}X{self.side}\nSurface: {self.side*self.side}"
    def surface(self):
        return self.side*self.side 
    def describe(self):
        print(f"Square: {self.side}X{self.side}\nSurface: {self.side*self.side}\nCreator:{self._developer}")
class Circle:
    def __init__(self,radius):
        self.radius=float(radius)
        self._developer="Samuel Lunghe"
    def __repr__(self):
        return f"Circle:\n1.Radius: {self.radius}\n2.Surface: {Circle.surface(self)}"
    def surface(self):
        return float(math.pi)*(self.radius)**2
    def describe(self):
        print(f"Circle:\n1.Radius: {self.radius}\n2.Surface: {Circle.surface(self)}\nCreator:{self._developer}")
# sq1=Square(4)
# print(sq1)    
# sq1.describe()
circ1=Circle(10)
# circ1.describe()
print(circ1)