# IPC inter-Process Communication 进程间的通信
# 队列 先进先出
# from multiprocessing import Queue
# q = Queue(5)  # 默认不传参 传参指定队列的大小
# q.put(1)  # 存放数据
# print(q.full())  # 判断队列是否满了
# q.get()  # 从队列取数据
# print(q.empty())  # 判断队列是否为空

from multiprocessing import Queue, Process


# 生产数据
def produce(q):
    q.put(1)


# 获取数据
def consume(q):
    print(q.get())


if __name__ == '__main__':
    # 设置队列
    q = Queue()
    # 写入数据，读取数据
    p = Process(target=produce, args=(q, ))
    p.start()
    c = Process(target=consume, args=(q, ))
    c.start()