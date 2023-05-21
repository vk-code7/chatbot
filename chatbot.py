import speech_recognition as sr
import pyttsx3
import connection

#pyaduio
#pyttsx3
#speechrecognition





def SpeakText(command):
    #initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

def Getquery():
    try:
        #initializing the recognizer
        r = sr.Recognizer()
        #use the microphone for input
        with sr.Microphone() as source:
            # wait for the recognizer to adjust the energy threshold
            r.adjust_for_ambient_noise(source, duration=0.5)
            #listen to the input from user
            print("Listening ...")
            audio2 = r.listen(source)
            print('working...')
            # using google to recognize audio
            query = r.recognize_google(audio_data = audio2, key = None, language = 'en-IN')
            query = query.lower()
            return query
    except Exception as e:
        print("Unknown Error occured")
    #except sr.RequestError as e:
    #    print("Could Not request Result; {0}".format(e))
    #except sr.UnknownValueError:
    #    print("Unknown Error occured")


while True :
    query = Getquery()
    response = connection.getResponse(query)
    print("uese: "+query)
    print("chatbot: "+ response)
    SpeakText(response)
connection.dataBase.close()