import pyttsx3
count=int(input("Count : "))
speak=("Time, Starts, Now")
for i in range(count):
    engine=pyttsx3.init()
    engine.say(speak)
    engine.runAndWait()
    speak=i
