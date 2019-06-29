from multiprocessing import  Process
def f(name):
    print("hello",name)
    print("我是子进程")
if __name__ == '__main__':

    p1=Process(target=f,args=('xxoo',))
    p1.start()
    import time
    time.sleep(5)
    print("执行主进程的内容了")
