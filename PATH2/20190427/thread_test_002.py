from threading import Thread,currentThread
from time import sleep,ctime
import os
import sys

#线程函数

def func(sec):
    print('线程属性测试')
    sleep(sec)
    #线程对象的getName()属性获取名称
    #currentThread().setName('线程%s'%i)
    print('%s已结束'%currentThread().getName())
def main():
    #创建线程
    thread = []
    for i in range(3):
        t = Thread(name = '线程%d'%i,target=func,args=(5,))
        thread.append(t)
        t.start()
    #回收线程
    for i in thread:
        i.join()


if __name__ == '__main__':
    main()