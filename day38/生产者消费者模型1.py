from multiprocessing import Process, Queue
import time
import random


# 生产者
def producer(name, food, q):
    for i in range(10):
        time.sleep(random.randint(1, 2))
        f = '%s 生产了%s%s' % (name, food, i)
        print(f)
        q.put(f)


# 消费者
def consumer(name, q):
    while True:
        f = q.get()
        if f is None:
            print('%s 看见没包子离开了' % name)
            break
        print('%s 消费了%s' % (name, f))
        time.sleep(random.randint(1, 3))


if __name__ == '__main__':
    q = Queue(20)
    p1 = Process(target=producer, args=('陆远', '包子', q))
    p2 = Process(target=producer, args=('别人', '包子', q))
    p1.start()
    p2.start()
    c1 = Process(target=consumer, args=('二胡软籽', q))
    c2 = Process(target=consumer, args=('桐生战兔', q))
    c1.start()
    c2.start()
    # 监测p1 p2进程是否结束
    p1.join()
    p2.join()
    # 放入None 让消费者离开
    q.put(None)
    q.put(None)