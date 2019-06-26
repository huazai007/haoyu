import  re
line = "Cats are smarter than dogs"
# .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
#() 是分组的意思
#print(matchObj.group())
#print(matchObj.group(1))
#print(matchObj.groups())
#obj=re.compile('\d{3}')
#ret=obj.findall('abc1233434')
#print(ret)
ret = re.sub('\d', 'H', 'eva3egon4yuan4')#将数字替换成'H'，参数1表示只替换1个
print(ret) #evaHegon4yuan4

ret = re.subn('\d', 'H', 'eva3egon4yuan4')#将数字替换成'H'，返回元组(替换的结果,替换了多少次)
print(ret)
r=re.split('(\w+)', ' runoob, runoob, runoob.')
print(r)

ret=re.split("\d+","eva3egon4yuan")
print(ret) #结果 ： ['eva', 'egon', 'yuan']

ret=re.split("(\d+)","eva3egon4yuan")
print(ret) #结果 ： ['eva', '3', 'egon', '4', 'yuan']

#在匹配部分加上（）之后所切出的结果是不同的，
#没有（）的没有保留所匹配的项，但是有（）的却能够保留了匹配的项，
#这个在某些需要保留匹配部分的使用过程是非常重要的。
