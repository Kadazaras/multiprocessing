import concurrent.futures
import time
import numpy as np

start = time.perf_counter()

def init_pool_initializer():
    np.random.seed()

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    arr = np.random.normal(10,1,10)
    arr2 = np.random.normal(0,1,10)
    print(f'Done Sleeping...{seconds}')
    return {'dates':arr2,'data':arr}


with concurrent.futures.ProcessPoolExecutor(max_workers=2, initializer = init_pool_initializer) as executor:
    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_something, secs)

    for result in results:
        print(result)

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
