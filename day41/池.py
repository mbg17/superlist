from concurrent.futures import ThreadPoolExecutor  # 线程池
import time


def func(n):
    time.sleep(3)
    print(n)
    return n * n


def call_back(m):
    print('结果是%s' % m.result())


tpool = ThreadPoolExecutor(5)  # 定义线程池大小
t_list = []
for i in range(20):
    # add_done_callback回调函数
    t = tpool.submit(func, i).add_done_callback(call_back)  # 异步提交线程
    t_list.append(t)

# tpool.shutdown()  # 线程池停止接受任务，并等待所有线程结束
# [print('***', t.result()) for t in t_list]  # 打印所有线程返回的结果
