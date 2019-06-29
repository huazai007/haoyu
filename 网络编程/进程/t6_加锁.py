import os
import time
import random
from multiprocessing import  Process,Lock


def work(lock,n):
    lock.acquire()
    print("{0}:{1}is running".format(n,os.getpid()))
    time.sleep(random.random())
    print("{0}:{1} is done".format(n,os.getpid()))
    lock.release()



if __name__ == "__main__":
    lock=Lock()
    for i in range(3):
        p=Process(target=work,args=(lock,i,))
        p.start()
