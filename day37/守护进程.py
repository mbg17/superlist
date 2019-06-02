from multiprocessing import Process
import time


# 子进程1
def func():
    while True:
        time.sleep(0.2)
        print('l am fine')


# 子进程2
def func2():
    print('func2 start')
    time.sleep(9)
    print('func2 end')


if __name__ == '__main__':
    p = Process(target=func)
    p.daemon = True  # 守护进程 子进程岁主进程代码的结束而结束
    p.start()
    Process(target=func2).start()  # 非守护进程 主进程等待该进程结束后在结束
    i = 0
    while i <= 3:
        time.sleep(2)
        print('主进程')
        i += 1
    p.terminate() # 杀死一个进程
    time.sleep(1)
    print(p.is_alive())# 检测进程是否还存活
