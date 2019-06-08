import threading



def value(a,b,l):
    while True:
        l.acquire()
        if a != b:
            print(('a = %d,b = %d')%(a,b))
        l.release()


def main():
    lock = threading.Lock()
    a = b = 0
    t = threading.Thread(target=value,args=(a,b,lock))
    t.start()
    while True:
        with lock:
            a += 1
            b += 1
    t.join()


if __name__ == '__main__':
    main()