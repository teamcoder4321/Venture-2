import pyttsx3
import speech_recognition
import random


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
        r.energy_threshold = 3000
        audio = r.listen(source,0,9)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Sorry, I didn't catch that.")
        return "None"
    return query

def game_play():
    speak("Welcome to the game, sir!")
    i = 0 
    Me_score = 0
    Com_score = 0

    while (i < 5):
        choose = ("rock","paper","scissor")
        com_choose = random.choice(choose)
        query = takeCommand().lower()
        if (query == "rock" or query == "stone"):
            if (com_choose == "rock"):
                speak("ROCK")
                print(f"Score :- Me :- {Me_score} : Com :- {Com_score}")
            elif (com_choose == "paper"):
                speak("PAPER")
                Com_score += 1
                print(f"Score :- Me :- {Me_score} : Com :- {Com_score}")
            else:
                speak("SCISSOR")
                Me_score += 1
                print(f"Score :- Me :- {Me_score} : Com :- {Com_score}")

        elif (query == "paper" or query == "wallpaper" or query == "papers"):
            if (com_choose == "rock"):
                speak("ROCK")
                Me_score += 1
                print(f"Score :- Me :- {Me_score} : Com :- {Com_score}")
            elif (com_choose == "paper"):

                speak("PAPER")
                print(f"Score :- Me :- {Me_score} : Com :- {Com_score}")
            else:
                speak("SCISSOR")
                Com_score += 1
                print(f"Score :- Me :- {Me_score} : Com :- {Com_score}")


        elif (query == "scissor" or query == "Caesar"):
            if (com_choose == "rock"):
                speak("ROCK")
                Com_score += 1
                print(f"Score :- Me :- {Me_score} : Com :- {Com_score}")
            elif (com_choose == "paper"):
                speak("PAPER")
                Me_score += 1
                print(f"Score :- Me :- {Me_score} : Com :- {Com_score}")
            else:
                speak("SCISSOR")
                print(f"Score :- Me :- {Me_score} : Com :- {Com_score}")
        
        
        i += 1
    print(f"Final Score :- Me :- {Me_score} : Com :- {Com_score}")
