import concurrent.futures as c_futures
import time
import random
import json

def p_func(fa, son):
    time.sleep(random.random())
    print(str(fa) + " => " + str(son) + " : " + str(time.time()) +"  "+ (str(son)+" ")*40)
    return

def thread_func(fa):
    time.sleep(1)
    thread_pool = c_futures.ThreadPoolExecutor(max_workers=5)
    thread_list = []
    for i in range(100):
        res = thread_pool.submit(p_func, fa, i)
        thread_list.append(res)
    thread_pool.shutdown(wait=True)
    # c_futures.wait(thread_list, return_when="ALL_COMPLETED")
    for res in thread_list:
        res.result()
    print('thread_func over')

def process_func():
    process_pool = c_futures.ProcessPoolExecutor(max_workers=3)
    process_list = []
    for i in range(3):
        res = process_pool.submit(thread_func, i)
        time.sleep(random.random())
        process_list.append(res)
    process_pool.shutdown(wait=True)
    # c_futures.wait(process_list, return_when="ALL_COMPLETED")
    for res in process_list:
        res.result()

if __name__ == '__main__':
    process_func()
    