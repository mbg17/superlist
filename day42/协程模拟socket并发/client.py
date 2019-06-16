import socket

sk = socket.socket()
sk.connect(('127.0.0.1', 8080))

msg = sk.recv(1024).decode('utf-8')
print(msg)
info = input('>>>').encode('utf-8')
sk.send(info)
sk.close()