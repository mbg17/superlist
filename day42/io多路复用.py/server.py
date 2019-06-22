import select
import socket

sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.setblocking(False)  # 设置非阻塞模式
sk.listen()

r_list = [sk]
while True:
    # 监听列表中的socket对象
    # 有数据返回则read_list返回有数据的对象
    read_list, write_list, xlist = select.select(r_list, [], [])
    for i in read_list:
        if i is sk:  # 判断是客户端还是服务端
            conn, addr = sk.accept()
            r_list.append(conn)
        else:
            msg = i.recv(1024)
            if msg == b'':  # 发送空消息则证明断开连接 关闭socke连接，并移除对应客户端对象
                i.close()
                r_list.remove(i)
                continue
            print(msg)
            i.send(b'hello')