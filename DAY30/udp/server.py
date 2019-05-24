import socket
address = ('127.0.0.1', 8080)

sk = socket.socket(type=socket.SOCK_DGRAM)  # socket.SOCK_DGRAM UDP类型的服务
sk.bind(address)  # 虽然是udp还是需要绑定ip和端口号
msg, addr = sk.recvfrom(1024)  # 每次接受都会返回消息和地址
print(msg.decode('utf-8'))  # 将bytes类型转换为utf-8

sk.sendto(b'hallo', addr)  # 返回消息需要带上地址
sk.close()