import socket
'''
sk=socket.socket() # 创建客户端的套接字 对象
sk.connect(('127.0.0.1',1111)) #链接fuwu
sk.send(b'hello server')
ret=sk.recv(1024)
print(ret)
sk.close()
'''

ip_port=('17.0.0.1',2222)
udp_sk=socket.socket(type=socket.SOCK_DGRAM)
udp_sk.sendto(b'hello',ip_port)
back_msg,addr=udp_sk.recvfrom(1024)
print(back_msg.decode('utf-8'),addr)