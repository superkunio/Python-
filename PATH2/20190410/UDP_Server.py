import socket
import time
udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
BCHost = ('192.168.18.3',8848)
udp_socket.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
timer = 0
while True:
    print(timer,end='\r')
    time.sleep(2)
    timer += 1
    udp_socket.sendto('This is my first UDP BroadCast from'.encode(),BCHost)
udp_socket.close()