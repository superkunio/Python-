from threading import Thread
from time import sleep


def func():
    sleep(3)
    print('Daemon 测试')



def main():
    t = Thread(target=func)
   # t.setDaemon(True)
    print(t.isDaemon())
    t.start()
    print("========主线程结束========")

if __name__ == '__main__':
    main()