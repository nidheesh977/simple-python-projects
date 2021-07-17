import pyttsx3
engine=pyttsx3.init()
engine.say("Welcome")
engine.runAndWait()
while True:
    count=int(input("Count : "))
    for i in range(count):
        engine.say(count-i)
        engine.runAndWait()
    engine.say("Time over")
    engine.runAndWait()

