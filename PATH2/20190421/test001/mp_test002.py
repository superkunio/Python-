import multiprocessing as mp
from time import sleep
import os
def fun1():
    sleep(3)
    print('洗衣服')
    print(os.getppid(),'----',os.getpid())
def fun2():
    sleep(2)
    print('写作业')
    print(os.getppid(), '----', os.getpid())

def fun3():
    sleep(4)
    print('睡觉')
    print(os.getppid(), '----', os.getpid())
def main():
    things = [fun1,fun2,fun3]
    process = []
    for x in things:
        p = mp.Process(target=x)
        p.start()
        process.append(p)
    for x in process:
        x.join()

if __name__ == '__main__':
    main()
