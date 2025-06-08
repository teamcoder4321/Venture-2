import pyttsx3
import datetime
engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)  # Set the voice to the first available voice
engine.setProperty("rate", 170)  # Set the speech rate (words per minute)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning, sir!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon, sir!")
    else:
        speak("Good Evening,sir!")
    speak("I am your personal assistant. How can I help you today?")