def normalize(name):
    return name[:1].upper()+name[1:].lower()
l1=['admin',"LisD","IdaN"]
l2=list(map(normalize,l1))
print(l2)
a="dldff"
print(a[:1].upper())