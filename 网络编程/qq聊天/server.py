import socket
ip_port=('127.0.0.1',8080)
udp_server_sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udp_server_sock.bind(ip_port)
while True:
    qq_msg,addr=udp_server_sock.recvfrom(1024)
    print('来自{0}:{1}的一条消息:\033[1;44m{2}\033[0m'.format(addr[0],addr[1],qq_msg.decode('utf-8')))
    back_msg=input('回复消息:').strip()

    udp_server_sock.sendto(back_msg.encode('utf-8'),addr)
#recv receive  receive接收

