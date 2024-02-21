# print("Time Remaining...")
import time
import pyttsx3

# def text_to_speech(text):
#     # Initialize the text-to-speech engine
#     engine = pyttsx3.init()

#     # Set properties (optional)
#     # engine.setProperty('rate', 150)  # Speed of speech
#     # engine.setProperty('volume', 0.9)  # Volume level (0.0 to 1.0)

#     voices = engine.getProperty('voices')
#     # print(voices)
#     engine.setProperty('voice', voices[0].id)

#     # Convert text to speech
#     engine.say(text)

#     # Wait for the speech to finish
#     engine.runAndWait()
# # text_to_speech("Hello, How are you doing today?")
class Point:
    def __init__(self,x,y,z=0):
        self.x=x
        self.y=y
        self.z=z
    def __repr__(self):
        return f"x:{self.x}\ny:{self.y}\nz:{self.z}"
    def describe(self):
        print(f"Point ({self.x},{self.y},{self.z})\nx:{self.x}\ny:{self.y}\nz:{self.z}")
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