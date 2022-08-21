import datetime
from speak import *

def note():
    speak("What would you like me to take note of?")
    note_text = take_command()
    note_date = datetime.datetime.now()
    file_name = str(note_date).replace(":", "-") + "-note.txt"
    with open(file_name, 'w') as f:
        f.write(note_text)
    speak("Your note has been created.")