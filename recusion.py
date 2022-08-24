def fun1():
    print('hey')
    fun2()
def fun2():
    print('hai')
    fun1()
def fact(i):
    if i==1:
        return 1
    else:
        return i*fact(i-1)
'''try:
    print(fact(200))
except RecursionError:
    setrecursionlimit(100)
    print(fact(200))'''

'''for i in range(100):
    a = open('c://sad/{0}.txt'.format(i),'w')
    a.write('SHARATH{}'.format('\t')*i)
    a.close()'''
import sys
'''print('ENTER YOUR USER NAME ABOVE 8 CHARACTERS : \t')
a= sys.stdin.read(7)
print(a)'''
'''b =0
while True:
    try:
        a = open('c://sad/{}.txt'.format(b),'r')
        print(a.read())
        b+=1
    except FileNotFoundError:
        b-=1
'''
sys.setrecursionlimit(10000)
def a():
    b()
def b():
    a()
try:
    a()
except RecursionError:
    a()