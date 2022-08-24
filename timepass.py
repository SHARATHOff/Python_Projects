'''for j,i in range(10,0,-1):
    print(' '*j,'*',end='')
    print()

for i in range(10):
    print(' '*i,'*',end='')
    print()
   ''' 
import smtplib

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('sharathbaln123456@gmail.com','Adminappappusharath')
server.sendmail('sharathbaln123456@gmail.com','sharathbalan2006@gmail.com','hai how are you iam fine sharath si the from a  pc ')