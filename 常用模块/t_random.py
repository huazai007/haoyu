import random
#随机小数
print(random.random())
print(random.uniform(1,3)) # 大于1 小于3 的小数

#s随机整数
random.randint(1,5)#大于1,小于等于5之间的整数
print(random.randrange(1,10,1)) #大于1 小于10之间的偶数

#随机选择一个返回
print(random.choice([1,'23',[4,5]]))
print(random.sample([1,23,[4,5]],2))

item=[1,3,4,5,7,9]
random.shuffle(item)
print(item)



def v_code():
    code=''
    for i in range(5):
        num=random.randint(0,9)
        alf=chr(random.randint(65,90))
        add=random.choice([num,alf])
        code="".join([code,str(add)])
    return code
#print(v_code())

add="aa"
code="".join(['a',str(1)])
print(code)