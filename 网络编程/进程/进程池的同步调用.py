import os,time
from multiprocessing import Pool

def work(n):
    print("%s run" %(os.getpid()))
    time.sleep(3)
    return n**2

if __name__ == "__main__":
    p=Pool(3)
    res_l=[]
    for i in range(10):
        res=p.apply(work,args=(i,))
    print(res_l)