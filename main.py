# speech recognization software
import speech_recognition as sr #for voice recognition
import webbrowser #for webbrowser
import pyttsx3 #for text to voice
#pip install pocketsphinx

recognizer=sr.Recognizer()
engine=pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__=="__main__":
    speak("Hey sir, its me Torus, how can i help you?")
while True:
    try:
    #listen for word Torus
        # obtain audio from the microphone
        with sr.Microphone() as source:
            print("listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        # recognize speech using google
        heard=recognizer.recognize_google(audio)
        print(f"Torus thinks you said {heard}.")
        if "Hello" in heard:
                speak("Yes sir, I'm listening.")
                # Add further actions here
        else:
            print("Hotword not detected.")
    except sr.UnknownValueError:
        print("Torus could not understand audio")
    except sr.RequestError as e:
        print("Torus error; {0}".format(e))
