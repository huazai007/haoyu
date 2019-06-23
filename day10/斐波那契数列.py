def fib(max):
    #a,b=0,1
    a=0
    b=1
    while max>0:
        a,b=b,a+b

        yield a

        max-=1
for i in fib(10):
    print(i)

1 1
1  2
2 3
3 5
5 8
8 13
13 21
21 54

