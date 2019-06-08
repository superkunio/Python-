#创建父子进程，分别将一个文件的上半部分和下半部分，复制到一个新的文件中。创建进程方法自选。按照字节分割
import os
import multiprocessing as mp
import time
path1 = 'D:\学习\project\\20190421\homework\\before.txt'
path2 = 'D:\学习\project\\20190421\homework\\after.txt'

size = os.path.getsize(path1)
def write_front():
    print('前半部分读取开始')
    f1 = open(path1, 'rb')
    f2 = open(path2, 'wb')
    front = size // 2
    print('前半部分开始写入')
    while True:
        if front < 1024:
            data = f1.read(front)
            f2.write(data)
            break
        data = f1.read(1024)
        f2.write(data)
        front -= 1024
    print('前半部分写入结束')
    f1.close()
    f2.close()
def write_back():
    print('后半部分读取开始')
    f1 = open(path1, 'rb')
    f2 = open(path2, 'ab')
    #以开头为基准,向后移动size//2位
    f1.seek(size//2,0)
    print('后半部分写入开始')
    while True:
        data = f1.read(1024)
        if not data:
            break
        f2.write(data)
    print('后半部分写入结束')
    f1.close()
    f2.close()

def main():
    step = [write_front,write_back]
    process = []
    for pro in step:
        p =mp.Process(target=pro)
        p.start()
        process.append(p)
    for x in process:
        x.join()


if __name__ == '__main__':
    main()

