import socket
import time
address = ('127.0.0.1', 8080)
sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(address)
while True:
    msg, addr = sk.recvfrom(1024)
    stft = time.strftime(msg.decode('utf-8'), time.localtime())
    sk.sendto(stft.encode('utf-8'), addr)
sk.close()