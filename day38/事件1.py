from multiprocessing import Event

e = Event()  # 创建一个事件，默认为阻塞状态
print(e.is_set())  # 查看当前事件的状态

e.set()  # 设置时间的状态为不阻塞
e.wait()  # 根据is_set()确定是否阻塞
print('run')
e.clear()  # 设置时间的状态为阻塞
e.wait()
print('run')