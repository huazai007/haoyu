from threading import Thread
import  time
def sayhi(name):
    time.sleep(2)
    print("{0} say hello".format(name))

if __name__ == "__main__":
    t=Thread(target=sayhi,args=('egon',))
    t.start()
    #t.join()
    print("主线程....................")
