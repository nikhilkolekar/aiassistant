import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime

# Initialize the recognizer and the text-to-speech engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    tts_engine.say(text)
    tts_engine.runAndWait()

def listen():
    """Capture and recognize speech input."""
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)
        
        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"Recognized: {command}")
            return command
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Could you please repeat?")
        except sr.RequestError:
            speak("Sorry, I'm having trouble connecting to the service.")

    return ""

def process_command(command):
    """Process the voice command."""
    if 'time' in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")
    elif 'open' in command:
        if 'google' in command:
            webbrowser.open("https://www.google.com")
            speak("Opening Google")
        elif 'youtube' in command:
            webbrowser.open("https://www.youtube.com")
            speak("Opening YouTube")
        else:
            speak("Sorry, I can't open that.")
    else:
        speak("I can do things like tell you the time, or open websites. Try saying something like 'What time is it?' or 'Open Google'.")

if __name__ == "__main__":
    speak("Hello, how can I assist you today?")
    while True:
        command = listen()
        if command:
            process_command(command)
        if 'exit' in command or 'quit' in command:
            speak("Goodbye!")
            break
