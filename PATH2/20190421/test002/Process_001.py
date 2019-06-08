from multiprocessing import Process
from time import sleep
#带参数的进程函数
def work(sec,name):
    for i in range(3):
        sleep(sec)
        print("I'm %s"%name)
        print("I'm working...")

def main():
    #通过args进行传参，按照索引，分别传输至对应位置
    #p = Process(target=work,args=(2,'Suchang'))
    #通过kwargs进行传参，按照键值对，分别传输至对应位置
    #p = Process(target=work,kwargs={'sec':2,'name':'suchang'})
    #通过args与kwargs相互配合的方式传参,注意args是一个可迭代对象
    p = Process(target=work,args=(2,),kwargs={'name':'suchang'})
    
    p.start()
    #通过修改进程对象的name属性，来获得自定义的进程名
    p.name = 'worker'
    print('Process isalive?:%s'%(p.is_alive()))
    print('Process name:%s'%p.name)
    print('Process PID:%s'%p.pid)
    p.join()
    print('Process isalive?:%s' % (p.is_alive()))


if __name__ == '__main__':
    main()
