from select import select
from socket import *
tcp_socket = socket()
#tcp_socket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
tcp_socket.bind(('0.0.0.0',8888))
tcp_socket.listen(6)
rlist = [tcp_socket]
wlist = []
xlist = []
while True:
    print('watting for an IO event...')
    rs,ws,xs = select(rlist,wlist,xlist)
    for r in rs:
        if r is tcp_socket:
            print('watting for connect .....')
            conn,addr = r.accept()
            rlist.append(conn)
        else:
            data = r.recv(1024)
            if not data:
                rlist.remove(r)
                r.close()
            else:
                print('来自{}的信息：{}'.format(addr,data.decode()))
                wlist.append(r)
    for w in ws:
        r.send(b'reccive your message')
        wlist.remove(w)
    for x in xs:
        pass