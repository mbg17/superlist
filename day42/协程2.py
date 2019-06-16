from gevent import monkey
monkey.patch_all()  # 将该模块下的函数打成包，监听阻塞状态
import time
import gevent


def eat():
    print('eat start')
    time.sleep(1)  # 切换到另一个函数并记录执行的位置
    print('eat end')


def play():
    print('play start')
    time.sleep(1)
    print('play end')


g1 = gevent.spawn(eat)  # 注册协程
g2 = gevent.spawn(play)
g1.join()  # 开启协程
g2.join()