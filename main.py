# speech recognization software
import speech_recognition as sr #for voice recognition
import webbrowser #for webbrowser
import pyttsx3 #for text to voice
#pip install pocketsphinx

engine=pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
def process_command(command):
    """Process recognized speech commands."""
    command = command.lower()
    if "hey toya" in command:
        speak("Hello! How can I assist you today?")
    elif "open google" in command:
        speak("Opening Google.")
        webbrowser.open("https://www.google.com")
    elif "exit" in command or "quit" in command:
        speak("Goodbye!")
        return True  # Signal to exit the loop
    else:
        speak("I didn't understand that command. Try again.")
    return False

if __name__=="__main__":
    speak("Hey sir, its me Tourus, how can i help you?")
    recognizer=sr.Recognizer()
while True:
    print("recognizing....")
    try:
    #listen for word toya
        # obtain audio from the microphone
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            print("listening...")
            audio = recognizer.listen(source,timeout=5, phrase_time_limit=5)

        # recognize speech using google
        heard=recognizer.recognize_google(audio)
        print(heard)
        speak(heard)
        # Process the command and check if we should exit
        if process_command(heard):
            break
    except sr.UnknownValueError:
        print("toya could not understand audio.")
        speak("I couldn't understand you. Please try again.")
    except sr.RequestError as e:
        print(f"toya error: {e}")
        speak("I'm having trouble connecting to the speech service. Please check your internet.")
    except sr.WaitTimeoutError:
        print("No speech detected within timeout.")
        speak("I didn't hear anything. Please speak again.")
    except KeyboardInterrupt:
        speak("Shutting down.")
        break