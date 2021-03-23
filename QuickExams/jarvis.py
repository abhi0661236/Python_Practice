import pyttsx3
import datetime
import speech_recognition as sr




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)

def takeCommand():
    """This function takes microphone input from the user and returns the 
    string output"""
    r = sr.Recognizer() 
    with sr.Microphone() as source:
        print("Listening")
        r.energy_threshold = 500
        audio = r.listen(source)

        try:
            print("Recognizing")
            query = r.recognize_google(audio, language = 'en-in')
            print(f"user said: {query}\n")
        except Exception as e:
            print(e)
            print("Say that again please")
            return "None"
        
    return query

    


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<3:
        speak("Welcome Sir ! I think you should take some rest")
    elif hour>=3 and hour<12:
        speak("Good Morning Sir !")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir !")
    elif hour>18 and hour<21:
        speak("Welcome Sir !")
    else:
        speak("Mr. Abhishek I think you should take some rest and me too. Good Night sir !")
    
    speak("How may I help you")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

if __name__ == "__main__":
    wishMe()
    speak("I am your personal assistant")
    #Logic for tasks based on the query of user\
    takeCommand()



