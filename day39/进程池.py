from multiprocessing import Process,Pool
import time

def func(n):
    for i in range(10):
        print(n)

if __name__=='__main__':
    # 实例化一个进程池，包含五个进程
    pool = Pool(5)
    # 开启进程池，按顺序执行任务
    # 函数名，可迭代对象
    start = time.time()
    pool.map(func,range(100))
    t1 = time.time()-start
    start2 = time.time()
    p_list = []
    for i in range(100):
        p = Process(target = func,args = (i,))
        p_list.append(p)
        p.start()
    [p.join() for p in p_list]
    t2 = time.time()-start2
    print(t1,t2)# 输出进程池和开启多个进程所占用的时间