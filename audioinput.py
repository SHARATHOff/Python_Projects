
import pyttsx3
import speech_recognition as sp
import pyautogui

eng = pyttsx3.init()

rec = sp.Recognizer()

my_micro = sp.Microphone(device_index=1)
def add():
    pyautogui.press('win')
    pyautogui.typewrite('class',interval=0.2)
    pyautogui.press('enter')
    pyautogui.hotkey('ctrl','a')
    pyautogui.hotkey('ctrl','c')


with my_micro as source :
    print('say.......')
    audio = rec.listen(source)
    to_tect=rec.recognize_google(audio)
print(to_tect)

if to_tect=="hai":
    eng.say("hai sir how are you...... ")
    add()
eng.runAndWait()
