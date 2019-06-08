from multiprocessing import Process,Lock
from time import sleep
import sys
#使用lock()控制进程互斥
def writer1(lock):
    lock.acquire()
    for i in range(20):
        sleep(0.5)
        sys.stdout.write('writer1 想向终端写入\n')
    lock.release()
def writer2(lock):
    lock.acquire()
    for i in range(20):
        sleep(0.5)
        sys.stdout.write('writer2 想向终端写入\n')
    lock.release()


def main():
    lock = Lock()
    p1 = Process(target=writer1,args=(lock,))
    p2 = Process(target=writer2,args=(lock,))
    p1.start()
    p2.start()




    p1.join()
    p2.join()


if __name__ == '__main__':
    main()
