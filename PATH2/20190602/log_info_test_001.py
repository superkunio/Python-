import re,sys

def get_address(port):
    f = open('1.txt')
    while True:
        data = ''
        for line in f:
            if line !='\n':
                data += line
            else:
                break
        if not data:
            return 'not found the port'
        try:
            print(data)
            PORT = re.search(r'\S+',data).group()
        except Exception as e:
            print(e)
            continue
        if PORT == port:
            pattern = r'address is (\w{4}\.\w{4\.\w{4}})'
            addr = re.search(pattern,data).group(1)
            return addr


if __name__ == '__main__':
    port = input('请输入一个端口号')
    print(get_address(port))