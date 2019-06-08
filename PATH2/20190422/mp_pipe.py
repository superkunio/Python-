from multiprocessing import Process,Pipe
import time

def func(name,fd):
    time.sleep(1)
    print('im super %s'%name)
    data = fd.recv()
    print('fd2 recv information%s'%data)
def main():
    fd1,fd2 = Pipe()
    process = []
    for x in range(5):
        p = Process(target=func,kwargs={'name':x,'fd':fd2})
        process.append(p)
        p.start()
    for x in range(5):
        fd1.send('\nfd1 send information')
    for x in process:
        x.join()

if __name__ == '__main__':
    main()