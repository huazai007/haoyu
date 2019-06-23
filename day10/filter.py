def is_odd(n):
    return n%2==1
tmplist=[1,3,4,5,6,7,9,10]
newlist=filter(is_odd,tmplist)
print(list(newlist))