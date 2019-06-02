from multiprocessing import Process
from multiprocessing import Semaphore  # 信号量
import time
import random


def func(i, sem):
    sem.acquire()
    print('%s 进入了房间' % i)
    time.sleep(random.randint(1, 5))
    print('%s 退出了房间' % i)
    sem.release()


if __name__ == '__main__':
    sem = Semaphore(4)  # 定义信号量
    for i in range(10):
        p = Process(target=func, args=(i, sem))
        p.start()