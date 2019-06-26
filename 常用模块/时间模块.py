import  time
#时间戳
print(type(time.time()))
#时间字符串
print(time.strftime("%Y-%m-%d %h-%H-%S"))

#时间元组:localtime 将一个时间戳 转换为当前时区的struct_time
print(time.localtime())