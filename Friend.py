import pyttsx3
import datetime
speak=("hai friend")
reply = {
        "how are you": "good to see you again",
        "what is the time now": datetime.datetime.now().time,
    }
while True:
    engine=pyttsx3.init()
    engine.say(speak)
    engine.runAndWait()
    user=input("Listening : ")
    speak = reply[user.lower()]
    print(speak)
