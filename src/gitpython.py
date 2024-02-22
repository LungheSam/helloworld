
import time
import pyttsx3
import math
from math import pi

class Point:
    def __init__(self,x,y,z=0):
        self.x=x
        self.y=y
        self.z=z
    def __repr__(self):
        return f"x:{self.x}\ny:{self.y}\nz:{self.z}"
    def describe(self):
        print(f"Point ({self.x},{self.y},{self.z})\nx:{self.x}\ny:{self.y}\nz:{self.z}")
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getZ(self):
        return self.z
    def say_coordinates(self):
        engine=pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[2].id)
        engine.setProperty("rate",150)
        engine.say(f"coordinates of the point are, x,:{self.x}\ny,:{self.y}\nz,:{self.z}")
        engine.runAndWait()
    def __add__(self,other):
        return (self.x+other.x,self.y+other.y,self.z+other.z)
    def __sub__(self,other):
        return (self.x-other.x,self.y-other.y,self.z-other.z)

A=Point(2,4)
B=Point(1,2)
A.describe()
B.describe()
A.say_coordinates()
print(A+B)