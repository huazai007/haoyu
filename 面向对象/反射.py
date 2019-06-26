#类  静态属性 类方法 静态方法
#命名空间.XXX == getattr(命名空间,'XXX')
class Student:
    ROLE = 'STUDENT'
    def __init__(self,name):
        self.name=name

    @classmethod
    def check_course(cls,values):
        print('查看课程了 %s' %(values))

    @staticmethod
    def login():
        print('登录')
    def hehe(self):
        print("你好,%s" %(self.name))
# 反射查看属性
# print(Student.ROLE)
# print(getattr(Student,'ROLE'))

# 反射调用方法
# getattr(Student,'check_course')()  # 类方法
# getattr(Student,'login')()         # 静态方法

s1=Student("haoyu")

num = input('num:>>> ')

if hasattr(Student,num):
    getattr(Student,num)("xxx")
    #getattr(s1,num)()

