from threading import Thread, RLock
import time
# 递归锁可以被多次acquire
# acquire 一次必须对应的 release 一次


def eat(name, lock):
    for i in range(len(name)):
        lock.acquire()
        print(name[i])
        lock.release()
        time.sleep(1)
    # lock.acquire()
    # print('%s拿到面条了' % name)
    # lock.acquire()
    # print('%s拿到叉子了' % name)
    # print('吃面了')
    # lock.release()
    # lock.release()


def eat2(name, lock):
    for i in range(len(name)):
        lock.acquire()
        print(name[i])
        lock.release()
        time.sleep(1)
    # lock.acquire()
    # print('%s拿到叉子了' % name)
    # time.sleep(2)
    # lock.acquire()
    # print('%s拿到面条了' % name)
    # print('吃面了')
    # lock.release()
    # lock.release()


lock = RLock()
l1 = [1, 2, 3, 4, 5]
l2 = ['a', 'b', 'c', 'd', 'e']
Thread(target=eat, args=(l1, lock)).start()
Thread(target=eat2, args=(l2, lock)).start()
