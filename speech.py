import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Use the microphone as source for input
with sr.Microphone() as source:
    print("🎙️ Speak something...")
    recognizer.adjust_for_ambient_noise(source)  # Optional: reduce background noise
    audio = recognizer.listen(source)

    try:
        print("🔍 Recognizing...")
        text = recognizer.recognize_google(audio)
        print("📝 You said:", text)

    except sr.UnknownValueError:
        print("❌ Could not understand audio")

    except sr.RequestError:
        print("❌ Could not request results from Google API")
