from threading import  Thread
from multiprocessing import  Process
import os
def work():
    print("hello")

if __name__ == "__main__":
    #在主进程下开启线程
    t=Thread(target=work)
    t.start()
    print("主线程/主进程")

    #在主进程下开启子进程
    p=Process(target=work)
    p.start()
    print("主线程/主进程")