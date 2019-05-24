# socket 套接字
# 基于文件通信
# AF_UNIX
# 基于网络通信
# AF_INET(IPV4) AF_INET6(IPV6)
# 代码示例
import socket
sk = socket.socket()  # 建立socke服务
ip = '127.0.0.1'
dk = 8080  # 端口必须为数字
sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 允许地址重用
sk.bind((ip, dk))  # 绑定端口
sk.listen()  # 监听端口 阻塞

conn, addr = sk.accept()  # 接受信息 conn 链接 addr 请求对象的地址
ret = conn.recv(1024)  # 每次接受的数据大小
print(ret)
conn.send(b'hi')  # 向请求对象发送消息 bytes类型
conn.close()  # 关闭连接
sk.close()  # 关闭socket链接
