import random

alp = "abcdefghijklmnopqrstuvwxyz"
print(list(alp))
print(str(alp))
while True:
    pas = "".join(random.sample(alp,k=8))
    print(str(pas))
