import socket
import time
import threading


def s_c():
    sk = socket.socket()
    sk.connect(('127.0.0.1', 8080))
    sk.send(b'hello')
    time.sleep(1)
    print(sk.recv(1024))


for i in range(20):
    threading.Thread(target=s_c).start()