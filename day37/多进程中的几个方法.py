from multiprocessing import Process
import time


def func(arg1, arg2):
    print('*' * arg1)
    time.sleep(5)
    print('*' * arg2)


if __name__ == '__main__':
    for i  in range(10):
        p = Process(target=func, args=(2, 4))
        p.start()
    # start,join之间的代码为异步进程
    # 监控子进程是否结束，结束后放行其他内容
    #p.join()
    print('执行完了')