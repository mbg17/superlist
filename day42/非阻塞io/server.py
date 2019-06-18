import socket

sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.setblocking(False)  # 设置为非阻塞状态，收不到消息报BlockingIOError异常
sk.listen()
conn_l = []
del_l = []
while True:
    try:
        conn, addr = sk.accept()  # 接收不到请求报错
        print('建立连接', addr)
        conn_l.append(conn)  # 收到连接加入到连接列表里
    except BlockingIOError:
        for i in conn_l:
            try:
                msg = i.recv(1024)  # 收不到消息报错
                if msg == b'':  # 收到空消息表示已断开连接
                    del_l.append(i)
                    continue
                print(msg)
                i.send(b'byebye')
            except BlockingIOError:
                pass
        for d in del_l:  # 遍历断开连接的列表，删除连接列表中的数据
            d.close()
            conn_l.remove(d)
        del_l.clear()  # 清空断开连接的列表
