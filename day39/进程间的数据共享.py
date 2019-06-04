from multiprocessing import Manager, Process, Lock


# 进程间的数据共享数据不安全容易出现资源抢占的问题，需要加锁
def func(dic, lock):
    lock.acquire()
    dic['count'] -= 1
    lock.release()


if __name__ == '__main__':
    m = Manager()  # 实例化一个共享数据的对象
    lock = Lock()
    dic = m.dict({'count': 100})  # 给对象赋值
    p_list = []
    # 开启50个进程对字典进行-1操作
    for i in range(50):
        p = Process(target=func, args=(dic, lock))
        p.start()
        p_list.append(p)
    # 判断所有子进程是否执行结束
    [i.join() for i in p_list]
    # 打印数据执行变更后的结果
    print(dic)