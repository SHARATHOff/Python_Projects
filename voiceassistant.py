from datetime import *
import time
import speech_recognition as sp
import pyttsx3
import pyautogui
spe =pyttsx3.init()

times = datetime.time(datetime.now())
rec = sp.Recognizer()
mymic = sp.Microphone(device_index=1)

with mymic as Source:
    print('speak......')
    audio = rec.listen(Source)
    to_text = rec.recognize_google(audio)
if to_text=='open message':
    pyautogui.press('win')
    pyautogui.typewrite('WhatsApp',interval=0.1)
    time.sleep(0.2)
    pyautogui.press('Enter')
    spe.say('Thanke for using me sir')
    spe.runAndWait()
#elif to_text == 'time':
    #spe.say(times)
   # spe.runAndWait()

    
    