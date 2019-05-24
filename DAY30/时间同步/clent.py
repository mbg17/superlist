import socket
import time
address = ('127.0.0.1', 8080)
sk = socket.socket(type=socket.SOCK_DGRAM)
sk.sendto(('%Y-%m-%d').encode('utf-8'), address)
msg, addr = sk.recvfrom(1024)
print(msg.decode('utf-8'))
sk.close()
# test