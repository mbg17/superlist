import socket

sk = socket.socket()
ip = '127.0.0.1'
dk = 8080

sk.bind((ip, dk))
sk.listen()

conn, addr = sk.accept()
while True:
    ret = conn.recv(1024).decode('utf-8')
    print(ret)
    if ret == 'bye':
        conn.send(b'bye')
        break
    info = input('>>>')
    conn.send(bytes(info, encoding='utf-8'))

conn.close()
sk.close()