from select import select
from socket import *
#创建套接字作为关注的IO
server_socket = socket()
server_socket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
server_socket.bind(('0.0.0.0',8888))
server_socket.listen(5)
rlist = [server_socket]
wlist = []
xlist = []
while True:
    #提交监测关注的IO，等待IO发生
    print('Watting for an IO Event...')
    rs,ws,xs = select(rlist,wlist,xlist)
    #遍历整个rs
    for r in rs:
        #当遍历至服务器套接字对象时，使用accept()函数，接收客户端套接字
        if r is server_socket:
            print('watting for connect....')
            client_socket,addr = r.accept()
            print("connect from ",addr)
            #将客户端套接字添加到关注列表
            rlist.append(client_socket)
        #如果不是服务器套接字对象，则说明遍历至客户端套接字对象，使用recv()函数，接收客户端发来的内容
        else:
            data = r.recv(1024)
            #如果客户端发送空字符串，说明客户端需要断开连接，此时继续监听是没有意义的，就从监听列表中，将其去掉，并关闭连接
            if not data:
                rlist.remove(r)
                r.close()
            #反之则接收并打印客户端的数据，为了向客户端返回数据，再将其添加至写IO列表内
            else:
                print(data.decode())
                #将客户端套接字放入wlist列表
                wlist.append(r)
    #遍历写IO列表，发现套接字对象后，使用send()函数向客户端返回信息，并将其从写列表中去除，列表中出现重复对象。
    for w in ws:
        w.send(b'Receive your message!')
        wlist.remove(w)
    for x in xs:
        pass
s.close()