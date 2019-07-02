import gevent
def eat(name):
    print("{0} eat 1 ".format(name))
    gevent.sleep(2)#模拟IO阻塞
    print("{0} eat 2 ".format(name))

def play(name):
    print("{0} play 1".format(name))
    gevent.sleep(1)
    print("{0} play 2 ".format(name))

g1=gevent.spawn(eat,'egon')
g2=gevent.spawn(play,name="haoyu")
g1.join()
g2.join()
print("master..............")