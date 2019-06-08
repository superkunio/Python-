import socket
s = socket.socket()
ServerHost = ('127.0.0.1',8888)
s.connect(ServerHost)
massage = input('-->')
s.send(massage.encode())
s.close()