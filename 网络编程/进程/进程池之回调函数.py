from multiprocessing import  Pool
import  requests
import  json
import  os

def get_page(url):
    print("<进程%s> get %s" %(os.getpid(),url))
    response=requests.get(url)
    if response.status_code == 200:
        return {'url':url,'text':response.text}



def pasre_page(res):
    print("<进程%s>parse %s" %(os.getpid(),res['url']))
    pares_res='url:<%s> size:[%s]\n' %(res['url',len(res['text'])])
    with open('/tmp/db.txt','a') as f:
        f.write(pares_res)

if __name__ == "__main__":
    urls=[
        'https://www.baidu.com',
        'https://www.python.org',
        'https://help.github.com',
        'https://www.sina.com.cn',
        'https://www.openstack.org',
    ]
    p=Pool(3)
    res_l=[]
    for url in urls:
        ## 这里表示，当get_page函数执行完成之后就会调用pasre_page函数，并且把get_page函数的返回值传给a函数。
        p.apply_async(get_page,args=(url,),callback=pasre_page)
        #res_l.append(res)
    p.close()
    p.join()
    #print([res.get() for res in res_l])