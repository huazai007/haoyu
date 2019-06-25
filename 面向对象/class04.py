# a,定义一个父类Animal，在构造方法中封装三个属性，姓名，性别，年龄，
# 再给其添加一个eat的方法，方法中显示%s正在吃饭（%s是哪个对象调用此方法，显示哪个对象名字）。
# b,定义两个子类Person,Dog，全部继承这个父类Animal.
# c,Person类中，有构造方法，封装一个皮肤的属性，有eat方法，方法中显示人类正在吃饭。
# d,Dog类中，有构造方法，封装一个毛色的属性，有eat方法，方法中显示狗狗正在吃饭。
# 上面这几个类创建完成之后，完成下列要求：
# ①：    实例化一个人类的对象，让其只封装皮肤属性。
# ②： 实例化一个人类的对象，让其封装姓名，性别，年龄，皮肤四个属性。
# ③： 实例化一个狗类的对象，让其只封装毛色属性。
# ④： 实例化一个狗类的对象，让其封装姓名，性别，年龄，毛色四个属性。
# ⑤： 实例化一个人类的对象，让其只执行父类的eat方法（可以对人类代码进行修改）。
# ⑥： 实例化一个狗类的对象，让其既执行父类的eat方法，又执行子类的eat方法。

class Animal:
    def __init__(self,name,sex,age):
        self.name=name
        self.sex=sex
        self.age=age

    def eat(self):
        print("{0}在吃饭".format(self.name))
class Person(Animal):
    def __init__(self,name,sex,age,skin):
        super().__init__(name,sex,age)
        self.skin=skin
    def eat(self):
        print("人类正在吃饭")
class Dog(Animal):
    def __init__(self,name,sex,age,colour):
        super().__init__(name,sex,age)
        self.colour=colour
    def eat(self):
        print("狗狗正在吃饭")


