import threading
import time
import datetime


begin = datetime.datetime.now()

def add(n):
    sum = 0
    for i in range(n):
        sum += i
    print(sum)

add(500000)
add(800000)
t1 = threading.Thread(target=add,args=(500000,))
t1.start()

t2 = threading.Thread(target=add,args=(800000,))
t2.start()

t1.join()
t2.join()

end = datetime.datetime.now()

print(end-begin)
