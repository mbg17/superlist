from multiprocessing import Process, Event
import time
import random


# 红绿灯事件
def car(e, i):
    if not e.is_set():
        print('car %s等红灯' % i)
        e.wait()
    print('car %s通过' % i)


def light(e):
    while True:
        if e.is_set():
            e.clear()
            print('\033[31m红灯亮了\033[0m')
        else:
            e.set()
            print('\033[32m绿灯亮了\033[0m')
        time.sleep(2)


if __name__ == '__main__':
    e = Event()
    traffic = Process(target=light, args=(e, ))
    traffic.start()
    for i in range(10):
        cars = Process(target=car, args=(e, i))
        cars.start()
        time.sleep(random.random())