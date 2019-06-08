from socket import *
import time

#设置目标地址，目标地址为广播地址
dest = ('221.198.196.255',9999)

s = socket(AF_INET,SOCK_DGRAM)
print('1')
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
print('2')
while True:
    time.sleep(2)
    s.sendto('hello world'.encode(),dest)
s.close()