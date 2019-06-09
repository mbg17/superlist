from threading import Thread, Semaphore
import time


def func(sem):
    sem.acquire()
    time.sleep(1)
    print('你好')
    sem.release()


sem = Semaphore(4)
for i in range(10):
    Thread(target=func, args=(sem, )).start()
