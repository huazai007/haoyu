class Persion:
    def __init__(self,name,age):
        self.name=name
        self.__age=age
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,value):
        if type(value) is  int:
            self.__age=value
        else:
            print("error")

    @age.deleter
    def age(self):
        del self.__age



p1=Persion("haoyu",7)
#print(p1.age())
#print(p1.age)
p1.age=123
print(p1.age)
del p1.age
print(p1.__dict__)