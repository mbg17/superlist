from threading import Thread, Lock
n = 10


def func(lock):
    global n
    lock.acquire()
    n -= 1
    lock.release()


lock = Lock()
for i in range(10):
    Thread(target=func, args=(lock, )).start()

print(n)