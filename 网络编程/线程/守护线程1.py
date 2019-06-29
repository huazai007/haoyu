from threading import  Thread
import  time
def sayhi(name):
    time.sleep(2)
    print("{0} say hello".format(name))

if __name__ == "__main__":
    t=Thread(target=sayhi,args=('egon',))
    t.setDaemon(True) #必须在t.start()之前设置
    t.start()
    
    print("住线程")
    print(t.is_alive())