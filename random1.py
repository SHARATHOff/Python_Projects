import random

lett = "abcdefghijklmnopqrstuvwxyz1234567890"
lenas =8
while True:
    a = "".join(random.sample(lett,k=lenas))
    print(a,end='\n')
    p = open('pas.txt','a')
    p.write(a)