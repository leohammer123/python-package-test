import time
import concurrent.futures
start = time.perf_counter()

def afunc(times):
        print('start--------------------'+f'time = {times}')
        time.sleep(times)
        return 'done and return'
    
with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = executor.map(afunc,secs)

    for result in results:
        print(result)

# for _  in range(10):
#         t = threading.Thread(target=afunc)
#         t.start()
#         threads.append(t)

# for thread in threads:
#         thread.join()
        
finish = time.perf_counter()

print(f'delta time is : {finish-start}')

#If you select a block of code 
#use the key sequence Ctrl+K+C
#you'll comment out the section of code.
#Ctrl+K+U will uncomment the code.