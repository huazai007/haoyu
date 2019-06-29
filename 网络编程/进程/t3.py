import os
from multiprocessing import  Process
class MyProcess(Process):
    def __init__(self,name):
        super().__init__()
        self.name=name
    def run(self):
        print(os.getpid())
        print("{0}正在和女主播聊mm".format(self.name))

#p=Process(target=,args=())
p1=MyProcess("wupeiqi")
p2=MyProcess("yuanhao")
p3=MyProcess("nezha")

# p3.
# p5=Process()
# p1.start()
# p2.start()
# p3.start()
# p1.join()
# p2.join()
# p3.join()
#
# print("master....")

class A:
    n="1111"

    def fun2(self):
        print("A-func2")
    def fun1(self,n):
        self.fun2()
        print(n)


class B(A):
    # def fun1(self):
    #     print("B-func")
    def fun2(self):
        print("B-func2")



a=A()
b=B()
t=123
#a.fun1("t")
print(A.n)
