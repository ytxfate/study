from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool
import time
import os

max_workers = 10
tp=ThreadPoolExecutor(max_workers=max_workers)

def sleep_(j, k):
    """线程池调用的函数"""
    time.sleep(j)
    print('{}: sleep '.format(k))


def main(n):
    """进程池调用的函数"""
    res_list=[]

    for i in range(19):
        res=tp.submit(sleep_,3,i)
        res_list.append(res)

    #以下循环是multiprocessing.Pool情况下再嵌套concurrent.futures.ThreadPoolExecutor时必须的,
    #否则子进程不会等待多线程执行完
    for j in res_list:
        '''在子进程调用main执行完毕之前 通过调用future.result()循环阻塞每个子线程。 只是这里第一次阻塞的时间里,其他线程基本上也就完成了(相同的)任务, 所以这里可以认为只有一次sleep_函数的执行时间'''
        j.result()

    #子进程最后会执行该输出
    print('{}------'.format(os.getpid()))

if __name__ == '__main__':
    p=Pool(processes=2)
    p.map(main,(1,2))