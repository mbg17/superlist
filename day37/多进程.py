from multiprocessing import Process
import os


def func(args):
    print(args)
    print('子进程：%(id)s' % {'id': os.getpid()})
    print('子进程的父进程：%(id)s' % {'id': os.getppid()})


# 主进程
if __name__ == '__main__':
    # 主进程注册了一个子进程
    p = Process(target=func, args=(12345, ))  # (12345, )表示一个元祖，(12345)表示一个数字
    # 激活子进程，并且和主进程同时运行
    p.start()
    print('*' * 10)
    # os.getpid() 获取当前进程的进程号，os.getppid() 获取当前进程父进程的进程号
    print('父进程：%(id)s' % {'id': os.getpid()})
    print('父进程的父进程：%(id)s' % {'id': os.getppid()})
