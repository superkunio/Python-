from multiprocessing import Process
import time
class ClockProcess(Process):
    def __init__(self,value):
        self.value = value
        #加载父类__init__方法
        super().__init__()
    #重写run方法，内容随意
    def run(self):
        for i in range(5):
            print('The time is {}'.format(time.ctime()))
            time.sleep(self.value)

def main():
    #创建自定义进程的类对象
    p = ClockProcess(2)
    p.start()
    p.join()


if __name__ == '__main__':
    main()