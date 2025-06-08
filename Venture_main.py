import pyttsx3
import speech_recognition 
import requests
from bs4 import BeautifulSoup
import datetime
import os



engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)  # Set the voice to the first available voice
engine.setProperty("rate", 170)  # Set the speech rate (words per minute)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 400
        audio = r.listen(source,0,9)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Sorry, I didn't catch that.")
        return "None"
    return query

def alarm(query):
    timehere = open("Alarm.txt", "a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")
    

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Goodbye, have a nice day!")
                    break

                elif "hello" in query:
                    speak("Hello sir! How can I assist you today?")
                elif "i am fine" in query:
                    speak("that's great sir!")
                elif "how are you" in query:
                    speak("I am fine sir")
                elif "thank you" in query:
                    speak("You are welcome sir!")

                elif "open" in query:
                   from Dictapp import openappweb
                   openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)
              
                

                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                    print("Done")
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                    print("query")
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)
                    print("Done")
               
                elif "temperature" in query:
                    search = "temperature in varanasi"
                    url = f"https://www.google.com/search?q={search}" + query
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_= "BNeawe").text
                    speak(f"current{search} is {temp}")
                    print(temp)

                elif "weather" in query:
                    search = "weather in varanasi"
                    url = f"https://www.google.com/search?q={search}" + query
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_= "BNeawe").text 
                    speak(f"current{search} is {temp}")
                    print(temp)

                elif "set an alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    speak("Alarm set time.")
                    a = input("Please tell the time:- ")
                    alarm(a)
                    speak("Alarm set successfully, sir!")

                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f"The time is {strTime}")
                    print(strTime)
                
                elif "finally sleep" in query:
                    speak("Goodbye,i am going to sleep mode, have a nice day!")
                    break

                