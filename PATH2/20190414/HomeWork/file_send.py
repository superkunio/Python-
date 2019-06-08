from socket import *
s = socket()
s.connect(('127.0.0.1',9999))
f = open('D:\\学习\\project\\20190414\\HomeWork\\Q1.BMP','rb')
while True:
    data = f.read(1024)
    if not data:
        break
    s.send(data)
f.close()
s.close()