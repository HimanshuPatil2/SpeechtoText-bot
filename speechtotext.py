# Import the required libraries
import pyttsx3 as p
import speech_recognition as sr

# Initialize the Text to Speech engine
bot1 = p.init()
voices = bot1.getProperty('voices')
bot1.setProperty('voice', voices[0].id)  # try another voice by changing voices[0] to voices[1]

def text_to_speech(text):
    bot1.say(text)
    bot1.runAndWait()

def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            print("Recognizing...")
            text = r.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except:
            print("Sorry, I did not get that")
            return ""

# Call the speech_to_text function
speech_to_text()
