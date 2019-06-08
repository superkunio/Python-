import select
import socket
#创建套接字作为关注IO
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(5)
rlist = [s]
wlist = []
xlist = []
#提交监测关注的IO，等待IO发生
while True:
    print('Watting for the IO Event...')
    rs,ws,xs = select.select(rlist,wlist,xlist)
    for r in rs:
        if r is s:
            c,addr = r.accept()
            print('connect from ',addr)
            #添加到关注列表
            rlist.append(c)
        else:
            data = r.recv(1024)
            if not data:
                rlist.remove(r)
                r.close()
            else:
                print(data.decode())
                r.send('Receive your message!!!'.encode())
    for w in ws:
        pass
    for x in xs:
        pass
s.close()