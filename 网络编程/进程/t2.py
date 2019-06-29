import time
from multiprocessing import  Process
def f(name,n):
    print("hello",name,n)
    time.sleep(5)
if __name__ == "__main__":
    p_lst=[]
    n=0
    for i in range(5):
        n+=1
        p=Process(target=f,args=("xxbb",n))
        p.start()

        p_lst.append(p)
        [p.join() for p in p_lst]
    print("我是父进程")