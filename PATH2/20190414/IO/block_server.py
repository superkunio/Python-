from socket import *
from time import sleep,ctime
s = socket()
addr_info = ('0.0.0.0',8848)
s.bind(addr_info)
s.listen(3)
#将套接字设置为非阻塞
s.setblocking(False)
while True:
    print('waiting for connect....')
    try:
        c,addr = s.accept()
    except BlockingIOError:
        sleep(2)
        print(ctime())
        continue
    else:
        print('connect from ',addr)
        c.setblocking(False)
        while True:
            data = c.recv(1024).decode()
            if not data:
                break
        print(data)
        c.send(ctime().encode())
        c.close()
s.close()