import os
import time
import random
from multiprocessing import Process
def work(n):
    print("{0}:{1}is running".format(n,os.getpid()))
    time.sleep(random.random())
    print("{0}:{1} is done".format(n,os.getpid()))
if __name__ == "__main__":
    for i in range(6):
        p=Process(target=work,args=(i,))
        p.start()

    print("master.......")