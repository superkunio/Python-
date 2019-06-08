from socket import *
sockfd = socket(AF_INET,SOCK_STREAM)
server_addr = ('192.168.18.3',8848)
sockfd.connect(server_addr)
while True:
    conte = input('continue?(Y/N)')
    if conte == 'n':
        break
    else:
        info = input('-->')
        sockfd.send(info.encode())
        data = sockfd.recv(1024)
        print('receive:',data.decode('utf-8'))
sockfd.close()