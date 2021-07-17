import pyttsx3
from random import randrange
texts=("friend","legend","programmer","dude")
text=texts[randrange(4)]
speak=(f"hai {text} , i'm listening")
engine=pyttsx3.init()
engine.say(speak)
engine.runAndWait()
while True:
    first=eval(input("Tables of : "))
    speak=(first)
    engine.say(speak)
    engine.runAndWait()
