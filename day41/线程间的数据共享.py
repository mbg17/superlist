from threading import Thread

class MyThread(Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        global g 
        g = 0
        print(g)

g = 100
t_list = []
for i in range(10):
    t = MyThread()
    t.start()
    t_list.append(t)
[t.join() for t in t_list]
print(g)