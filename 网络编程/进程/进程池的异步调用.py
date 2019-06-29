import os
import  time
import random
from multiprocessing import Pool
def work(n):
    print("%s run" %(os.getpid()))
    time.sleep(random.random())
    return n**2
if __name__ == "__main__":
    p=Pool(3)
    res_l=[]
    for i in range(10):
        res=p.apply_async(work,args=(i,))
        res_l.append(res)

    p.close()
    p.join()
    for res in res_l:
        print(res.get())