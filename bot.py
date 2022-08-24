import pyautogui
import time

def add():
    pyautogui.press('win')
    pyautogui.typewrite('cass',interval=0.1)
    time.sleep(0.2)
    pyautogui.press('enter',interval=0.3)
    pyautogui.hotkey('ctrl','a')
    pyautogui.hotkey('ctrl','c')
add()
def enter():
    pyautogui.press('Enter')
pyautogui.press('win')
pyautogui.typewrite('chrome')
enter()
time.sleep(1)
#pyautogui.doubleClick(604,502)for home page whatsapp
pyautogui.doubleClick(485,77,interval=0.5)
time.sleep(4)
pyautogui.click(189,196)
pyautogui.hotkey('ctrl','v')
enter()
def zoomclass():
    pyautogui.typewrite('zoom',interval=0.2)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.doubleClick(587,374,interval=0.5)

def googlemeet():
    time.sleep(2)
    pyautogui.click(460,651)
    pyautogui.position(1012,490)



