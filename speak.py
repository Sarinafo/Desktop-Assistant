import pyttsx3
import speech_recognition as sr

r = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("Please say a command...")
            audio = r.listen(source)
            command = r.recognize_google(audio)
            command = command.lower()
            if 'chad' in command:
                command = command.replace('chad', "")
                print(command)
    except:
        pass
    return command
