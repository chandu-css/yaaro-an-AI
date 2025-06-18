import pyttsx3

# initialize the speach
engine = pyttsx3.init()
engine.setProperty('rate', 170)
def speak(text):
    print(f"Yaaro: {text}")
    engine.say(text)
    engine.runAndWait()