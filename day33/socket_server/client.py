import socket

sk = socket.socket()
sk.connect(('127.0.0.1', 8080))
while True:
    msg = input('>>>').encode('utf-8')
    sk.send(msg)
    ret = sk.recv(1024).decode('utf-8')
    if ret == 'q':
        sk.close
        break
    print(ret)