# 守护线程随着主线程中的子进程结束而结束
from threading import Thread
import time


def func1():
    while True:
        print('*' * 10)
        time.sleep(1)


def func2():
    print(666)
    time.sleep(5)


t = Thread(target=func1)
t.daemon = True  # 守护线程 随其他非守护线程的结束而结束
t.start()
t2 = Thread(target=func2)
t2.start()
t2.join()  # 监测子线程是否结束
print('主线程')
