# 以继承的方式实现线程的启动

from multiprocessing import Process
import os


class MyProcess(Process):
    def __init__(self, args):
        super().__init__()
        self.args = args

    def func(self):
        print(self.args)

    # 线程启动后执行的代码
    def run(self):
        self.func()


if __name__ == '__main__':
    # 以自定义类的方式创建一个子进程
    p = MyProcess('陆远')
    # 启动子进程
    p.start()