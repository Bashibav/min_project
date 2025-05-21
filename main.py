# speech recognization software
import speech_recognition as sr #for voice recognition
import webbrowser #for webbrowser
import pyttsx3 #for text to voice
import musicLibrary #impot music from musiclibrary.py
import requests
from openai import OpenAI
#pip install pocketsphinx

engine=pyttsx3.init()
new_key=" "

def speak(text):
    engine.say(text)
    engine.runAndWait()

def process_command(command):
    """Process recognized speech commands."""
    command = command.lower()
    if "hey jarvis" in command:
        speak(" How can I assist you today?")
    elif "open google" in command:
        speak("Opening Google.")
        webbrowser.open("https://www.google.com")
    elif "open facebook" in command:
        speak("Opening Facebook.")
        webbrowser.open("https://www.facebook.com")
    elif "open github" in command:
        speak("Opening GitHub.")
        webbrowser.open("https://www.github.com")
    elif "open youtube" in command:
        speak("Opening Youtube.")
        webbrowser.open("https://www.youtube.com")
    elif command.lower().startswith("play"):
        try:
            song = command.split(" ", 1)[1].strip()  # Get song name after "play"
            link = musicLibrary.music.get(song.lower())
            if link:
                speak(f"Playing {song}.")
                webbrowser.open(link)
            else:
                speak(f"Sorry, I couldn't find the song {song} in the library.")
        except AttributeError:
            speak("Error accessing the music library.")
    elif "news" in command.lower():
        req=requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={new_key}")
        if req.status_code == 200:
            data = req.json()
            articles = data.get('articles', [])

        # speak the headlines
        for  article in articles:
            speak(article['title'])
        else:
            print("Failed to fetch news:", req.status_code, req.text)
    elif "exit" in command or "quit" in command:
        speak("Goodbye!")
        return True  # Signal to exit the loop
    else:
        #let open Ai handle this
       pass
    return False

if __name__=="__main__":
    speak("hello....")
    recognizer=sr.Recognizer()
while True:
    print("recognizing....")
    try:
    #listen for word jarvis
        # obtain audio from the microphone
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            print("listening...")
            audio = recognizer.listen(source,timeout=5, phrase_time_limit=5)

        # recognize speech using google
        heard=recognizer.recognize_google(audio)
        print(heard)
        speak("yes")
        # Process the command and check if we should exit
        if process_command(heard):
            break
    except sr.UnknownValueError:
        print("jarvis could not understand audio.")
        speak("I couldn't understand you. Please try again.")
    except sr.RequestError as e:
        print(f"jarvis error: {e}")
        speak("I'm having trouble connecting to the speech service. Please check your internet.")
    except sr.WaitTimeoutError:
        print("No speech detected within timeout.")
        speak("I didn't hear anything. Please speak again.")
    except KeyboardInterrupt:
        speak("Shutting down.")
        break