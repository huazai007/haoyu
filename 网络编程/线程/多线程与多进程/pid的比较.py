
from threading import Thread
from multiprocessing import Process
import os
def work(n):
    print("hello,{0}:{1}".format(n,os.getpid()))
if __name__ == "__main__":
    for i in range(5):
        t=Thread(target=work,args=(i,))
        t.start()
    print("master....:{0}".format(os.getpid()))

    for i in range(5):
        p=Process(target=work,args=(i,))
        p.start()
    print("master...:{0}".format(os.getpid()))

