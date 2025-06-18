from deepface import DeepFace
import cv2

def detect_emotion():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Oops! I can't open webcam")
        return None
    
    ret, frame = cap.read()
    cap.release()

    if not ret:
        print("Falied to grab frame, can you please try again?")
        return 'neutral'

    try:
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        emotion = result[0]['dominant_emotion']
        print(f"Detected Emotion: {emotion}")
        return emotion
    except Exception as e:
        print("Hmm, I could't understand your feeling...")
        return 'neutral'
