from concurrent.futures import ThreadPoolExecutor, wait
import time

pool = ThreadPoolExecutor(max_workers=5)

def func_test(i):
    time.sleep(1)
    print(i)

res_list = []
for i in range(20):
   res = pool.submit(func_test, i)
   res_list.append(res)
# wait方法可以让主线程阻塞
wait(res_list,return_when="ALL_COMPLETED")
print("over")