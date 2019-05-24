import socket

sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.listen()
coon, sddr = sk.accept()
while True:
    info = input('>>>')
    if info == 'q':
        coon.send(b'q')
        break
    coon.send(info.encode('gbk'))
    num = int(coon.recv(1024).decode('gbk'))
    coon.send(b'ok')
    msg = coon.recv(num).decode('gbk')
    print(msg)
sk.close()