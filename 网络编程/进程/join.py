import time
from multiprocessing import Process
def f(name):
    print("hello",name)
    time.sleep(5)
    print("我是子进程")
if __name__ == "__main__":
    p=Process(target=f,args=('xxoo',))
    p.start()
    p.join()
    print("我是父进程")