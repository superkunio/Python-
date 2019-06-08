from multiprocessing import Process
from time import sleep,ctime


def tm():
    while True:
        sleep(2)
        print(ctime())
#主进程不写p.join()，主进程代码运行完毕后退出
def main():
    p = Process(target=tm)
    #令子进程，跟随主进程停止而停止，必须要放在p.start()前，且不与p.join()同用
    p.daemon = True
    p.start()
    sleep(5)
    print('主进程退出')
if __name__ == '__main__':
    main()