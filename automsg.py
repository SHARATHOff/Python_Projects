import time
import pyautogui

for i in range(10):
    time.sleep(1)
    pyautogui.typewrite('hai')
    pyautogui.press('enter')
    time.sleep(0.1)
