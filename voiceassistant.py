import time
import speech_recognition as sp
import pyautogui

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

    
    