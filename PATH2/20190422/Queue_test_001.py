from multiprocessing import Queue
from time import sleep


def main():
    q = Queue(6)
    for x in range(6):
        q.put(x)
    #由于写入速度没那么快，所以要在判断函数前加上等待
    sleep(3)
    for x in range(6):
        print(q.get())
    print(q.empty())
    print(q.full())
    print(q.qsize())
    q.close()


if __name__ == '__main__':
    main()