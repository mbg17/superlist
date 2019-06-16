from gevent import monkey
monkey.patch_all()
import time
import gevent


def task():
    time.sleep(1)
    print('in task')


def sync():
    for i in range(10):
        task()


def asyn():
    g_list = []
    for i in range(10):
        g = gevent.spawn(task)
        g_list.append(g)
    gevent.joinall(g_list)# 监听所有协程的运行状态


sync()
asyn()
