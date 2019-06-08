from socket import *

#创建套接字
s = socket(AF_INET,SOCK_DGRAM)
#设置套接字可以收发接广播
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
#固定接收端口
s.bind(('0.0.0.0',9999))
print('1')
while True:
    try:
        print('2')
        msg,addr = s.recvfrom(1024)
        print('3')
        print('从{}获取信息：{}'.format(addr,msg.decode()))
    except(KeyboardInterrupt):
        raise
    except Exception as e:
        print(e)
s.close()
