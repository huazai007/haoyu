class A:
    name ="haoyu"
    count=1
    def func1(self):
        return A.name+str(A.count+9)
    @classmethod
    def func2(cls):
        return cls.name+str(cls.count+11)
#print(A.name)
#print(A.func1())###
#a1=A()
#print(a1.func1())
print(A.func2())