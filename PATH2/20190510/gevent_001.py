
import gevent
from time import sleep

def foo(a,b):
    print('a = %d,b = %d'%(a,b))
    gevent.sleep(2)
    print('running foo again')

def bar():
    print('running int bar')
    gevent.sleep(3)
    print('running bar again')




f = gevent.spawn(foo,1,2)
g = gevent.spawn(bar)
sleep(3)

print('=======================================')
gevent.joinall([f,g])