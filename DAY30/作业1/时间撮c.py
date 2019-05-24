import socket
import time
ck = socket.socket()
ip = '127.0.0.1'
dk = 8080

ck.connect((ip, dk))

while True:
    ck.send(bytes(str(int(time.time())), encoding='utf-8'))
    time.sleep(10)

ck.close()