import socket

sk = socket.socket()
sk.connect(('127.0.0.1', 8080))

msg = sk.recv(1024).decode('utf-8')
print(msg)
sk.send(b'bye')
sk.close()