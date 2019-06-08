#通过set()和wait()来人为控制进程的阻塞，对临界资源进行操作
from multiprocessing import Process,Event
from time import sleep

def wait_event(event):
    print('进程1想要操作临界区')
    event.wait()
    print("开始操作临界区资源",event.is_set())
    #使用with open读取文件
    with open('file','rb') as f:
        print(f.read())

def wait_event_timeout(event):
    print('进程2也想操作临界区')
    event.wait(2)
    if event.is_set():
        with open('file') as f:
            print(f.read())
    else:
        print('无法读取文件')
def main():
    e = Event()
    p1 = Process(target=wait_event,args=(e,))
    p2 = Process(target=wait_event_timeout,args=(e,))
    p1.start()
    p2.start()
    print('主进程开始')
    with open('file','w') as f:
        sleep(3)
        f.write('i love China')
    e.set()
    p1.join()
    p2.join()
    print('主进程结束')



if __name__ == '__main__':
    main()