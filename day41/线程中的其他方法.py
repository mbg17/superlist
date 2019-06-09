import threading
import os
import time
def func():
    time.sleep(3)
    print(os.getpid()) # 获取进程ID
    print(threading.current_thread()) # 打印当前线程类型
    print(threading.get_ident())# 获取当前线程id
for i in range(10):
    threading.Thread(target=func).start()
print(threading.active_count()) # 当前存活进程数
print(threading.current_thread())
print(threading.enumerate()) # 当前存活进程的列表