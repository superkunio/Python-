from socket import *
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',9999))
s.listen(6)
while True:
    c,addr = s.accept()
    print('connect from ',addr)
    data = c.recv(4096)
    print('*******************************')
    print(data.decode())
    print('*******************************')

    #用来记录发送至客户端的HTML文件,使用三引号，要注意缩进，内容不要与变量平齐,或者多次回车刷新换行。
    body_info = '''HTTP/1.1 200 OK
        Content-Encoding: gzip
        Content-Type: text/html

        <h1>1111<h1>
        <h2>中文输入，测试</h2>
        '''
    c.send(body_info.encode())
    c.close()
s.close()