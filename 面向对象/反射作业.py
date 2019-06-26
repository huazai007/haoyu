# 选课系统的代码
# login
# 判断身份 并且根据身份实例化
# 根据每个身份对应的类 让用户选择能够做的事情
class Manager:
    OPERATE_DIC = [
        ('创造学生账号', 'create_student'),
        ('创建课程', 'create_course'),
        ('查看学生信息', 'check_student_info'),
    ]

    def __init__(self, name):
        self.name = name

    def create_student(self):
        print('创建学生账号')

    def create_course(self):
        print('创建课程')

    def check_student_info(self):
        print('查看学生信息')


class Student:
    OPERATE_DIC = [
        ('查看所有课程', 'check_course'),
        ('选择课程', 'choose_course'),
        ('查看已选择的课程', 'choosed_course')
    ]

    def __init__(self, name):
        self.name = name

    def check_course(self):
        print('check_course')

    def choose_course(self):
        print('choose_course')

    def choosed_course(self):
        print('查看已选择的课程')
def login():
    username=input("user: ")
    password=input("pwd: ")
    with open('/tmp/userinfo') as f:
        for line in f:
            user,pwd,ident=line.strip().split('|')
            if user == username and pwd == password:
                print("登录成功")
                return username,ident


import sys
def main():
    usr,id=login()
    print(usr,id)
    file=sys.modules['__main__']
    print(file)
    cls=getattr(file,id)
    obj=cls(usr)
    operate_dic=cls.OPERATE_DIC
    print(operate_dic)
    while True:
        for num,i in enumerate(operate_dic,1):
            print(num,i[0])
        choice=int(input("num>>>"))
        choice_item=operate_dic[choice-1]
        print(choice_item)
        getattr(obj,choice_item[1])()
main()