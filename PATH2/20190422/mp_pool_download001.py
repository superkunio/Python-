'''
进程池，启动一个进程就要克隆一份数据，假设父进程1G，那么启动进程开销很大
避免启动太多造成系统瘫痪，就有进程池，即同一时间允许的进程数量
ps：线程没有池，因为线程启动开销小，线程有类似信号量来控制
'''
'''
windows上必须加语句：
if __name__ == '__main__':
    freeze_support()
'''
from multiprocessing import Pool,freeze_support
import time
import os

def Foo(i):
    time.sleep(2)
    # print(os.getpid())
    return i+100
def Bar(arg):
    print("hello world",arg)
    print(os.getpid())

if __name__ == '__main__':
    freeze_support()
    pool = Pool(processes=5)  # 允许进程池里同时放入5个进程
    print(os.getpid())
    for i in range(10):  # 启动了但是还没被允许，因为同一时间只有5个在运行
        # pool.apply_async(func=Foo, args=(i,)) # 并行
        # pool.apply(func=Foo, args=(i,))  # 串行
        pool.apply_async(func=Foo, args=(i,),callback=Bar) # 并行，并且当且仅当Foo执行完后再执行Bar
        # 回调应用场景：批量备份完后，往数据库写日志，但是为啥不让子线程写，而让父进程写？因为父进程里写日志只连一次，子进程里每次都连
    print('end')
    pool.close()
    pool.join() # 这里要先关闭再JOIN。进程池中进程执行完后再关闭，如果注释，那么程序直接关闭