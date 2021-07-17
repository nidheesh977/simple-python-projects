import speech_recognition as sr
import googletrans
import pyttsx3

r=sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source,duration=1)
    print("say anything : ")
    audio= r.listen(source)
    try:
        text = r.recognize_google(audio)

        a = googletrans.LANGUAGES
        language_index = list(a.values()).index('german')
        key = list(a.keys())
        language = key[language_index]

        translator = googletrans.Translator()
        translated = translator.translate(text, dest = language).text
        print(text + ' - ' + translated)

        engine=pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.setProperty('rate', 120)

        engine.say(translated)
        engine.runAndWait()

    except:
        print("sorry, could not recognise")