#写出自己的线程类

from threading import Thread
from time import ctime,sleep
class myThread(Thread):
    def __init__(self,target,args=(),kwargs={}):
        super().__init__()
        self.target = target
        self.args = args
        self.kwargs = kwargs
    def run(self):
       self.target(*self.args,**self.kwargs)



def player(song,sec):
    for i in range(2):
        print('playing %s:%s'%(song,ctime()))
        sleep(sec)


def main():
    t = myThread(target=player,args=('靓丽女孩',),kwargs={'sec':2})
    t.start()
    t.join()


if __name__ == '__main__':
    main()
