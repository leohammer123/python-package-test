import time
import threading
start = time.perf_counter()

def afunc():
        print('start--------------------')
        time.sleep(1)
        print('end----------------------')
    
threads = []

for _  in range(10):
        t = threading.Thread(target=afunc)
        t.start()
        threads.append(t)

for thread in threads:
        thread.join()
        
finish = time.perf_counter()

print(f'delta time is : {finish-start}')
