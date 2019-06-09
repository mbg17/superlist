from threading import Thread
import time


def func(n):
    time.sleep(1)
    print(n)


# 启动多线程
for i in range(10):
    t = Thread(target=func, args=(i, ))
    t.start()
