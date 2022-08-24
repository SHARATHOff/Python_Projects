from datetime import *
import pyttsx3
import speech_recognition as sp

times = datetime.time(datetime.now())
times = list(times)
print(times)
eng = pyttsx3.init()

rec = sp.Recognizer()

my_micro = sp.Microphone(device_index=1)


with my_micro as source :
    print('say.......')
    audio = rec.listen(source)
    to_tect=rec.recognize_google(audio)
print(to_tect)

if to_tect=="hai":
    eng.say("hai sir how are you...... ")
    
eng.runAndWait()
