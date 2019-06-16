import queue

queue.Queue()  # 普通队列
queue.LifoQueue()  # 栈队列 先进后出
q = queue.PriorityQueue()  # 优先级队列
q.put((1, 'a'))
# 第一个变量为优先级 第二个为数据 优先级相同 按ascii码大小排 优先级数字越小 优先级越高
# q.get_nowait()
# q.put_nowait()