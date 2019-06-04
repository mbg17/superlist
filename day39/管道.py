from multiprocessing import Process, Pipe


def func(conn1, conn2):
    conn2.close()  # 子进程关闭管道不影响主进程管道
    while True:
        try:
            print(conn1.recv())  # 当其他管道关闭且没有数据可取时，会抛出一个EofError异常
        except EOFError:
            conn1.close()
            break


if __name__ == '__main__':
    conn1, conn2 = Pipe()  # 实例化管道返回两个链接对象
    Process(target=func, args=(conn1, conn2)).start()
    conn1.close()  # 主进程关闭管道对子进程不影响
    for i in range(20):
        conn2.send('hello')
    conn2.close()