from threading import  Thread
from multiprocessing import  Process
import  os
def work(num):
    global n
    n=num
    print(n)


if __name__ == "__main__":
    # n=100
    # p=Process(target=work,args=(123,))
    # p.start()
    # p.join()
    # print("master....",n) #毫无疑问,子进程p已经将自己的全局的n已经将自己的全局的n 改成了123,单仅仅该的是是自己的,查看父进程的n 仍然是100 啊
    # work(123)
    n=100
    t=Thread(target=work,args=(123,))
    t.start()
    #t.join()
    print("master:",n)# 查看结果为123.因为统一进程内的线程之间共享进程内的数据

