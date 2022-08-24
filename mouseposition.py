import pyautogui
while True:
    m = pyautogui.position()
    print(m)
    key = input
    if key ==27:
        break
    
    