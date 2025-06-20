import pyttsx3
import speech_recognition 
import requests
from bs4 import BeautifulSoup
import datetime
import os
import pyautogui
import webbrowser
import random
from plyer import notification
from pygame import mixer
import speedtest_cli


for i in range(3):
    a = input("Enter the password: ")
    pw_file = open("password.txt", "r")
    pw = pw_file.read()
    pw_file.close()
    if (a==pw):
        print("Access Granted , PLZ Speak [WAKE UP VENTURE] to start the program!")
       
        break
    elif (i==2):
        print("Access Denied!")
        exit()
    elif (a!=pw):
        print("Try Again,Sir!")


from INTRO import play_gif
play_gif
        
    



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
        r.energy_threshold = 800
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

                ############################# VENTURE: AI 2.0 reloded   #####################
                elif "change password" in query:
                    speak("what's the new password?")
                    new_pw = input("Enter the new password: ")
                    new_password = open("password.txt", "w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Password changed successfully!")
                    speak(f"Your new password is {new_pw}")
                    print(f"Your new password is {new_pw}")


                elif "schedule my day" in query:
                    tasks = []
                    speak("Do you want to clear old tasks? (yes/no)")
                    query = takeCommand().lower()
                    if "yes" in query:
                        file = open("tasks.txt", "w")
                        file.write(f"")
                        file.close()
                        speak("Old tasks cleared!")
                        no_tasks = int(input("Enter the number of tasks:- "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input(f"Enter task:- "))
                            file = open("tasks.txt", "a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                    elif "no" in query:
                        i = 0
                        no_tasks = int(input("Enter the number of tasks:- "))
                        for i in range(no_tasks):
                            tasks.append(input("Enter task :- "))
                            file = open("tasks.txt", "a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()


                elif "show my schedule" in query:
                    file = open("tasks.txt", "r")
                    content = file.read()
                    speak(content)
                    print(content)
                    file.close()
                    mixer.init()
                    mixer.music.load("norti.wav")
                    mixer.music.play()
                    notification.notify(
                        title = "My Schedule",
                        message = content,
                        timeout = 15
                    )

                elif "focus mode" in query:
                    a = int(input("Are you sure, Sir? :- (yes/no) " ) )
                    if (a==1):
                        speak("Entering the focus mode.......!")
                        # from Focusmode import is_admin
                        # is_admin()
                        os.startfile("C:\Users\hp\Desktop\Venture 2\Focusmode.py")
                        # exit()   

                    else:
                        pass
                elif "show my focus" in query:
                    from Focus_Graph import focus_graph
                    focus_graph()


                elif "launch" in query:
                    query = query.replace("launch", "")
                    query = query.replace("venture", "")
                    
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(0.5)
                    pyautogui.press("enter")
                    
                    
                elif "internet speed" in query:
                    wifi = speedtest_cli.Speedtest()
                    upload_net = wifi.upload()/1048576          #megabytes = 1024*1024 bytes
                    download_net = wifi.download()/1048576
                    speak(f"Your Internet speed is upload {upload_net} mbps and download {download_net} mbps")
                    print(f"Your Internet speed is upload {upload_net} mbps and download {download_net} mbps")

                elif "ipl score" in query:
                    from plyer import notification
                    import requests
                    from bs4 import BeautifulSoup
                    url = "https://www.cricbuzz.com/live-scores"
                    page = requests.get(url)
                    soup = BeautifulSoup(page.text, "html.parser")
                    team1 = soup.find_all(class_="cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
                    team2 = soup.find_all(class_="cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
                    team1_score = soup.find_all(class_ = "cb-ovr-flo")[8].get_text()
                    team2_score = soup.find_all(class_ = "cb-ovr-flo")[10].get_text()

                    a = print(f"{team1} : {team1_score}")  
                    b = print(f"{team2} : {team2_score}")

                    notification.notify(
                        title = "IPL Score",
                        message = f"{team1} : {team1_score}\n  {team2} : {team2_score}",
                        timeout = 15
                    )  

                elif "play a game" in query:
                    from game import game_play
                    game_play()
                    pyautogui.press("enter")
                
                elif "screenshot" in query:
                    import pyautogui
                    im = pyautogui.screenshot()
                    im.save("screenshot.jpg")

                elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("smile, sir!")
                    pyautogui.press("enter")


                elif "hello" in query:
                    speak("Hello sir! How can I assist you today?")
                elif "i am fine" in query:
                    speak("that's great sir!")
                elif "how are you" in query:
                    speak("I am fine sir")
                elif "thank you" in query:
                    speak("You are welcome sir!")

                elif "tired" in query:
                    speak("Playing your favorite song, sir!")
                    a = (1,2,3,)
                    b = random.choice(a)
                    if b == 1:
                        webbrowser.open("https://www.youtube.com/watch?v=sUf2PtEZris&pp=ygUQc2hha3kgc2hha3kgc29uZw%3D%3D")


                elif "stop" in query:
                    pyautogui.press("k")
                    speak("stop sir!")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("Playing sir!")
                
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("Muted sir!")
                                
                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Volume up sir!")
                    volumeup()
                
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Volume down sir!")
                    volumedown()

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

                elif "news" in query:
                    from NewsRead import letestsnews
                    letestsnews()
                    print("Done")

                elif "calculate" in query:
                    from Calculatenumbers import WolfRamAlpha
                    from Calculatenumbers import Calc
                    query = query.replace("calculate","")
                    query = query.replace("venture","")
                    Calc(query)

                elif "whatsapp" in query:
                    from Whatsapp import sendMessage
                    sendMessage()


               
                elif "Temperature" in query:

                    search = "temperature in varanasi"
                    url = f"https://www.google.com/search?client=opera&q={search}" + query
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_= "BNeawe").text
                    speak(f"current{search} is {temp}")
                    print(temp)

                elif "weather" in query:
                    search = "weather in {query}"
                    url = f"https://www.google.com/search?client=opera&q={search}" + query
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
                
                elif "go to shutdown" in query:
                    speak("Goodbye,i am going to sleep mode, have a nice day!")
                    exit()
                
                elif "remember that" in query:
                    rememberMessage = query.replace("remember that", "")
                    rememberMessage = query.replace("venture", "")
                    speak("you told me to remember that" + rememberMessage)
                    remember = open("Remember.txt", "w")
                    remember.write(rememberMessage)
                    remember.close()
                
                elif "what do you remember" in query:
                    remember = open("Remember.txt", "r")
                    speak("You told me" + remember.read())

                elif "shutdown system"  in query:
                    speak("are yuou sure, sir!")
                    shutdown = input("Do You wish to shutdown your computer? (yes/no): ")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")
                    
                    elif shutdown == "no":
                        break
                

                    

                