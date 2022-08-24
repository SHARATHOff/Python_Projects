from math import radians
import random

lettsm = 'abcdefghijklmnopqrstuvwxyz'
letup = lettsm.upper()
letters = list(lettsm)
#print(letters)
password = input('ENTER THE PASSWORD : ')
guss_password = ''

while password!=guss_password:
    guss_password=''
    for i in range(len(password)):
        guss_ = letters[(random.randint(0,25))]
        guss_password = str(guss_+str(guss_password))
    print(guss_password)
print(password , 'is' ,guss_password)
