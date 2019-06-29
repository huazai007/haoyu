from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
import  os,time,random
def task(n):

    print("{0} is running".format(os.getpid()))
    time.sleep(random.randint(1,3))
    return n**2
if __name__ == "__main__":

    executor=ThreadPoolExecutor(max_workers=3)
    # for i in range(11):
    #     future=executor.submit(task,i)

    res=executor.map(task,range(1,12))
        #取代了for +submit
    for i in res:
        print(i)