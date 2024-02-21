# print("Time Remaining...")
import time
import pyttsx3

def text_to_speech(text):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set properties (optional)
    # engine.setProperty('rate', 150)  # Speed of speech
    # engine.setProperty('volume', 0.9)  # Volume level (0.0 to 1.0)

    # Convert text to speech
    engine.say(text)

    # Wait for the speech to finish
    engine.runAndWait()

# Example usage:
text = "Hello, how are you today?"
text_to_speech(text)

# for i in range(30,1,-1):
#     # time.sleep(1)
#     i=i if i>=10 else "0"+str(i)
#     print(i)