from threading import Thread
import time
def foo():
    print("123")
    time.sleep(4)
    print("end123")

def bar():
    print("456")
    time.sleep(3)
    print("end456")

t1=Thread(target=foo)
t2=Thread(target=bar)

t1.setDaemon(True)#等所有非守护线程运行完毕就会被回收掉 所以"end123" 不会被打印了

t1.start()
t2.start()
print("master...")