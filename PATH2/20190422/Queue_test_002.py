from multiprocessing import Process,Queue
from time import sleep

def func1(q):
    sleep(1)
    q.put({'a':1,'b':2})
def func2(q):
    sleep(2)
    print('收到消息:',q.get())

def main():
    #创建消息队列
    q = Queue()
    process = [func1,func2]
    working = []
    for x in process:
        p = Process(target=x,args=(q,))
        p.start()
        working.append(p)
    for x in working:
        x.join()

if __name__ == '__main__':
    main()

