#my version：缺点，需要遍历整个文件，如果遇见大文件，会导致运行效率降低
#创建父子进程，分别将一个文件的上半部分和下半部分，复制到一个新的文件中。创建进程方法自选。按照字节分割
import multiprocessing as mp
import time
def write_front():
    print('前半部分读取开始')
    f1 = open('D:\学习\project\\20190421\homework\\before.txt', 'rb')
    f2 = open('D:\学习\project\\20190421\homework\\after.txt', 'wb')
    info = f1.read()
    front = info[:len(info) // 2]
    print('前半部分开始写入')
    f2.write(front)
    print('前半部分写入结束')
    f1.close()
    f2.close()
def write_back():
    time.sleep(0.5)
    print('后半部分读取开始')
    f1 = open('D:\学习\project\\20190421\homework\\before.txt', 'rb')
    f2 = open('D:\学习\project\\20190421\homework\\after.txt', 'ab')
    info = f1.read()
    back = info[len(info) // 2:]
    print('后半部分写入开始')
    f2.write(back)
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