# import os
# import time
# from multiprocessing import  Process
# class MyProcess(Process):
#     def __init__(self,persion):
#         super().__init__()
#         self.person=persion
#     def run(self):
#         print(os.getpid(),self.name)
#         print("{}正在和女主播聊天 ".format(self.person))
# p=MyProcess("哪吒")
# p.daemon=True
# p.start()
# time.sleep(10)
# print("master.....")

import time
from multiprocessing import Process

def foo():
    print(123)
    time.sleep(1)
    print("end123")

def bar():
    print(456)
    time.sleep(3)
    print("end456")


p1=Process(target=foo)
p2=Process(target=bar)

p1.daemon=True
p1.start()
p2.start()
time.sleep(0.1)
print("main-------")#打印该行则主进程代码结束,则守护进程p1应该被终止.#可能会有p1任务执行的打印信息123,因为主进程打印main----时,p1也执行了,但是随即被终止.
