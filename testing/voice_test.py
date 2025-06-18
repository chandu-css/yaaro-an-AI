# import pyttsx3

# engine = pyttsx3.init()
# voices = engine.getProperty('voices')

# for index, voice in enumerate(voices):
#     print(f"{index}: {voice.name} ({voice.languages}) - {voice.id}")

# import pyttsx3

# engine = pyttsx3.init()
# voices = engine.getProperty('voices')

# # Force use first available voice
# if voices:
#     engine.setProperty('voice', voices[1].id)

# engine.say("This is a test using a specific voice.")
# engine.runAndWait()

from gtts import gTTS
from playsound import playsound
import os

def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = "temp.mp3"
    tts.save(filename)
    playsound(filename)
    os.remove(filename)  # Clean up

# Test
speak("Hello, this is your AI buddy. I'm speaking now.")

