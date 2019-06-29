
from threading import  Thread
import  time
class Saihai(Thread):
    def __init__(self,name):
        super().__init__()
        self.name=name
    def run(self):
        time.sleep(2)
        print("{0} say hello ".format(self.name))
if __name__ == "__main__":
    t=Saihai("huazai")
    t.start() #继承的父类里有个start(), 这个start() 负责调用self.run()
    #t.join()
    print("master.....")
