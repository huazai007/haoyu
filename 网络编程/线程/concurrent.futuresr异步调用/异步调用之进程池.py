from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
import  os,time,random
def task(n):
    print("{0} is running".format(os.getpid()))
    time.sleep(random.randint(1,3))
    return n**2

if __name__ == "__main__":
    executor=ProcessPoolExecutor(max_workers=3)
    futures=[]
    for i in range(11):
        future=executor.submit(task,i)
        futures.append(future)
    executor.shutdown(True)
    
    # print("++++>")
    # for future in futures:
    #     print(future.result())
