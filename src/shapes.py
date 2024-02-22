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
    def getRadius(self):
        return self.radius
    def surface(self):
        return float(math.pi)*(self.radius)**2
    def describe(self):
        print(f"Circle:\n1.Radius: {self.radius}\n2.Surface: {Circle.surface(self)}\nCreator:{self._developer}")
class Triangle:
    def __init__(self,base,height):
        self.base=base 
        self.height=height
        self._developer="Samuel Lunghe"
    def surface(self):
        return 0.5*self.height*self.base
    def getHeight(self):
        return self.height
    def getBase(self):
        return self.base
    def __repr__(self) -> str:
        return f"Triangle:\n1.Height:{self.height}\n2.Base:{self.base}\n3.Surface:{Triangle.surface(self)}\nCreator:{self._developer}"
    def describe(self):
        print(f"Triangle:\n1.Height:{self.height}\n2.Base:{self.base}\n3.Surface:{Triangle.surface(self)}\nCreator:{self._developer}")
# sq1=Square(4)
# print(sq1)    
# sq1.describe()
circ1=Circle(10)
# circ1.describe()
print(circ1)