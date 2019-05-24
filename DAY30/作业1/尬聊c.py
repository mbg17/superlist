import socket

ck = socket.socket()
ip = '127.0.0.1'
dk = 8080

ck.connect((ip, dk))

while True:
    info = input('>>>')
    ck.send(bytes(info, encoding='utf-8'))
    ret = ck.recv(1024).decode('utf-8')
    if ret == 'bye':
        ck.send(b'bye')
        break

ck.close()