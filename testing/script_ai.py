from deepface import DeepFace
import cv2
import pyttsx3

# initialize the speach
engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    print(f"PA says: {text}")
    engine.say(text)
    engine.runAndWait()

def detect_emotion():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        speak("Oops! I can't open webcam")
        return None
    
    ret, frame = cap.read()
    cap.release()

    if not ret:
        speak("Falied to grab frame, can you please try again?")
        return 'neutral'

    try:
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        emotion = result[0]['dominant_emotion']
        print(f"Detected Emotion: {emotion}")
        return emotion
    except Exception as e:
        speak("Hmm, I could't understand your feeling...")
        return None

def follow_up_conversation(emotion):
    if emotion in ['sad', 'tired', 'angry', 'neutral']:
        speak("You look a bit off now. Would you like to talk about it?")
        user_response = input("You: ")
        if any(word in user_response.lower() for word in ['yes', 'okay', 'sure']):
            speak("I am here to listen, what happen. How are you really feeling?")
            detail = input("You: ")
            if any(word in detail.lower() for word in ['bad', 'stress', 'work']):
                speak("Thats sounds tough, Want me to suggest something to uplift you?")
            elif any(word in detail.lower() for word in ['bored', 'low']):
                speak("Oh, really. Shall we play some game or chit chat for some time?")
            elif any(word in detail.lower() for word in ['lonely', 'alone']):
                speak("Oh, really. Shall we play some game or chit chat for some time?")
            else:
                speak("Thanks for sharing. I am always here for you!")
        else:
            speak("No worries. I am gald you are here and touch me when ever you want!!")
    elif emotion == 'happy':
        speak("you look great today! Keep that smile going!!")
    else:
        speak("Hope you are having a smooth day!")


if __name__ == "__main__":
    # Step 1: Detect Emotion
    emotion = detect_emotion()

    # Step 2: Continue Conversation
    if emotion:
        follow_up_conversation(emotion)

        #follow_up_conversation(emotion)
 