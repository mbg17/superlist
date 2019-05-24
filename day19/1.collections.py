# 堆栈 ：先进后出
# 队列 ：先进先出 queue
import queue
q = queue.Queue()  # 创建队列
# put 放入值
# get 取值 娶不到值阻塞
# qsize 获取队列大小
# nametuple(名称，[属性列表]) 命名的元祖
# from collections import deque 双端队列
# q = deque() 创建队列
# deque.append() 从后面放数据
# deque.appendleft() 从前面放数据
# deque.pop() 从后面取数据
# deque.popleft() 从前面取数据
# deque.insert() 插入数据
# OrderedDict 有序字典
# key不固定 value默认值为定义的值 可以用lambda 返回默认值
from collections import defaultdict
dt = defaultdict(list)
print(dt)
