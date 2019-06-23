'''
def triangles():
	b = [1]
	while True:
		yield b
		b = [1] + [x + b[i + 1] for i, x in enumerate(b[:-1])] + [1]

n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
   '''

b=[1,2,1]
b=[1] + [x + b[i + 1] for i, x in enumerate(b[:-1])] + [1]
print(b)
'''
b=['aa','bb','cc']
for i,v in enumerate(b[:-1]):
    print(i,v)
  
  '''
a=map(str,[1,2,3,4])
print(a)

def fn(x,y):
    return  x*10+y
from functools import  reduce
a=reduce(fn,[1,3,4,5,7])
print(a)