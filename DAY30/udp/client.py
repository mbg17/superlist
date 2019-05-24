import socket

SK = socket.socket(type=socket.SOCK_DGRAM)
address = ('127.0.0.1', 8080)
SK.sendto(b'HI', address)

msg, addr = SK.recvfrom(1024)
print(msg.decode('utf-8'))
SK.close()