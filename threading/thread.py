#same program wtih thread
import time
import threading
start = time.perf_counter()

def afunc():
        print('start--------------------')
        time.sleep(1)
        print('end----------------------')
    
t1  = threading.Thread(target= afunc)
t2  = threading.Thread(target= afunc)

t1.start()
t2.start()


t1.join()
t2.join()

finish = time.perf_counter()

print(f'delta time is : {finish-start}')
