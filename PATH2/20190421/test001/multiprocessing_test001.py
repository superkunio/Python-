import multiprocessing as mp
from time import sleep

def fun(a):
    sleep(3)
    a = 10000
    print('子进程事件',a)
def main():
    a = 1
    #创建进程对象
    p = mp.Process(target=fun(a))

    #启动进程,p.start()至p.join()之间的代码，为父进程执行内容
    p.start()
    sleep(2)
    print('父进程事件',a)

    #回收进程

    p.join(1)
if __name__ == '__main__':
    main()