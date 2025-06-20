import wolframalpha
import pyttsx3
import speech_recognition


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)  # Set the voice to the first available voice
engine.setProperty("rate", 170)  # Set the speech rate (words per minute)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def WolfRamAlpha(query):
    apikey = "3785Q4-EPXAP84E7X"
    # apikey = "VQRRYV-WJ8UL76UQL"
    requester = wolframalpha.Client(apikey)
    requested = requester.query(query)
    

    try:
        answer = next(requested.results).text
        return answer
    except:
        speak("The value in not answerable")

def Calc(query):
    Term = str(query)
    Term = Term.replace("venture", "")
    # Term = Term.replace("calculate", "")
    Term = Term.replace("multiply", "*")
    Term = Term.replace("divide", "/")
    Term = Term.replace("plus", "+")
    Term = Term.replace("minus", "-")
    Term = Term.replace(" ", "")
  
    Final =  str(Term)
  
    try:
        result = WolfRamAlpha(Final)
        print(f"{result}")
        speak(result)

    except:
        speak("The value in not answerable")


# client = wolframalpha.Client('YOUR_APP_ID')
# res = client.query('2+2')
# print(next(res.results).text)