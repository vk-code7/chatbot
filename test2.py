import speech_recognition as sr
import pyttsx3


def speak(command):
    engine = pyttsx3.init()
    engine.say(command)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        
        print("listening")
        audio = r.listen(source)
        try:
            print('working')
            query = r.recognize_google(audio,language = 'en-in')
            return query.lower 
        except Exception as e:
            return "some error accured.."

while True:
    query = takeCommand()
    print(f"User said: {query}")