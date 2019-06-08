from select import select
from socket import *
s = socket()
s.bind(('127.0.0.1',9999))
s.listen(3)
rlist = [s]
wlist = []
xlist = []
while True:
    rs,ws,xs = select(rlist,wlist,xlist)
    print('有IO事件')
    for x in rs:
        if x is s:
            c,addr = s.accept()
            rlist.append(c)
            print('connect from',addr)
        else:
            data = s.recv(1024)
            if not data:
                rlist.remove(rs)
                rs.close()



