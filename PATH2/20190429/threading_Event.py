import threading
from time import sleep

s = None
e = threading.Event()

def bar():
    print('bar拜山头')
    global s
    s = '天王盖地虎'

def foo():
    print('说出口令就是自己人')
    sleep(2)
    if s == '天王盖地虎':
        print('我是座山雕，自己人')
    else:
        print('打死他')
    e.set()#等foo验证完毕再执行其他的


def fun():
    print('呵呵')
    sleep(1)
    global s
    s = '小鸡炖蘑菇'

def main():
    b = threading.Thread(target=bar)
    f = threading.Thread(target=foo)
    #f1 = threading.Thread(target=fun)
    b.start()
    f.start()
    e.wait()#运行b、f之后其他都不运行
    #f1.start()
    fun()
    b.join()
    f.join()
    #f1.join()



if __name__ == '__main__':
    main()

