import  json
dic={'k1':"a","k2":'b',"k3":'c','k4':4}
str_dic=json.dumps(dic)
print(type(str_dic))
with open('/tmp/a.json','w') as f:
    json.dump(dic,f)
    f.close()