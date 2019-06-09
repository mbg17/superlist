from threading import Thread, RLock
import time
# 递归锁可以被多次acquire
# acquire 一次必须对应的 release 一次


def eat(name, lock):
    lock.acquire()
    print('%s拿到面条了' % name)
    lock.acquire()
    print('%s拿到叉子了' % name)
    print('吃面了')
    lock.release()
    lock.release()


def eat2(name, lock):
    lock.acquire()
    print('%s拿到叉子了' % name)
    time.sleep(2)
    lock.acquire()
    print('%s拿到面条了' % name)
    print('吃面了')
    lock.release()
    lock.release()


lock = RLock()
Thread(target=eat, args=('陆元', lock)).start()
Thread(target=eat2, args=('路径', lock)).start()
