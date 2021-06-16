# normal prgram process
import time
start = time.perf_counter()

def afunc():
        print('start--------------------')
        time.sleep(1)
        print('end----------------------')
    
afunc()
afunc()

finish = time.perf_counter()

print(f'delta time is : {finish-start}')
