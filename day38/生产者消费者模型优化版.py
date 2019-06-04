from multiprocessing import Process, JoinableQueue
import time
import random

# put join / get task_done
# 生产者
def producer(name, food, q):
    for i in range(10):
        time.sleep(random.randint(1, 2))
        f = '%s 生产了%s%s' % (name, food, i)
        print(f)
        q.put(f)
    q.join()  # 阻塞状态，等待队列数据消耗完毕


# 消费者
def consumer(name, q):
    while True:
        f = q.get()  # 没取到数据则阻塞状态
        print('%s 消费了%s' % (name, f))
        time.sleep(random.randint(1, 3))
        q.task_done()  # 每消耗一个数据，返回一个表示给队列，用join() 接收


if __name__ == '__main__':
    q = JoinableQueue(20)
    p1 = Process(target=producer, args=('陆远', '包子', q))
    p2 = Process(target=producer, args=('别人', '包子', q))
    p1.start()
    p2.start()
    c1 = Process(target=consumer, args=('二胡软籽', q))
    c2 = Process(target=consumer, args=('桐生战兔', q))
    c1.daemon = True  # 守护线程 子进程随主进程结束而结束
    c2.daemon = True
    c1.start()
    c2.start()
    # 监测p1 p2进程是否结束
    p1.join()
    p2.join()
