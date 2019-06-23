'''
a=1
def test():
    global a
    a=a+1
    print(a)
#test()

def test1(name,age):
    print(name,age)

#test1("haoyu",6)

def test2(name,*var):
    print(name)
    print(var)
#test2("haoyu",3,4,5)

def test3(name,**var):
    print(name)
    print(var)
#test3("haoyu",a=1,c=3)

a=lambda arg1,arg2:arg1+arg2
#print(a(1,2))

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

print('L[0:3] =', L[0:3])
print('L[:3] =', L[:3])
print('L[1:3] =', L[1:3])
print('L[-2:] =', L[-2:])


import os
print([d for d in os.listdir("/tmp")])
'''
def genc():
    for i in range(10):
        yield i
    def inner():
        for a in genc():
            print(a)
    return inner()
print(genc())

