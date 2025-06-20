import requests
import json
import pyttsx3



engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)  # Set the voice to the first available voice
engine.setProperty("rate", 170)  # Set the speech rate (words per minute)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def letestsnews():
    api_dict = {"business":"https://newsapi.org/v2/top-headlines?sources=business-insider&apiKey=378bb5ff8391497a8adcca2d4b685ca7",
            "entertainment":"https://newsapi.org/v2/top-headlines?country=in&country=in&category=entertainment&apiKey=378bb5ff8391497a8adcca2d4b685ca7",
            "general":"https://newsapi.org/v2/top-headlines?country=in&country=in&category=general&apiKey=378bb5ff8391497a8adcca2d4b685ca7",
            "health":"https://newsapi.org/v2/top-headlines?country=in&country=in&category=health&apiKey=378bb5ff8391497a8adcca2d4b685ca7",
            "science":"https://newsapi.org/v2/top-headlines?country=in&country=in&category=science&apiKey=378bb5ff8391497a8adcca2d4b685ca7",   
            "sports":"https://newsapi.org/v2/top-headlines?country=in&country=in&category=sports&apiKey=378bb5ff8391497a8adcca2d4b685ca7",
            "technology":"https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=378bb5ff8391497a8adcca2d4b685ca7",
            "politics":"https://newsapi.org/v2/top-headlines?country=in&country=in&category=politics&apiKey=378bb5ff8391497a8adcca2d4b685ca7",
            # "headline":https://newsapi.org/v2/top-headlines?country=in&apiKey=378bb5ff8391497a8adcca2d4b685ca7,
            # "business2":""https://newsapi.org/v2/top-headlines?country=in&apiKey=378bb5ff8391497a8adcca2d4b685ca7",
            # "https://newsapi.org/v2/top-headlines?country=in&country=in&category=business&apiKey=378bb5ff8391497a8adcca2d4b685ca7"
            
}
    

    content = None
    url = None
    speak("Which category of news would you like to hear? You can choose from ,[business], [entertainment], [general], [health], [science], [sports], or [technology].")
    field = input("Type field news: ")
    for key ,value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("url was found")
            break
        else:
            url = True
    if url is True:
        print("url was not found")
               

    news = requests.get(url).text
    news = json.loads(news)
    speak("Here are the top news stories for the day:")

    arts = news["articles"]
    for articles in arts:
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"for more info visit: {news_url}")

        a = input("[press 1 to cont] and [press 2 to stop]: ")
        if str(a) == "1":
            pass
        elif str(a) == "2":
            break

    speak("Thanks for listening!")
    