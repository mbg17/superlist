from threading import Condition, Thread


def func(com, n):
    con.acquire()
    con.wait()  # 等待条件，执行相应数量的线程
    print('第%s个线程' % n)
    con.release()


con = Condition()
for i in range(10):
    Thread(target=func, args=(con, i)).start()
while True:
    num = int(input('>>>'))
    con.acquire()
    con.notify(num)  #设置可运行线程的数量
    con.release()