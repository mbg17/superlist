import os
import time
from multiprocessing import Pool

def func(n):
    print('start func %s'% n,os.getpid())
    time.sleep(1)
    print('start func %s'% n,os.getpid())

if __name__ == '__main__':
    pool = Pool(5)
    # 同步提交进程
    for i in range(10):
        pool.apply(func,args = (1,))
    # 异步提交进程
    for i in range(10):
        pool.apply_async(func,args = (1,))
    pool.close()# 关闭进程池接受任务
    pool.join()# 监测进程池任务执行结束