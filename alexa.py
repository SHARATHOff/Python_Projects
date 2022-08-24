
import speech_recognition
from favourite import *

rec = speech_recognition.Recognizer()

mymic = speech_recognition.Microphone(device_index=1)


with mymic as Source:
    audio = rec.listen(Source)
    to_text = rec.recognize_google(audio)
to_text = str(to_text)
to_text= to_text.lower()
if to_text=='play':
    favtamil_song()
elif to_text=='playmarveltrailer':
    docterstrange_trailer()
else:
    pass