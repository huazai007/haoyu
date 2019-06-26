from collections import namedtuple
point=namedtuple('point',['x','y'])
p=point(1,2)
#print(p.x)

#namedtuple('名称',[属性list])
circle=namedtuple('circle',['x','y','z'])

from collections import deque

q=deque(['a','b','c'])
q.append('x')
q.appendleft('yy')
#print(q)

from collections import OrderedDict
d=dict([('a,',1),('b',2),("c",3)])
#print(d)
od=OrderedDict([('a',1),('b',2),("c",3)])
#print(od)
od=OrderedDict()
od['zz']=11
od['xx']=22
od['yy']=33
#print(od)
#print(od.keys())

'''
values=[11,22,33,44,55,66,77,88,99,100]
my_dict={}
for v in values:
    if v >66:
        if 'k1' in my_dict.keys():
            my_dict['k1'].append(v)
        else:
            my_dict['k1']=[v]

    else:
        if 'k2' in my_dict.keys():
            my_dict['k2'].append(v)
        else:
            my_dict['k2']=[v]
print(my_dict)
'''
'''
from collections import  defaultdict
values=[11,22,33,44,55,66,77,88,99,100]
my_dict=defaultdict(list)
for v in values:
    print(my_dict)
    if v> 66:
        my_dict['k1'].append(v)
    else:
        my_dict['k2'].append(v)

'''
from collections import Counter
c=Counter('afaerwerqerafdasfaerafadsfzvfdfadf')
print(c)