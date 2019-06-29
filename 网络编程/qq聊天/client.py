import  socket
BUFSIZE=1024
upd_client_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
qq_name_dict={
    'egg':('127.0.0.1',8080),
    'yuan':('127.0.0.1',8080),
}

while True:
    qq_name=input('请选择聊天对象: ').strip()
    if qq_name not in qq_name_dict:continue
    while True:
        msg=input('请输入消息,回车发送,输入q结束和他的聊天: ').strip()

        if msg == "q" or not msg:break

        upd_client_socket.sendto(msg.encode('utf-8'),qq_name_dict[qq_name])

        back_msg,addr=upd_client_socket.recvfrom(BUFSIZE)
        print('来自[{0}:{1}]的一条消息:\033[1;44m{2}\033[0m'.format(addr[0],addr[1],back_msg.decode('utf-8')))

upd_client_socket.close()