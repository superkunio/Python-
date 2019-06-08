from GIL_problem import *
import time

t = time.time()
for i in range(10):
    count(1,1)
print('line cpu:',time.time() - t)