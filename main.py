import datetime
import pywhatkit
import wikipedia
import webbrowser
from weather import *
from speak import *
from send_email import *
from notepad import *



def run_chad():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        speak('Now playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        speak('The time is now ' + time)
    elif 'date' in command:
        date = datetime.datetime.now().strftime('%A,%d %B, %Y')
        print(date)
        speak("Today's date is " + date)
    elif 'wikipedia' in command:
        person = command.replace('wikipedia', '')
        info = wikipedia.summary(person, 1)
        print(info)
        speak(info)
    elif 'google' in command:
        thing = command.replace('google', '')
        webbrowser.open(f'https://www.google.com/search?q={thing}')
        speak('Here are the results of your google search ')
    elif 'weather in' in command:
        city = command.split("in", 1)
        weather_data = weather_api(city[1])
        speak(weather_data)
    elif 'send email' in command:
        mail_info()
    elif 'goodbye' in command:
        speak("bye bye")
        quit()
    elif 'create a note' in command:
        note()

    else:
        speak("Say that again.")


while True:
    run_chad()


