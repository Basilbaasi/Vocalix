import pyttsx3
import speech_recognition as sr

# Initialize TTS engine
engine = pyttsx3.init('sapi5')  # 'sapi5' is for Windows
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # You can choose voices[1] for female voice

def speak(text: str):
    """Convert text to speech."""
    print(f"🗣️ Speaking: {text}")
    engine.say(text)
    engine.runAndWait()

def listen() -> str:
    """Capture voice input from microphone and return as text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.pause_threshold = 3  # Wait 2 second for pauses
        audio = recognizer.listen(source)

    try:
        print("🔍 Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"🧠 You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Could you say it again?")
        return "none"
    except sr.RequestError:
        speak("Speech recognition service is not available.")
        return "none"
