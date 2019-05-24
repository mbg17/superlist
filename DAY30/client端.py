import socket

ck = socket.socket()
ip = '127.0.0.1'
dk = 8080
ck.connect((ip, dk))  # 服务端的地址

ck.send(b'hello')
ret = ck.recv(1024)
print(ret)
ck.close()