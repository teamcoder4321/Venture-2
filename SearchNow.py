import speech_recognition
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser
import requests
from bs4 import BeautifulSoup


def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 400
        audio = r.listen(source,0,4)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Sorry, I didn't catch that.")
        return "None"
    return query

query = takeCommand().lower()

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)  # Set the voice to the first available voice
engine.setProperty("rate", 170)  # Set the speech rate (words per minute)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("venture","")
        query = query.replace("google ssearch", "")
        query = query.replace("google", "")
        speak("searching google")
        # pywhatkit.search(query)

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query, 1)
            speak(result)

        except:
            speak("No result found")


def searchYoutube(query):
    if "youtube" in query:
        speak("This is What i found for Your Search!")
        query = query.replace("youtube search", "")
        query = query.replace("youtube", "")
        query = query.replace("venture", "")
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done, sir")

def searchWikipedia(query):
    if "wikipedia" in query:
        speak("Searching from Wikipedia!")
        query = query.replace("venture", "")
        query = query.replace("wikipedia", "")
        query = query.replace("wikipedia search", "")
        result = wikipedia.summary(query,sentences = 2)
        speak("According to Wikipedia")
        print(result)

    def searchWeather(query):
        if "weather" in query:
            search = "weather in varanasi"
            url = f"https://www.google.com/search?client=opera&q={search}" + query
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"Current {search} is {temp}")
            print(f"Current {search} is {temp}")

    def searchTemperature(query):
        if "temperature" in query:
            search = "temperature in varanasi"
            url = f"https://www.google.com/search?client=opera&q={search}" + query
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"Current {search} is {temp}")
            print(f"Current {search} is {temp}")
