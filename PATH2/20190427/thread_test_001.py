from threading import Thread
from time import sleep
import os


#线程函数

def music():
    for i in range(5):
        sleep(2)
        print("葫芦娃",os.getpid())



def main():
    a = 1
    t = Thread(target=music)
    t.start()

    for i in range(5):
        print(a)
        sleep(1.5)
        print("黑猫警长",os.getpid())
    t.join()
if __name__ == '__main__':
    main()