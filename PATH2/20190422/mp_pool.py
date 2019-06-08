from multiprocessing import Process,Pool,freeze_support
from time import ctime,sleep
def work(msg):
    sleep(2)
    print(msg)
def main():
    freeze_support()
    #创建进程池
    pool = Pool(processes=4)
    #将事件放入进程池队列，等待执行
    for i in range(10):
        msg = 'hello %d'%i
        pool.apply_async(func=work,args = (msg,))
    #关闭进程池
    pool.close()
    #回收
    pool.join()

if __name__ == '__main__':
    main()