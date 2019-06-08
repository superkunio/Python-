from multiprocessing import Pool
import  time

def fun(n):
    time.sleep(1)
    print("执行pool map事件")
    return n*n


def main():
    pool =Pool(4)
    l = [1,2,4,5,6,7,8]
    j = pool.map(fun,l)
    print(j)
    pool.close()
    pool.join()


if __name__ == '__main__':
    main()