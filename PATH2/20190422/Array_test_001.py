from multiprocessing import Process,Array
import time

def func(a):
    for i in a:
        print(i)
    a[3] = 587





def main():
    #创建共享内存，放入列表，由于ctype是‘i’，所以第三位的列表的元素，全为整数
    #shm = Array('i',[0,1,2,3,4,5])
    #创建共享内存，开辟5个整形空间
    #shm = Array('i', 5)
    #存入字符串
    shm = Array('c',b'Hello')
    p = Process(target=func,args=(shm,))
    p.start()
    p.join()
    for i in shm:
        print(i)
    print(shm.value)#打印字符串

if __name__ == '__main__':
    main()
