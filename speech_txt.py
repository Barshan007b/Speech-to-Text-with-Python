import pyttsx3
import speech_recognition as sr

def get():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = r.listen(source)
        print("⏳ Recognizing...")

    try:
        text = r.recognize_google(audio)  
        print(f"📝 You said: {text}")
        return text
    except sr.UnknownValueError:
        print("❌ Sorry, I did not understand that.")
        return None
    except sr.RequestError:
        print("❌ Could not request results; check your network connection.")
        return None
    except Exception as e:
        print(f"❌ An error occurred: {e}")
        return None

# Run function
get()
