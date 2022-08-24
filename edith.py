import pywhatkit
import speech_recognition as sp
import pyttsx3
import pyautogui
def speach(ints):
    com = pyttsx3.init()
    ints = com.say('')
    com.runAndWait()
def ironman():
    pywhatkit.playonyt('edith')


voice = sp.Recognizer()
mic = sp.Microphone(device_index=1)

with mic as source:
    audio = voice.listen(source)
    intext = voice.recognize_google(audio)

if intext=='hai':
    print('hai')
    