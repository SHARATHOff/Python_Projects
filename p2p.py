import socket
import time
import threading 
wish = input("wish to be host or client :")
def server1():
     global conn,addr
     server = socket.socket()
     host = socket.gethostname()
     host = socket.gethostbyname(host)
     port = 7890
     server.bind((host,port))
     print(host)
     server.listen()
     print("listening......")
     conn,addr = server.accept()
     print(addr)
                 
def client():
     global client
     client = socket.socket()
     host = '192.168.100.101'
     port = 7890
     address = (host,port)
     client.connect(address)
def recivingmessage(qwerty):
     while True:
          message = qwerty.recv(1024).decode()
          print(message ," : " ,end=" ")
def sendingmessage(qwertys):
     while True:
          message = input("ENTER :")
          message=qwertys.send(message.encode())
          
if wish=='c':
     client()
     t1 = threading.Thread(target=recivingmessage,args=(client,))
     t2 = threading.Thread(target=sendingmessage,args=(client,))
     t1.start()
     t2.start()
     
elif wish =='s':
     server1()
     t1 = threading.Thread(target=recivingmessage,args=(conn,))
     t2 = threading.Thread(target=sendingmessage,args=(conn,))
     t1.start()
     t2.start()
else:
     print('Exit')
