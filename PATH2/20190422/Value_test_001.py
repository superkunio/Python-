from multiprocessing import Process,Value
import time
import random
#操作共享内存增加
def deposite(v):
    for i in range(100):
        time.sleep(0.05)
        #对value属性操作及操作共享内存数据
        v.value += random.randint(1,200)

def withdraw(v):
    for i in range(100):
        time.sleep(0.04)
        v.value -= random.randint(1,180)

def main():
    #创建共享内存
    money = Value('i',2000)
    process = [deposite,withdraw]
    working = []
    for x in process:
        p = Process(target=x,args=(money,))
        p.start()
        working.append(p)
    for x in working:
        x.join()
    print('余额为：%d'%money.value)

if __name__ == '__main__':
    main()
