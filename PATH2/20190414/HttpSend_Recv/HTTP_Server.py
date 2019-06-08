from socket import *

def handleClient(connfd):
    request = connfd.recv(4096)
    request_lines = request.splitlines()
    #将request请求按行分割
    print('+++++++++++++++++++++++++++++')
    for line in request_lines:
        print(line.decode())
    print('+++++++++++++++++++++++++++++')

    try:
        file_path = 'D:\\学习\\project\\20190414\\HttpSend_Recv\\index.html'
        f = open(file_path,'r')
    except IOError:
        #如果页面没找到，返回错误信息,通过字符串+=运算，将其拼接为符合格式的字符串。
        response = "HTTP/1.1 404  not found\r\n"#响应行，响应头不用写
        response +="\r\n"#空行
        response +='page not found'#响应体
    else:
        #如果页面顺利打开，通过字符串+=运算，将其拼接为符合格式的字符串。
        response = "HTTP/1.1 200  OK\r\n"#响应行，响应头不用写
        response +="\r\n"#空行
        response += f.read()#响应体
    finally:
        #将读取的文件内容，发送给浏览器。
        connfd.send(response.encode())




def main():
    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    Server_ip = '127.0.0.1'
    Server_port = 9999
    Server_info = (Server_ip,Server_port)
    s.bind(Server_info)
    s.listen(7)
    while True:
        conn,addr = s.accept()
        handleClient(conn)


if __name__ =='__main__':
    main()

