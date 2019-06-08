from multiprocessing import Process
import os
import signal
def startup():
    print('路面畅通准备发车！！！')
def speedup():
    print('加快速度，系好安全带！！！')
def stop():
    print('已经到站，下车')
def StoPUsr1(pid):
    os.kill(signal.SIGUSR1,pid)
def StoPUsr2(pid):
    os.kill(signal.SIGUSR1,pid)
def TicketCollector():
    tcpid = os.getpid()
    dpid = os.getppid()
    signal.signal(signal.SIGINT,StoPUsr1(dpid))
    signal.signal(signal.SIGQUIT,StoPUsr2(dpid))
    signal.signal(signal.SIGUP, StoPUsr1(dpid))


def main():
    p = Process(target=TicketCollector())

    p.start()
    signal.signal(signal.SIGUSR1,startup)
    signal.signal(signal.SIGUSR2,speedup)
    signal.signal(signal.SIGUSR1,stop)
    p.join()


if __name__ == '__main__':
    main()