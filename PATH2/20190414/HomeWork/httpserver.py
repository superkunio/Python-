from socket import *
s = socket()
s.bind(('127.0.0.1',9999))
s.listen(8)
conn,addr = s.accept()
print('connect from',addr)
f = open('D:\\学习\\project\\20190414\\HomeWork\\Q2.BMP','wb')
while True:
    data = conn.recv(1024)
    f.write(data)
    if not data:
        break
f.close()
conn.close()
s.close()
