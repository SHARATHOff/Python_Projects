def A():
    a = 10
    for j in range(a,-1,-1):
        print(' '*j,'*',end='')
        print()
    for i in range(1,a+1):
        print(' '*i,'*',end='')
        print()

A()
