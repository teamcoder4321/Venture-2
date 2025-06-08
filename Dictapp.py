import os
import pyautogui
import webbrowser
import pyttsx3
from time import sleep

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)  # Set the voice to the first available voice
engine.setProperty("rate", 200)  # Set the speech rate (words per minute)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

dictapp = {"commandprompt": "cmd",
           "notepad": "notepad",
           "paint": "mspaint",
           "chrome": "chrome",
           "word": "winword",
           "powerpoint": "powerpnt",
           "excel": "excel",
           "vscode": "code",
           "discord": "discord",
           "spotify": "spotify",
           "steam": "steam",
           "youtube": "youtube",
           "netflix": "netflix",
           "twitch": "twitch",
           "twitter": "twitter",
           "instagram": "instagram",
           "facebook": "facebook",
           "github": "github",
           "discord": "discord",
           "telegram": "telegram",
           "whatsapp": "whatsapp",
           "zoom": "zoom",
           "teams": "teams",
           "opera": "opera",
           "brave": "brave",
           "firefox": "firefox",
           "edge": "edge",}

def openappweb(query):
    speak("Opening Sir!")
    if ".com" in query or ".in" in query or ".org" in query:
        query = query.replace("open", "")
        query = query.replace("venture", "")
        query = query.replace("launch", "")
        query = query.replace(" ", "")
        webbrowser.open(f"https://www.{query}")

    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"start {dictapp[app]}")

def closeappweb(query):
    speak("Closing Sir!")
    if "one tab" in query or "one tab" in query :
        pyautogui.hotkey("ctrl", "w")
        speak("Tab closed sir!")
    elif "2 tabs" in query or "2 tabs" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("All tabs closed sir!")
    elif "3 tabs" in query or "3 tabs" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("All tabs closed sir!")
    elif "4 tabs" in query or "4 tabs" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("All tabs closed sir!")
    elif "5 tabs" in query or "5 tabs" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("All tabs closed sir!")

    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {dictapp[app]}.exe")
                speak(f"{app} closed sir!")
                break
        else:
            speak("Application not found sir!")