from multiprocessing import Process, Pipe,Lock
import time
import random
# 管道数据不安全 

def producer(con, pro, name, food):
    con.close()
    for i in range(20):
        time.sleep(random.random())
        f = '%s 生产了%s %s' % (name, food, i)
        print(f)
        pro.send(f)
    pro.send(None)
    pro.send(None)
    pro.close()


def consumer(con, pro, name,lock):
    pro.close()
    while True:
        lock.acquire()
        food = con.recv()
        lock.release()
        if food is None:
            con.close()
            break
        print('%s 吃了%s' % (name, food))
        time.sleep(random.random())



if __name__ == '__main__':
    con, pro = Pipe()
    lock = Lock()
    p = Process(target=producer, args=(con, pro, '陆远', 'food'))
    c = Process(target=consumer, args=(con, pro, 'me',lock))
    c1 = Process(target=consumer, args=(con, pro, 'me',lock))
    p.start()
    c.start()
    c1.start()
    con.close()
    pro.close()