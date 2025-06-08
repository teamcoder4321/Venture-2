import pyttsx3
import datetime
import os


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)  # Set the voice to the first available voice
engine.setProperty("rate", 170)  # Set the speech rate (words per minute)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

extractedtime = open("Alarmtext.txt", "rt")
time = extractedtime.read()
Time = str(time)
extractedtime.close()

deletetime = open("Alarmtext.txt", "r+")
deletetime.truncate(0)  # Clear the file content
deletetime.close()

def ring(time):
    timeset = str(time)
    timenow = timeset.replace("venture", "")
    timenow = timenow.replace("set an alarm", "")
    timenow = timenow.replace("and", ":")
    AlarmTime = timenow.str(timenow)
    print(AlarmTime)
    while True:
        currenttime = datetime.datetime.now().strftime("%H:%M:%S")
        if currenttime == AlarmTime:
            speak("Wake up sir! It's time to get up!")
            os.startfile("alarm.mp3")
        elif currenttime + "00:00:30" == AlarmTime:
            exit()
ring(time)