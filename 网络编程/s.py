import socket
'''
sk=socket.socket() # 创建服务端套接字 对象
sk.bind(('127.0.0.1',1111))#把地址 端口绑定到 服务端 套接字 对象上
sk.listen() # 监听链接
conn,addr=sk.accept() # 接受客户端链接
print(conn)
ret=conn.recv(1024) # 打印客户端发送的信息
print(ret)
conn.send(b"hello sb") # 向客户端返回信息
conn.close() #关闭客户端的套接字
sk.close() # 关闭服务端的套接字
'''

udp_sk=socket.socket(type=socket.SOCK_DGRAM)
udp_sk.bind(('127.0.0.1',2222))
msg,addr=udp_sk.recvfrom(1024)
print(msg)
udp_sk.sendto(b'hi',addr)
udp_sk.close()